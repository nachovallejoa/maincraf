# Instalación

## Requisitos

- Minecraft Java Edition 1.20.1.
- Prism Launcher o Modrinth App, actualizado a una versión que permita importar archivos `.mrpack`.
- Conexión a internet para que el launcher descargue los componentes requeridos durante la instalación.
- Java 17 para ejecutar Minecraft 1.20.1. Los launchers suelen gestionar Java automáticamente; si se configura manualmente, selecciona Java 17.
- La memoria recomendada depende de la memoria disponible en el equipo. No hay especificaciones de hardware confirmadas para fijar un valor único.

## Descargar el paquete

### Desde Releases

1. Abre la sección **Releases** del repositorio.
2. En el Release más reciente, descarga el archivo `.mrpack`.

### Desde Actions

1. Abre la pestaña **Actions** del repositorio.
2. Entra en la ejecución completada más reciente del workflow **Build Modpack**.
3. En **Artifacts**, descarga el artefacto `mrpack`.
4. Si el artefacto se descarga como ZIP, extráelo para obtener el archivo `.mrpack`.

## Importar en Prism Launcher

1. Abre Prism Launcher.
2. Selecciona **Add Instance** y después **Import**.
3. Elige el archivo `.mrpack` descargado.
4. Confirma la instalación y espera a que termine la descarga de archivos.
5. Inicia la instancia creada.

## Importar en Modrinth App

1. Abre Modrinth App.
2. Ve a la biblioteca de instancias y selecciona la opción para importar un modpack o archivo.
3. Selecciona el `.mrpack` descargado.
4. Espera a que termine la importación y la descarga de archivos.
5. Inicia la instancia.

## Memoria y argumentos JVM

La memoria y los argumentos JVM recomendados no están fijados en los datos recibidos para este paquete. Conserva los valores predeterminados del launcher mientras no se conozcan las especificaciones del equipo y no agregues argumentos JVM avanzados sin pruebas.

## Si el juego no arranca

1. Confirma que estás iniciando la instancia importada y que el launcher terminó las descargas.
2. Revisa que la instancia esté usando Minecraft 1.20.1 y Java 17.
3. Consulta los registros de la instancia:
   - En Prism Launcher, abre la instancia y usa **Minecraft Log** o **View Folder** para encontrar `logs/latest.log`.
   - En Modrinth App, abre la instancia y usa la opción de abrir su carpeta; busca `logs/latest.log`.
4. Si existe un informe de fallo, busca también la carpeta `crash-reports`.
5. Guarda el registro completo del intento de inicio y compártelo al solicitar ayuda. No publiques datos privados que el launcher pueda incluir en los registros.
