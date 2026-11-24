#!/usr/bin/env python3
"""Build a Modrinth .mrpack from pack/mods.json and optional project overrides."""

import hashlib
import json
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "pack" / "mods.json"
OVERRIDES_SOURCE = ROOT / "pack" / "overrides"
OWN_MODS_SOURCE = ROOT / "mods-propios" / "build" / "libs"
MODRINTH_API = "https://api.modrinth.com/v2/version/"


def fail(message):
    raise RuntimeError(message)


def fetch_version(mod):
    version_id = mod.get("version_id")
    label = mod.get("slug", version_id or "<mod sin ID>")

    if not isinstance(version_id, str) or not version_id:
        fail(f"No se puede obtener la versión de {label}: falta version_id.")

    request = urllib.request.Request(
        MODRINTH_API + version_id,
        headers={"User-Agent": "LaMareaDeLosMilSoles-modpack-builder/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.load(response)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        fail(f"No se pueden obtener los datos de Modrinth para {label} ({version_id}): {exc}")

    if data.get("id") != version_id:
        fail(f"Modrinth devolvió un ID inesperado para {label} ({version_id}).")

    files = data.get("files")
    if not isinstance(files, list) or not files:
        fail(f"La versión de {label} ({version_id}) no contiene archivos.")

    primary = next((item for item in files if item.get("primary") is True), None)
    if primary is None:
        fail(f"La versión de {label} ({version_id}) no declara archivo principal.")

    filename = mod.get("file_name")
    hashes = primary.get("hashes") or {}
    for field, value in (
        ("file_name", filename),
        ("url", primary.get("url")),
        ("sha1", hashes.get("sha1")),
        ("sha512", hashes.get("sha512")),
        ("size", primary.get("size")),
    ):
        if value is None or value == "":
            fail(f"Falta {field} en los datos de Modrinth para {label} ({version_id}).")

    if not isinstance(filename, str) or not filename.endswith(".jar"):
        fail(f"file_name inválido para {label} ({version_id}): se esperaba un nombre .jar.")

    if primary.get("filename") != filename:
        fail(
            f"El file_name del manifiesto no coincide con el archivo principal de Modrinth "
            f"para {label} ({version_id}): {filename!r} != {primary.get('filename')!r}."
        )

    if not isinstance(primary["size"], int) or primary["size"] < 0:
        fail(f"Tamaño de archivo inválido en Modrinth para {label} ({version_id}).")

    if mod.get("version_number") and data.get("version_number") != mod["version_number"]:
        fail(
            f"version_number no coincide para {label} ({version_id}): "
            f"{mod['version_number']!r} != {data.get('version_number')!r}."
        )

    return primary


def validate_manifest(manifest):
    for field in ("name", "version", "minecraft_version", "fabric_loader_version", "mods"):
        if field not in manifest:
            fail(f"Falta el campo {field!r} en {MANIFEST_PATH.relative_to(ROOT)}.")

    if not isinstance(manifest["mods"], list):
        fail("'mods' debe ser una lista en pack/mods.json.")

    for mod in manifest["mods"]:
        for field in ("slug", "version_id", "version_number", "file_name", "env"):
            if field not in mod:
                fail(f"Falta el campo {field!r} en una entrada de mods.json.")
        if mod["env"] not in ("client", "both"):
            fail(f"env inválido para {mod['slug']}: debe ser 'client' o 'both'.")


def copy_overrides(destination):
    if OVERRIDES_SOURCE.is_dir():
        for item in OVERRIDES_SOURCE.iterdir():
            target = destination / item.name
            if item.is_dir():
                shutil.copytree(item, target, dirs_exist_ok=True)
            else:
                shutil.copy2(item, target)

    own_jars = []
    if OWN_MODS_SOURCE.is_dir():
        own_jars = sorted(
            path
            for path in OWN_MODS_SOURCE.glob("*.jar")
            if not path.name.endswith("-sources.jar")
            and not path.name.endswith("-dev.jar")
        )

    if own_jars:
        mods_dir = destination / "mods"
        mods_dir.mkdir(parents=True, exist_ok=True)
        for jar in own_jars:
            shutil.copy2(jar, mods_dir / jar.name)


def build():
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"No se encontró {MANIFEST_PATH.relative_to(ROOT)}.")
    except json.JSONDecodeError as exc:
        fail(f"JSON inválido en {MANIFEST_PATH.relative_to(ROOT)}: {exc}")

    validate_manifest(manifest)

    index_files = []
    for mod in manifest["mods"]:
        primary = fetch_version(mod)
        env = {"client": "required", "server": "unsupported"}
        if mod["env"] == "both":
            env = {"client": "required", "server": "required"}

        index_files.append(
            {
                "path": f"mods/{mod['file_name']}",
                "hashes": {
                    "sha1": primary["hashes"]["sha1"],
                    "sha512": primary["hashes"]["sha512"],
                },
                "env": env,
                "downloads": [primary["url"]],
                "fileSize": primary["size"],
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

    archive_name = f"{manifest['name']}-{manifest['version']}.mrpack"
    archive_path = ROOT / archive_name

    with tempfile.TemporaryDirectory(prefix="mrpack-build-") as temp_name:
        temp = Path(temp_name)
        (temp / "modrinth.index.json").write_text(
            json.dumps(index, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        overrides = temp / "overrides"
        overrides.mkdir()
        copy_overrides(overrides)

        with zipfile.ZipFile(
            archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
        ) as archive:
            archive.write(temp / "modrinth.index.json", "modrinth.index.json")
            for path in sorted(overrides.rglob("*")):
                if path.is_file():
                    archive.write(path, PurePosixPath("overrides") / path.relative_to(overrides))

    print(archive_path)


if __name__ == "__main__":
    try:
        build()
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
