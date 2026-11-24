# Instalación

## Estado del paquete

**Este repositorio no contiene actualmente un paquete instalable verificado.** `pack/mods.json` es provisional: hay mods sin IDs confirmados y dependencias obligatorias con versiones/artefactos pendientes. El constructor debe detenerse si no puede resolver y validar los metadatos; no rellenes huecos manualmente con suposiciones ni descargues archivos de fuentes no autorizadas.

No se ha comprobado la estructura de instalación específica de TLauncher. No se garantiza una compilación exitosa, inicio, compatibilidad integral ni rendimiento. Espera el resultado real del workflow y la revisión de los bloqueos antes de distribuir o instalar un artefacto como final.

## Cuando exista un artefacto `.mrpack` validado

### Descargar desde Releases

1. Abre la sección **Releases** del repositorio.
2. Descarga el archivo `.mrpack` de una versión cuya compilación esté completada correctamente.
3. Si el archivo está empaquetado como ZIP, extráelo para obtener el `.mrpack`.

### Descargar desde Actions

1. Abre la pestaña **Actions** del repositorio.
2. Entra en una ejecución completada correctamente del workflow **Build Modpack**.
3. En **Artifacts**, descarga el artefacto del modpack.
4. Si se descargó como ZIP, extráelo para obtener el archivo `.mrpack`.

## Importar en Prism Launcher o Modrinth App

Solo cuando exista un `.mrpack` validado por build y revisado:

1. Abre el launcher y usa la opción para importar una instancia o modpack desde archivo.
2. Selecciona el `.mrpack`.
3. Confirma la importación y espera que el launcher obtenga los componentes requeridos desde sus fuentes autorizadas.
4. Antes de jugar, verifica que instancia use Minecraft `1.20.1` y el loader del manifiesto.

Los pasos y disponibilidad pueden variar según la versión del launcher. TLauncher no está cubierto por instrucciones verificadas.

## Memoria y argumentos JVM

No hay cifra de memoria o argumentos JVM recomendados verificados para este paquete. El usuario declaró 12 GB de RAM instalados, unos 10 GB disponibles y Windows usando unos 500 MB; son datos declarados, no mediciones independientes ni resultados de pruebas. Conserva los valores predeterminados del launcher hasta disponer de validación en el equipo. No se afirma un heap óptimo ni se recomiendan banderas JVM específicas.

## Si el juego no arranca

1. Confirma que instalaste una instancia importada desde el artefacto correcto y espera a que el launcher termine las descargas.
2. Verifica la versión de Minecraft y Fabric Loader mostrada en la instancia.
3. Guarda `logs/latest.log` y, si existe, el informe correspondiente en `crash-reports`.
4. Comparte los registros completos al solicitar ayuda, retirando datos privados. No se pueden diagnosticar fallos sin logs.
