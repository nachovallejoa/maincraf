#!/usr/bin/env python3
"""Construye el ZIP de instalación para TLauncher."""

import json
import re
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath

from build_mrpack import (
    DIST,
    ROOT,
    USER_AGENT,
    compiled_own_mod_jars,
    get_modrinth_mods,
    read_manifest,
)

FABRIC_META = "https://meta.fabricmc.net/v2/versions/loader"
THIRD_PARTY_FILENAME = "mods-terceros.json"
INSTALLER_FILES = (
    "instalar.ps1",
    "INSTALAR.bat",
    "LEEME.txt",
)


def _safe_component(value):
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip(".-")
    return cleaned or "modpack"


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


def fetch_fabric_profile(mc_version, loader_version):
    url = (
        f"{FABRIC_META}/{mc_version}/{loader_version}/profile/json"
    )
    try:
        profile = _request_json(url)
        if not isinstance(profile, dict):
            raise ValueError("la respuesta no es un objeto JSON")
        profile_id = profile.get("id")
        if not isinstance(profile_id, str) or not profile_id.strip():
            raise ValueError("la respuesta no contiene un campo id válido")
        profile_id = profile_id.strip()
        if "/" in profile_id or "\\" in profile_id or profile_id in (".", ".."):
            raise ValueError(f"id de perfil no seguro: {profile_id!r}")
        return profile_id, profile
    except Exception as exc:
        raise RuntimeError(f"No se pudo obtener el perfil Fabric desde {url}: {exc}") from exc


def _add_tree(zip_file, source, archive_prefix, omit_empty=False):
    if not source.exists():
        return
    if source.is_file():
        if omit_empty and source.stat().st_size == 0:
            return
        zip_file.write(source, archive_prefix)
        return

    for item in sorted(source.rglob("*")):
        if not item.is_file():
            continue
        if omit_empty and item.stat().st_size == 0:
            continue
        relative = item.relative_to(source).as_posix()
        zip_file.write(item, f"{archive_prefix}/{relative}")


def _add_overrides_to_root(zip_file, overrides):
    if not overrides.is_dir():
        return
    for item in sorted(overrides.rglob("*")):
        if not item.is_file() or item.stat().st_size == 0:
            continue
        relative = item.relative_to(overrides).as_posix()
        zip_file.write(item, relative)


def _client_mod_list(mods):
    result = []
    for mod in mods:
        if mod["env"]["client"] == "unsupported":
            continue
        # Solo las versiones que tienen uso en cliente se agregan al listado.
        if mod["env"]["client"] not in ("required", "optional"):
            continue
        result.append(
            {
                "url": mod["url"],
                "sha1": mod["sha1"],
                "filename": mod["filename"],
                "size": mod["size"],
            }
        )
    return result


def _validate_filename(filename):
    path = PurePosixPath(filename.replace("\\", "/"))
    if path.is_absolute() or ".." in path.parts or len(path.parts) != 1:
        raise ValueError(f"Nombre de archivo de mod no válido: {filename!r}")
    return path.name


def _package_installers(zip_file):
    installer_dir = ROOT / "tlauncher"
    for filename in INSTALLER_FILES:
        source = installer_dir / filename
        if not source.is_file():
            raise ValueError(
                f"Falta el archivo requerido para el paquete TLauncher: {source}"
            )
        zip_file.write(source, filename)


def build():
    manifest = read_manifest()
    mods = get_modrinth_mods(manifest)
    profile_id, profile = fetch_fabric_profile(
        manifest["minecraft_version"], manifest["fabric_loader_version"]
    )

    DIST.mkdir(parents=True, exist_ok=True)
    archive_name = (
        f"{_safe_component(manifest['name'])}-"
        f"{_safe_component(manifest['version'])}-tlauncher.zip"
    )
    archive_path = DIST / archive_name
    third_party = _client_mod_list(mods)

    for mod in third_party:
        mod["filename"] = _validate_filename(mod["filename"])

    with zipfile.ZipFile(
        archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        archive.writestr(
            f"versions/{profile_id}/{profile_id}.json",
            json.dumps(profile, ensure_ascii=False, indent=2) + "\n",
        )

        overrides = ROOT / "pack" / "overrides"
        _add_overrides_to_root(archive, overrides)

        for jar in compiled_own_mod_jars():
            archive.write(jar, f"mods/{jar.name}")

        archive.writestr(
            THIRD_PARTY_FILENAME,
            json.dumps(third_party, ensure_ascii=False, indent=2) + "\n",
        )
        _package_installers(archive)

    print(f"Creado: {archive_path}")
    print(f"Id del perfil Fabric: {profile_id}")
    print(f"Mods de terceros para descargar al instalar: {len(third_party)}")


if __name__ == "__main__":
    try:
        build()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
