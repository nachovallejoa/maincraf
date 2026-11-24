# Manifiesto documental de dependencias — propuesta etapa dos

> Este documento registra candidatos y datos de fichas, no autoriza instalación ni redistribución. Manifiesto/JARs del pack no recibidos; versiones instaladas y dependencias de la instancia **[SIN VERIFICAR]**. No incluir binarios ni JARs de terceros en el repositorio. Prominence II declara licencia ARR: no redistribuir pack ni archivos sin autorización expresa.

## Candidatos Fabric 1.20.1

| Mod | Versión candidata | Autor | URL documental | Licencia documentada | Dependencias / condición | Redistribución |
|---|---|---|---|---|---|---|
| Sodium | `0.5.13` **[SIN VERIFICAR: build exacta]** | **[SIN VERIFICAR]** | [Proyecto](https://modrinth.com/mod/sodium) · [build indicada, pendiente de confirmar](https://modrinth.com/mod/sodium/version/OihdIimA) | Polyform Shield 1.0.0 según página de proyecto | Build/archivo y dependencias exactas no validados. Indium puede ser necesario con 0.5.x en MC 1.20 o anterior según guía para compatibilidad con otros mods; no se confirma mínimo para esta build. | Revisar términos y obligaciones por canal; no redistribuir hasta validarlo. |
| Lithium | `0.11.4` **[SIN VERIFICAR: detalles de build]** | **[SIN VERIFICAR]** | [Proyecto](https://modrinth.com/mod/lithium) · [build indicada](https://modrinth.com/mod/lithium/version/mc1.20.1-0.11.4-fabric) | **[SIN VERIFICAR]** para esta build en esta revisión. LGPL-3.0-only fue indicada en material recibido, no validada por archivo. | Verificar build, metadatos y dependencias contra manifiesto/JAR. | No redistribuir hasta confirmar licencia aplicable. |
| FerriteCore | `6.0.1` | **[SIN VERIFICAR]** en esta revisión | [Proyecto](https://modrinth.com/mod/ferrite-core) · [build](https://modrinth.com/mod/ferrite-core/version/6.0.1) | MIT según ficha consultada | Ficha: Fabric/Quilt, Minecraft 1.20–1.20.2. Conflicto mencionado con Hydrogen no verificado. | Sujeta a licencia y revisión del archivo/canal. |
| ModernFix | `5.25.2+mc1.20.1` | **[SIN VERIFICAR]** en esta revisión | [Proyecto](https://modrinth.com/mod/modernfix) · [build](https://modrinth.com/mod/modernfix/version/5.25.2%2Bmc1.20.1) | LGPL-3.0-only según ficha consultada | Ficha: Fabric 1.20.1. No aplicar configuración no verificada de Dynamic Resources. | Sujeta a licencia y revisión del archivo/canal. |
| Entity Culling | `1.12.1-1.20.1` | **[SIN VERIFICAR]** en esta revisión | [Proyecto](https://modrinth.com/mod/entityculling) · [build](https://modrinth.com/mod/entityculling/version/xM6y5W1N) | tr7zw Protective License, personalizada, según ficha | Ficha: Fabric 1.20.1/cliente. Compatibilidad pack/Sodium y advertencias específicas pendientes. | Revisar términos completos y canal; no asumir permiso general de redistribución. |
| ImmediatelyFast | `1.2.1+1.20.1` | **[SIN VERIFICAR]** en esta revisión | [Proyecto](https://modrinth.com/mod/immediatelyfast) · [build](https://modrinth.com/mod/immediatelyfast/version/txcO4lNF) | LGPL-3.0-or-later según ficha | Ficha: Fabric/Forge/Quilt, MC 1.20–1.20.1; incompatibilidad declarada con MemoryLeakFix `<=1.1.1`, comprobar instancia. | Sujeta a licencia y revisión del archivo/canal. |
| BadOptimizations | `2.1.4` | **[SIN VERIFICAR]** en esta revisión | [Proyecto](https://modrinth.com/mod/badoptimizations) · [build correspondiente al enlace aportado](https://modrinth.com/mod/badoptimizations/version/GydKiUd0) | MIT según ficha consultada | El enlace identifica 2.1.4 (1.20.1), no 2.4.1. Otra build 2.4.1 para 1.20.1 no verificada. | Sujeta a licencia y revisión del archivo/canal. |
| Sodium Extra | `0.5.9` | **[SIN VERIFICAR]** en esta revisión | [Proyecto](https://modrinth.com/mod/sodium-extra) · [build y requisitos](https://modrinth.com/mod/sodium-extra/version/mc1.20.1-0.5.9) | LGPL-3.0-only según ficha consultada | Requiere Sodium y Fabric API; Reese’s Sodium Options e Iris opcionales según ficha. Validar versiones contra archivo exacto. | Sujeta a licencia y revisión del archivo/canal. |
| Dynamic FPS | `3.9.5` | **[SIN VERIFICAR]** en esta revisión | [Proyecto](https://modrinth.com/mod/dynamic-fps) · [build](https://modrinth.com/mod/dynamic-fps/version/D9mrJwm0) | MIT según ficha consultada | Ficha: cliente Fabric, MC 1.20–1.20.1; requiere Fabric API, Cloth Config opcional. Reduce recursos en segundo plano/inactividad/batería; no se propone como acelerador en primer plano. | Sujeta a licencia y revisión del archivo/canal. |
| Fabric API | `0.92.6+1.20.1` **[SIN VERIFICAR]** | **[SIN VERIFICAR]** | URL de build para esta versión no verificada en esta revisión. | **[SIN VERIFICAR]** | Incluir solo si el manifiesto o mod aprobado lo requiere. Sodium Extra y Dynamic FPS requieren Fabric API según las fichas consultadas; confirmar build exacta. | No redistribuir hasta verificar fuente, licencia y condiciones. |

## Dependencias condicionales (no incluidas por defecto)

| Dependencia | Datos disponibles | Estado |
|---|---|---|
| Indium | Guía oficial de Sodium: puede ser necesario para compatibilidad con otros mods con Sodium 0.5.x en Minecraft 1.20 o anterior; deja de ser necesario desde Sodium 0.6.x. | Build mínima y necesidad para esta instancia **[SIN VERIFICAR]**. |
| Iris | No se confirma el mínimo `1.7.6+` que se atribuyó a Sodium `0.5.13`. | Añadir solo si se requiere; build y licencia de instancia pendientes. |
| Reese’s Sodium Options | Opcional en la ficha consultada de Sodium Extra `0.5.9`. | No incluir por defecto; build/autores/licencia aplicables **[SIN VERIFICAR]**. |
| Cloth Config API | Opcional en la ficha consultada de Dynamic FPS `3.9.5`. | Necesidad de interfaz y build concreta pendientes; no incluir por defecto. |
| Mod Menu | No es requisito funcional confirmado en esta propuesta; necesidad citada previamente para interfaz no verificada. | No incluir por defecto; versión/build/autor/licencia **[SIN VERIFICAR]**. |

## Condiciones de uso y revisión

- Las licencias se transcriben como datos documentales de las fichas consultadas y no sustituyen la licencia/metadata del archivo concreto ni revisión legal del canal.
- Entity Culling usa licencia personalizada: revisar el texto completo y los permisos aplicables antes de empaquetar/publicar.
- Autoría y condiciones legales completas por archivo no se verificaron para varios candidatos; se mantienen explícitamente pendientes, sin inventar campos.
- Prominence II: Hasturian Era declara ARR; no redistribuir pack ni archivos sin autorización expresa. [Ficha](https://modrinth.com/modpack/prominence-2-fabric).
- No se autoriza redistribución de JARs ni se subirán binarios de terceros a este repositorio.
- Antes de aprobar: recibir manifiesto y JARs, verificar versión/loader/dependencias/hash local y revisar licencia por archivo y canal.
