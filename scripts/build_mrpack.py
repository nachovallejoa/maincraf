#!/usr/bin/env python3
"""Build a Modrinth .mrpack from pack/mods.json and project overrides."""

from __future__ import annotations

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
MANIFEST = ROOT / "pack" / "mods.json"
OVERRIDES = ROOT / "pack" / "overrides"
OWN_MODS = ROOT / "mods-propios"
INDEX_PATH = "modrinth.index.json"


class BuildError(Exception):
    """Expected input or download error."""


def read_json(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(stream)
    except (OSError, json.JSONDecodeError) as exc:
        raise BuildError(f"No se pudo leer {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(value, dict):
        raise BuildError(f"{path.relative_to(ROOT)} debe contener un objeto JSON.")
    return value


def checked_relative_path(value: str, description: str) -> str:
    if not isinstance(value, str) or not value:
        raise BuildError(f"Ruta no válida para {description}: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        raise BuildError(f"Ruta no segura para {description}: {value!r}")
    return path.as_posix()


def get_version(version_id: str, slug: str) -> dict:
    url = f"https://api.modrinth.com/v2/version/{version_id}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "LaMareaDeLosMilSoles-ModpackBuilder/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, OSError, UnicodeDecodeError,
            json.JSONDecodeError) as exc:
        raise BuildError(
            f"No se pudieron obtener los datos de Modrinth para {slug} "
            f"(version_id {version_id}): {exc}"
        ) from exc

    if not isinstance(data, dict):
        raise BuildError(f"Respuesta inválida de Modrinth para {slug} ({version_id}).")
    return data


def get_primary_file(data: dict, slug: str, version_id: str) -> dict:
    files = data.get("files")
    if not isinstance(files, list) or not files:
        raise BuildError(f"Modrinth no devolvió archivos para {slug} ({version_id}).")

    primary = next(
        (item for item in files if isinstance(item, dict) and item.get("primary") is True),
        None,
    )
    if primary is None and len(files) == 1 and isinstance(files[0], dict):
        primary = files[0]
    if primary is None:
        raise BuildError(
            f"No se encontró un archivo principal único para {slug} ({version_id})."
        )

    hashes = primary.get("hashes")
    if not isinstance(hashes, dict):
        raise BuildError(f"Faltan hashes del archivo principal de {slug} ({version_id}).")

    required = ("sha1", "sha512")
    for name in required:
        if not isinstance(hashes.get(name), str) or not hashes[name]:
            raise BuildError(
                f"Falta el hash {name} del archivo principal de {slug} ({version_id})."
            )

    if not isinstance(primary.get("url"), str) or not primary["url"]:
        raise BuildError(f"Falta la URL del archivo principal de {slug} ({version_id}).")
    if not isinstance(primary.get("size"), int) or primary["size"] < 0:
        raise BuildError(f"Falta el tamaño del archivo principal de {slug} ({version_id}).")

    return primary


def copy_overrides(destination: Path) -> None:
    if not OVERRIDES.exists():
        return
    if not OVERRIDES.is_dir():
        raise BuildError("pack/overrides existe, pero no es un directorio.")

    for source in sorted(OVERRIDES.rglob("*")):
        relative = source.relative_to(OVERRIDES)
        target = destination / relative
        if source.is_symlink():
            raise BuildError(f"No se admiten enlaces simbólicos en overrides: {relative}")
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif source.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)


def own_mod_jars() -> list[Path]:
    if not OWN_MODS.exists():
        return []
    return sorted(
        path
        for path in OWN_MODS.glob("**/build/libs/*.jar")
        if path.is_file()
        and not path.name.endswith("-sources.jar")
        and not path.name.endswith("-dev.jar")
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    try:
        manifest = read_json(MANIFEST)
        name = manifest.get("name")
        version = manifest.get("version")
        minecraft_version = manifest.get("minecraft_version")
        loader_version = manifest.get("fabric_loader_version")
        mods = manifest.get("mods")

        if not isinstance(name, str) or not name.strip():
            raise BuildError("pack/mods.json debe especificar un name no vacío.")
        if not isinstance(version, str) or not version.strip():
            raise BuildError("pack/mods.json debe especificar un version no vacío.")
        if not isinstance(minecraft_version, str) or not minecraft_version.strip():
            raise BuildError("pack/mods.json debe especificar minecraft_version.")
        if not isinstance(loader_version, str) or not loader_version.strip():
            raise BuildError(
                "fabric_loader_version es null; no se puede generar la dependencia "
                "fabric-loader requerida en modrinth.index.json."
            )
        if not isinstance(mods, list):
            raise BuildError("pack/mods.json debe contener mods como una lista.")

        index_files = []
        seen_paths = set()

        for mod in mods:
            if not isinstance(mod, dict):
                raise BuildError("Cada entrada de mods debe ser un objeto JSON.")
            slug = mod.get("slug")
            version_id = mod.get("version_id")
            file_name = mod.get("file_name")
            env = mod.get("env")

            if not isinstance(slug, str) or not slug:
                raise BuildError(f"Entrada de mod con slug no válido: {mod!r}")
            if not isinstance(version_id, str) or not version_id:
                raise BuildError(f"Falta version_id para {slug}.")
            if not isinstance(mod.get("version_number"), str):
                raise BuildError(f"Falta version_number para {slug}.")
            if env not in ("client", "both"):
                raise BuildError(
                    f"env no admitido para {slug}: {env!r}; se esperaba client o both."
                )

            safe_file_name = checked_relative_path(file_name, slug)
            if "/" in safe_file_name:
                raise BuildError(f"file_name debe ser solo un nombre de archivo para {slug}.")
            mod_path = f"mods/{safe_file_name}"
            if mod_path in seen_paths:
                raise BuildError(f"Ruta de mod duplicada en el manifiesto: {mod_path}")
            seen_paths.add(mod_path)

            data = get_version(version_id, slug)
            primary = get_primary_file(data, slug, version_id)

            if data.get("id") != version_id:
                raise BuildError(
                    f"Modrinth devolvió un ID de versión distinto para {slug} "
                    f"(solicitado {version_id})."
                )
            if data.get("version_number") != mod["version_number"]:
                raise BuildError(
                    f"version_number de Modrinth no coincide para {slug} "
                    f"(version_id {version_id})."
                )
            if primary.get("filename") != safe_file_name:
                raise BuildError(
                    f"El nombre del archivo principal de Modrinth no coincide para "
                    f"{slug}: {primary.get('filename')!r}."
                )

            index_files.append({
                "path": mod_path,
                "hashes": {
                    "sha1": primary["hashes"]["sha1"],
                    "sha512": primary["hashes"]["sha512"],
                },
                "env": {
                    "client": "required",
                    "server": "required" if env == "both" else "unsupported",
                },
                "downloads": [primary["url"]],
                "fileSize": primary["size"],
            })

        own_jars = own_mod_jars()

        with tempfile.TemporaryDirectory(prefix="mrpack-build-") as temp_dir:
            staging = Path(temp_dir)
            copy_overrides(staging / "overrides")

            if own_jars:
                own_destination = staging / "overrides" / "mods"
                own_destination.mkdir(parents=True, exist_ok=True)
                for jar in own_jars:
                    target = own_destination / jar.name
                    if target.exists():
                        raise BuildError(
                            f"Nombre duplicado en overrides/mods: {jar.name}"
                        )
                    shutil.copy2(jar, target)

            index = {
                "formatVersion": 1,
                "game": "minecraft",
                "versionId": version,
                "name": name,
                "files": index_files,
                "dependencies": {
                    "minecraft": minecraft_version,
                    "fabric-loader": loader_version,
                },
            }
            (staging / INDEX_PATH).write_text(
                json.dumps(index, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

            output = ROOT / f"{name}-{version}.mrpack"
            with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.write(staging / INDEX_PATH, INDEX_PATH)
                overrides_dir = staging / "overrides"
                if overrides_dir.exists():
                    for file_path in sorted(overrides_dir.rglob("*")):
                        if file_path.is_file():
                            archive.write(
                                file_path,
                                file_path.relative_to(staging).as_posix(),
                            )

        print(f"Paquete creado: {output.relative_to(ROOT)}")
        print(f"SHA-256: {sha256_file(output)}")
        return 0

    except BuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
