# Auditoría de mods

**Estado:** borrador de investigación; ninguna combinación aprobada ni instalada. No se suben JARs de terceros.
**Plataforma candidata:** Minecraft 1.20.1 + Fabric. **Alternativa:** Forge 1.20.1 solo si lo requiere el manifiesto.
**Hardware declarado:** Athlon 5150, Radeon R3, 12 GB RAM (~9,9 GB utilizables declarados), HDD, Windows, 1280×720; no verificado independientemente. GPU/controlador/OpenGL local: [SIN VERIFICAR].

## Alcance y criterios

- El paquete revisado no incluye manifiesto/inventario RPG, JARs ni logs. No hay mediciones de FPS, frametimes, RAM, CPU/GPU, inicio o generación.
- Disponibilidad de una build no demuestra compatibilidad integral ni rendimiento en el pack o en el equipo objetivo.
- **Imprescindible:** requisito demostrado por manifiesto aprobado. **Recomendado:** necesidad confirmada y evidencia adecuada; no basta una expectativa de rendimiento. **Opcional:** función no esencial. **Reemplazable:** alternativa sujeta a autorización y comparación. **Prescindible:** necesidad evaluada y descartada. **Incompatible:** fuente técnica aplicable o prueba reproducible para esa combinación.
- Compatibilidad pendiente no significa incompatibilidad. Ningún candidato está aprobado.
- Revisar términos, dependencias y avisos antes de distribuir cualquier binario; la licencia citada no autoriza automáticamente la redistribución. Nunca incluir JARs.

## Candidatos Fabric 1.20.1

| Mod | Versión candidata | Evidencia y licencia declarada | Estado/cautela |
|---|---|---|---|
| Sodium | 0.5.13 Fabric, Minecraft 1.20.1 | [Ficha](https://modrinth.com/mod/sodium/version/mc1.20.1-0.5.13-fabric); Polyform Shield 1.0.0. | Candidato de renderizado; soporte oficial requiere drivers OpenGL 4.5+, pero hardware antiguo puede funcionar sin garantía. Radeon R3/API local [SIN VERIFICAR]. Indium 1.0.36+ solo si se requiere; Iris 1.7.6+ si se usa, no parte de base. |
| Lithium | 0.11.4 Fabric 1.20.1 | [Archivo](https://www.curseforge.com/minecraft/mc-mods/lithium/files/7268114); LGPLv3. | Candidato; pack y efecto local sin verificar. |
| FerriteCore | 6.0.1 Fabric, Minecraft 1.20–1.20.2 | [Ficha](https://modrinth.com/ferrite-core/version/6.0.1); MIT. | Candidato. No combinar con Hydrogen para 1.20.1: el proyecto declara incompatibilidad en 1.18+. |
| ModernFix | 5.25.2+mc1.20.1 Fabric | [Ficha](https://modrinth.com/mod/modernfix/version/5.25.2%2Bmc1.20.1); LGPL-3.0-only. | Candidato; predeterminados al inicio. `mixin.perf.dynamic_resources` se deja sin override (falso por defecto según código consultado). |
| ImmediatelyFast | 1.5.5+1.20.4 Fabric; rango publicado 1.20–1.20.4 | [Ficha](https://modrinth.com/mod/immediatelyfast/version/1.5.5%2B1.20.4-fabric); LGPL-3.0-or-later. | Candidato; 1.20.1 está en el rango, pero compatibilidad con el pack sin verificar. |
| Entity Culling | 1.12.1-1.20.1 Fabric (registro recibido) | Archivo/dependencias/licencia exactos en esta revisión: [SIN VERIFICAR]. | Opcional; medir y comprobar entidades/NPCs del pack, posible carga CPU. |
| Particle Core | 0.2.5+1.20.1 Fabric (registro recibido) | Archivo/dependencias/licencia exactos: [SIN VERIFICAR]. | Opcional; valorar solapamiento con partículas nativas. |
| Noisium | 2.3.0+mc1.20-1.20.1 Fabric (registro recibido) | Archivo/licencia/estado exactos: [SIN VERIFICAR]. | Opcional, ensayo aislado de generación; no atribuir mejora a chunks existentes o arranque. |
| Dynamic FPS | 3.9.5 Fabric (registro recibido) | Dependencias/licencia exactas [SIN VERIFICAR]; registro recibido indica Fabric API requerida y Cloth Config opcional. | Opcional para inactividad/segundo plano; no presentarlo como FPS de primer plano. |
| LightSpeedRe | 2.0.7.fabric.1.20.1 (registro recibido) | Build, dependencia y licencia exactas [SIN VERIFICAR]. | Ensayo experimental individual frente a ModernFix; no apilar inicialmente. |

## Forge y exclusiones

Embeddium, FerriteCore y ModernFix para Forge 1.20.1 aparecen como candidatos en el material recibido; la pila exacta, dependencias, licencias y compatibilidad completa con RPG requieren nueva verificación. Forge solo si el manifiesto lo exige. No mezclar JARs Fabric/Forge.

Excluidos de la base inicial: C2ME (build Alpha/riesgos sin resolver), Starlight/Phosphor (cuello de botella no observado), shaders/texturas HD/cosméticos (no necesarios para objetivo inicial), OptiFine/OptiFabric, Hydrogen junto a FerriteCore, e Indium sin dependencia demostrada. Reconsiderar si el manifiesto lo requiere.

## Base propuesta y campos pendientes

Base de primer ensayo, no aprobada: Sodium + Lithium + FerriteCore + ModernFix + ImmediatelyFast, tras validar archivos, launcher, Java y GPU/API. Fabric API únicamente si una build elegida la requiere.

Para completar por mod: necesidad en pack; loader/MC/archivo exactos; URL y fecha; autor/licencia; dependencias e incompatibilidades; hash del JAR local (sin subirlo); prueba de arranque/mundo; mediciones; alternativas; mantenimiento/calidad; autorización y decisión final.

## Registro de cambios/autorización

| Fecha | Añadir/quitar/reemplazar | Motivo | Evidencia comparativa | Mantenimiento | Compatibilidad comprobada | Calidad afectada | Autorización | Decisión |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
