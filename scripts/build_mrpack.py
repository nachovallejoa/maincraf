#!/usr/bin/env python3
"""Build a Modrinth .mrpack using a flexible pack/mods.json manifest.

Only Python's standard library is used. Third-party mods are resolved from
Modrinth during the build; no third-party mod binaries are stored in the repo.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "pack" / "mods.json"
OUTPUT_DIR = ROOT / "dist"
USER_AGENT = "MarDeNubes-ModpackBuilder/1.0 (GitHub Actions)"
MODRINTH_API = "https://api.modrinth.com/v2"


class BuildError(RuntimeError):
    """Raised for invalid manifest data or failed API/download operations."""


def _text(value: Any) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def read_manifest(path: Path | str = MANIFEST_PATH) -> dict[str, Any]:
    """Read pack/mods.json and normalize the required flexible fields.

    Every mod entry must contain a Modrinth version ID in `version_id` or `id`.
    Other mod metadata is obtained from the Modrinth API by
    `fetch_modrinth_release`.
    """
    manifest_path = Path(path)
    try:
        with manifest_path.open("r", encoding="utf-8") as stream:
            raw = json.load(stream)
    except FileNotFoundError as exc:
        raise BuildError(f"No existe el manifiesto: {manifest_path}") from exc
    except json.JSONDecodeError as exc:
        raise BuildError(
            f"JSON invalido en {manifest_path}, linea {exc.lineno}, "
            f"columna {exc.colno}: {exc.msg}"
        ) from exc

    if not isinstance(raw, dict):
        raise BuildError(f"El manifiesto {manifest_path} debe ser un objeto JSON.")

    minecraft_version = _text(raw.get("minecraft_version")) or _text(
        raw.get("game_version")
    )
    if not minecraft_version:
        raise BuildError(
            "Falta minecraft_version (o game_version) con un valor no vacio "
            "en pack/mods.json."
        )

    loader_version = _text(raw.get("fabric_loader_version")) or _text(
        raw.get("loader_version")
    )
    if not loader_version:
        raise BuildError(
            "Falta fabric_loader_version (o loader_version) con un valor no "
            "vacio en pack/mods.json."
        )

    pack_name = _text(raw.get("name")) or "modpack"
    pack_version = _text(raw.get("version")) or "1.0.0"

    raw_mods = raw.get("mods", [])
    if not isinstance(raw_mods, list):
        raise BuildError("El campo mods de pack/mods.json debe ser una lista.")

    normalized_mods: list[dict[str, Any]] = []
    for index, mod in enumerate(raw_mods):
        if not isinstance(mod, dict):
            raise BuildError(f"mods[{index}] debe ser un objeto JSON.")
        version_id = _text(mod.get("version_id")) or _text(mod.get("id"))
        if not version_id:
            label = _text(mod.get("name")) or _text(mod.get("slug")) or f"mods[{index}]"
            raise BuildError(
                f"Falta el id de version de Modrinth (version_id o id) para {label}."
            )
        normalized = dict(mod)
        normalized["version_id"] = version_id
        normalized_mods.append(normalized)

    result = dict(raw)
    result["name"] = pack_name
    result["version"] = pack_version
    result["minecraft_version"] = minecraft_version
    result["fabric_loader_version"] = loader_version
    result["mods"] = normalized_mods
    return result


def _request_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise BuildError(f"Fallo la consulta a {url}: {exc}") from exc
    if not isinstance(data, dict):
        raise BuildError(f"La respuesta de {url} no es un objeto JSON.")
    return data


def _side(value: Any) -> str:
    """Normalize Modrinth client/server side values for mrpack env metadata."""
    side = _text(value)
    if side in {"required", "optional", "unsupported"}:
        return side
    # Modrinth's unknown/absent side is treated as optional for this index.
    return "optional"


def fetch_modrinth_release(mod: dict[str, Any]) -> dict[str, Any]:
    """Fetch and normalize one Modrinth release and its project environment.

    Public helper intentionally shared with build_tlauncher.py.
    """
    version_id = _text(mod.get("version_id")) or _text(mod.get("id"))
    if not version_id:
        label = _text(mod.get("name")) or _text(mod.get("slug")) or "mod sin nombre"
        raise BuildError(f"Falta el ID de version de Modrinth para {label}.")

    label = (
        _text(mod.get("name"))
        or _text(mod.get("slug"))
        or _text(mod.get("file_name"))
        or version_id
    )

    try:
        version_data = _request_json(f"{MODRINTH_API}/version/{version_id}")
        project_id = _text(version_data.get("project_id"))
        files = version_data.get("files")
        if not project_id:
            raise BuildError(f"Modrinth no devolvio project_id para {label} ({version_id}).")
        if not isinstance(files, list) or not files:
            raise BuildError(f"Modrinth no devolvio archivos para {label} ({version_id}).")

        primary = next(
            (
                item
                for item in files
                if isinstance(item, dict) and item.get("primary") is True
            ),
            None,
        )
        if primary is None:
            primary = next((item for item in files if isinstance(item, dict)), None)
        if not isinstance(primary, dict):
            raise BuildError(f"No hay archivo principal utilizable para {label} ({version_id}).")

        url = _text(primary.get("url"))
        filename = _text(primary.get("filename"))
        hashes = primary.get("hashes")
        if not isinstance(hashes, dict):
            hashes = {}
        sha1 = _text(hashes.get("sha1"))
        sha512 = _text(hashes.get("sha512"))
        size = primary.get("size")

        if not url or not filename or not sha1 or not sha512:
            raise BuildError(
                f"El archivo principal de {label} ({version_id}) no tiene "
                "url, filename, sha1 y sha512 completos."
            )
        if not isinstance(size, int) or size < 0:
            raise BuildError(f"El archivo principal de {label} ({version_id}) no tiene size valido.")

        project_data = _request_json(f"{MODRINTH_API}/project/{project_id}")
        client_side = _side(project_data.get("client_side"))
        server_side = _side(project_data.get("server_side"))

        return {
            "version_id": version_id,
            "project_id": project_id,
            "name": label,
            "url": url,
            "filename": filename,
            "sha1": sha1.lower(),
            "sha512": sha512.lower(),
            "size": size,
            "env": {
                "client": client_side,
                "server": server_side,
            },
            "version_data": version_data,
            "project_data": project_data,
        }
    except BuildError as exc:
        raise BuildError(f"No se pudieron obtener los datos de {label}: {exc}") from exc


def compiled_own_mod_jars(root: Path | str = ROOT) -> list[Path]:
    """List own compiled mod JARs, excluding sources and development JARs."""
    base = Path(root)
    results: list[Path] = []
    own_mods_root = base / "mods-propios"
    if not own_mods_root.exists():
        return results

    for jar in sorted(own_mods_root.glob("**/build/libs/*.jar")):
        lower_name = jar.name.lower()
        if lower_name.endswith("-sources.jar") or lower_name.endswith("-dev.jar"):
            continue
        results.append(jar)
    return results


def _safe_relative_filename(filename: str, label: str) -> str:
    # Modrinth filenames are expected to be simple archive filenames. Reject
    # path traversal rather than silently extracting untrusted paths.
    if Path(filename).name != filename or filename in {"", ".", ".."}:
        raise BuildError(f"Nombre de archivo inseguro para {label}: {filename!r}")
    return filename


def _copy_overrides(root: Path, archive: zipfile.ZipFile) -> None:
    overrides = root / "pack" / "overrides"
    if not overrides.exists() or not overrides.is_dir():
        return

    for path in sorted(overrides.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(overrides)
        archive.write(path, Path("overrides") / relative)


def build_mrpack(root: Path | str = ROOT) -> Path:
    base = Path(root)
    manifest = read_manifest(base / "pack" / "mods.json")
    releases = [fetch_modrinth_release(mod) for mod in manifest["mods"]]

    index_files: list[dict[str, Any]] = []
    for release in releases:
        filename = _safe_relative_filename(release["filename"], release["name"])
        index_files.append(
            {
                "path": f"mods/{filename}",
                "hashes": {
                    "sha1": release["sha1"],
                    "sha512": release["sha512"],
                },
                "env": release["env"],
                "downloads": [release["url"]],
                "fileSize": release["size"],
            }
        )

    index = {
        "formatVersion": 1,
        "game": "minecraft",
        "versionId": manifest["version"],
        "name": manifest["name"],
        "files": index_files,
        "dependencies": {
            "minecraft": manifest["minecraft_version"],
            "fabric-loader": manifest["fabric_loader_version"],
        },
    }

    output_dir = base / "dist"
    output_dir.mkdir(parents=True, exist_ok=True)
    pack_stem = re.sub(r"[^A-Za-z0-9._-]+", "-", manifest["name"]).strip("-._")
    if not pack_stem:
        pack_stem = "modpack"
    version_stem = re.sub(r"[^A-Za-z0-9._-]+", "-", manifest["version"]).strip("-._")
    if not version_stem:
        version_stem = "1.0.0"
    output_path = output_dir / f"{pack_stem}-{version_stem}.mrpack"

    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(
            "modrinth.index.json",
            json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        )
        _copy_overrides(base, archive)

        own_jars = compiled_own_mod_jars(base)
        for jar in own_jars:
            archive.write(jar, Path("overrides") / "mods" / jar.name)

    return output_path


def main() -> int:
    try:
        output = build_mrpack()
    except BuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Creado: {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
