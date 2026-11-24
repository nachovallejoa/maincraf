# Instalacion

## TLauncher (Windows)

### Requisitos

- Windows y TLauncher instalado.
- Conexion a Internet para descargar los mods de terceros durante la instalacion.
- La carpeta de datos de TLauncher debe existir. Por defecto, en Windows es `%APPDATA%\.minecraft`.
- [SIN VERIFICAR] La prueba de este perfil con la version instalada de TLauncher y con la opcion de directorios aislados no se ha realizado.

### Descargar y extraer el paquete

1. Abre la pagina **Releases** del repositorio y descarga el archivo que termina en `-tlauncher.zip`. Tambien se puede descargar como artefacto desde **Actions** cuando un workflow haya terminado correctamente.
2. No descargues `INSTALAR.bat` por separado desde el repositorio. El BAT no funciona suelto ni desde la carpeta `tlauncher` del repositorio.
3. En Windows, haz clic derecho en el ZIP y elige **Extraer todo**. Extrae todo el contenido a una carpeta.
4. Abre esa carpeta extraida y haz doble clic en `INSTALAR.bat`. No ejecutes el instalador desde dentro del ZIP.

El instalador usa `%APPDATA%\.minecraft` por defecto. Si la carpeta no existe, se detiene sin instalar. Para una carpeta de juego personalizada, se puede ejecutar PowerShell desde la carpeta extraida con una ruta explicita:
`powershell -NoProfile -ExecutionPolicy Bypass -File ".\instalar.ps1" -MinecraftDir "RUTA_COMPLETA_A\.minecraft"`

El instalador respalda los mods que ya existan, y copia la configuracion y `options.txt` existentes, dentro de `respaldo-modpack-fecha-hora` en `.minecraft`. Si una descarga de Modrinth falla o no coincide con el SHA1/tamano esperado, se informa al final; no uses el pack si falta un mod necesario.

### Iniciar y revertir

1. Abre TLauncher.
2. En la lista de versiones, selecciona `fabric-loader-0.20.1-1.20.1`.
3. En los ajustes de TLauncher, configura la memoria indicada abajo.
4. Inicia el juego.

TLauncher permite cambiar el directorio general de los archivos del juego en sus ajustes. La documentacion consultada describe esa ubicacion, pero no confirma una opcion de carpetas aisladas por version que cambie donde se buscan `mods` y `config`. Por tanto, deja desactivada cualquier opcion de directorio separado por version si aparece. [SIN VERIFICAR] La presencia y comportamiento de esa opcion dependen de la version concreta del launcher.

Para volver atras, cierra Minecraft. En `.minecraft`, mueve o elimina la carpeta `mods` instalada y, desde la carpeta `respaldo-modpack-fecha-hora`, restaura `mods-anteriores` como `mods` si el instalador la creo. Restaura tambien `config` y `options.txt` desde ese respaldo si quieres recuperar esos archivos. No elimines el respaldo hasta comprobar que ya no lo necesitas.

## Opcional: Prism Launcher o Modrinth App

Importa el archivo `.mrpack` desde la funcion de importar modpack de tu launcher. Los launchers compatibles descargan los mods de Modrinth; no copies JARs de terceros desde este repositorio.

## Memoria y argumentos JVM

El manifiesto no incluye argumentos JVM ni una recomendacion de memoria para el paquete. Para un equipo con unos 10 GB de RAM disponibles para Windows, una recomendacion prudente es asignar **4 GB** a Minecraft. No asignes toda la RAM del equipo al juego. [SIN VERIFICAR] La memoria concreta adecuada depende de otros programas abiertos y del hardware; no se midio esta instancia.

No se necesitan argumentos JVM adicionales aportados por el paquete.

## Si el juego no arranca

- Abre la carpeta de datos de Minecraft desde TLauncher con su boton de carpeta, o revisa `%APPDATA%\.minecraft`.
- Consulta `logs/latest.log` y, si hubo un cierre inesperado, el archivo mas reciente de `crash-reports/`.
- En TLauncher, activa la consola de desarrollador o la consola de Minecraft en los ajustes para ver errores durante el inicio.
- Comprueba que seleccionaste la version Fabric instalada y que no hubo descargas fallidas. Guarda el texto del error y el registro antes de pedir ayuda.
