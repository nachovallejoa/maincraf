#!/usr/bin/env python3
"""Construye el ZIP instalable para TLauncher; no distribuye JARs de terceros."""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any

from build_mrpack import (
    ROOT,
    compiled_own_mod_jars,
    fetch_modrinth_version,
    read_manifest,
)

USER_AGENT = "MarDeNubesTLauncherBuilder/1.0 (GitHub Actions; Fabric Meta client)"


def _safe_component(value: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip(".-")
    if not safe:
        raise ValueError("Nombre o versión no válido para el nombre del ZIP")
    return safe


def _get_fabric_profile(minecraft_version: str, loader_version: str) -> dict[str, Any]:
    url = (
        "https://meta.fabricmc.net/v2/versions/loader/"
        f"{urllib.parse.quote(minecraft_version, safe='')}/"
        f"{urllib.parse.quote(loader_version, safe='')}/profile/json"
    )
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            profile = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise ValueError(f"No se pudo obtener el perfil de Fabric desde {url}: {exc}") from exc

    if not isinstance(profile, dict):
        raise ValueError(f"El perfil de Fabric devuelto por {url} no es un objeto JSON")
    profile_id = profile.get("id")
    if not isinstance(profile_id, str) or not profile_id.strip():
        raise ValueError(f"El perfil de Fabric de {url} no contiene un id válido")
    if any(part in profile_id for part in ("/", "\\", "..")):
        raise ValueError(f"El id de versión de Fabric no es seguro: {profile_id!r}")
    return profile


def _copy_overrides_to_zip(archive: zipfile.ZipFile, source: Path) -> None:
    if not source.is_dir():
        return
    for item in sorted(source.rglob("*")):
        if not item.is_file() or item.stat().st_size == 0:
            continue
        relative = item.relative_to(source).as_posix()
        archive.write(item, relative)


def _add_own_mods(archive: zipfile.ZipFile, root: Path) -> None:
    for jar in compiled_own_mod_jars(root):
        archive.write(jar, (PurePosixPath("mods") / jar.name).as_posix())


def build_tlauncher(
    root: Path | str = ROOT,
    manifest: dict[str, Any] | None = None,
) -> Path:
    root_path = Path(root)
    if manifest is None:
        manifest = read_manifest(root_path / "pack" / "mods.json")

    profile = _get_fabric_profile(
        manifest["minecraft_version"],
        manifest["fabric_loader_version"],
    )
    profile_id = profile["id"]

    third_party: list[dict[str, Any]] = []
    for mod in manifest["mods"]:
        details = fetch_modrinth_version(mod["version_id"])
        # El instalador es para el cliente. No incluir archivos exclusivamente
        # de servidor, según la información de entorno que responde la API.
        if details["client_side"] == "unsupported":
            continue
        third_party.append(
            {
                "url": details["url"],
                "sha1": details["sha1"],
                "filename": details["filename"],
                "size": details["size"],
            }
        )

    dist = root_path / "dist"
    dist.mkdir(parents=True, exist_ok=True)
    filename = (
        f"{_safe_component(manifest['name'])}-"
        f"{_safe_component(manifest['version'])}-tlauncher.zip"
    )
    output = dist / filename
    version_relative = PurePosixPath("versions") / profile_id / f"{profile_id}.json"

    try:
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(
                version_relative.as_posix(),
                json.dumps(profile, ensure_ascii=False, indent=2) + "\n",
            )
            _copy_overrides_to_zip(archive, root_path / "pack" / "overrides")
            _add_own_mods(archive, root_path)
            archive.writestr(
                "mods-terceros.json",
                json.dumps(third_party, ensure_ascii=False, indent=2) + "\n",
            )

            for relative in (
                Path("tlauncher") / "instalar.ps1",
                Path("tlauncher") / "INSTALAR.bat",
                Path("tlauncher") / "LEEME.txt",
            ):
                source = root_path / relative
                if not source.is_file():
                    raise ValueError(f"Falta el archivo requerido para el ZIP: {source}")
                archive.write(source, source.name)
    except OSError as exc:
        raise ValueError(f"No se pudo escribir el ZIP de TLauncher {output}: {exc}") from exc

    return output


def main() -> int:
    try:
        manifest = read_manifest()
        output = build_tlauncher(ROOT, manifest)
        print(f"ZIP para TLauncher creado: {output}")
        return 0
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
