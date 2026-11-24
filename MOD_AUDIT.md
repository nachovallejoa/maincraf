# Auditoría de mods

## Estado y alcance

- Estado inicial recibido: repositorio vacío, sin manifiesto ni mods confirmados en el proyecto.
- La consulta de esta misión encontró el árbol de raíz vacío antes de documentar; el único archivo previo creado es el contexto de esta misión.
- `INCOMPLETE: 0 archivos revisados; árbol del repositorio y README, because el repositorio está vacío y no tiene commits (el README devolvió 404).`
- Los siguientes son candidatos externos, no mods instalados ni auditados en un pack real.
- No se ejecutó Minecraft ni se midieron FPS, frametimes, memoria, CPU/GPU ni tiempos.

## Criterios

- Clasificación de candidatos: **Pendiente de clasificación** hasta recibir manifiesto y pruebas.
- Una ficha de descarga o que el proyecto anuncie optimizaciones no prueba rendimiento en este equipo.
- Registrar versión/archivo, Minecraft, loader, licencia, dependencias e incompatibilidades.
- No retirar/reemplazar mods de un pack real sin autorización y comparación de compatibilidad, rendimiento, mantenimiento y calidad.
- Revisar licencia de artefacto antes de redistribuir. No subir JARs de terceros.

## Candidatos Fabric 1.20.1

| Mod | Archivo propuesto | Licencia indicada | Datos verificados en la revisión recibida | Estado |
|---|---|---|---|---|
| Sodium | 0.5.13 Fabric 1.20.1 | Polyform Shield 1.0.0 | Archivo existente. Indium ≥1.0.36 e Iris ≥1.7.6 si se usan. Soporte oficial exige driver compatible con OpenGL 4.5; GPU concreta sin verificar. https://modrinth.com/mod/sodium/version/mc1.20.1-0.5.13-fabric | Candidato; carga y rendimiento pendientes |
| Lithium | mc1.20.1-0.11.4 Fabric | LGPLv3 | Archivo existente; proyecto declara que no requiere Fabric API. https://www.curseforge.com/minecraft/mc-mods/lithium/files/7268114 | Candidato |
| FerriteCore | 6.0.1 Fabric | MIT | Archivo Fabric/Quilt para 1.20–1.20.2. Conflicto Hydrogen [SIN VERIFICAR]. https://modrinth.com/mod/ferrite-core/version/6.0.1 | Candidato |
| ModernFix | 5.25.2+mc1.20.1 Fabric | LGPLv3 | Archivo catalogado para Fabric. https://www.curseforge.com/minecraft/mc-mods/modernfix/files/7306748 | Candidato |
| Entity Culling | 1.12.1 Fabric 1.20.1 | tr7zw Protective License | Archivo existente; “Required content: Any compatible version”, no acredita Fabric API requerida. Puede usar CPU libre y conviene cautela con CPU saturada. https://modrinth.com/mod/entityculling/version/xM6y5W1N | Opcional; probar on/off. No redistribuir JAR fuera de lo permitido |
| ImmediatelyFast | 1.2.4+1.20.1 propuesto | LGPL indicada por proyecto | Versión exacta propuesta no validada; proyecto documenta incompatibilidades pertinentes con OptiFine/OptiFabric y MemoryLeakFix ≤1.1.1. https://modrinth.com/mod/immediatelyfast | Pendiente de validar archivo exacto |
| BadOptimizations | 2.2.3 (1.20.1) | MIT | Archivo existente, sin dependencias obligatorias declaradas; optimizaciones cliente descritas. https://www.curseforge.com/minecraft/mc-mods/badoptimizations/files/6673591 | Opcional; probar |
| Particle Core | 0.3.3+1.20.1 Fabric | MIT | Archivo Fabric existente. No confundir con artefacto Forge `+forge`. https://www.curseforge.com/minecraft/mc-mods/particle-core/files/7581167 | Opcional; validar partículas RPG |
| Dynamic FPS | 3.9.5 Fabric | MIT | Fabric API requerida, Cloth Config opcional; foco en segundo plano/inactividad, no FPS activos. https://modrinth.com/mod/dynamic-fps/version/D9mrJwm0 | Opcional por inactividad |

**Estrategia de prueba propuesta, no aprobada:** base mínima Sodium + Lithium + FerriteCore; sumar ModernFix y luego otros grupos, midiendo. La Radeon R3/OpenGL de esta instalación sigue sin verificar.

## Alternativa Forge 1.20.1 (no mezclar con Fabric)

| Candidato recibido | Estado |
|---|---|
| Embeddium 0.3.31+mc1.20.1 | Versión, licencia, compatibilidad y conflictos detallados [SIN VERIFICAR] en esta revisión |
| Radium 0.12.4 | Archivo exacto pendiente; no combinar con Canary según la información recibida |
| FerriteCore 6.0.1 Forge; ModernFix 5.26.2+mc1.20.1 Forge | Candidatos; compatibilidad del pack pendiente |
| Entity Culling, ImmediatelyFast, BadOptimizations | Archivos/compatibilidad completa de esta pila pendientes |
| Particle Core 0.3.3+1.20.1+forge | Archivo citado para Forge/NeoForge; probar función |
| Dynamic FPS 3.9.2 Forge | [SIN VERIFICAR] |

## Exclusiones iniciales propuestas

C2ME, Starlight/Phosphor, Noisium (sin artefacto exacto identificado), Canary junto con Radium, OptiFine/OptiFabric, Indium sin dependencia demostrada, shaders, texturas HD y cosméticos. Esto no autoriza borrar contenido de un pack.

## Ficha para completar

### [Nombre]
- Estado / clasificación: candidato; pendiente de clasificación.
- Minecraft / archivo exacto / loader / URL:
- Licencia del artefacto y redistribución:
- Dependencias / incompatibilidades:
- Compatibilidad RPG:
- FPS / 1% low / frametimes / memoria / CPU / GPU:
- Pruebas y evidencia/log:
- Decisión autorizada por / fecha:

## Registro de mediciones

| Mod/grupo | Archivo exacto | Compatibilidad | FPS medio | 1% low | Frametime | Heap/RAM | CPU | GPU | Evidencia |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
