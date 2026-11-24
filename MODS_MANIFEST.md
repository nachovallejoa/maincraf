# Manifiesto del modpack — selección final

El manifiesto técnico (`pack/mods.json`) registra los cuatro mods seleccionados para Minecraft 1.20.1/Fabric. Los hallazgos de revisión confirman sus IDs y archivos en Modrinth. Licencias individuales no constan en los datos de entrada; quedan pendientes de consultar directamente en las fichas/proyectos, sin inferir licencias ni permisos de redistribución.

| Mod / slug | Versión | ID de versión Modrinth | Archivo verificado | Entorno | Licencia | Modrinth |
|---|---|---|---|---|---|---|
| Sodium (`sodium`) | `mc1.20.1-0.5.13-fabric` | `OihdIimA` | `sodium-fabric-0.5.13+mc1.20.1.jar` | Solo cliente | **Pendiente [SIN VERIFICAR]**; la entrada no proporciona licencia del archivo/proyecto. | [Proyecto Sodium](https://modrinth.com/mod/sodium) · [Versión](https://modrinth.com/mod/sodium/version/OihdIimA) |
| Lithium (`lithium`) | `mc1.20.1-0.11.4-fabric` | `iEcXOkz4` | `lithium-fabric-mc1.20.1-0.11.4.jar` | Cliente y servidor | **Pendiente [SIN VERIFICAR]**; la entrada no proporciona licencia del archivo/proyecto. | [Proyecto Lithium](https://modrinth.com/mod/lithium) · [Versión](https://modrinth.com/mod/lithium/version/iEcXOkz4) |
| FerriteCore (`ferrite-core`) | `6.0.1` | `unerR5MN` | `ferritecore-6.0.1-fabric.jar` | Cliente y servidor | **Pendiente [SIN VERIFICAR]**; la entrada no proporciona licencia del archivo/proyecto. | [Proyecto FerriteCore](https://modrinth.com/mod/ferrite-core) · [Versión](https://modrinth.com/mod/ferrite-core/version/unerR5MN) |
| ModernFix (`modernfix`) | `5.25.2+mc1.20.1` | `rPmgLeZC` | `modernfix-fabric-5.25.2+mc1.20.1.jar` | Cliente y servidor | **Pendiente [SIN VERIFICAR]**; la entrada no proporciona licencia del archivo/proyecto. | [Proyecto ModernFix](https://modrinth.com/mod/modernfix) · [Versión](https://modrinth.com/mod/modernfix/version/rPmgLeZC) |

## Dependencias y validación

- Las respuestas consultadas de Modrinth no declaran dependencias obligatorias para las versiones elegidas. El conjunto mínimo no agrega Fabric API.
- Si se incorporan mods que utilicen APIs de Fabric, revisar de nuevo sus dependencias y los requisitos de renderizado Sodium.
- Minecraft 1.20.1 y Fabric son coherentes con las versiones documentadas en los hallazgos. La versión exacta de Fabric Loader no se verificó: `fabric_loader_version` permanece `null`.
- No se ha verificado un lanzamiento conjunto, compilación del paquete, compatibilidad efectiva en el equipo ni rendimiento. No declarar la instancia lista o validada.
- No hay duplicados entre estos cuatro mods. Los objetivos pueden solaparse parcialmente, sin que las fuentes aportadas demuestren equivalencia o incompatibilidad.

## Fuera de la selección

Opcionales de rendimiento no incluidos: Sodium Extra `0.5.9`, ImmediatelyFast `1.2.21+1.20.1`, BadOptimizations `2.4.1`.

Candidatos RPG, combate y misiones fuera de esta selección: Skill Tree `1.6.1+1.20.1-fabric`; Pufferfish’s Skills `0.16.7+1.20`; Simply Skills `1.3.2+1.20.1`; PlayerEx: Directors Cut `4.0.5+1.20.1`; RPG Inventory `1.8.0`; Reforged `1.20.1-1.0.9-Fabric`; Better Combat `1.9.0+1.20.1-fabric`; Remnants `3.0.0+fabric-1.20.1`; Bosses of Mass Destruction `1.7.5-1.20.1`; Village Diplomacy `1.4.0`; FTB Quests `2001.4.22`. Se mantienen fuera por falta de auditoría suficiente de versiones/dependencias; no se declara incompatibilidad.

## Pendientes de fuente

- Licencia individual y condiciones aplicables: las respuestas/fuentes incluidas en los hallazgos no devolvieron esa información para cada versión.
- Dependencias obligatorias: los resultados consultados indicaron que no se declaraban para las versiones incluidas; revisar de nuevo si cambia la selección.
- Prueba conjunta de lanzamiento y medición de recursos: no se suministraron resultados.
