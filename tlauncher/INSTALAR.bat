@echo off
setlocal

set "AVISO=El instalador no funciona suelto ni desde la carpeta tlauncher del repositorio. Descarga de Releases el archivo que termina en -tlauncher.zip, extraelo COMPLETO (clic derecho, Extraer todo) y haz doble clic en INSTALAR.bat dentro de esa carpeta extraida. Nunca lo bajes solo desde el repositorio ni lo ejecutes desde dentro del .zip sin extraer."

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
