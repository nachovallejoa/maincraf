# Instalación

## Requisitos

- Minecraft 1.20.1.
- Prism Launcher o Modrinth App, actualizado a una versión que permita importar archivos `.mrpack`.
- Java 17 para Minecraft 1.20.1. Los launchers suelen gestionar Java automáticamente; si se configura manualmente, selecciona Java 17.
- Conexión a Internet durante la instalación para descargar los archivos necesarios.

El paquete no fija una versión exacta de Fabric Loader. No consideres la instancia validada ni fuerces una versión manual de Loader.

## Descargar el paquete

### Desde Releases

1. Abre la sección **Releases** del repositorio en GitHub.
2. En la publicación más reciente, descarga el archivo `.mrpack` adjunto.

### Desde Actions

1. Abre la pestaña **Actions** del repositorio.
2. Selecciona una ejecución completada de **Build modpack**.
3. En **Artifacts**, descarga `modrinth-modpack`.
4. Si GitHub lo descarga como ZIP, extrae ese ZIP para obtener el archivo `.mrpack`. No importes el ZIP del artefacto.

## Importar en Prism Launcher

1. Abre Prism Launcher.
2. Elige **Add Instance** y después **Import**.
3. Selecciona el archivo `.mrpack` descargado.
4. Confirma la importación y espera a que el launcher descargue los archivos.
5. Inicia la instancia desde Prism Launcher.

## Importar en Modrinth App

1. Abre Modrinth App.
2. Ve a **Library** y usa la opción para importar un modpack o archivo.
3. Selecciona el archivo `.mrpack` descargado.
4. Espera a que termine la instalación y luego inicia la instancia.

Los nombres de las opciones pueden variar ligeramente entre versiones del launcher.

## Memoria y argumentos JVM

- Heap máximo recomendado como punto de partida: `-Xmx6G`, condicionado a disponer de aproximadamente 10 GB de memoria total disponible. No es una medición del consumo del paquete.
- No se recomienda añadir un valor para `-Xms`.
- Conserva los argumentos JVM predeterminados del launcher; no añadas opciones de GC no verificadas.

## Si el juego no arranca

1. Comprueba que la versión de Minecraft seleccionada sea 1.20.1 y que el launcher haya terminado de descargar la instancia.
2. Revisa el registro de la instancia:
   - **Prism Launcher:** abre la instancia y usa **Minecraft Log** o **View Logs**.
   - **Modrinth App:** abre la instancia y usa la opción para ver los registros/logs.
3. Si el launcher ofrece un registro de instalación, consúltalo también. En Minecraft, los registros suelen estar dentro de la carpeta de la instancia, en `logs/latest.log`.
4. Guarda el registro desde el inicio del error y compártelo al pedir ayuda. Oculta cualquier dato personal o token que pudiera aparecer.
