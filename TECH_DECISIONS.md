# Decisiones técnicas — propuestas pendientes de aprobación

> No hay decisión técnica final aprobada. La disponibilidad de una build no demuestra compatibilidad con el pack ni rendimiento en el hardware real. Conclusiones sujetas al manifiesto, runtime, driver y pruebas locales.

## Comparativa de versiones y loaders

| Minecraft / loader | Situación documental recibida | Evaluación y límites |
|---|---|---|
| 1.19.2 + Fabric | Candidata histórica; Sodium 1.19.x citado anteriormente. | Menos justificación que 1.20.1 para el pack citado; comparación de rendimiento no verificada. |
| 1.19.2 + Forge | Embeddium/FerriteCore/ModernFix citados. | Disponibilidad citada no equivale a compatibilidad; sin mediciones locales. |
| 1.19.2 + NeoForge | Se mencionó recomendación para Forge de esa generación. | Fuentes y soporte exacto pendientes. |
| 1.20.1 + Fabric | Candidata documental asociada a Prominence II y a artefactos de optimización. | Candidata principal condicional; manifiesto completo, GPU/driver y rendimiento local pendientes. No instalar el pack completo solo por la referencia promocional. |
| 1.20.1 + Forge | Embeddium como alternativa a Sodium. | Solo considerar si el manifiesto exige Forge. Pack, driver y rendimiento sin verificar. |
| 1.20.1 + NeoForge | No priorizada. | Sin aprobación ni evidencia del pack. |
| 1.21.1 + loaders citados | Sodium 0.6.13 documentado para Fabric 1.21.1; se citaron packs RPG como ejemplos. | No priorizada: pack equivalente, loader final y compatibilidad local no verificados. Requisito Java 21 y Java instalado: [SIN VERIFICAR]. |
| 26.2 + loaders citados | Vulkan descrito como experimental; soporte Radeon R3 desconocido. | No priorizada. Runtime, builds, mods y pack RPG exactos pendientes. |

Minecraft 1.20.1 se asocia documentalmente con Java 17, pero Java local no se verificó. OpenGL Core 3.2 asociado a Minecraft no certifica el controlador de la Radeon R3. Especificaciones generales recibidas (1080p/30 en Fast, 12 GB, CPU de cuatro núcleos, GPU Vulkan 1.3) no garantizan rendimiento; son declaraciones, no mediciones.

**[SIN VERIFICAR]** OpenGL/Vulkan local, compatibilidad Radeon R3 con Sodium/Embeddium, soporte OpenGL 4.5 efectivo y FPS/RAM comparativos. No hay benchmark Fabric/Forge/NeoForge en el equipo.

## Segunda etapa: propuesta de versión, loader y mods

**Estado: pendiente de aprobación.** Propuesta documental; no se instalaron mods, no se modificaron archivos de instancia y no se ejecutaron pruebas. Rendimiento: **NO DATA**. Esta lista no sustituye el manifiesto del pack ni confirma compatibilidad conjunta.

### Versión y loader

Candidata principal provisional: **Minecraft 1.20.1 + Fabric**, para conservar la posibilidad de usar Prominence II: la ficha consultada declara 1.20.1 y Fabric. No se confirmó que ese sea el pack instalado o el objetivo definitivo. No se pudo concluir que Prominence II carezca de publicación para 1.21.1: **[SIN VERIFICAR]**. No hay pruebas locales que declaren una versión ganadora en FPS.

Alternativa 1.21.1 + Fabric: Sodium 0.6.13 es un candidato documentado, pero no se verificó un pack que conserve el contenido objetivo. Java 21 requerido para la alternativa y versión instalada: **[SIN VERIFICAR]**. Forge 1.20.1 solo se considera si el manifiesto lo exige.

Fuentes: [Prominence II](https://modrinth.com/modpack/prominence-2-fabric) · [Sodium 0.5.13](https://modrinth.com/mod/sodium/version/mc1.20.1-0.5.13-fabric) · [Sodium 0.6.13 para 1.21.1](https://modrinth.com/mod/sodium/version/mc1.21.1-0.6.13-fabric).

### Mods candidatos

Los artefactos siguientes son candidatos documentales, no una selección validada como conjunto. El manifiesto del pack y los JAR exactos no se recibieron.

| Mod / versión | Clasificación y condiciones | Licencia indicada en las fuentes consultadas |
|---|---|---|
| Sodium 0.5.13 | Candidato de renderizado; validar Radeon R3, controlador y OpenGL. Indium solo si el manifiesto exige Fabric Rendering API con Sodium 0.5.x. | Polyform Shield 1.0.0; revisar términos antes de redistribuir. |
| Lithium 0.11.4 | Candidato de optimización de lógica; compatibilidad del pack pendiente. | LGPL-3.0-only. |
| FerriteCore 6.0.1 | Candidato de memoria; solapamiento potencial con ModernFix no demuestra conflicto. | MIT. |
| ModernFix 5.25.2+mc1.20.1 | Candidato para ensayar inicio/carga; no aplicar configuración no verificada. | LGPL-3.0-only. |
| Sodium Extra 0.5.9 | Opcional; dependencias exactas del artefacto por cotejar. | LGPL-3.0-only. |
| ImmediatelyFast 1.2.21+1.20.1 | Opcional; versión y JAR exactos sin verificar. | Proyecto: LGPL-3.0-or-later; licencia del archivo exacto pendiente. |
| BadOptimizations 2.4.1 | Opcional; compatibilidad conjunta sin verificar. | MIT según ficha consultada. |
| Dynamic FPS 3.9.5 | Opcional para recursos fuera de foco; no se propone como mejora de FPS enfocado. | MIT; requisito Fabric API no acreditado: [SIN VERIFICAR]. |

No se incluyen configuraciones: la clave/valor ModernFix `mixin.perf.dynamic_resources=false` no se verificó; no se proponen valores de Sodium Extra. Entity Culling, Particle Core, More Culling, C2ME, ScalableLux y Noisium quedan fuera o pospuestos por evidencias, dependencias, compatibilidad o licencias pendientes; ver `MOD_AUDIT.md` y `MOD_COMPATIBILITY.md`.

### Condiciones antes de aprobar

Confirmar manifiesto y JAR exactos, loader, sistema, Java, launcher, driver y OpenGL; revisar dependencias/licencias por artefacto; autorizar una instancia aislada y respaldos; probar base reproducible y añadir un candidato a la vez. No instalar, cambiar ni redistribuir nada sin autorización expresa.

## Configuración

No se verificaron claves/valores exactos de Sodium Extra ni la clave y efecto de `mixin.perf.dynamic_resources=false` para ModernFix. No crear presets ni archivos de configuración a partir de esta propuesta. Tiempo de inicio: **NO DATA**.

## Aprobación y condiciones

No se autorizaron cambios. Antes de instalar, retirar, reemplazar o editar archivos: recibir y revisar manifiesto/JAR, verificar driver, OpenGL, Java, launcher, sistema y arquitectura; confirmar builds, dependencias y licencias exactas; acordar instancia aislada y respaldos; ejecutar pruebas controladas de inicio, carga, compatibilidad y rendimiento. Hasta entonces, decisión final y resultados: **pendientes / NO DATA**.

## Decisiones propuestas anteriores (no aprobadas)

| ID | Propuesta | Justificación y condición | Estado |
|---|---|---|---|
| TDP-01 | Investigar primero Minecraft 1.20.1 + Fabric. | Candidatos documentales y referencia RPG; depende de manifiesto y pruebas. | Pendiente |
| TDP-02 | Mantener Forge 1.20.1 solo si el manifiesto lo exige. | Embeddium en lugar de Sodium; loader y renderer únicos. | Pendiente |
| TDP-03 | No afirmar rendimiento sin benchmark reproducible. | No hay medidas locales; fichas/promoción no son resultados. | Regla de evidencia |
| TDP-04 | No aplicar clave Dynamic Resources de ModernFix sin verificar. | Clave/build y pack no validados. | Pendiente de auditoría |
| TDP-05 | No precargar options.txt/JSON de Sodium. | Esquema y serialización exactos no verificados. | Pendiente de prueba aislada |
| TDP-06 | Mantener candidatos opcionales fuera de base inicial. | Manifiesto, necesidad y compatibilidad pendientes. | Pendiente |
| TDP-07 | No introducir overrides Lithium. | No se demostraron necesidad ni overrides válidos. | Pendiente |
| TDP-08 | No redistribuir JAR sin revisión de términos. | Especialmente licencia personalizada; nunca subir binarios de terceros. | Regla de autorización |
| TDP-09 | No añadir inicialmente C2ME, DashLoader, Fastload/Ksyxis ni prioridades de hilos. | Beneficio y compatibilidad local no demostrados; requieren prueba y aprobación. | Pendiente |

## Límites y comprobaciones pendientes

- Radeon R3, driver y OpenGL/Vulkan locales: **[SIN VERIFICAR]**; no asegurar que Sodium arranque ni que Embeddium lo resuelva.
- Manifiesto RPG/JARs no entregados; compatibilidad completa: **[SIN VERIFICAR]**.
- No se ejecutó juego ni benchmark; sin FPS, RAM, carga o estabilidad.
- Resolver discrepancias del inventario contra manifiesto, no por intuición.
- Revisar licencias por archivo y canal; no subir ni redistribuir JARs de terceros.
- Confirmar Java, launcher, Windows/build, driver, APIs gráficas y requisitos RPG antes de elegir.

## Registro de aprobación

| ID | Decisión final | Aprobador | Fecha | Evidencia/condiciones |
|---|---|---|---|---|
| | | | | |
