#!/usr/bin/env python3
"""Build a TLauncher version folder and one-folder ZIP.

Third-party mod JARs are downloaded from Modrinth at build time only. The
Minecraft game JAR is not copied or redistributed: the Fabric profile inherits
the vanilla version named in `inheritsFrom`.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path
from typing import Any

from build_mrpack import (
    BuildError,
    ROOT,
    compiled_own_mod_jars,
    fetch_modrinth_release,
    read_manifest,
)

FABRIC_META_PROFILE = "https://meta.fabricmc.net/v2/versions/loader/{minecraft}/{loader}/profile/json"
USER_AGENT = "MarDeNubes-ModpackBuilder/1.0 (GitHub Actions)"


def _safe_name(name: str) -> str:
    # Preserve only ASCII letters, digits and hyphens; collapse other runs.
    safe = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-")
    if not safe:
        raise BuildError("El nombre del pack no produce un ID de carpeta valido.")
    return safe


def _safe_filename(filename: str, label: str) -> str:
    if Path(filename).name != filename or filename in {"", ".", ".."}:
        raise BuildError(f"Nombre de archivo inseguro para {label}: {filename!r}")
    return filename


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
            value = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise BuildError(f"No se pudo descargar el perfil Fabric desde {url}: {exc}") from exc
    if not isinstance(value, dict):
        raise BuildError(f"El perfil Fabric de {url} no es un objeto JSON.")
    return value


def _download_checked(
    url: str,
    destination: Path,
    expected_sha1: str,
    label: str,
) -> None:
    last_error: Exception | None = None
    for attempt in (1, 2):
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": USER_AGENT},
            )
            with urllib.request.urlopen(request, timeout=120) as response:
                payload = response.read()

            actual = hashlib.sha1(payload).hexdigest().lower()
            if actual != expected_sha1.lower():
                raise BuildError(
                    f"SHA-1 no coincide para {label}: esperado {expected_sha1}, "
                    f"recibido {actual}."
                )

            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)
            return
        except (urllib.error.URLError, TimeoutError, OSError, BuildError) as exc:
            last_error = exc
            if attempt == 1:
                continue

    raise BuildError(
        f"No se pudo descargar/verificar el mod {label} tras 2 intentos: {last_error}"
    )


def _copy_nonempty_overrides(source: Path, destination: Path) -> None:
    if not source.exists() or not source.is_dir():
        return
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        # The stated pack rule is to omit empty override files.
        if path.stat().st_size == 0:
            continue
        relative = path.relative_to(source)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def build_tlauncher(root: Path | str = ROOT) -> tuple[Path, str, int]:
    base = Path(root)
    manifest = read_manifest(base / "pack" / "mods.json")

    folder_name = f"{_safe_name(manifest['name'])}-{_safe_name(manifest['version'])}"
    version_folder = base / "dist" / folder_name
    if version_folder.exists():
        shutil.rmtree(version_folder)
    version_folder.mkdir(parents=True)

    profile_url = FABRIC_META_PROFILE.format(
        minecraft=manifest["minecraft_version"],
        loader=manifest["fabric_loader_version"],
    )
    profile = _request_json(profile_url)
    # Keep every upstream profile value unchanged except its launcher ID.
    profile["id"] = folder_name
    json_path = version_folder / f"{folder_name}.json"
    json_path.write_text(
        json.dumps(profile, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    mods_dir = version_folder / "mods"
    mods_dir.mkdir(parents=True)

    included = 0
    for mod in manifest["mods"]:
        release = fetch_modrinth_release(mod)
        env = release["env"]
        # Skip files not intended for clients, including client_side unsupported.
        if env["client"] == "unsupported":
            continue
        filename = _safe_filename(release["filename"], release["name"])
        _download_checked(
            release["url"],
            mods_dir / filename,
            release["sha1"],
            release["name"],
        )
        included += 1

    own_jars = compiled_own_mod_jars(base)
    for jar in own_jars:
        target = mods_dir / jar.name
        if target.exists():
            raise BuildError(
                f"Colision de nombre de JAR en mods/: {jar.name}. "
                "Renombra uno de los JAR propios antes de empaquetar."
            )
        shutil.copy2(jar, target)
        included += 1

    overrides = base / "pack" / "overrides"
    _copy_nonempty_overrides(overrides, version_folder)

    # Ensure these folders are represented in the ZIP even when empty.
    for folder in ("resourcepacks", "shaderpacks", "saves"):
        (version_folder / folder).mkdir(parents=True, exist_ok=True)

    # [SIN VERIFICAR] TLauncher documents that TLauncherAdditional.json may
    # appear after first launch, but its complete format/required fields were
    # not verified. Do not generate or ship one.
    readme_source = base / "tlauncher" / "LEEME.txt"
    if not readme_source.is_file():
        raise BuildError(f"Falta el archivo requerido: {readme_source}")
    shutil.copy2(readme_source, version_folder / "LEEME.txt")

    zip_path = base / "dist" / f"{folder_name}-tlauncher.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(version_folder.rglob("*")):
            relative = path.relative_to(version_folder.parent)
            if path.is_dir():
                # ZIP directory entries keep empty player folders when possible.
                if not any(path.iterdir()):
                    archive.writestr(str(relative).replace("\\", "/") + "/", "")
                continue
            archive.write(path, str(relative).replace("\\", "/"))

    return zip_path, folder_name, included


def main() -> int:
    try:
        zip_path, folder_name, count = build_tlauncher()
    except BuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Carpeta: {folder_name}")
    print(f"Mods incluidos: {count}")
    print(f"ZIP: {zip_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
