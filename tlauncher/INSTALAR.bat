@echo off
setlocal
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0instalar.ps1" %*
set "RESULTADO=%ERRORLEVEL%"
echo.
if not "%RESULTADO%"=="0" (
  echo El instalador termino con codigo %RESULTADO%.
)
pause
exit /b %RESULTADO%
