# Decisiones técnicas — propuestas pendientes de aprobación

> No hay decisión técnica final aprobada. La disponibilidad de un build no demuestra compatibilidad del pack ni rendimiento en el hardware real. Esta comparativa es documental; las conclusiones dependen del manifiesto, runtime, driver y pruebas.

## Comparativa de versiones y loaders

| Minecraft / loader | Situación documental recibida | Evaluación y límites |
|---|---|---|
| 1.19.2 + Fabric | Candidata histórica; la propuesta señala Sodium 1.19.x deprecado. | Menor justificación que 1.20.1 en el paquete actual. Pack y rendimiento comparativo sin verificar. |
| 1.19.2 + Forge | Se citaron Embeddium/FerriteCore/ModernFix. | Disponibilidad citada no equivale a compatibilidad; no se midió localmente. |
| 1.19.2 + NeoForge | La entrada menciona recomendación de Forge para esa generación. | Fuentes RPG y soporte exacto no validados en esta revisión; no priorizar. |
| 1.20.1 + Fabric | Java 17 asociado documentalmente; candidatos Sodium/Lithium y otros; Prominence II citado como ejemplo RPG Fabric 1.20.1. | **Candidata principal**, no decisión. Manifiesto, pack completo, GPU/driver y rendimiento local no verificados. No instalar pack completo por referencia promocional. |
| 1.20.1 + Forge | Java 17; Embeddium candidato en vez de Sodium. | **Alternativa condicionada** solo si el manifiesto lo exige. Pack, driver y rendimiento no verificados. Elegir un único loader/renderer. |
| 1.20.1 + NeoForge | No priorizada en la propuesta recibida frente a Forge. | Sin aprobación ni evidencia de pack en esta revisión. |
| 1.21.1 + loaders citados | Java 21 indicado en la propuesta; packs RPG citados como ejemplos. | No priorizada: pack equivalente y compatibilidad local no verificados. |
| 26.2 + loaders citados | La entrada describe Vulkan como experimental y soporte de Radeon R3 desconocido. | No priorizada. Runtime, builds/mods y pack RPG exactos no verificados en esta revisión. |

Java Edition 1.20.1 se asocia a Java 17 en la documentación de la propuesta, pero el Java local no se verificó. La transición de Minecraft a OpenGL Core 3.2 no certifica el controlador Radeon R3 de Windows. Los requisitos oficiales actuales citados en la revisión describen como objetivo mínimo 1080p/30 en Fast: 12 GB con gráficos integrados, CPU de cuatro núcleos y GPU compatible con Vulkan 1.3; el rendimiento no está garantizado por debajo. Los 12 GB instalados declarados no verifican 12 GB utilizables ni compatibilidad gráfica.

**[SIN VERIFICAR]** OpenGL/Vulkan reportados por el driver local, compatibilidad Radeon R3 con Sodium/Embeddium, soporte OpenGL 4.5 de Sodium y cualquier FPS/RAM comparativo. No hay benchmark Fabric/Forge/NeoForge en el equipo. La entrada identifica Prominence II: Hasturian Era como referencia RPG Fabric 1.20.1, no como recomendación de instalarlo completo.

## Decisiones propuestas (todas pendientes de aprobación)

| ID | Propuesta | Justificación y condición | Estado |
|---|---|---|---|
| TDP-01 | Investigar primero Minecraft 1.20.1 + Fabric. | Evidencia documental de candidatos y referencia RPG; depende del manifiesto y pruebas. | Pendiente de aprobación |
| TDP-02 | Mantener Forge 1.20.1 como alternativa solo si lo exige el manifiesto. | Embeddium en lugar de Sodium; loader y renderer únicos. | Pendiente de manifiesto/pruebas |
| TDP-03 | No afirmar rendimiento sin benchmark reproducible. | No hay medidas locales; fichas/promoción no son resultados. | Regla de evidencia |
| TDP-04 | Mantener ModernFix `mixin.perf.dynamic_resources=false`. | El código consultado fija false como default y permite override; no valida el pack. | Pendiente de auditoría y autorización |
| TDP-05 | No precargar `options.txt` completo ni JSON de Sodium. | No se verificó esquema/serialización exactos de Minecraft 1.20.1/Sodium 0.5.13. | Pendiente de prueba aislada |
| TDP-06 | Mantener candidatos opcionales fuera de la base inicial. | Sin manifiesto, necesidad, compatibilidad ni autorización suficientes. | Pendiente |
| TDP-07 | No usar overrides Lithium; mantener defaults. | Documentación de Lithium 0.11.4 indica que ausencia de overrides conserva defaults. | Propuesta documental, prueba pendiente |
| TDP-08 | No redistribuir JARs sin revisión de términos. | En especial Entity Culling, con licencia personalizada; nunca subir binarios de terceros. | Regla de autorización |
| TDP-09 | No añadir inicialmente C2ME, DashLoader, Fastload/Ksyxis ni prioridades de hilos. | Beneficios/compatibilidad local no demostrados; añadir solo con necesidad, prueba y aprobación. | Pendiente |

## Límites y comprobaciones previas

- Radeon R3, driver y OpenGL/Vulkan local: **[SIN VERIFICAR]**; no asegurar que Sodium arranque ni que Embeddium solucione fallos.
- Manifiesto RPG y JARs: no entregados según inventario; compatibilidad completa **[SIN VERIFICAR]**.
- No se ejecutó juego ni benchmark; no hay cifras de FPS, RAM, carga o estabilidad.
- Resolver la discrepancia de listas (por ejemplo, Entity Culling `1.7.0`/`1.12.1` e ImmediatelyFast `1.2.4`/`1.2.21`) contra el manifiesto, no por intuición.
- Revisar licencias por archivo y canal de distribución. No redistribuir JARs ni subirlos al repositorio.
- Confirmar Java, launcher, Windows/build, driver, APIs gráficas y requisitos RPG antes de escoger.

## Registro de aprobación

| ID | Decisión final | Aprobador | Fecha | Evidencia/condiciones |
|---|---|---|---|---|
| | | | | |
