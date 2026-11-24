#!/usr/bin/env python3
"""Construye un .mrpack sin guardar JARs de mods de terceros en el repositorio."""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "pack" / "mods.json"
OVERRIDES_PATH = ROOT / "pack" / "overrides"
DIST_PATH = ROOT / "dist"
USER_AGENT = "MarDeNubesModpackBuilder/1.0 (GitHub Actions; Modrinth API client)"


def _nonempty_string(value: Any) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def read_manifest(path: Path | str = MANIFEST_PATH) -> dict[str, Any]:
    """Lee y valida el manifiesto del pack."""
    manifest_path = Path(path)
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"No existe el manifiesto: {manifest_path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"JSON no válido en {manifest_path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"El manifiesto debe ser un objeto JSON: {manifest_path}")

    minecraft_version = _nonempty_string(
        data.get("minecraft_version") or data.get("game_version")
    )
    loader_version = _nonempty_string(
        data.get("fabric_loader_version") or data.get("loader_version")
    )
    if not minecraft_version:
        raise ValueError(
            f"Falta minecraft_version (o game_version) en {manifest_path}"
        )
    if not loader_version:
        raise ValueError(
            f"Falta fabric_loader_version (o loader_version) en {manifest_path}"
        )

    mods = data.get("mods", [])
    if mods is None:
        mods = []
    if not isinstance(mods, list):
        raise ValueError(f"El campo mods debe ser una lista en {manifest_path}")

    normalized_mods: list[dict[str, Any]] = []
    for index, mod in enumerate(mods):
        if not isinstance(mod, dict):
            raise ValueError(f"mods[{index}] debe ser un objeto JSON")
        version_id = _nonempty_string(mod.get("version_id") or mod.get("id"))
        if not version_id:
            raise ValueError(
                f"mods[{index}] no contiene un id de versión de Modrinth "
                "(version_id o id)"
            )
        normalized_mods.append({**mod, "version_id": version_id})

    pack_name = _nonempty_string(data.get("name")) or "modpack"
    pack_version = _nonempty_string(data.get("version")) or "1.0.0"

    return {
        **data,
        "name": pack_name,
        "version": pack_version,
        "minecraft_version": minecraft_version,
        "fabric_loader_version": loader_version,
        "mods": normalized_mods,
    }


def _api_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            result = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise ValueError(f"Falló la consulta a {url}: {exc}") from exc
    if not isinstance(result, dict):
        raise ValueError(f"La respuesta de {url} no es un objeto JSON")
    return result


def fetch_modrinth_version(version_id: str) -> dict[str, Any]:
    """Obtiene metadatos completos de versión/proyecto desde Modrinth."""
    try:
        version = _api_json(
            "https://api.modrinth.com/v2/version/" + urllib.parse.quote(version_id)
        )
        files = version.get("files")
        if not isinstance(files, list) or not files:
            raise ValueError("la versión no contiene archivos")

        primary_file = next(
            (item for item in files if isinstance(item, dict) and item.get("primary")),
            next((item for item in files if isinstance(item, dict)), None),
        )
        if not isinstance(primary_file, dict):
            raise ValueError("no se encontró archivo principal")

        url = _nonempty_string(primary_file.get("url"))
        filename = _nonempty_string(primary_file.get("filename"))
        hashes = primary_file.get("hashes")
        project_id = _nonempty_string(version.get("project_id"))
        size = primary_file.get("size")

        if not url or not filename or not isinstance(hashes, dict):
            raise ValueError("faltan url, filename o hashes en el archivo principal")
        sha1 = _nonempty_string(hashes.get("sha1"))
        sha512 = _nonempty_string(hashes.get("sha512"))
        if not sha1 or not sha512:
            raise ValueError("faltan los hashes sha1 o sha512")
        if not isinstance(size, int) or isinstance(size, bool) or size < 0:
            raise ValueError("el tamaño del archivo no es un entero válido")
        if not project_id:
            raise ValueError("la versión no contiene project_id")

        project = _api_json(
            "https://api.modrinth.com/v2/project/"
            + urllib.parse.quote(project_id)
        )
        client_side = _modrinth_environment(project.get("client_side"))
        server_side = _modrinth_environment(project.get("server_side"))

        return {
            "version_id": version_id,
            "project_id": project_id,
            "url": url,
            "filename": filename,
            "sha1": sha1,
            "sha512": sha512,
            "size": size,
            "client_side": client_side,
            "server_side": server_side,
        }
    except Exception as exc:
        raise ValueError(
            f"No se pudieron obtener los datos de Modrinth para "
            f"la versión {version_id}: {exc}"
        ) from exc


def _modrinth_environment(value: Any) -> str:
    if value in ("required", "optional", "unsupported"):
        return value
    # Modrinth usa valores desconocidos/no proporcionados; se consideran
    # opcionales para no declarar incompatibilidad sin evidencia.
    return "optional"


def compiled_own_mod_jars(root: Path | str = ROOT) -> list[Path]:
    """Devuelve JARs compilados propios, excluyendo sources y dev."""
    root_path = Path(root)
    mods_root = root_path / "mods-propios"
    if not mods_root.is_dir():
        return []
    jars = []
    for jar in mods_root.glob("**/build/libs/*.jar"):
        if jar.name.endswith("-sources.jar") or jar.name.endswith("-dev.jar"):
            continue
        jars.append(jar)
    return sorted(jars)


def _safe_pack_component(value: str) -> str:
    value = value.strip()
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip(".-")
    if not value:
        raise ValueError("El nombre o versión del pack no sirve para un nombre de archivo")
    return value


def _add_overrides(
    archive: zipfile.ZipFile,
    overrides_dir: Path,
    include_empty_files: bool = True,
) -> None:
    if not overrides_dir.is_dir():
        return
    for source in sorted(overrides_dir.rglob("*")):
        if not source.is_file():
            continue
        relative = source.relative_to(overrides_dir).as_posix()
        archive_name = (PurePosixPath("overrides") / relative).as_posix()
        archive.write(source, archive_name)


def _add_own_jars(archive: zipfile.ZipFile, root: Path) -> None:
    for jar in compiled_own_mod_jars(root):
        archive.write(jar, (PurePosixPath("overrides") / "mods" / jar.name).as_posix())


def build_mrpack(
    root: Path | str = ROOT,
    manifest: dict[str, Any] | None = None,
) -> Path:
    root_path = Path(root)
    if manifest is None:
        manifest = read_manifest(root_path / "pack" / "mods.json")

    files = []
    for mod in manifest["mods"]:
        version_data = fetch_modrinth_version(mod["version_id"])
        files.append(
            {
                "path": f"mods/{version_data['filename']}",
                "hashes": {
                    "sha1": version_data["sha1"],
                    "sha512": version_data["sha512"],
                },
                "env": {
                    "client": version_data["client_side"],
                    "server": version_data["server_side"],
                },
                "downloads": [version_data["url"]],
                "fileSize": version_data["size"],
            }
        )

    index = {
        "formatVersion": 1,
        "game": "minecraft",
        "versionId": manifest["version"],
        "name": manifest["name"],
        "files": files,
        "dependencies": {
            "minecraft": manifest["minecraft_version"],
            "fabric-loader": manifest["fabric_loader_version"],
        },
    }

    DIST_PATH_LOCAL = root_path / "dist"
    DIST_PATH_LOCAL.mkdir(parents=True, exist_ok=True)
    archive_name = (
        f"{_safe_pack_component(manifest['name'])}-"
        f"{_safe_pack_component(manifest['version'])}.mrpack"
    )
    output = DIST_PATH_LOCAL / archive_name

    try:
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(
                "modrinth.index.json",
                json.dumps(index, ensure_ascii=False, indent=2) + "\n",
            )
            _add_overrides(
                archive,
                root_path / "pack" / "overrides",
                include_empty_files=True,
            )
            _add_own_jars(archive, root_path)
    except OSError as exc:
        raise ValueError(f"No se pudo escribir el archivo .mrpack {output}: {exc}") from exc

    return output


def main() -> int:
    try:
        manifest = read_manifest()
        output = build_mrpack(ROOT, manifest)
        print(f".mrpack creado: {output}")
        return 0
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
