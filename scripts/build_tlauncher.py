#!/usr/bin/env python3
"""Crea el paquete ZIP listo para instalar en TLauncher."""

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

from build_mrpack import (
    BuildError,
    DIST_DIR,
    ROOT,
    USER_AGENT,
    _compiled_own_mod_jars,
    _safe_pack_stem,
    _copy_tree_files,
    read_manifest,
    get_modrinth_mods,
)

FABRIC_META_BASE = "https://meta.fabricmc.net/v2/versions/loader"


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


def fetch_fabric_profile(minecraft_version: str, loader_version: str) -> dict[str, Any]:
    mc = urllib.parse.quote(minecraft_version, safe="")
    loader = urllib.parse.quote(loader_version, safe="")
    url = f"{FABRIC_META_BASE}/{mc}/{loader}/profile/json"
    profile = _http_json(url)
    if not isinstance(profile, dict):
        raise BuildError(f"Fabric Meta no devolvio un perfil JSON valido: {url}")

    profile_id = profile.get("id")
    if not isinstance(profile_id, str) or not profile_id.strip():
        raise BuildError(f"El perfil de Fabric Meta no contiene un id valido: {url}")
    if not isinstance(profile.get("inheritsFrom"), str) or not profile["inheritsFrom"].strip():
        raise BuildError(f"El perfil de Fabric Meta no contiene inheritsFrom: {url}")
    return profile


def _nonempty_file(path: Path) -> bool:
    try:
        return path.is_file() and path.stat().st_size > 0
    except OSError:
        return False


def _write_tlauncher_manifest(path: Path, mods: list[dict[str, Any]]) -> None:
    # Los mods con client_side unsupported son exclusivos de servidor para el pack cliente.
    entries = []
    for mod in mods:
        if mod["client_side"] == "unsupported":
            continue
        entries.append(
            {
                "url": mod["url"],
                "sha1": mod["sha1"],
                "filename": mod["filename"],
                "size": mod["size"],
            }
        )
    path.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_tlauncher_zip() -> Path:
    manifest = read_manifest()
    mods = get_modrinth_mods(manifest)
    profile = fetch_fabric_profile(
        manifest["minecraft_version"],
        manifest["fabric_loader_version"],
    )

    profile_id = profile["id"]
    if any(char in profile_id for char in ("/", "\\", "..")):
        raise BuildError(f"Fabric Meta devolvio un id no seguro para una ruta: {profile_id!r}")

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    output = DIST_DIR / (
        f"{_safe_pack_stem(manifest['name'])}-"
        f"{_safe_pack_stem(manifest['version'])}-tlauncher.zip"
    )
    overrides = ROOT / "pack" / "overrides"
    launcher_files = ROOT / "tlauncher"
    own_jars = _compiled_own_mod_jars()

    required_launcher_files = ("instalar.ps1", "INSTALAR.bat", "LEEME.txt")
    for filename in required_launcher_files:
        path = launcher_files / filename
        if not path.is_file():
            raise BuildError(f"Falta el archivo requerido para el ZIP TLauncher: {path}")

    try:
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            profile_path = f"versions/{profile_id}/{profile_id}.json"
            archive.writestr(
                profile_path,
                json.dumps(profile, ensure_ascii=False, indent=2) + "\n",
            )

            if overrides.is_dir():
                for path in sorted(overrides.rglob("*")):
                    if not path.is_file() or not _nonempty_file(path):
                        continue
                    archive.write(path, path.relative_to(overrides).as_posix())

            for jar in own_jars:
                archive.write(jar, f"mods/{jar.name}")

            manifest_temp = DIST_DIR / "mods-terceros.json"
            _write_tlauncher_manifest(manifest_temp, mods)
            archive.write(manifest_temp, "mods-terceros.json")
            manifest_temp.unlink(missing_ok=True)

            for filename in required_launcher_files:
                archive.write(launcher_files / filename, filename)
    except (OSError, zipfile.BadZipFile) as exc:
        raise BuildError(f"No se pudo crear el ZIP de TLauncher {output}: {exc}") from exc

    print(f"Creado: {output}")
    return output


def main() -> int:
    try:
        build_tlauncher_zip()
        return 0
    except BuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
