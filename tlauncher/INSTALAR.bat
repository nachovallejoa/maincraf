@echo off
setlocal

set "AVISO=Este instalador no funciona suelto. Descarga de Releases el archivo que termina en -tlauncher.zip, descomprimelo COMPLETO (clic derecho, Extraer todo) y haz doble clic en INSTALAR.bat dentro de esa carpeta extraida. Nunca lo bajes solo desde el repositorio ni lo ejecutes desde dentro del .zip sin extraer."

if not exist "%~dp0instalar.ps1" (
    echo %AVISO%
    pause
    exit /b 1
)

if not exist "%~dp0mods-terceros.json" (
    echo %AVISO%
    pause
    exit /b 1
)

if not exist "%~dp0versions\" (
    echo %AVISO%
    pause
    exit /b 1
)

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0instalar.ps1"
pause
endlocal
