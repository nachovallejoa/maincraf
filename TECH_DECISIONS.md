# Decisiones técnicas — propuestas pendientes de aprobación

> No hay decisión técnica final aprobada. La disponibilidad de una build no demuestra compatibilidad con el pack ni rendimiento en el hardware real. Conclusiones sujetas al manifiesto, runtime, driver y pruebas locales.

## Comparativa de versiones y loaders

| Minecraft / loader | Situación documental recibida | Evaluación y límites |
|---|---|---|
| 1.19.2 + Fabric | Candidata histórica; Sodium 1.19.x citado como anterior. | Menos justificación que 1.20.1 para el pack citado; comparación de rendimiento no verificada. |
| 1.19.2 + Forge | Embeddium/FerriteCore/ModernFix citados. | Disponibilidad citada no equivale a compatibilidad; no medido localmente. |
| 1.19.2 + NeoForge | Se mencionó recomendación para Forge de esa generación. | Fuentes y soporte exacto pendientes. |
| 1.20.1 + Fabric | Java 17 asociado documentalmente; candidatos de optimización y Prominence II citados. | Candidata principal provisional; pack completo, manifiesto, GPU/driver y rendimiento local pendientes. No instalar pack completo por referencia promocional. |
| 1.20.1 + Forge | Java 17; Embeddium como alternativa a Sodium. | Alternativa condicional solo si el manifiesto lo exige. Pack, driver y rendimiento sin verificar. |
| 1.20.1 + NeoForge | No priorizada en la propuesta recibida. | Sin aprobación ni evidencia del pack. |
| 1.21.1 + loaders citados | Java 21 indicado en la propuesta; packs RPG citados como ejemplos. | No priorizada: pack equivalente y compatibilidad local no verificados. |
| 26.2 + loaders citados | Vulkan descrito como experimental; soporte Radeon R3 desconocido. | No priorizada. Runtime, builds, mods y pack RPG exactos pendientes. |

Minecraft 1.20.1 se asocia documentalmente con Java 17, pero el Java local no fue verificado. La transición de Minecraft a OpenGL Core 3.2 no certifica el controlador Radeon R3 de Windows. Requisitos y límites citados previamente (1080p/30 en Fast, 12 GB, CPU de cuatro núcleos, GPU Vulkan 1.3) no garantizan rendimiento; las especificaciones recibidas son declaraciones, no mediciones.

**[SIN VERIFICAR]** OpenGL/Vulkan local, compatibilidad Radeon R3 con Sodium/Embeddium, soporte OpenGL 4.5 efectivo y FPS/RAM comparativos. No hay benchmark Fabric/Forge/NeoForge en el equipo. Prominence II: Hasturian Era se usa aquí como referencia de pack RPG Fabric 1.20.1, no como recomendación de instalarlo completo.

## Segunda etapa: propuesta de versión, loader y mods

**Estado: pendiente de aprobación.** Propuesta documental; no se instalaron mods, modificaron archivos ni ejecutaron pruebas. Rendimiento: **NO DATA**. La lista no reemplaza el manifiesto de una instancia ni confirma compatibilidad conjunta.

### Versión y loader

Propuesta principal provisional: **Minecraft 1.20.1 + Fabric**, para conservar la posibilidad de usar Prominence II: Hasturian Era, cuya ficha declara Minecraft 1.20.1 y Fabric. Esto no valida los mods propuestos con una instalación concreta ni demuestra que esta combinación dé más FPS. El pack declara licencia ARR: no redistribuir pack ni archivos sin autorización expresa. [Ficha del pack](https://modrinth.com/modpack/prominence-2-fabric).

**Minecraft 1.21.1 + Fabric: [SIN VERIFICAR]**. La información recibida menciona alternativas RPG, pero no se verificó fuente que identifique cuáles o que conserven la campaña/contenido de Prominence II. No se recomienda como rendimiento superior. No hay benchmark local.

Forge 1.20.1 se consideraría solo si el manifiesto del pack lo exige. No se propone como mejora de rendimiento; candidatos sin validar.

Sodium declara soporte oficial para tarjetas de escritorio con drivers compatibles con OpenGL 4.5 o superior y enumera Radeon HD 7000 o posteriores como referencia. La Radeon R3 indicada no queda dentro de esa referencia. AMD clasifica Radeon R3 de Athlon como soporte heredado, sin nuevos drivers previstos. Esto no demuestra el OpenGL efectivo ni que Sodium falle. GPU, driver y OpenGL local pendientes. [Sodium](https://modrinth.com/mod/sodium) · [AMD](https://www.amd.com/en/resources/support-articles/faqs/GPU-630.html).

### Mods candidatos

Las builds son candidatos documentales, no archivos aprobados. **[SIN VERIFICAR]** señala dato no confirmado en las fuentes consultadas. La compatibilidad conjunta con el pack no se deduce de la existencia de una build.

| Mod | Candidato 1.20.1 Fabric | Condiciones/estado documental | Licencia / redistribución |
|---|---|---|---|
| Sodium | `0.5.13` **[SIN VERIFICAR: build exacta]** | Candidato cliente/renderizado. Guía oficial: Indium puede ser necesario con Sodium 0.5.x en Minecraft 1.20 o anterior para compatibilidad con otros mods; deja de ser necesario desde 0.6.x. No confirmados mínimos Indium 1.0.36+ ni Iris 1.7.6+. Revisar archivo, dependencias, manifiesto, GPU/driver. [Proyecto](https://modrinth.com/mod/sodium) · [Guía](https://github.com/CaffeineMC/sodium/wiki/Installation) · [build indicada, pendiente](https://modrinth.com/mod/sodium/version/OihdIimA) | Polyform Shield 1.0.0 declarada en página del proyecto; revisar términos y canal antes de redistribuir. |
| Lithium | `0.11.4` **[SIN VERIFICAR: detalles de build]** | Dependencias, archivo y licencia de esta build no validados. Revisar metadatos/manifiesto. [Proyecto](https://modrinth.com/mod/lithium) · [build indicada](https://modrinth.com/mod/lithium/version/mc1.20.1-0.11.4-fabric) | LGPL-3.0-only mencionada en material recibido; licencia de build **[SIN VERIFICAR]**. No redistribuir hasta verificar. |
| FerriteCore | `6.0.1` | Ficha consultada: Fabric/Quilt, MC 1.20–1.20.2. Revisar duplicados/pack. Incompatibilidad con Hydrogen no verificada. [Build](https://modrinth.com/mod/ferrite-core/version/6.0.1) | MIT según ficha; redistribución sujeta a licencia. |
| ModernFix | `5.25.2+mc1.20.1` | Ficha consultada: Fabric 1.20.1. Archivo y pack por verificar. No se aprueba ajuste Dynamic Resources. [Build](https://modrinth.com/mod/modernfix/version/5.25.2%2Bmc1.20.1) | LGPL-3.0-only según ficha; redistribución sujeta a licencia. |
| Entity Culling | `1.12.1-1.20.1` | Ficha confirma Fabric/1.20.1/cliente. Pack/Sodium no probados. Advertencias de CPU/artefactos visuales **[SIN VERIFICAR]**. [Build](https://modrinth.com/mod/entityculling/version/xM6y5W1N) | tr7zw Protective License, personalizada. Revisar texto y canal antes de redistribuir. |
| ImmediatelyFast | `1.2.1+1.20.1` | Ficha: Fabric/Forge/Quilt, MC 1.20–1.20.1. Declara incompatibilidad con MemoryLeakFix `<=1.1.1`; comprobar pack. [Build](https://modrinth.com/mod/immediatelyfast/version/txcO4lNF) | LGPL-3.0-or-later según ficha; redistribución sujeta a licencia. |
| BadOptimizations | `2.1.4` | ID `GydKiUd0` corresponde a 2.1.4 (1.20.1), no 2.4.1. Otra build 2.4.1 para 1.20.1 no verificada. [Build](https://modrinth.com/mod/badoptimizations/version/GydKiUd0) | MIT según ficha; redistribución sujeta a licencia. |
| Sodium Extra | `0.5.9` | Ficha: requiere Sodium y Fabric API; Reese’s Sodium Options e Iris opcionales. Revisar archivos exactos/manifiesto. [Build](https://modrinth.com/mod/sodium-extra/version/mc1.20.1-0.5.9) | LGPL-3.0-only según ficha; redistribución sujeta a licencia. |
| Dynamic FPS | `3.9.5` | Ficha: cliente Fabric 1.20–1.20.1; requiere Fabric API, Cloth Config opcional. Reduce recursos en segundo plano/inactividad/batería; no presentarlo como acelerador de FPS en primer plano. [Build](https://modrinth.com/mod/dynamic-fps/version/D9mrJwm0) | MIT según ficha; redistribución sujeta a licencia. |
| Fabric API | `0.92.6+1.20.1` **[SIN VERIFICAR]** | Incluir solo si manifiesto o mod aprobado lo requiere. Build/licencia exacta no demostradas. | Autor, licencia y condiciones **[SIN VERIFICAR]**; no redistribuir hasta verificar. |

### Opcionales y descartes del perfil inicial

Añadir opcionales solo después de validar la base y probarlos individualmente. Particle Core no se combina inicialmente con Sodium Extra por precaución; solapamiento, dependencias y build indicada `0.2.5+1.20.1` **[SIN VERIFICAR]**. More Culling, C2ME, Noisium/Noisiumed y LazyDFU quedan fuera de la primera pasada: incompatibilidades, versiones y razones técnicas citadas previamente **[SIN VERIFICAR]**, no hechos demostrados. No retirarlos de una instancia sin autorización. ImmediatelyFast `1.2.1+1.20.1` es la candidata del enlace verificado; no mezclar con `1.2.21+1.20.4`. Que el pack actual enumere Entity Culling no demuestra compatibilidad de cualquier versión con una instalación específica.

### Configuración

No se han verificado claves/valores concretos para recomendar. No crear ni modificar configuración como preset. Retirar `mixin.perf.dynamic_resources=false` como ajuste recomendado hasta validar documentación/build exacta; `NOT_PRELOADABLE_UNVERIFIED` no es valor verificado y no debe escribirse en `sodium-options.json`; no hace falta generar `lithium.properties` vacío; no reemplazar `options.txt` con fragmentos; sin opciones de Sodium Extra propuestas. Tiempos de arranque: **NO DATA**.

### Aprobación y condiciones

No autoriza cambios. Antes de instalar, retirar, reemplazar o editar archivos: recibir/revisar manifiesto y JARs; verificar driver, OpenGL, Java, launcher, sistema y arquitectura; confirmar builds, dependencias y licencias exactas; acordar instancia aislada y respaldos; ejecutar pruebas controladas de arranque, carga, compatibilidad y rendimiento. Hasta entonces la decisión final sigue pendiente y resultados **NO DATA**.

## Decisiones propuestas anteriores (no aprobadas)

| ID | Propuesta | Justificación y condición | Estado |
|---|---|---|---|
| TDP-01 | Investigar primero Minecraft 1.20.1 + Fabric. | Candidatos documentales y referencia RPG; depende de manifiesto/pruebas. | Pendiente |
| TDP-02 | Mantener Forge 1.20.1 solo si el manifiesto lo exige. | Embeddium en lugar de Sodium; loader y renderer únicos. | Pendiente |
| TDP-03 | No afirmar rendimiento sin benchmark reproducible. | No hay medidas locales; fichas/promoción no son resultados. | Regla de evidencia |
| TDP-04 | No aplicar clave Dynamic Resources de ModernFix sin verificación. | Clave/build y pack no validados. | Pendiente de auditoría |
| TDP-05 | No precargar options.txt/JSON de Sodium. | Esquema/serialización exactos no verificados. | Pendiente de prueba aislada |
| TDP-06 | Mantener candidatos opcionales fuera de base inicial. | Manifiesto, necesidad y compatibilidad pendientes. | Pendiente |
| TDP-07 | No introducir overrides Lithium; conservar defaults. | Sin overrides propuestos ni necesidad demostrada. | Pendiente |
| TDP-08 | No redistribuir JARs sin revisión de términos. | Especialmente licencia personalizada de Entity Culling; nunca subir binarios de terceros. | Regla de autorización |
| TDP-09 | No añadir inicialmente C2ME, DashLoader, Fastload/Ksyxis ni prioridades de hilos. | Beneficios/compatibilidad local no demostrados; requiere necesidad, prueba y aprobación. | Pendiente |

## Límites y comprobaciones previas

- Radeon R3, driver y OpenGL/Vulkan locales **[SIN VERIFICAR]**; no asegurar que Sodium arranque o Embeddium lo solucione.
- Manifiesto RPG/JARs no entregados; compatibilidad completa **[SIN VERIFICAR]**.
- No se ejecutó juego ni benchmark; sin cifras de FPS, RAM, carga o estabilidad.
- Resolver discrepancias de inventario contra manifiesto, no por intuición.
- Revisar licencias por archivo y canal; no redistribuir JARs ni subir binarios de terceros.
- Confirmar Java, launcher, Windows/build, driver, APIs gráficas y requisitos RPG antes de elegir.

## Registro de aprobación

| ID | Decisión final | Aprobador | Fecha | Evidencia/condiciones |
|---|---|---|---|---|
|  |  |  |  |  |
