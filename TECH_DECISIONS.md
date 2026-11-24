# Decisiones técnicas — propuestas pendientes de aprobación

> Ninguna decisión técnica final está aprobada. Disponibilidad de build no demuestra compatibilidad del pack ni rendimiento en hardware real.

## Comparativa de versiones y loaders

| Minecraft/loader | Java documentado en el material revisado | Evidencia disponible | Estado/riesgo |
|---|---|---|---|
| 1.19.2 | Java 17 | Prominence I citado como legado/descontinuado | No propuesta como base; pack/base exactos sin verificar |
| 1.20.1 + Fabric | Java 17 | Builds candidatas para Fabric y pack Prominence II listado para Fabric 1.20.1 | **Candidata principal documental**, no aprobada; manifiesto de destino y compatibilidad completa sin verificar |
| 1.20.1 + Forge | Java 17 | Embeddium 0.3.31+mc1.20.1 listado para Forge/NeoForge | Alternativa solo si el manifiesto exige Forge; pack y hardware sin verificar |
| 1.20.6 + Fabric | Java 21 en tabla de investigación | Cambios de desarrollo para 1.20.5/1.20.6 citados | Pack/base exactos sin verificar |
| 1.21.1 + Fabric | Java 21 | Ejemplos de packs citados, sin equivalencia demostrada | Exploratoria; herramientas/rendimiento y pack exacto sin verificar |
| 1.21.1 + NeoForge | Java 21 | Medieval MC citado como listado para NeoForge 1.21.1 | Posibilidad de explorar packs, no base optimizada auditada |
| 1.21.4 (loader no determinado) | Java 21 indicado para esa generación en la investigación; requisito exacto no comprobado | No se identificó pack comparable con la misma claridad | No propuesta como base |

`[SIN VERIFICAR]` significa falta de evidencia concreta, no inexistencia de combinación. Las referencias a packs no prueban adecuación, elección del usuario ni compatibilidad con Radeon R3.

## Propuestas técnicas (todas pendientes de aprobación)

| ID | Propuesta | Justificación/condición | Estado |
|---|---|---|---|
| TDP-01 | Investigar primero 1.20.1 + Fabric | Coincidencia documental de candidatos y pack RPG citado; requiere manifiesto, confirmación y pruebas | Pendiente aprobación |
| TDP-02 | Mantener Forge 1.20.1 como alternativa condicionada | Solo si el pack lo exige; Embeddium está listado en Forge/NeoForge | Pendiente manifiesto y pruebas |
| TDP-03 | No afirmar rendimiento sin benchmark reproducible | No hay mediciones locales | Regla de evidencia |
| TDP-04 | ModernFix Dynamic Resources `false` | Código consultado indica default false; pack sin auditar | Mantener hasta auditoría autorizada |
| TDP-05 | No precargar Sodium JSON ni fragmento `options.txt` | Esquema/valores exactos no verificados para este fin | Pendiente validación en instancia |
| TDP-06 | Mantener mods condicionales fuera de la base | No hay manifiesto ni cuello de botella identificado | Añadir solo por necesidad, prueba y autorización |
| TDP-07 | No imponer `-Xmx4G` como óptimo | Propuesta anterior, no valor medido ni decisión aprobada | Heap se fija y mide en protocolo |
| TDP-08 | No redistribuir JARs sin revisar términos | Licencias tienen condiciones específicas | Autorización/política de distribución pendiente |

## Límites y comprobaciones antes de decidir

- Radeon R3/OpenGL y controlador local **[SIN VERIFICAR]**; no asegurar que Sodium arranque ni que Embeddium resuelva un fallo.
- Manifiesto RPG y JARs ausentes; compatibilidad completa **[SIN VERIFICAR]**.
- Sin ejecución o benchmark; no hay cifras de FPS, RAM, carga o estabilidad.
- C2ME fuera de la base hasta verificar build, estado y compatibilidad.
- Revisar licencias específicas y permisos para distribución prevista.
- Confirmar Java, launcher, Windows, controlador, OpenGL/Vulkan y necesidades RPG.

## Registro de aprobación

| ID | Decisión final | Aprobador | Fecha | Evidencia/condiciones |
|---|---|---|---|---|
|  |  |  |  |  |

## Fuentes citadas en la revisión recibida

- [Java Edition 1.20.1](https://minecraft.wiki/w/Java_Edition_1.20.1) · [Fabric install](https://wiki.fabricmc.net/install)
- [Sodium 0.5.13](https://modrinth.com/mod/sodium/version/mc1.20.1-0.5.13-fabric) · [Lithium 0.11.4](https://modrinth.com/mod/lithium/version/mc1.20.1-0.11.4-fabric)
- [ModernFix 5.25.2](https://modrinth.com/mod/modernfix/version/5.25.2%2Bmc1.20.1) · [ImmediatelyFast 1.2.4](https://modrinth.com/mod/immediatelyfast/version/1.2.4%2B1.20.1)
- [Entity Culling 1.7.0](https://modrinth.com/mod/entityculling/version/1JrKE0F6) · [Embeddium 0.3.31](https://modrinth.com/mod/embeddium/version/0.3.31%2Bmc1.20.1)
