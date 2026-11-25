# PROJECT_CONTEXT

## Modo autónomo

El usuario aprobó todo y delegó todas las decisiones al equipo. No quiere cuestionarios ni conocer el contenido del modpack.

Hardware actualizado: 12 GB instalados, unos 10 GB disponibles; Windows usa unos 500 MB.

Launcher del usuario: TLauncher en Windows.

## Paquete del modpack

- Perfil objetivo Minecraft `1.20.1`; Fabric Loader declarado `0.20.1` según Fabric Meta.
- El manifiesto lista releases para Fabric/Minecraft `1.20.1`; no afirma que estén probadas juntas.
- No se suben JAR de mods de terceros.
- Las configuraciones del juego/mods no se presentan como validadas si no se probaron con los JAR exactos.
- La recomendación JVM aportada es `-Xms2G -Xmx6G`; es orientación y no medición del hardware.

## Mods propios y límites de estado

- Se conserva el código de los módulos propios que llegó con esta entrada.
- Compilación, integración de JAR y funcionamiento en el launcher quedan pendientes hasta que se ejecuten las pruebas.
- `nucleo-campana` tiene declarado un entrypoint cuya implementación no se recibió.
- `decisiones-campana` está declarado, sin archivos de implementación recibidos.
- Las marcas `[SIN VERIFICAR]` y notas de información incompleta se conservan como pendientes; no se inventa contenido para cubrir huecos.

## Integración y pruebas

TLauncher para Windows es el objetivo de instalación. La compilación debe comprobarse con GitHub Actions y el usuario debe jugar el paquete para completar las pruebas de instalación y juego.

## Registro de datos pendientes

La entrada incluye una nota `INCOMPLETE` contradictoria con los hallazgos del paquete, que sí especifican ImmediatelyFast compatible y la incorporación de Fabric API. Se conserva aquí la incertidumbre como nota de origen, no como reemplazo del manifiesto final: esa nota indica que las consultas no confirmarían ImmediatelyFast compatible y que inclusión de Fabric API queda sin establecer, mientras que la sección de hallazgos posterior afirma versiones compatibles e inclusión explícita de Fabric API.

Pendientes expresamente indicados: arranque conjunto, instalación en TLauncher/Windows, compilación e integración de mods propios, hashes/JAR descargados, rendimiento medido, persistencia y migraciones. El hardware indicado arriba se comunicó después como actualizado; el rendimiento no se ha medido.