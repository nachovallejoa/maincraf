@echo off
setlocal

set "PAQUETE_INCOMPLETO=Este instalador no funciona suelto. Descarga de Releases el archivo que termina en -tlauncher.zip, descomprimelo COMPLETO (clic derecho, Extraer todo) y haz doble clic en INSTALAR.bat dentro de esa carpeta extraida. No lo bajes solo desde el repositorio ni lo ejecutes desde dentro del .zip."

if not exist "%~dp0instalar.ps1" (
    echo %PAQUETE_INCOMPLETO%
    pause
    exit /b 1
)

if not exist "%~dp0mods-terceros.json" (
    echo %PAQUETE_INCOMPLETO%
    pause
    exit /b 1
)

if not exist "%~dp0versions\" (
    echo %PAQUETE_INCOMPLETO%
    pause
    exit /b 1
)

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0instalar.ps1"
pause
endlocal
