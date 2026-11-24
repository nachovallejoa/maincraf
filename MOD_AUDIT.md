# Auditoría de mods

## Estado y alcance

- Los candidatos siguientes son documentales; no son lista de instalación, aprobación ni compatibilidad probada.
- Manifiesto y JARs del pack no recibidos; no se verificó el pack completo.
- No se ejecutó Minecraft ni se midieron FPS, frametimes, RAM, CPU/GPU, arranque, carga o compatibilidad.
- No instalar, modificar ni redistribuir mods sin autorización expresa y revisión de licencia. No subir binarios/JARs de terceros.
- Las mediciones se dejan vacías intencionalmente: **NO DATA**.

## Clasificación

| Categoría | Regla |
|---|---|
| Imprescindible | Requisito funcional confirmado por manifiesto/JAR. |
| Recomendado provisional | Candidato pertinente para probar; no equivale a aprobación. |
| Opcional | Solo para uso/escenario concreto. |
| Reemplazable | Alternativa para una función; comparar y autorizar. |
| Prescindible | No justificado o cubierto por opciones existentes; requiere evidencia. |
| Incompatible | Conflicto reproducible de combinación exacta; no asignar por sospecha. |

## Candidatos propuestos para Fabric 1.20.1

| Mod / build candidata | Clasificación | Función / condición documental | FPS | Frametime | RAM | Arranque | Carga |
|---|---|---|---|---|---|---|---|
| Sodium `0.5.13` | Recomendado provisional | Renderizador candidato; build exacta **[SIN VERIFICAR]**. Radeon R3/driver, OpenGL, pack y dependencias sin probar. Polyform Shield 1.0.0 figura en proyecto. |  |  |  |  |  |
| Lithium `0.11.4` | Recomendado provisional | Candidato complementario al renderizado; build, dependencias y licencia exactas **[SIN VERIFICAR]**. |  |  |  |  |  |
| FerriteCore `6.0.1` | Recomendado provisional | Ficha consultada: Fabric/Quilt, MC 1.20–1.20.2, MIT. Pack no probado; incompatibilidad citada con Hydrogen no verificada. |  |  |  |  |  |
| ModernFix `5.25.2+mc1.20.1` | Recomendado provisional | Ficha consultada: Fabric 1.20.1, LGPL-3.0-only. Build/pack/configuración local pendientes. No se aprueba clave Dynamic Resources. |  |  |  |  |  |
| Entity Culling `1.12.1-1.20.1` | Opcional | Ficha consultada: Fabric 1.20.1/cliente; pack y Sodium no probados. Alertas concretas de CPU/artefactos visuales **[SIN VERIFICAR]**. Licencia personalizada. |  |  |  |  |  |
| ImmediatelyFast `1.2.1+1.20.1` | Opcional | Ficha: Fabric/Forge/Quilt, MC 1.20–1.20.1. Comprobar incompatibilidad declarada con MemoryLeakFix `<=1.1.1`; interacción con pack sin probar. |  |  |  |  |  |
| BadOptimizations `2.1.4` | Opcional | La URL recibida identifica 2.1.4 (1.20.1), no 2.4.1. Otra build 2.4.1 compatible no verificada. |  |  |  |  |  |
| Sodium Extra `0.5.9` | Opcional | Ficha: requiere Sodium y Fabric API; Reese’s Sodium Options e Iris opcionales. No hay opciones/configuración validadas. |  |  |  |  |  |
| Dynamic FPS `3.9.5` | Opcional | Ficha: Fabric 1.20–1.20.1, requiere Fabric API, Cloth Config opcional. Reduce recursos en segundo plano/inactividad/batería; no es acelerador de primer plano. |  |  |  |  |  |
| Fabric API `0.92.6+1.20.1` | Dependencia condicionada | Incluir solo si manifiesto o mod aprobado lo requiere. Build/licencia/autor exactos **[SIN VERIFICAR]**. |  |  |  |  |  |
| Particle Core `0.2.5+1.20.1` | Reemplazable | No añadir de entrada junto con Sodium Extra. Build, dependencias y solapamiento **[SIN VERIFICAR]**. |  |  |  |  |  |
| More Culling `0.24.6` | Prescindible | Excluido inicialmente; solapamiento y dependencia citados **[SIN VERIFICAR]**. |  |  |  |  |  |
| C2ME `0.2.0+alpha.11.18+1.20.1` | Prescindible | Fuera de primera pasada; build/riesgos específicos **[SIN VERIFICAR]** en esta revisión. |  |  |  |  |  |
| Noisium / Noisiumed | Prescindible | Build exacta y relación con Fast Noise **[SIN VERIFICAR]**. |  |  |  |  |  |
| LazyDFU `0.1.3` | Prescindible | No prioritario; beneficio específico **[SIN VERIFICAR]**. |  |  |  |  |  |

Los excluidos no deben borrarse de una instancia existente sin autorización. Sin manifiesto no se puede determinar si alguno forma parte de la instalación.

## Fuentes documentales citadas

- [Sodium](https://modrinth.com/mod/sodium) · [guía oficial de instalación](https://github.com/CaffeineMC/sodium/wiki/Installation) · [build indicada, pendiente de confirmar](https://modrinth.com/mod/sodium/version/OihdIimA)
- [Lithium](https://modrinth.com/mod/lithium) · [build indicada](https://modrinth.com/mod/lithium/version/mc1.20.1-0.11.4-fabric)
- [FerriteCore 6.0.1](https://modrinth.com/mod/ferrite-core/version/6.0.1)
- [ModernFix](https://modrinth.com/mod/modernfix) · [build 5.25.2](https://modrinth.com/mod/modernfix/version/5.25.2%2Bmc1.20.1)
- [Entity Culling](https://modrinth.com/mod/entityculling) · [build](https://modrinth.com/mod/entityculling/version/xM6y5W1N)
- [ImmediatelyFast](https://modrinth.com/mod/immediatelyfast) · [build](https://modrinth.com/mod/immediatelyfast/version/txcO4lNF)
- [BadOptimizations](https://modrinth.com/mod/badoptimizations) · [build 2.1.4 indicada por la URL](https://modrinth.com/mod/badoptimizations/version/GydKiUd0)
- [Sodium Extra](https://modrinth.com/mod/sodium-extra) · [build](https://modrinth.com/mod/sodium-extra/version/mc1.20.1-0.5.9)
- [Dynamic FPS](https://modrinth.com/mod/dynamic-fps) · [build](https://modrinth.com/mod/dynamic-fps/version/D9mrJwm0)
- [Prominence II: Hasturian Era](https://modrinth.com/modpack/prominence-2-fabric): referencia de MC 1.20.1/Fabric; licencia ARR, no redistribuir sin autorización.

## Estado de mediciones

| Métrica | Resultado |
|---|---|
| FPS | **NO DATA** — no se ejecutó benchmark. |
| Frametime | **NO DATA** — no se midió. |
| RAM | **NO DATA** — no se midió. |
| Tiempo de arranque | **NO DATA** — no se midió. |
| Tiempo de carga | **NO DATA** — no se midió. |
| Compatibilidad/estabilidad | **NO DATA** — no se probó una instancia. |

Campos vacíos no significan cero ni resultado favorable. Requiere pruebas controladas y reproducibles en instancia aislada después de revisión/autorización.
