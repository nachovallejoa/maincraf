# Matriz de compatibilidad — Minecraft 1.20.1

## Estado

**Compatibilidad del pack completo: [SIN VERIFICAR].** No se entregó manifiesto RPG, lista de JARs ni instancia ejecutable. No se ejecutó Minecraft. La publicación de un archivo demuestra disponibilidad declarada, no compatibilidad con este hardware o con el pack.

| Campo | Estado |
|---|---|
| Minecraft propuesto | 1.20.1, no aprobado |
| Loader candidato | Fabric; condicionado al manifiesto |
| Alternativa | Forge, solo si el pack lo exige |
| Java | Java 17 documentado/recomendado para 1.20.1; runtime local **[SIN VERIFICAR]** |
| Pack/manifiesto | No entregado |
| Launcher/instancia | **[SIN VERIFICAR]** |
| Driver Radeon/OpenGL | **[SIN VERIFICAR]** |
| JARs/hashes | No entregados |

## Estados

- **Candidato:** evidencia de versión/plataforma publicada, sin prueba local.
- **Pendiente:** evidencia insuficiente.
- **Compatible en prueba:** solo tras prueba reproducible y evidencia adjunta.
- **Fallo:** reproducido con logs y pasos.

## Matriz Fabric

| Candidato | Archivo/plataforma y fuente | Dependencias/cautelas | Arranque | Mundo nuevo/existente | Funciones RPG | Rendimiento |
|---|---|---|---|---|---|---|
| Sodium 0.5.13 | `mc1.20.1-0.5.13-fabric`, Fabric/Quilt [ficha](https://modrinth.com/mod/sodium/version/mc1.20.1-0.5.13-fabric) | Indium ≥1.0.36 si se usa; Iris ≥1.7.6 si se usa. Radeon/OpenGL local **[SIN VERIFICAR]** | Pendiente | Pendiente | Pendiente | No medido |
| Lithium 0.11.4 | `mc1.20.1-0.11.4-fabric`, Fabric/Quilt [ficha](https://modrinth.com/mod/lithium/version/mc1.20.1-0.11.4-fabric) | Dependencia exacta **[SIN VERIFICAR]**; archivo de overrides vacío mantiene defaults según [documentación](https://github.com/CaffeineMC/lithium-fabric/blob/mc1.20.1-0.11.4/lithium-mixin-config.md) | Pendiente | Pendiente | Pendiente | No medido |
| ModernFix 5.25.2 | `5.25.2+mc1.20.1`, Fabric [ficha](https://modrinth.com/mod/modernfix/version/5.25.2%2Bmc1.20.1) | Dynamic Resources `false` hasta auditar pack | Pendiente | Pendiente | Revisar recursos/modelos/bloques | No medido |
| Entity Culling 1.7.0 | `1.7.0-1.20.1` Fabric [ficha](https://modrinth.com/mod/entityculling/version/1JrKE0F6) | Fabric API obligatoria **[SIN VERIFICAR]**; probar entidades/modelos | Pendiente | Pendiente | Pendiente | No medido |
| ImmediatelyFast 1.2.4 | `1.2.4+1.20.1`, MC 1.20–1.20.1, Fabric/Forge/Quilt [ficha](https://modrinth.com/mod/immediatelyfast/version/1.2.4%2B1.20.1) | Buffering de texto en carteles apagado por defecto; esquema completo **[SIN VERIFICAR]** | Pendiente | Pendiente | Revisar GUI, carteles, texto y partículas | No medido |
| FerriteCore 6.0.1 | Candidato citado | Ficha/build/dependencias/compatibilidad **[SIN VERIFICAR]** en la revisión | Pendiente | Pendiente | Pendiente | No medido |
| BadOptimizations 2.4.1 | Candidato citado | Metadata completa **[SIN VERIFICAR]** | Pendiente | Pendiente | Pendiente | No medido |
| Dynamic FPS 3.9.5 | Candidato citado | Dependencias/licencia exactas **[SIN VERIFICAR]** | Pendiente | Pendiente | Probar foco/reanudación | No medir como FPS activo |
| Fabric API 0.92.2+1.20.1 | Candidato citado | Usar solo si una build lo requiere | Pendiente | Pendiente | Pendiente | No medido |
| More Culling / Particle Core / Noisium / Ksyxis | Candidatos citados | Build, efectos y dependencias exactos **[SIN VERIFICAR]** | Pendiente | Prueba con respaldo | Pendiente | No medido |
| Indium 1.0.36+ | Candidato | Sodium exige al menos esa versión si se usa | Pendiente | Pendiente | Añadir solo si lo requiere el manifiesto | No medido |

## Matriz Forge/NeoForge

| Candidato | Evidencia documentada | Pendiente |
|---|---|---|
| Embeddium `0.3.31+mc1.20.1` | Ficha confirma Forge y NeoForge 1.20.1, LGPL-3.0-only: [fuente](https://modrinth.com/mod/embeddium/version/0.3.31%2Bmc1.20.1) | Pack, GPU, dependencias y pruebas |
| Entity Culling Forge | Candidato recibido | Ficha exacta/dependencias **[SIN VERIFICAR]** |
| ImmediatelyFast Forge | La ficha comprobada corresponde a `1.2.4+1.20.1`; no extrapolar a otra build | Archivo Forge exacto y prueba |
| FerriteCore/ModernFix/Dynamic FPS/BadOptimizations Forge | Candidatos recibidos | Builds y compatibilidad Forge exactas **[SIN VERIFICAR]** |
| Radium o Canary | Alternativas citadas | Versión/licencia/dependencias/pack **[SIN VERIFICAR]**; no asumir que se combinan |

## Pruebas mínimas antes de declarar compatibilidad

1. Registrar juego, loader, Java, launcher, driver, mods/versiones/hashes locales y configuración.
2. Arrancar y guardar `latest.log`.
3. Probar mundo nuevo y copia de mundo existente.
4. Revisar modelos, texturas, bloques, fluidos, entidades, GUI y partículas.
5. Probar sistemas RPG imprescindibles indicados por el usuario, además de recursos/datapacks.
6. Probar cambios de chunks/spawn solo en respaldo.
7. Registrar crash report y pasos reproducibles ante fallos.
8. No declarar compatibilidad hasta tener evidencia; no subir JARs.

## Registro vacío

| Fecha | Loader/versiones | Escenario | Arranque | Funciones | Logs/evidencia | Estado |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Pendientes

Manifiesto exacto, loader aprobado, runtime/launcher/driver, configuraciones y recursos, requisitos RPG y resultados reproducibles.
