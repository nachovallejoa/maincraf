#!/usr/bin/env python3
"""Crea el archivo .mrpack usando Modrinth y los datos locales del pack."""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "pack" / "mods.json"
DIST_DIR = ROOT / "dist"
USER_AGENT = "DerivaModpackBuilder/1.0 (GitHub Actions; contact: repository maintainers)"


class BuildError(RuntimeError):
    pass


def _read_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as stream:
            return json.load(stream)
    except FileNotFoundError as exc:
        raise BuildError(f"No existe el manifiesto requerido: {path}") from exc
    except json.JSONDecodeError as exc:
        raise BuildError(f"JSON invalido en {path}: {exc}") from exc


def _first_nonempty(mapping: dict[str, Any], names: tuple[str, ...]) -> str | None:
    for name in names:
        value = mapping.get(name)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def read_manifest(path: Path = MANIFEST_PATH) -> dict[str, Any]:
    """Lee el manifiesto con alias de campos tolerantes y valida lo imprescindible."""
    raw = _read_json(path)
    if not isinstance(raw, dict):
        raise BuildError(f"El manifiesto debe ser un objeto JSON: {path}")

    minecraft_version = _first_nonempty(raw, ("minecraft_version", "game_version"))
    loader_version = _first_nonempty(raw, ("fabric_loader_version", "loader_version"))

    if not minecraft_version:
        raise BuildError(
            "Falta minecraft_version (o game_version) o esta vacio en pack/mods.json."
        )
    if not loader_version:
        raise BuildError(
            "Falta fabric_loader_version (o loader_version) o esta vacio en pack/mods.json."
        )

    mods = raw.get("mods")
    if not isinstance(mods, list):
        raise BuildError("El campo 'mods' debe ser una lista en pack/mods.json.")

    normalized_mods: list[dict[str, Any]] = []
    for index, item in enumerate(mods, start=1):
        if not isinstance(item, dict):
            raise BuildError(f"El mod #{index} no es un objeto JSON.")
        version_id = _first_nonempty(item, ("version_id", "id"))
        if not version_id:
            raise BuildError(f"Falta version_id (o id) del mod #{index} en pack/mods.json.")
        normalized_mods.append({"version_id": version_id})

    name = _first_nonempty(raw, ("name",)) or "modpack"
    pack_version = _first_nonempty(raw, ("version",)) or "1.0.0"

    return {
        "name": name,
        "version": pack_version,
        "minecraft_version": minecraft_version,
        "fabric_loader_version": loader_version,
        "mods": normalized_mods,
    }


def _http_json(url: str) -> Any:
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
        raise BuildError(f"Fallo consultando {url}: {exc}") from exc


def get_modrinth_mod_data(version_id: str) -> dict[str, Any]:
    """Obtiene version y proyecto de Modrinth. Compartida con build_tlauncher.py."""
    if not isinstance(version_id, str) or not version_id.strip():
        raise BuildError("Se intento consultar un id de version Modrinth vacio.")

    version_url = "https://api.modrinth.com/v2/version/" + urllib.parse.quote(
        version_id.strip(), safe=""
    )
    try:
        version = _http_json(version_url)
        if not isinstance(version, dict):
            raise BuildError("La respuesta de version no es un objeto JSON.")

        files = version.get("files")
        if not isinstance(files, list) or not files:
            raise BuildError("La version no contiene archivos descargables.")
        primary = next(
            (file for file in files if isinstance(file, dict) and file.get("primary") is True),
            None,
        )
        if primary is None:
            primary = next((file for file in files if isinstance(file, dict)), None)
        if not primary:
            raise BuildError("No se encontro archivo principal en la version.")

        file_url = primary.get("url")
        filename = primary.get("filename")
        hashes = primary.get("hashes")
        if not isinstance(file_url, str) or not file_url.strip():
            raise BuildError("El archivo principal no incluye una URL.")
        if not isinstance(filename, str) or not filename.strip():
            raise BuildError("El archivo principal no incluye filename.")
        if not isinstance(hashes, dict):
            raise BuildError("El archivo principal no incluye hashes.")
        sha1 = hashes.get("sha1")
        sha512 = hashes.get("sha512")
        project_id = version.get("project_id")
        if not isinstance(sha1, str) or not sha1.strip():
            raise BuildError("El archivo principal no incluye hash sha1.")
        if not isinstance(sha512, str) or not sha512.strip():
            raise BuildError("El archivo principal no incluye hash sha512.")
        if not isinstance(project_id, str) or not project_id.strip():
            raise BuildError("La version no incluye project_id.")

        size = primary.get("size")
        if not isinstance(size, int) or size < 0:
            raise BuildError("El archivo principal no incluye un size valido.")

        project_url = "https://api.modrinth.com/v2/project/" + urllib.parse.quote(
            project_id, safe=""
        )
        project = _http_json(project_url)
        if not isinstance(project, dict):
            raise BuildError("La respuesta del proyecto no es un objeto JSON.")

        client_side = _normalize_env(project.get("client_side"))
        server_side = _normalize_env(project.get("server_side"))

        return {
            "version_id": version_id,
            "project_id": project_id,
            "url": file_url,
            "filename": filename,
            "sha1": sha1,
            "sha512": sha512,
            "size": size,
            "client_side": client_side,
            "server_side": server_side,
        }
    except BuildError as exc:
        raise BuildError(f"Modrinth version_id '{version_id}': {exc}") from exc


def _normalize_env(value: Any) -> str:
    if value in ("required", "optional", "unsupported"):
        return value
    return "optional"


def get_modrinth_mods(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    """Consulta los metadatos completos de cada mod indicado por el manifiesto."""
    results: list[dict[str, Any]] = []
    for item in manifest["mods"]:
        version_id = item["version_id"]
        results.append(get_modrinth_mod_data(version_id))
    return results


def _safe_pack_stem(name: str) -> str:
    cleaned = re.sub(r"[^\w.-]+", "-", name.strip(), flags=re.UNICODE).strip("-.")
    return cleaned or "modpack"


def _copy_tree_files(archive: zipfile.ZipFile, source: Path, prefix: str) -> None:
    if not source.is_dir():
        return
    for path in sorted(source.rglob("*")):
        if path.is_file():
            relative = path.relative_to(source).as_posix()
            archive.write(path, f"{prefix}/{relative}" if prefix else relative)


def _compiled_own_mod_jars() -> list[Path]:
    base = ROOT / "mods-propios"
    if not base.is_dir():
        return []
    jars: list[Path] = []
    for jar in sorted(base.glob("**/build/libs/*.jar")):
        if jar.name.endswith("-sources.jar") or jar.name.endswith("-dev.jar"):
            continue
        jars.append(jar)
    return jars


def build_mrpack() -> Path:
    manifest = read_manifest()
    mod_data = get_modrinth_mods(manifest)

    index = {
        "formatVersion": 1,
        "game": "minecraft",
        "versionId": manifest["version"],
        "name": manifest["name"],
        "files": [
            {
                "path": f"mods/{mod['filename']}",
                "hashes": {
                    "sha1": mod["sha1"],
                    "sha512": mod["sha512"],
                },
                "env": {
                    "client": mod["client_side"],
                    "server": mod["server_side"],
                },
                "downloads": [mod["url"]],
                "fileSize": mod["size"],
            }
            for mod in mod_data
        ],
        "dependencies": {
            "minecraft": manifest["minecraft_version"],
            "fabric-loader": manifest["fabric_loader_version"],
        },
    }

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    output = DIST_DIR / (
        f"{_safe_pack_stem(manifest['name'])}-{_safe_pack_stem(manifest['version'])}.mrpack"
    )

    overrides = ROOT / "pack" / "overrides"
    own_jars = _compiled_own_mod_jars()

    try:
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(
                "modrinth.index.json",
                json.dumps(index, ensure_ascii=False, indent=2) + "\n",
            )
            if overrides.is_dir():
                _copy_tree_files(archive, overrides, "overrides")
            for jar in own_jars:
                archive.write(jar, f"overrides/mods/{jar.name}")
    except OSError as exc:
        raise BuildError(f"No se pudo escribir el paquete .mrpack {output}: {exc}") from exc

    print(f"Creado: {output}")
    return output


def main() -> int:
    try:
        build_mrpack()
        return 0
    except BuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
