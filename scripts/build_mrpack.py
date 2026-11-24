#!/usr/bin/env python3
"""Construye un .mrpack consultando los datos verificables en Modrinth."""

import json
import re
import shutil
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "pack" / "mods.json"
DIST_DIR = ROOT / "dist"
USER_AGENT = "HorizonteModpackBuilder/1.0 (GitHub Actions)"
API_BASE = "https://api.modrinth.com/v2"


class BuildError(RuntimeError):
    """Error con datos de manifiesto, API o archivos de entrada."""


def _nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def _first_nonempty(data, keys):
    for key in keys:
        value = data.get(key)
        if _nonempty_string(value):
            return value.strip()
    return None


def read_manifest(path=MANIFEST_PATH):
    """Lee el manifiesto validando Minecraft, Loader y los IDs de versión."""
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BuildError("No existe pack/mods.json.") from exc
    except (OSError, json.JSONDecodeError) as exc:
        raise BuildError("No se pudo leer pack/mods.json: {}".format(exc)) from exc

    if not isinstance(data, dict):
        raise BuildError("pack/mods.json debe contener un objeto JSON.")

    minecraft_version = _first_nonempty(
        data, ("minecraft_version", "game_version")
    )
    if not minecraft_version:
        raise BuildError(
            "Falta minecraft_version (o game_version) en pack/mods.json."
        )

    loader_version = _first_nonempty(
        data, ("fabric_loader_version", "loader_version")
    )
    if not loader_version:
        raise BuildError(
            "Falta fabric_loader_version (o loader_version) en pack/mods.json."
        )

    raw_mods = data.get("mods", [])
    if not isinstance(raw_mods, list):
        raise BuildError("El campo mods de pack/mods.json debe ser una lista.")

    mods = []
    for index, item in enumerate(raw_mods, 1):
        if not isinstance(item, dict):
            raise BuildError("La entrada de mod #{} no es un objeto.".format(index))
        version_id = _first_nonempty(item, ("version_id", "id"))
        if not version_id:
            raise BuildError(
                "La entrada de mod #{} no tiene version_id ni id.".format(index)
            )
        mods.append({"version_id": version_id})

    name = _first_nonempty(data, ("name",)) or "modpack"
    version = _first_nonempty(data, ("version",)) or "1.0.0"
    return {
        "name": name,
        "version": version,
        "minecraft_version": minecraft_version,
        "fabric_loader_version": loader_version,
        "mods": mods,
    }


def _get_json(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            return json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        raise BuildError("No se pudo consultar {}: {}".format(url, exc)) from exc


def _get_version_data(version_id):
    return _get_json("{}/version/{}".format(API_BASE, version_id))


def _get_project_data(project_id):
    return _get_json("{}/project/{}".format(API_BASE, project_id))


def _project_env(project):
    def side_value(field):
        value = project.get(field, "unknown")
        if value in ("required", "optional", "unsupported"):
            return value
        # La especificación de Modrinth permite unknown y valores no previstos.
        return "optional"

    return {
        "client": side_value("client_side"),
        "server": side_value("server_side"),
    }


def resolve_mod(version_id):
    """Obtiene el archivo principal, hashes, tamaño, URL y env de un mod."""
    try:
        version_data = _get_version_data(version_id)
        if not isinstance(version_data, dict):
            raise BuildError("La respuesta de versión no es un objeto JSON.")

        files = version_data.get("files")
        if not isinstance(files, list) or not files:
            raise BuildError("La versión no incluye archivos descargables.")

        primary = next(
            (file for file in files if isinstance(file, dict) and file.get("primary")),
            None,
        )
        if primary is None:
            primary = next((file for file in files if isinstance(file, dict)), None)
        if primary is None:
            raise BuildError("La lista de archivos no contiene un archivo utilizable.")

        url = primary.get("url")
        filename = primary.get("filename")
        hashes = primary.get("hashes")
        project_id = version_data.get("project_id")
        size = primary.get("size")

        if not _nonempty_string(url):
            raise BuildError("El archivo principal no tiene URL.")
        if not _nonempty_string(filename):
            raise BuildError("El archivo principal no tiene nombre.")
        if not _nonempty_string(project_id):
            raise BuildError("La versión no tiene project_id.")
        if not isinstance(hashes, dict):
            raise BuildError("El archivo principal no incluye hashes.")
        sha1 = hashes.get("sha1")
        sha512 = hashes.get("sha512")
        if not _nonempty_string(sha1) or not _nonempty_string(sha512):
            raise BuildError("El archivo principal debe incluir SHA1 y SHA512.")
        if not isinstance(size, int) or size < 0:
            raise BuildError("El archivo principal no incluye un tamaño válido.")

        project = _get_project_data(project_id)
        if not isinstance(project, dict):
            raise BuildError("La respuesta del proyecto no es un objeto JSON.")

        return {
            "version_id": version_id,
            "project_id": project_id,
            "url": url,
            "filename": filename,
            "sha1": sha1,
            "sha512": sha512,
            "size": size,
            "env": _project_env(project),
            "client_side": project.get("client_side", "unknown"),
            "server_side": project.get("server_side", "unknown"),
        }
    except BuildError as exc:
        raise BuildError(
            "No se pudieron obtener los datos del mod con version_id {!r}: {}".format(
                version_id, exc
            )
        ) from exc


def resolve_mods(manifest):
    return [resolve_mod(mod["version_id"]) for mod in manifest["mods"]]


def compiled_own_mod_jars():
    """Lista JAR compilados propios, excluyendo classifiers sources y dev."""
    jars = []
    mods_dir = ROOT / "mods-propios"
    if not mods_dir.exists():
        return jars

    for path in sorted(mods_dir.glob("**/build/libs/*.jar")):
        if path.name.endswith("-sources.jar") or path.name.endswith("-dev.jar"):
            continue
        jars.append(path)
    return jars


def _safe_pack_component(text):
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", text.strip())
    return text.strip(".-") or "modpack"


def _copy_tree_contents(source, destination):
    if not source.is_dir():
        return
    for item in sorted(source.iterdir()):
        target = destination / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)


def build_mrpack():
    manifest = read_manifest()
    resolved = resolve_mods(manifest)
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    pack_name = _safe_pack_component(manifest["name"])
    pack_version = _safe_pack_component(manifest["version"])
    output_path = DIST_DIR / "{}-{}.mrpack".format(pack_name, pack_version)

    index = {
        "formatVersion": 1,
        "game": "minecraft",
        "versionId": manifest["version"],
        "name": manifest["name"],
        "files": [
            {
                "path": "mods/{}".format(mod["filename"]),
                "hashes": {
                    "sha1": mod["sha1"],
                    "sha512": mod["sha512"],
                },
                "env": mod["env"],
                "downloads": [mod["url"]],
                "fileSize": mod["size"],
            }
            for mod in resolved
        ],
        "dependencies": {
            "minecraft": manifest["minecraft_version"],
            "fabric-loader": manifest["fabric_loader_version"],
        },
    }

    staging = DIST_DIR / ".mrpack-staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    (staging / "modrinth.index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    overrides = ROOT / "pack" / "overrides"
    if overrides.is_dir() and any(overrides.iterdir()):
        _copy_tree_contents(overrides, staging / "overrides")

    own_jars = compiled_own_mod_jars()
    if own_jars:
        own_mods_dir = staging / "overrides" / "mods"
        own_mods_dir.mkdir(parents=True, exist_ok=True)
        for jar in own_jars:
            shutil.copy2(jar, own_mods_dir / jar.name)

    try:
        with zipfile.ZipFile(
            output_path, "w", compression=zipfile.ZIP_DEFLATED
        ) as archive:
            for path in sorted(staging.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(staging).as_posix())
    finally:
        shutil.rmtree(staging, ignore_errors=True)

    print("Creado: {}".format(output_path))
    return output_path


if __name__ == "__main__":
    try:
        build_mrpack()
    except BuildError as error:
        print("ERROR: {}".format(error), file=sys.stderr)
        sys.exit(1)
