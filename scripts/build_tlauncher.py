#!/usr/bin/env python3
"""Construye el ZIP de instalación para TLauncher, sin redistribuir mods ajenos."""

import json
import re
import shutil
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

from build_mrpack import (
    BuildError,
    DIST_DIR,
    ROOT,
    USER_AGENT,
    compiled_own_mod_jars,
    read_manifest,
    resolve_mods,
)


FABRIC_META = "https://meta.fabricmc.net/v2/versions/loader"


def _safe_pack_component(text):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", text.strip()).strip(".-") or "modpack"


def fetch_fabric_profile(minecraft_version, loader_version):
    url = "{}/{}/{}/profile/json".format(
        FABRIC_META, minecraft_version, loader_version
    )
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            profile = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        raise BuildError(
            "No se pudo descargar el perfil Fabric desde {}: {}".format(url, exc)
        ) from exc

    if not isinstance(profile, dict):
        raise BuildError("El perfil Fabric recibido no es un objeto JSON.")
    version_id = profile.get("id")
    if not isinstance(version_id, str) or not version_id.strip():
        raise BuildError("El perfil Fabric no contiene un campo id válido.")
    if profile.get("inheritsFrom") != minecraft_version:
        raise BuildError(
            "El perfil Fabric no hereda de Minecraft {}.".format(minecraft_version)
        )
    return version_id, profile


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


def build_tlauncher():
    manifest = read_manifest()
    resolved = resolve_mods(manifest)
    version_id, profile = fetch_fabric_profile(
        manifest["minecraft_version"], manifest["fabric_loader_version"]
    )

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    pack_name = _safe_pack_component(manifest["name"])
    pack_version = _safe_pack_component(manifest["version"])
    output_path = DIST_DIR / "{}-{}-tlauncher.zip".format(pack_name, pack_version)

    staging = DIST_DIR / ".tlauncher-staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    version_dir = staging / "versions" / version_id
    version_dir.mkdir(parents=True)
    (version_dir / "{}.json".format(version_id)).write_text(
        json.dumps(profile, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    overrides = ROOT / "pack" / "overrides"
    _copy_tree_contents(overrides, staging)

    own_jars = compiled_own_mod_jars()
    if own_jars:
        mods_dir = staging / "mods"
        mods_dir.mkdir(parents=True, exist_ok=True)
        for jar in own_jars:
            shutil.copy2(jar, mods_dir / jar.name)

    third_party = [
        {
            "url": mod["url"],
            "sha1": mod["sha1"],
            "filename": mod["filename"],
            "size": mod["size"],
        }
        for mod in resolved
        if mod.get("client_side") != "unsupported"
    ]
    (staging / "mods-terceros.json").write_text(
        json.dumps(third_party, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
    )

    for filename in ("instalar.ps1", "INSTALAR.bat", "LEEME.txt"):
        source = ROOT / "tlauncher" / filename
        if not source.is_file():
            raise BuildError("Falta el archivo requerido tlauncher/{}.".format(filename))
        shutil.copy2(source, staging / filename)

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
    print("Perfil Fabric: {}".format(version_id))
    return output_path


if __name__ == "__main__":
    try:
        build_tlauncher()
    except BuildError as error:
        print("ERROR: {}".format(error), file=sys.stderr)
        sys.exit(1)
