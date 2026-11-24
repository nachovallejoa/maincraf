# Auditoría de mods

## Estado y alcance

- Estado: candidatos documentales; no es lista de instalación, aprobación ni compatibilidad probada.
- Manifiesto y JARs: no encontrados según el inventario recibido; el paquete completo no puede verificarse.
- No se ejecutó Minecraft ni se midieron FPS, frametimes, RAM, CPU/GPU, carga o compatibilidad.
- No instalar, modificar ni redistribuir mods sin autorización expresa. No subir JARs ni otros binarios de terceros.
- No redistribuir JARs sin revisar licencia y términos del archivo exacto.

## Clasificación

| Categoría | Regla |
|---|---|
| Imprescindible | Dependencia o requisito funcional confirmado por manifiesto/JAR. |
| Recomendado | Candidato pertinente para prueba; no equivale a aprobado. |
| Opcional | Solo necesario para usos o escenas concretas. |
| Reemplazable | Alternativa para la misma función; exige comparar y autorizar. |
| Prescindible | No justificado o cubierto por opciones existentes; requiere evidencia. |
| Incompatible | Conflicto reproducible de combinación exacta; no usar por mera sospecha. |

## Discrepancia de versiones

Las listas recibidas difieren, entre otros, en Entity Culling (`1.7.0` frente a `1.12.1-1.20.1`) e ImmediatelyFast (`1.2.4` frente a `1.2.21`). Sin manifiesto/JARs no se puede decidir cuál corresponde al proyecto. La tabla conserva candidatos documentales separados; no combinarlos como instalación real.

## Candidatos Fabric 1.20.1

| Mod | Versión candidata documental | Función/lado | Evidencia, estado y cautelas |
|---|---|---|---|
| Sodium | `0.5.13` | Renderer, cliente | Ficha exacta confirma Fabric/Quilt 1.20.1, solo cliente y PolyForm Shield 1.0.0. Radeon R3/driver y pack sin probar. Si se usa Indium, ficha exige 1.0.36 o superior; Indium solo si el pack necesita Fabric Rendering API. |
| Lithium | `0.11.4` | Lógica, Fabric/Quilt | Archivo 1.20.1 confirmado; licencia publicada LGPLv3, sin afirmar variante no verificada. Compatibilidad del pack pendiente. Archivo de overrides vacío conserva defaults según documentación de esa rama. |
| ModernFix | `5.25.2+mc1.20.1` | Arranque/memoria, Fabric candidato | Archivo exacto y metadatos/licencia pendientes de verificación en este paquete. Mantener `mixin.perf.dynamic_resources=false`; no asumir compatibilidad con pack. |
| FerriteCore | `6.0.1` | Memoria, Fabric/Quilt | Ficha exacta confirma 1.20.1, MIT y lado cliente/servidor opcional. Ahorro concreto no medido; conflicto citado con Hydrogen permanece sin verificar. |
| Entity Culling | `1.12.1-1.20.1` | Culling, cliente Fabric | Archivo Fabric publicado; usa CPU y beneficio neto en Athlon 5150 no medido. Licencia personalizada tr7zw Protective License: no redistribuir el JAR fuera de los términos del autor/plataforma. |
| ImmediatelyFast | `1.2.21` (archivo `+1.20.4`, declara 1.20.1) | Renderizado, cliente Fabric | Archivo y LGPLv3 confirmados. Efecto en esta iGPU no medido. |
| Dynamic FPS | `3.9.5` | Actividad en segundo plano | Versión, archivo, dependencias y licencia exactos: **[SIN VERIFICAR]**. No tratar como acelerador de FPS en primer plano. |
| Fabric API | `0.92.6+1.20.1` | API Fabric | Ficha y Apache-2.0 confirmadas; no es automáticamente necesaria. Añadir solo si los mods aprobados la requieren. |
| C2ME | Sin versión aprobada | Chunks/paralelismo | Fuera de la base inicial; CPU/I/O y efecto local sin medir. Archivo/licencia exactos: **[SIN VERIFICAR]**. |

## Candidatos Forge 1.20.1

Usar Forge solo si lo exige el manifiesto. No combinar Embeddium con Sodium o Rubidium; no sumar renderers equivalentes.

| Mod | Versión candidata recibida | Condición/estado |
|---|---|---|
| Embeddium | `0.3.31+mc1.20.1` | Candidato Forge; driver Radeon R3 y rendimiento no verificados. Licencia exacta del archivo sin verificar aquí. |
| Radium | `0.12.4` | Versión, licencia e incompatibilidad citada con Canary **[SIN VERIFICAR]**. |
| ModernFix | `5.28.0+mc1.20.1` | Archivo/versión/licencia exactos **[SIN VERIFICAR]**; Dynamic Resources false. |
| FerriteCore | `6.0.1` | MIT verificada para proyecto/versión; compatibilidad con pack no probada. |
| Entity Culling | `1.12.1-1.20.1` | Archivo Forge publicado; licencia personalizada; no redistribuir JAR fuera de términos. |
| ImmediatelyFast | `1.5.5` | Archivo, versión y licencia exactos **[SIN VERIFICAR]**. |
| Dynamic FPS | `3.7.7` | Archivo, dependencias y licencia exactos **[SIN VERIFICAR]**; segundo plano solamente. |
| Particle Core | `0.3.3+1.20.1+forge` | Opcional; no incluir en núcleo. Versión/licencia exactas **[SIN VERIFICAR]**. |

## Licencias y redistribución

- Sodium: PolyForm Shield 1.0.0, confirmada en ficha exacta.
- Lithium: LGPLv3 publicada en ficha exacta; no precisar variante no confirmada en el archivo.
- FerriteCore: MIT confirmada en ficha 6.0.1.
- ImmediatelyFast 1.2.21: LGPLv3 confirmada en ficha del archivo.
- Fabric API 0.92.6: Apache-2.0 confirmada en ficha.
- Entity Culling: licencia personalizada tr7zw Protective License. La política del autor permite inclusión en modpacks alojados en CurseForge/Modrinth bajo sus condiciones, pero no autoriza redistribución general del JAR. Revisar términos antes de publicar/empaquetar.
- ModernFix, Dynamic FPS, Embeddium, Radium y Particle Core: licencia del archivo exacto **[SIN VERIFICAR]** en esta revisión.

## Campos pendientes por candidato

- Autoría del archivo exacto, hash SHA-256 y fuente de descarga (sin subir el JAR).
- Dependencias reales del manifiesto y metadatos del JAR.
- Compatibilidad con el pack completo y el hardware/controlador local.
- Licencia del archivo exacto y permiso según canal/plataforma de distribución.
- FPS, frametimes, CPU, RAM y tiempos de carga medidos reproduciblemente.
- Clasificación aprobada por responsable.

Fuentes documentales verificadas y límites: ver enlaces exactos en el paquete de revisión y mantenerlos asociados a cada versión; las fichas no demuestran compatibilidad local ni rendimiento.