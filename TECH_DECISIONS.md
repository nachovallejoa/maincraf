# Decisiones técnicas — paquete final de modpack

## Decisiones del director y motivos

| Decisión | Motivo | Estado y límites |
|---|---|---|
| Base Minecraft 1.20.1 + Fabric | Es la versión elegida en el contexto y las cuatro versiones seleccionadas están documentadas para Minecraft 1.20.1 y Fabric. | Versión exacta de Fabric Loader sin fijar; `fabric_loader_version: null`. No declarar instancia validada. |
| Selección base de cuatro mods: Sodium, Lithium, FerriteCore y ModernFix | Modrinth confirma IDs de versión y nombres de archivo: Sodium `OihdIimA`, Lithium `iEcXOkz4`, FerriteCore `unerR5MN`, ModernFix `rPmgLeZC`. Sus objetivos son renderizado, lógica, memoria y optimizaciones diversas. | No hubo prueba conjunta de lanzamiento; no se afirma rendimiento ni compatibilidad efectiva en ejecución. |
| Sodium solo cliente; Lithium, FerriteCore y ModernFix ambos lados | Los entornos documentados para las versiones elegidas son client para Sodium y client/server para los otros tres. | El manifiesto conserva esta distinción. |
| No agregar Fabric API al conjunto mínimo | Las respuestas consultadas de Modrinth para las versiones elegidas no declaran dependencias obligatorias. | Si se añaden mods que utilicen APIs de Fabric, revisar dependencias, incluido soporte de renderizado Sodium, antes de incorporarlos. |
| Sin archivos de `pack/overrides/` ni configuración forzada | No hay contenido de configuración completo verificado; se mantienen los valores predeterminados y se evita inventar opciones. | No se añaden configuraciones parciales o supuestas. Lithium con opciones predeterminadas; una configuración vacía es normal según su documentación consultada. |
| `-Xmx6G` como orientación, no ajuste certificado | El usuario declaró unos 10 GB disponibles; el valor es un punto de partida condicionado, no una medición del consumo del pack. | Sin `-Xms` añadido y sin banderas de GC extra; usar argumentos predeterminados del launcher. Hardware y consumo no medidos independientemente. |
| Mantener fuera mods RPG y candidatos opcionales | Versiones/dependencias y selección individual no están auditadas suficientemente para esta entrega. | No se les declara incompatibles; exclusión por falta de auditoría suficiente. |
| No entregar código de mods propios | No se proporcionó código ni proyecto; la entrada no acredita autorización explícita de implementación ni permite comprobar Gradle. | Los módulos descritos quedan planificados; compilación e instalación no disponibles. No inventar código para completar el vacío. |
| Constructor `.mrpack` debe fallar con Loader `null` | El índice Modrinth necesita versión de dependencia `fabric-loader`, y no hay versión exacta verificada. | No estimar ni fijar un ejemplo. La compilación automática puede fallar de forma intencional hasta resolver la versión exacta. |
| No subir binarios de mods de terceros | Los JARs de terceros no deben almacenarse en el repositorio. El script descarga archivos desde Modrinth durante el build y solo inspecciona posibles artefactos propios construidos localmente. | No se incluyeron JARs de terceros en los archivos guardados. |

## Selección registrada

| Mod | Versión | ID de versión Modrinth | Archivo | Entorno |
|---|---|---|---|---|
| Sodium | `mc1.20.1-0.5.13-fabric` | `OihdIimA` | `sodium-fabric-0.5.13+mc1.20.1.jar` | Cliente |
| Lithium | `mc1.20.1-0.11.4-fabric` | `iEcXOkz4` | `lithium-fabric-mc1.20.1-0.11.4.jar` | Cliente y servidor |
| FerriteCore | `6.0.1` | `unerR5MN` | `ferritecore-6.0.1-fabric.jar` | Cliente y servidor |
| ModernFix | `5.25.2+mc1.20.1` | `rPmgLeZC` | `modernfix-fabric-5.25.2+mc1.20.1.jar` | Cliente y servidor |

Los hallazgos proporcionados no incluyen licencia individual ni prueba de lanzamiento conjunta. Consultar `MODS_MANIFEST.md` para registrar los enlaces oficiales y dejar licencias como pendientes cuando no haya dato confirmado.

## Fuera de esta selección

Opcionales de rendimiento descartados para esta entrega: Sodium Extra `0.5.9`, ImmediatelyFast `1.2.21+1.20.1`, BadOptimizations `2.4.1`.

Candidatos RPG/combate/misiones fuera de selección: Skill Tree `1.6.1+1.20.1-fabric`; Pufferfish’s Skills `0.16.7+1.20`; Simply Skills `1.3.2+1.20.1`; PlayerEx: Directors Cut `4.0.5+1.20.1`; RPG Inventory `1.8.0`; Reforged `1.20.1-1.0.9-Fabric`; Better Combat `1.9.0+1.20.1-fabric`; Remnants `3.0.0+fabric-1.20.1`; Bosses of Mass Destruction `1.7.5-1.20.1`; Village Diplomacy `1.4.0`; FTB Quests `2001.4.22`. No se afirma incompatibilidad: versiones y dependencias no auditadas suficientemente.

## Pendientes de verificación

- Elegir y documentar una versión exacta de Fabric Loader a partir de una fuente verificable antes de tratar la instancia como construible/validada.
- Obtener licencias verificadas de los cuatro archivos seleccionados para completar el manifiesto; no inferirlas del nombre del proyecto.
- Ejecutar el build en GitHub después de resolver Loader; revisar logs y resultado sin confundir un paquete generado con una prueba de lanzamiento.
- Probar instalación y juego real por el usuario; no hay resultados de FPS, memoria o estabilidad disponibles.
- Auditar mods RPG/optativos y cualquier dependencia nueva antes de modificar el conjunto.
