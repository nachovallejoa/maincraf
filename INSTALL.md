# Instalacion

## TLauncher (Windows)

### Requisitos

- Windows y TLauncher instalado.
- Conexion a Internet para descargar los mods de terceros desde Modrinth durante la instalacion.
- La carpeta de datos de Minecraft existente. Por defecto, en Windows es `%APPDATA%\.minecraft`.
- Minecraft 1.20.1 usa Java 17. El launcher debe poder usar Java compatible.

### Obtener y extraer el paquete

1. Abre la pagina **Releases** de este repositorio. Descarga el archivo cuyo nombre termina en `-tlauncher.zip`.
2. Tambien puedes descargar el ZIP desde **Actions**: abre una ejecucion terminada correctamente y descarga el artefacto de instalacion.
3. Extrae el ZIP completo: clic derecho sobre el archivo y elige **Extraer todo**.
4. Abre la carpeta extraida y haz doble clic en `INSTALAR.bat`.

**Importante:** `INSTALAR.bat` no funciona si se descarga suelto desde el repositorio, si se ejecuta desde la carpeta `tlauncher` del repositorio o si se abre dentro del ZIP sin extraerlo. Necesita `mods-terceros.json` y la carpeta `versions` que vienen dentro del ZIP completo.

El instalador usa `%APPDATA%\.minecraft` por defecto. Si tu TLauncher tiene configurada otra carpeta de juego, el script permite una ruta alternativa al ejecutarlo con PowerShell, por ejemplo:

```powershell
.\instalar.ps1 -Destino "D:\Games\.minecraft"
```

Si la carpeta indicada no existe, el instalador se detiene sin crearla.

### Finalizar y jugar

1. Cuando termine, abre TLauncher.
2. Selecciona en la lista de versiones la version instalada que muestra el instalador.
3. En los ajustes de TLauncher, asigna la memoria indicada al final de este documento.
4. Inicia el juego.

TLauncher documenta una ubicacion configurable para el directorio del juego y carpetas de versiones. Su documentacion consultada no confirma que exista una opcion general de “carpeta separada por version” que cambie la ubicacion de `mods/`. **[SIN VERIFICAR]** Por seguridad, deja seleccionada la carpeta `.minecraft` que usa el launcher y no actives una opcion de directorios separados si tu version del launcher la muestra; si usas una ruta propia, indica esa carpeta con `-Destino`.

### Respaldo y vuelta atras

Antes de copiar el contenido nuevo, el instalador mueve la carpeta `mods` previa que contenga archivos y guarda copias de `config` y `options.txt` existentes en `respaldo-modpack-<fecha-y-hora>` dentro de `.minecraft`.

Para volver atras:

1. Cierra Minecraft y TLauncher.
2. Abre `.minecraft\respaldo-modpack-<fecha-y-hora>`.
3. Restaura desde alli la carpeta `mods` anterior y los archivos/carpeta de configuracion que quieras recuperar. Si ya existe un `mods` nuevo, apartalo antes de devolver el anterior.
4. Elimina la carpeta de version Fabric instalada solo si no vas a volver a seleccionarla.

## Prism Launcher o Modrinth App (opcional)

El archivo `.mrpack` se puede importar en Prism Launcher mediante **Add Instance > Import**. Modrinth App tambien permite instalar y jugar modpacks en su aplicacion. TLauncher no usa el archivo `.mrpack`; para TLauncher usa el ZIP terminado en `-tlauncher.zip`.

## Memoria, argumentos y diagnostico

El manifiesto no proporciona memoria ni argumentos JVM. **[SIN VERIFICAR]** Con unos 10 GB de RAM total en Windows, una recomendacion prudente inicial es asignar **4 GB** al juego, dejando memoria al sistema y otras aplicaciones. La ayuda oficial de Minecraft advierte que la asignacion debe corresponder a la RAM disponible y da como referencia que en sistemas de 64 bits no se recomienda asignar mas de la mitad de la RAM total. No se agregan argumentos JVM personalizados; conserva los que configure TLauncher.

Para problemas de inicio, abre la carpeta de juego desde el icono de carpeta de TLauncher y revisa `logs\latest.log`; si el juego genero un informe de fallo, revisa tambien `crash-reports\`. En TLauncher puedes activar la consola de desarrollador en sus ajustes para ver la salida de inicio. Adjunta el registro completo al pedir ayuda.
