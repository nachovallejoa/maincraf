# Contexto del proyecto

## Modo autónomo

El usuario aprobó todo y delegó todas las decisiones al equipo. No quiere cuestionarios ni conocer el contenido del modpack; el equipo toma las decisiones necesarias, preserva las sorpresas narrativas y entrega la documentación y el paquete para que el usuario lo descubra jugando. La autonomía no autoriza inventar datos de compatibilidad, dependencias, licencias ni resultados de pruebas, ni subir, retirar, sustituir, modificar o redistribuir archivos de mods de terceros.

## Hardware declarado por el usuario

El usuario informó 12 GB de RAM instalados, unos 10 GB disponibles y que Windows usa unos 500 MB. Son datos declarados, no una medición o verificación independiente. El sistema operativo, la configuración completa, la RAM física total y los benchmarks siguen sin verificarse.

## Entrega de modpack

La Marea de los Mil Soles usa Minecraft 1.20.1 y Fabric Loader 0.20.1 según los hallazgos recibidos. `pack/mods.json` contiene una selección provisional y sus incertidumbres: dependencias obligatorias pendientes, metadatos no verificados y falta de evidencia suficiente para garantizar que sea instalable. No se presenta como un paquete completo listo para publicar. Los mods de terceros se obtienen de sus fuentes autorizadas durante la compilación/instalación; no se almacenan sus JAR en Git.

No se incluyen configuraciones especulativas. Memoria y argumentos JVM recomendados no están establecidos con evidencia de pruebas para el equipo. La estructura de instalación específica en TLauncher sigue sin verificar.

## Mods propios y pruebas

La entrega recibida describe un módulo propio de campaña, pero la implementación y los archivos de `mareas-core` señalados no se incorporan en esta actualización porque el árbol existente del repositorio contiene `venas-core` y el contenido textual recibido usa una ruta diferente. No se inventa ni se renombra código para cubrir esta discrepancia. La compilación no se ejecutó. Compatibilidad de Loom, compilación Gradle y ejecución en juego quedan pendientes de prueba.

Las consultas incompletas sobre mods y dependencias se registran como pendientes indicando que las fuentes consultadas no devolvieron verificación suficiente; no se completan con suposiciones.
