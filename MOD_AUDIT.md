# Auditoría de mods — propuesta segunda etapa

## Estado y alcance

- Los candidatos siguientes son documentales; no son lista de instalación, aprobación ni compatibilidad probada.
- El manifiesto del pack y los JAR exactos no se recibieron; no se verificó el pack completo.
- No se ejecutó Minecraft ni se midieron FPS, frametimes, RAM, CPU/GPU, arranque, carga ni estabilidad.
- No instalar, modificar ni redistribuir mods sin autorización y revisión de licencias. No subir archivos binarios/JAR de terceros.
- **NO DATA** significa medición ausente, no cero ni estimación.

## Clasificación

| Categoría | Regla |
|---|---|
| Imprescindible | Requisito funcional confirmado por manifiesto/JAR. Ningún candidato se marca así. |
| Recomendado provisional | Candidato pertinente para probar; no equivale a aprobación. |
| Opcional / reemplazable | Solo para escenario concreto; comparar y autorizar. |
| Prescindible | No justificado o cubierto por opciones existentes; exige evidencia. |
| Incompatible | Conflicto reproducible de combinación exacta; no asignarlo por sospecha. |

## Candidatos propuestos para Fabric 1.20.1

| Mod / build | Clasificación | Función / condiciones documentales | FPS | Frametime | RAM | Arranque | Carga |
|---|---|---|---|---|---|---|---|
| Sodium `0.5.13` | Recomendado provisional, condicionado a validar GPU/driver/OpenGL | Candidato de renderizado. Build exacta consultada; compatibilidad con Radeon R3 y pack sin probar. Polyform Shield 1.0.0 según página; revisar términos. | NO DATA | NO DATA | NO DATA | NO DATA | NO DATA |
| Lithium `0.11.4` | Recomendado provisional | Candidato de lógica de juego. Build consultada; dependencias y compatibilidad conjunta pendientes. LGPL-3.0-only según ficha. | NO DATA | NO DATA | NO DATA | NO DATA | NO DATA |
| FerriteCore `6.0.1` | Recomendado provisional | Ficha consultada indica Fabric/Quilt y MC 1.20–1.20.2. MIT según ficha; duplicados/pack y posible solapamiento con ModernFix pendientes. | NO DATA | NO DATA | NO DATA | NO DATA | NO DATA |
| ModernFix `5.25.2+mc1.20.1` | Recomendado provisional para ensayo aislado | Ficha consultada indica Fabric 1.20.1 y LGPL-3.0-only. No aplicar `mixin.perf.dynamic_resources=false`: clave/valor/efecto sin verificar. | NO DATA | NO DATA | NO DATA | NO DATA | NO DATA |
| Sodium Extra `0.5.9` | Opcional | Add-on para Sodium; ficha consultada indica LGPL-3.0-only. Dependencias exactas por cotejar; no se validaron opciones/configuración. | NO DATA | NO DATA | NO DATA | NO DATA | NO DATA |
| ImmediatelyFast `1.2.21+1.20.1` | Opcional; artefacto exacto pendiente | Proyecto describe mejoras de renderizado inmediato y menciona incompatibilidades conocidas con OptiFine/OptiFabric. Release exacta, dependencias y licencia del archivo sin verificar. Proyecto muestra LGPL-3.0-or-later. | NO DATA | NO DATA | NO DATA | NO DATA | NO DATA |
| BadOptimizations `2.4.1` | Opcional; versión exacta pendiente de cotejo | Candidato documental de microoptimizaciones; ficha/compatibilidad conjunta por verificar. MIT según ficha consultada para candidato citado. | NO DATA | NO DATA | NO DATA | NO DATA | NO DATA |
| Dynamic FPS `3.9.5` | Opcional / reemplazable | Reduce recursos en segundo plano, inactividad o batería; no se propone como aumento de FPS con juego enfocado. Ficha indica MIT. Requisito Fabric API: SIN VERIFICAR. | NO DATA | NO DATA | NO DATA | NO DATA | NO DATA |

## Dependencias condicionales

| Componente | Condición para considerar | Pendiente |
|---|---|---|
| Fabric API `0.92.6+1.20.1` | Solo si el manifiesto o un mod elegido la requiere. | Necesidad para el conjunto, autor y licencia/artefacto exactos: cotejar; la fuente consultada indicaba Apache-2.0. |
| Indium `1.0.36` o posterior | Solo si un mod requiere Fabric Rendering API con Sodium 0.5.x. | Indium requiere Fabric API; no compatible con Sodium 0.6.0 o posterior. Versión exacta y licencia del artefacto elegido: cotejar. |

## Candidatos pospuestos / no verificados

Estos datos provienen de la propuesta recibida y no se deben tratar como hechos confirmados aquí. No descargar ni incluir JARs por esta auditoría.

| Mod / build propuesta | Estado y pendientes |
|---|---|
| Entity Culling `1.12.1-1.20.1` | Pospuesto para prueba aislada. Advertencia de CPU y aplicabilidad al Athlon no verificadas aquí. Licencia/tr7zw Protective License y términos específicos pendientes; no redistribuir sin cotejar el archivo. |
| Particle Core `0.2.5+1.20.1` | Pospuesto; posible solapamiento funcional con Sodium Extra no demostrado. Build, dependencias y MIT indicados en la propuesta, sin verificar. |
| More Culling `0.24.6` | Pospuesto. Dependencias, licencia GPL-3.0-only y coste/beneficio locales sin verificar. |
| C2ME `0.2.0+alpha.11.18+1.20.1` | Fuera de base inicial. Release alpha, estabilidad, compatibilidad, dependencias y discrepancia de licencia LGPL/MIT sin verificar para el artefacto exacto. |
| ScalableLux | Pospuesto; release Fabric 1.20.1 no comprobada. |
| Noisium | Pospuesto; no se verificó artefacto utilizable en versiones consideradas. |
| FastLoad / DashLoader | Pospuestos; releases y compatibilidad no verificadas. |
| Hydrogen | No incluido; posible incompatibilidad con FerriteCore sin verificar. |

## Referencias consultadas y suministradas

- [Prominence II](https://modrinth.com/modpack/prominence-2-fabric)
- [Sodium 0.5.13](https://modrinth.com/mod/sodium/version/mc1.20.1-0.5.13-fabric) · [documentación de hardware](https://github.com/CaffeineMC/sodium)
- [Lithium 0.11.4](https://modrinth.com/mod/lithium/version/mc1.20.1-0.11.4-fabric)
- [FerriteCore 6.0.1](https://modrinth.com/mod/ferrite-core/version/6.0.1)
- [ModernFix 5.25.2+mc1.20.1](https://modrinth.com/mod/modernfix/version/5.25.2%2Bmc1.20.1)
- [Sodium Extra 0.5.9](https://modrinth.com/mod/sodium-extra/version/mc1.20.1-0.5.9)
- [ImmediatelyFast](https://modrinth.com/mod/immediatelyfast) · [versión propuesta, por verificar](https://modrinth.com/mod/immediatelyfast/version/1.2.21+1.20.1)
- [BadOptimizations 2.4.1 propuesta](https://modrinth.com/mod/badoptimizations/version/2.4.1)
- [Dynamic FPS 3.9.5](https://modrinth.com/mod/dynamic-fps/version/D9mrJwm0)
- [Fabric API](https://modrinth.com/mod/fabric-api/version/0.92.6+1.20.1) · [Indium](https://modrinth.com/mod/indium)
- Referencias de candidatos pospuestos: [Entity Culling](https://modrinth.com/mod/entityculling/version/xM6y5W1N), [Particle Core](https://modrinth.com/mod/particle-core/version/ryjPL8AJ), [More Culling](https://modrinth.com/mod/moreculling/version/1.20.1-0.24.6), [C2ME](https://modrinth.com/mod/c2me-fabric/version/fyt7FtgA), [ScalableLux](https://modrinth.com/mod/scalablelux/version/Yx1tgJMI), [Noisium](https://modrinth.com/mod/noisium). Estas referencias no se volvieron a verificar en esta revisión.

## Mediciones

| Métrica | Resultado |
|---|---|
| FPS | NO DATA — no se ejecutó benchmark. |
| Frametime | NO DATA — no se midió. |
| RAM | NO DATA — no se midió. |
| CPU/GPU | NO DATA — no se midió. |
| Tiempo de arranque | NO DATA — no se midió. |
| Tiempo de carga | NO DATA — no se midió. |
| Compatibilidad / estabilidad | NO DATA — no se probó instancia. |

Campos vacíos/NO DATA no significan cero ni resultado favorable. Cualquier medición posterior requiere instancia aislada, condiciones reproducibles y aprobación expresa.
