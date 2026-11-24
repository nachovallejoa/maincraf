# Instalacion

## TLauncher en Windows (recomendado)

### Requisitos

- Windows y TLauncher instalados.
- Una carpeta `.minecraft` ya creada. El instalador usa por defecto `%APPDATA%\.minecraft`.
- Conexion a Internet para descargar los mods de terceros desde Modrinth.
- El paquete completo descargado desde GitHub.

### Descargar y ejecutar

1. Abre la seccion **Releases** del repositorio y descarga el archivo cuyo nombre termina en `-tlauncher.zip`. Tambien puedes descargar el mismo ZIP desde **Actions**, en los artefactos de una ejecucion completada.
2. Descomprime el ZIP completo: clic derecho en el archivo y elige **Extraer todo**.
3. **No ejecutes `INSTALAR.bat` si lo descargaste suelto del repositorio, y no lo abras dentro del ZIP sin extraer.** El instalador necesita los archivos del paquete junto a el.
4. En la carpeta extraida, haz doble clic en `INSTALAR.bat`.
5. Espera el mensaje de resultado. El instalador respalda los mods existentes y copia los archivos de configuracion incluidos; descarga los mods de terceros y comprueba sus SHA1.
6. Abre TLauncher y elige en la lista de versiones el perfil instalado. El nombre exacto aparece al terminar la instalacion.
7. En los ajustes de TLauncher, asigna la memoria indicada al final de este documento.

El destino por defecto es `%APPDATA%\.minecraft`. El instalador tambien permite pasarle como argumento una carpeta `.minecraft` existente si tu TLauncher usa otro directorio. TLauncher permite cambiar su directorio de juego desde sus ajustes; si lo cambiaste, asegúrate de instalar en esa carpeta y de lanzar el perfil usando ese mismo directorio.

### Carpetas separadas por version

[SIN VERIFICAR] La documentacion de TLauncher consultada describe el directorio de juego configurable y el uso de `.minecraft/versions/` y `.minecraft/mods/`, pero no documenta una opcion que, por version, haga que el perfil busque automaticamente los mods en otra carpeta. Por seguridad, este instalador usa la carpeta `mods/` del directorio `.minecraft` elegido. No actives ni supongas una opcion de mods separados por version: deja que el perfil use el directorio de juego habitual. Si tu configuracion de TLauncher apunta a otro directorio de juego, instala el paquete ahi mediante el parametro de destino.

### Volver atras

El instalador crea una carpeta `respaldo-modpack-<fecha y hora>` dentro de `.minecraft` cuando hay mods, `config/` u `options.txt` que respaldar. Para revertir:

1. Cierra Minecraft y TLauncher.
2. Abre la carpeta de respaldo que indico el instalador.
3. Restaura los mods anteriores desde `mods-anteriores` (si existe) y devuelve `config/` y `options.txt` a la carpeta `.minecraft`.
4. Si quieres retirar el perfil instalado, elimina la carpeta de version con su ID de `.minecraft/versions/`.

No borres el respaldo hasta comprobar que no necesitas recuperar ningun archivo.

## Prism Launcher o Modrinth App (opcional)

Descarga el archivo `.mrpack` desde Releases o desde Actions e importalo en Prism Launcher o Modrinth App usando su funcion de importar modpack. Este no es el metodo indicado para instalar en TLauncher.

## Memoria y argumentos JVM

La pauta inicial para este paquete es un maximo de heap de **4 GB**. Si tu ordenador tiene unos 10 GB de RAM y Windows utiliza aproximadamente 500 MB reservados, comienza por 4 GB y comprueba el uso; no es una medicion de rendimiento. En el perfil de TLauncher configura esa asignacion de memoria.

Argumentos JVM iniciales documentados para este paquete:

```text
-Xmx4G -XX:+UseG1GC
```

No agregues otros flags sin medir primero. La ayuda oficial de Minecraft explica que `-Xmx4G` asigna 4 GB y recomienda no asignar mas de la mitad de la RAM en sistemas de 64 bits. Si los 10 GB son la RAM total del equipo, esa regla pone un maximo recomendado de 5 GB; por eso 4 GB es el punto de partida conservador descrito para este equipo. Fuente: [Minecraft Help: memory allocation](https://help.minecraft.net/hc/en-us/articles/39083573916941-Troubleshoot-Minecraft-Java-Edition-Crashes-by-Checking-Memory-Allocation).

## Si el juego no arranca

- Comprueba que se selecciono el perfil instalado y que el directorio de juego de TLauncher coincide con el destino donde se instalo.
- Revisa el registro `logs/latest.log` dentro del directorio de juego de Minecraft.
- Si hay un informe de fallo, revisa `crash-reports/`.
- En TLauncher, activa la consola de desarrollador desde sus ajustes y conserva el registro generado. [SIN VERIFICAR] La ubicacion exacta del registro propio de TLauncher depende de la version del launcher.
- Si falla una descarga, vuelve a ejecutar el instalador con conexion estable; informa los nombres de los archivos fallidos y la ruta indicada por el instalador.

[SIN VERIFICAR] El conjunto no se declara probado en ejecucion. Dependencias adicionales, compatibilidad completa entre mods y arranque real deben probarse en una instancia antes de considerar el paquete validado.
