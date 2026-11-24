#!/usr/bin/env python3
"""Construye el paquete Modrinth .mrpack desde pack/mods.json."""

import json
import os
import re
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "pack" / "mods.json"
MODRINTH_API = "https://api.modrinth.com/v2"
USER_AGENT = "MarDeNubes-ModpackBuilder/1.0 (GitHub Actions)"
DIST = ROOT / "dist"


def _nonempty_text(value):
    return isinstance(value, str) and bool(value.strip())


def read_manifest(path=None):
    """Lee el manifiesto y comprueba los campos requeridos para construir."""
    manifest_path = Path(path) if path is not None else MANIFEST_PATH
    if not manifest_path.is_file():
        raise ValueError(f"No existe el manifiesto requerido: {manifest_path}")

    try:
        with manifest_path.open("r", encoding="utf-8") as stream:
            data = json.load(stream)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"No se pudo leer {manifest_path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"El manifiesto debe ser un objeto JSON: {manifest_path}")

    mc_version = data.get("minecraft_version") or data.get("game_version")
    loader_version = data.get("fabric_loader_version") or data.get("loader_version")
    if not _nonempty_text(mc_version):
        raise ValueError(
            f"Falta minecraft_version (o game_version) o está vacío en {manifest_path}"
        )
    if not _nonempty_text(loader_version):
        raise ValueError(
            f"Falta fabric_loader_version (o loader_version) o está vacío en {manifest_path}"
        )

    mods = data.get("mods")
    if not isinstance(mods, list):
        raise ValueError(f"El campo 'mods' debe ser una lista en {manifest_path}")

    name = data.get("name")
    if not _nonempty_text(name):
        name = "modpack"

    version = data.get("version")
    if not _nonempty_text(version):
        version = "1.0.0"

    return {
        "raw": data,
        "name": name.strip(),
        "version": version.strip(),
        "minecraft_version": mc_version.strip(),
        "fabric_loader_version": loader_version.strip(),
        "mods": mods,
    }


def _request_json(url):
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
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        raise RuntimeError(f"Consulta fallida a {url}: {exc}") from exc


def _version_id(mod, position):
    if not isinstance(mod, dict):
        raise ValueError(f"El elemento mods[{position}] no es un objeto JSON")
    value = mod.get("version_id")
    if not _nonempty_text(value):
        value = mod.get("id")
    if not _nonempty_text(value):
        raise ValueError(
            f"mods[{position}] no tiene un id de versión Modrinth "
            "(se requiere version_id o id)"
        )
    return value.strip()


def _modrinth_side(value):
    if value in ("required", "optional", "unsupported"):
        return value
    # Modrinth identifica estados desconocidos como unknown. Para el formato
    # del manifiesto, la regla solicitada los trata como optional.
    return "optional"


def fetch_modrinth_version(version_id):
    """Obtiene los datos de archivo y entorno de una versión de Modrinth."""
    version_url = f"{MODRINTH_API}/version/{version_id}"
    try:
        version = _request_json(version_url)
        files = version.get("files")
        if not isinstance(files, list) or not files:
            raise ValueError("la versión no contiene archivos")

        file_info = next(
            (item for item in files if isinstance(item, dict) and item.get("primary") is True),
            None,
        )
        if file_info is None:
            file_info = next((item for item in files if isinstance(item, dict)), None)
        if file_info is None:
            raise ValueError("no se encontró archivo principal ni primer archivo")

        filename = file_info.get("filename")
        url = file_info.get("url")
        hashes = file_info.get("hashes")
        size = file_info.get("size")
        project_id = version.get("project_id")

        if not _nonempty_text(filename):
            raise ValueError("falta filename")
        if not _nonempty_text(url):
            raise ValueError("falta url de descarga")
        if not isinstance(hashes, dict):
            raise ValueError("faltan hashes")
        if not _nonempty_text(hashes.get("sha1")):
            raise ValueError("falta el hash sha1")
        if not _nonempty_text(hashes.get("sha512")):
            raise ValueError("falta el hash sha512")
        if not isinstance(size, int) or isinstance(size, bool) or size < 0:
            raise ValueError("falta un size entero válido")
        if not _nonempty_text(project_id):
            raise ValueError("falta project_id")

        project_url = f"{MODRINTH_API}/project/{project_id}"
        project = _request_json(project_url)
        environment = project.get("environment")
        if not isinstance(environment, dict):
            raise ValueError("el proyecto no contiene environment")

        return {
            "version_id": version_id,
            "project_id": project_id,
            "filename": filename,
            "url": url,
            "sha1": hashes["sha1"],
            "sha512": hashes["sha512"],
            "size": size,
            "env": {
                "client": _modrinth_side(environment.get("client_side")),
                "server": _modrinth_side(environment.get("server_side")),
            },
        }
    except Exception as exc:
        raise RuntimeError(f"No se pudieron obtener datos del mod {version_id}: {exc}") from exc


def get_modrinth_mods(manifest):
    """Consulta Modrinth para todos los mods del manifiesto."""
    results = []
    for position, mod in enumerate(manifest["mods"]):
        version_id = _version_id(mod, position)
        results.append(fetch_modrinth_version(version_id))
    return results


def compiled_own_mod_jars():
    """Encuentra JAR compilados propios, excluyendo sources y dev."""
    base = ROOT / "mods-propios"
    if not base.is_dir():
        return []
    jars = []
    for jar in base.glob("**/build/libs/*.jar"):
        if jar.name.endswith("-sources.jar") or jar.name.endswith("-dev.jar"):
            continue
        jars.append(jar)
    return sorted(jars)


def _safe_pack_filename(filename):
    candidate = PurePosixPath(filename.replace("\\", "/"))
    if candidate.is_absolute() or ".." in candidate.parts or len(candidate.parts) != 1:
        raise ValueError(f"Nombre de archivo no válido de Modrinth: {filename!r}")
    return candidate.name


def _safe_zip_component(value):
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip(".-")
    return text or "modpack"


def _add_tree(zip_file, source, archive_prefix, skip_empty=False):
    if not source.exists():
        return
    if source.is_file():
        if skip_empty and source.stat().st_size == 0:
            return
        zip_file.write(source, archive_prefix)
        return

    for file_path in sorted(source.rglob("*")):
        if not file_path.is_file():
            continue
        if skip_empty and file_path.stat().st_size == 0:
            continue
        relative = file_path.relative_to(source).as_posix()
        zip_file.write(file_path, f"{archive_prefix}/{relative}")


def build():
    manifest = read_manifest()
    mods = get_modrinth_mods(manifest)

    index = {
        "formatVersion": 1,
        "game": "minecraft",
        "versionId": manifest["version"],
        "name": manifest["name"],
        "files": [
            {
                "path": f"mods/{_safe_pack_filename(mod['filename'])}",
                "hashes": {
                    "sha1": mod["sha1"],
                    "sha512": mod["sha512"],
                },
                "env": mod["env"],
                "downloads": [mod["url"]],
                "fileSize": mod["size"],
            }
            for mod in mods
        ],
        "dependencies": {
            "minecraft": manifest["minecraft_version"],
            "fabric-loader": manifest["fabric_loader_version"],
        },
    }

    DIST.mkdir(parents=True, exist_ok=True)
    archive_name = (
        f"{_safe_zip_component(manifest['name'])}-"
        f"{_safe_zip_component(manifest['version'])}.mrpack"
    )
    archive_path = DIST / archive_name

    with zipfile.ZipFile(
        archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        archive.writestr(
            "modrinth.index.json",
            json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        )

        overrides = ROOT / "pack" / "overrides"
        if overrides.is_dir():
            _add_tree(archive, overrides, "overrides")

        for jar in compiled_own_mod_jars():
            archive.write(jar, f"overrides/mods/{jar.name}")

    print(f"Creado: {archive_path}")


if __name__ == "__main__":
    try:
        build()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
