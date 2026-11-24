# Auditoría de mods — candidatos Minecraft 1.20.1

## Estado y alcance

Candidatos documentales, no lista instalada ni aprobada. No se ejecutó Minecraft ni se midieron FPS, frametimes, RAM, CPU/GPU, carga o compatibilidad. No se proporcionó manifiesto RPG ni JARs; compatibilidad con el pack completo: **[SIN VERIFICAR]**. Hardware declarado (no verificado independientemente): Athlon 5150, Radeon R3 integrada, 12 GB RAM, HDD, Windows, 1280×720. Driver/OpenGL local: **[SIN VERIFICAR]**.

No modificar el pack sin autorización. No subir JARs. Revisar términos antes de redistribuir; licencia identificada no equivale a permiso universal de distribución.

## Criterios

- Diferenciar datos de ficha, pruebas locales y pendientes.
- No atribuir mejoras sin mediciones repetibles.
- Registrar archivo exacto, Minecraft, loader, dependencias y hash local si está disponible (sin subir el JAR).
- Probar estabilidad y funciones RPG: modelos, entidades, partículas, bloques, recursos, progresión y mecánicas.
- Usar copias de mundos para pruebas que puedan alterar chunks/guardados.
- Conservar `latest.log`, crash report y pasos de reproducción.

## Candidatos Fabric 1.20.1

| Candidato | Archivo/versión citada | Hecho de fuente comprobado en esta revisión | Pendientes y cautelas | Estado |
|---|---|---|---|---|
| Sodium | `mc1.20.1-0.5.13-fabric` | Fabric/Quilt 1.20.1; PolyForm Shield 1.0.0. [Ficha](https://modrinth.com/mod/sodium/version/mc1.20.1-0.5.13-fabric) | GPU/OpenGL Radeon R3 local y pack **[SIN VERIFICAR]**. Si Indium: 1.0.36+; si Iris: 1.7.6+. Revisar términos de redistribución. | Candidato a prueba |
| Lithium | `mc1.20.1-0.11.4-fabric` | Fabric/Quilt 1.20.1; LGPL-3.0-only. [Ficha](https://modrinth.com/mod/lithium/version/mc1.20.1-0.11.4-fabric) | Dependencia del JAR exacto **[SIN VERIFICAR]**. Archivo de overrides vacío conserva defaults según [documentación de rama](https://github.com/CaffeineMC/lithium-fabric/blob/mc1.20.1-0.11.4/lithium-mixin-config.md). | Candidato a prueba |
| ModernFix | `5.25.2+mc1.20.1` Fabric | MC 1.20.1/Fabric y LGPL-3.0-only. [Ficha](https://modrinth.com/mod/modernfix/version/5.25.2%2Bmc1.20.1) | `mixin.perf.dynamic_resources=false` por defecto, confirmado en [código](https://github.com/embeddedt/ModernFix/blob/2535174e/common/src/main/java/org/embeddedt/modernfix/core/config/ModernFixEarlyConfig.java); mantener apagado hasta auditar pack. Compatibilidad **[SIN VERIFICAR]**. | Candidato incremental |
| Entity Culling | `1.7.0-1.20.1` Fabric | Archivo y tr7zw Protective License. [Ficha](https://modrinth.com/mod/entityculling/version/1JrKE0F6) | La ficha consultada no confirma Fabric API como dependencia obligatoria; dependencia **[SIN VERIFICAR]**. Probar entidades/modelos RPG y revisar licencia. | Opcional |
| ImmediatelyFast | `1.2.4+1.20.1` | MC 1.20–1.20.1, Fabric/Forge/Quilt y LGPL-3.0-or-later. [Ficha](https://modrinth.com/mod/immediatelyfast/version/1.2.4%2B1.20.1) | Buffering de texto de carteles desactivado por defecto por incompatibilidades. Configuración completa/dependencias **[SIN VERIFICAR]**. | Opcional |
| Embeddium | `0.3.31+mc1.20.1` | Forge y NeoForge 1.20.1; LGPL-3.0-only. [Ficha](https://modrinth.com/mod/embeddium/version/0.3.31%2Bmc1.20.1) | Alternativa de loader, no para Fabric. Pack/GPU **[SIN VERIFICAR]**. | Solo si loader lo exige |
| FerriteCore | `6.0.1` Fabric, citado | Versión citada en material recibido. | Ficha/licencia/dependencias exactas y compatibilidad requieren revisión. | Candidato sin aprobación |
| BadOptimizations | `2.4.1-1.20.1` | Versión citada en material recibido. | Metadata, licencia, dependencias, pack e impacto **[SIN VERIFICAR]**. | Opcional posterior |
| Dynamic FPS | `3.9.5` | Versión citada en material recibido. | Archivo/dependencias/licencia exactos **[SIN VERIFICAR]**. Solo considerar para segundo plano; no presentarlo como FPS activo. | Condicional |
| Fabric API | `0.92.2+1.20.1` | Versión citada en material recibido. | Necesidad para el conjunto y ficha exacta **[SIN VERIFICAR]**; añadir solo si se requiere. | Dependencia condicional |
| More Culling | `1.20.1-0.24.6` | Candidato citado. | Build, dependencias/licencia/pack **[SIN VERIFICAR]**. Solapamiento parcial con Entity Culling. | Condicional |
| Particle Core | `0.2.5+1.20.1` | Candidato citado. | Dependencias y cambios visuales **[SIN VERIFICAR]**. | Condicional |
| Noisium | `2.3.0+mc1.20-1.20.1` | Candidato citado. | Build/licencia/estado y beneficio local **[SIN VERIFICAR]**. No extrapolar a chunks existentes. | Condicional |
| Ksyxis | `1.3.4` | Candidato citado. | Loader/build/efecto en spawn chunks **[SIN VERIFICAR]**. Solo en copia y con autorización. | Condicional, un jugador |
| Indium | `1.0.36+mc1.20.1` | Sodium indica 1.0.36+ si se utiliza. | Añadir solo si manifiesto/mod consumidor lo necesita; resto **[SIN VERIFICAR]**. | No por defecto |

## Exclusiones y solapamientos

- No combinar Sodium con Embeddium; pertenecen a alternativas de plataforma.
- Para Forge, no combinar reemplazos equivalentes de lógica sin verificar conflicto y necesidad.
- C2ME queda fuera de la base: build/pack/efectos no resueltos.
- Starlight, LazyDFU, Fastload, LightSpeedRe, Sodium Extra, Memory Leak Fix, OptiFine/OptiFabric no forman parte de la base aprobada; no hay aprobación ni beneficio local demostrado.
- No incluir shaders, texturas pesadas, animaciones ni cambios visuales como optimizaciones.

## Configuración precargable documentada

No precargar Sodium JSON ni `options.txt`: esquema/valores exactos para estas builds y propósito no verificados. Lithium puede conservarse intencionalmente vacío para defaults, según su documentación de rama. ModernFix Dynamic Resources se mantiene en `false` según código citado. Consultar archivos en `config-propuesta/instancia-1.20.1/`; son propuestas documentales, no validación en juego.

## Registro de pruebas pendiente

| Fecha | Instancia/pack y hash | Configuración | Escenario | Repeticiones | Logs/incidentes | Rendimiento observado | Resultado funcional | Decisión/aprobador |
|---|---|---|---|---:|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

## Datos pendientes

Manifiesto RPG/loader/versión; JARs y hashes locales; configs, recursos/datapacks/shaders; Java, launcher, Windows y controlador Radeon; pruebas de carga/regresión/rendimiento; y revisión de licencias según distribución prevista.
