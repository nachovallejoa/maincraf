# Decisiones técnicas — modpack final

## Decisiones del director y motivos

| Decisión | Motivo | Límite / estado |
|---|---|---|
| Mantener Minecraft `1.20.1` y Fabric Loader `0.20.1` | Los hallazgos recibidos señalan esa versión documental y la entrada más reciente consultada con `stable: true`. | No prueba que el paquete completo sea compatible o instalable. |
| Usar el nombre provisional `La Marea de los Mil Soles` | Nombre aportado como provisional en el paquete recibido. | Provisional; no altera la selección de mods. |
| Mantener el inventario provisional y hacer visibles los huecos | La selección incluye información declarada, pero varias fuentes no devolvieron IDs y datos suficientes; las dependencias obligatorias siguen pendientes. | No se afirma compatibilidad integral ni completitud. |
| No inferir los datos de dependencias faltantes | Para Better Combat y Bosses of Mass Destruction no se aportaron versiones/IDs exactos verificados de todas las dependencias. | Registrar los nombres de dependencias y la verificación pendiente. |
| Descartar ImmediatelyFast `1.2.21+1.20.1` | La evidencia citada solo mostró variantes `1.2.21+1.20.4` y `1.2.21+1.21.1`, sin respaldar la variante exacta para 1.20.1. | No trasladar versiones de Minecraft distintas. |
| No presentar el paquete como listo para publicar o instalar | La fuente explícitamente advierte que hay metadatos y dependencias sin verificar y que falta validación del conjunto. | La automatización debe fallar de forma segura ante metadatos incompletos, sin rellenarlos. |
| No subir JARs de mods de terceros | Los artefactos deben obtenerse desde sus fuentes autorizadas; el repositorio no redistribuye binarios de terceros. | Los JAR tampoco se crean ni se adjuntan manualmente. |
| No agregar configuraciones de mods especulativas | No se verificaron todas las claves/valores predeterminados de las versiones exactas. | No entregar archivos vacíos ni opciones afirmadas como verificadas. |
| No fijar memoria ni argumentos JVM como óptimos | Hay datos de hardware declarados por el usuario (12 GB instalados, unos 10 GB disponibles y Windows usa unos 500 MB), pero no hay pruebas de ejecución/benchmark ni configuración completa verificada. | No recomendar un heap ni flags específicos como resultado medido. |
| Registrar la implementación propia con cautela | El texto entregado usa `mods-propios/mareas-core`; el árbol del branch existente organiza un módulo `venas-core` y solo contiene parte de la estructura. | No sustituir nombres ni inventar archivos Java para forzar una coincidencia. Compilación pendiente. |
| Mantener las discrepancias de fuentes como pendientes | Se reportó una discrepancia de ID traducido/clase y un directorio de ejecución no confirmado. | No elegir una alternativa sin una fuente aprobada. |
| Dejar las pruebas en estado pendiente | La compilación del proyecto descrito no se ejecutó y no hay prueba de juego. | Esperar la compilación de GitHub y la prueba real del usuario; no declarar resultados anticipados. |

## Selección explícitamente descartada en la revisión recibida

Sodium Extra `0.5.9`, Dynamic FPS `3.9.5`, Skill Tree `1.6.1+1.20.1-fabric`, Pufferfish’s Skills `0.16.7+1.20`, Simply Skills `1.3.2+1.20.1`, PlayerEX: Directors Cut `4.0.5+1.20.1`, RPG Inventory `1.8.0`, Questlog `3.3.2-1.20.1-fabric`, Reforged `1.20.1-1.0.9-Fabric` e ImmediatelyFast `1.2.21+1.20.1`. La exclusión no demuestra incompatibilidad general; respeta los hallazgos y límites de verificación aportados.

## Pendientes de verificación de fuentes

Las consultas recibidas no aportaron verificación suficiente de IDs, artefactos, licencias o compatibilidad para Sodium, Remnants, Village Diplomacy y FTB Quests; tampoco cerraron las dependencias obligatorias citadas. Para Better Combat, el dato INCOMPLETE identifica el proyecto `gedNE4y2`, pero slug, versión compatible, artefacto y licencia no fueron verificados. Hardware en ejecución, rendimiento y estructura de TLauncher permanecen sin verificar.
