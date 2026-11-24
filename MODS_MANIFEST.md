# Manifiesto documental de dependencias — propuesta segunda etapa

> Este documento registra candidatos y datos de las fichas consultadas; no autoriza instalación ni redistribución. El manifiesto y JARs del pack no se recibieron; versiones instaladas y dependencias de la instancia: **[SIN VERIFICAR]**. No incluir binarios/JARs de terceros en el repositorio. Prominence II declara licencia ARR: no redistribuir pack ni archivos sin autorización expresa.

## Candidatos Fabric 1.20.1

| Mod | Versión candidata | Autor | URL documental | Licencia documentada | Dependencias / condición | Redistribución |
|---|---|---|---|---|---|---|
| Sodium | `0.5.13` | [SIN VERIFICAR] | [Proyecto](https://modrinth.com/mod/sodium) · [build](https://modrinth.com/mod/sodium/version/mc1.20.1-0.5.13-fabric) | Polyform Shield 1.0.0 según ficha consultada | Build exacta y dependencias aún deben cotejarse con el artefacto. Indium puede ser necesario con Sodium 0.5.x si otro mod requiere Fabric Rendering API; no se confirma necesidad para el pack. | Revisar términos y obligaciones por canal; no redistribuir hasta verificar. |
| Lithium | `0.11.4` | [SIN VERIFICAR] | [Proyecto](https://modrinth.com/mod/lithium) · [build](https://modrinth.com/mod/lithium/version/mc1.20.1-0.11.4-fabric) | LGPL-3.0-only indicada por ficha consultada; aplicabilidad al archivo [SIN VERIFICAR] | Confirmar build, metadatos, dependencias en manifiesto/JAR exactos. | No redistribuir hasta confirmar licencia aplicable. |
| FerriteCore | `6.0.1` | [SIN VERIFICAR] | [Proyecto](https://modrinth.com/mod/ferrite-core) · [build](https://modrinth.com/mod/ferrite-core/version/6.0.1) | MIT según ficha consultada | Ficha consultada indica Fabric/Quilt y Minecraft 1.20–1.20.2. Dependencias del artefacto y conflictos reportados con Hydrogen no verificados. | Sujeta a licencia y revisión del archivo/canal. |
| ModernFix | `5.25.2+mc1.20.1` | [SIN VERIFICAR] | [Proyecto](https://modrinth.com/mod/modernfix) · [build](https://modrinth.com/mod/modernfix/version/5.25.2%2Bmc1.20.1) | LGPL-3.0-only según ficha consultada | Ficha indica Fabric 1.20.1. No aplicar configuración de Dynamic Resources sin validación por build exacta. | Sujeta a licencia y revisión del archivo/canal. |
| Sodium Extra | `0.5.9` | [SIN VERIFICAR] | [Proyecto](https://modrinth.com/mod/sodium-extra) · [build](https://modrinth.com/mod/sodium-extra/version/mc1.20.1-0.5.9) | LGPL-3.0-only según ficha consultada | Ficha consultada indica Sodium y Fabric API requeridos; Reese's Sodium Options e Iris opcionales. Cotejar manifiesto/build exactos antes de decidir. | Sujeta a licencia y revisión del archivo/canal. |
| ImmediatelyFast | `1.2.21+1.20.1` | [SIN VERIFICAR] | [Proyecto](https://modrinth.com/mod/immediatelyfast) · [build propuesta, sin verificar](https://modrinth.com/mod/immediatelyfast/version/1.2.21+1.20.1) | Página del proyecto muestra LGPL-3.0-or-later; licencia del archivo exacto [SIN VERIFICAR] | Build propuesta, dependencias y compatibilidad exactas no confirmadas en esta revisión. | No redistribuir hasta cotejar JAR, licencia y términos exactos. |
| BadOptimizations | `2.4.1` propuesta | [SIN VERIFICAR] | [Proyecto](https://modrinth.com/mod/badoptimizations) · [build propuesta, por verificar](https://modrinth.com/mod/badoptimizations/version/2.4.1) | MIT según ficha consultada; archivo exacto [SIN VERIFICAR] | Cotejar la build exacta; no inferir dependencia de una versión distinta. | Sujeta a licencia y revisión del archivo/canal. |
| Dynamic FPS | `3.9.5` | [SIN VERIFICAR] | [Proyecto](https://modrinth.com/mod/dynamic-fps) · [build](https://modrinth.com/mod/dynamic-fps/version/D9mrJwm0) | MIT según ficha consultada | Ficha confirma Fabric, MC 1.20–1.20.1 y reducción de recursos al estar en segundo plano/inactivo/con batería. Requisito Fabric API no acreditado aquí: **[SIN VERIFICAR]**. Cloth Config opcional no se confirma en esta revisión. | Sujeta a licencia y revisión del archivo/canal. |

## Dependencias condicionales (no incluidas por defecto)

| Dependencia | Versión candidata | Autor | URL | Licencia indicada | Condición / estado |
|---|---|---|---|---|---|
| Fabric API | `0.92.6+1.20.1` | [SIN VERIFICAR] | [Build propuesta](https://modrinth.com/mod/fabric-api/version/0.92.6+1.20.1) | Apache-2.0 indicada en ficha consultada; archivo/build exactos [SIN VERIFICAR] | Añadir solo si manifiesto del pack o mod aprobado la requiere; URL de build, autor y dependencia del conjunto no verificados en esta revisión. |
| Indium | `1.0.36` o posterior | [SIN VERIFICAR] | [Proyecto](https://modrinth.com/mod/indium) | [SIN VERIFICAR] para artefacto elegido | Solo si un mod del pack requiere Fabric Rendering API con Sodium 0.5.x; requiere Fabric API. No compatible con Sodium 0.6.0 o posterior. Cotejar build mínima y licencia exacta. |

## Candidatos pospuestos (datos no verificados en esta revisión)

| Mod | Versión propuesta | Autor | URL recibida | Licencia recibida / estado | Dependencias / distribución |
|---|---|---|---|---|---|
| Entity Culling | `1.12.1-1.20.1` | [SIN VERIFICAR] | [Build propuesta](https://modrinth.com/mod/entityculling/version/xM6y5W1N) | tr7zw Protective License mencionada en propuesta; [SIN VERIFICAR] aquí | Verificar texto completo, términos y dependencias del artefacto antes de empaquetar/publicar. |
| Particle Core | `0.2.5+1.20.1` | [SIN VERIFICAR] | [Build propuesta](https://modrinth.com/mod/particle-core/version/ryjPL8AJ) | MIT alegada en propuesta; [SIN VERIFICAR] | Build, dependencias y posible solapamiento con Sodium Extra pendientes. |
| More Culling | `0.24.6` | [SIN VERIFICAR] | [Build propuesta](https://modrinth.com/mod/moreculling/version/1.20.1-0.24.6) | GPL-3.0-only alegada en propuesta; [SIN VERIFICAR] | Dependencias y archivo exacto por verificar. |
| C2ME | `0.2.0+alpha.11.18+1.20.1` | [SIN VERIFICAR] | [Build propuesta](https://modrinth.com/mod/c2me-fabric/version/fyt7FtgA) | Discrepancia LGPL-3.0-only/MIT indicada; [SIN VERIFICAR] | Versión alpha, compatibilidad, dependencias y licencia del JAR exacto pendientes; no incluir en base inicial. |

## Notas de distribución

- Licencias de fichas son datos documentales y no sustituyen el texto de licencia del artefacto concreto ni revisión de términos/canal.
- ImmediatelyFast: proyecto consultado indica LGPL-3.0-or-later; archivo `1.2.21+1.20.1`, dependencias y licencia concreta no acreditados.
- No redistribuir JARs hasta validar hash/versión, autor, licencia y permisos aplicables. No subir binarios de terceros a este repositorio.
- Prominence II declara ARR según la ficha citada; no redistribuir pack ni archivos sin autorización expresa.
- Antes de aprobar: recibir manifiesto/JARs, cotejar versión, loader, dependencias, hash local y licencia por archivo; registrar cualquier dato ausente como pendiente, no inventarlo.
