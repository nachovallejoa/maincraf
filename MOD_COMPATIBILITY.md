# Matriz de compatibilidad de mods

## Estado y alcance

- Plantilla de registro; no es certificación.
- Candidata documental principal: Fabric 1.20.1. Forge 1.20.1: alternativa condicionada al manifiesto.
- Manifiesto y JARs no encontrados según inventario recibido; no se ejecutó Minecraft en este equipo.
- No marcar compatible hasta validar versiones exactas, dependencias, arranque, mundo y logs. Compatibilidad no equivale a rendimiento aprobado.
- No subir JARs de terceros.

## Entorno por completar

| Campo | Valor |
|---|---|
| Identificador de instancia / fecha / responsable | |
| Sistema operativo y build | |
| CPU / núcleos / hilos | |
| RAM instalada/utilizable | |
| GPU / memoria compartida | |
| Driver y versión | |
| OpenGL/Vulkan reportado | |
| Resolución/Hz | |
| Minecraft | |
| Java: distribución, versión y arquitectura | |
| Loader y versión | |
| Launcher y versión | |
| Manifiesto y hash | |
| Heap y argumentos JVM | |
| `latest.log` y hash | |

## Estados

| Estado | Significado |
|---|---|
| Pendiente | No probado o faltan datos esenciales. |
| Compatible en prueba | Superó los casos registrados en esa instancia concreta. |
| Compatible con limitaciones | Funciona con incidencias o limitaciones documentadas. |
| Incompatible | Falla reproducible en combinación exacta con evidencia. |
| No evaluado | No corresponde probar aún o no está seleccionado. |

## Inventario real por completar

| Componente | Versión declarada | Archivo instalado | SHA-256 local | Fuente | Dependencias verificadas | Estado |
|---|---|---|---|---|---|---|
| Minecraft | 1.20.1 candidata | | | | | Pendiente |
| Java | 17 asociada documentalmente a 1.20.1 | | | | | Pendiente |
| Loader | Fabric candidato / Forge condicional | | | | | Pendiente |
| Modpack/manifiesto | No disponible en inventario recibido | | | | | Pendiente |
| Driver gráfico | No disponible | | | | | Pendiente |

## Candidatos Fabric 1.20.1

| Mod | Candidato documental | Condición conocida | Estado |
|---|---|---|---|
| Sodium | 0.5.13 | Radeon R3/driver y pack no verificados; Indium 1.0.36+ solo si el pack necesita FRAPI. | Pendiente |
| Lithium | 0.11.4 | Dependencias y compatibilidad con pack pendientes. | Pendiente |
| ModernFix | 5.25.2+mc1.20.1 | Mantener `mixin.perf.dynamic_resources=false`; compatibilidad del pack sin probar. | Pendiente |
| FerriteCore | 6.0.1 | Pack pendiente; posible conflicto con Hydrogen mencionado, no verificado en esta revisión. | Pendiente |
| Entity Culling | 1.12.1-1.20.1 | Cliente; coste/beneficio CPU pendiente; licencia personalizada. | Pendiente |
| ImmediatelyFast | 1.2.21 (archivo `+1.20.4`, declara 1.20.1) | Dependencias del manifiesto y comportamiento local pendientes. | Pendiente |
| Dynamic FPS | 3.9.5 | Archivo/dependencias exactos sin verificar; no tratar como acelerador activo. | Pendiente |
| Fabric API | 0.92.6+1.20.1 | Añadir solo si dependencia concreta lo requiere. | Pendiente |

## Candidatos Forge 1.20.1

| Mod | Candidato documental | Condición conocida | Estado |
|---|---|---|---|
| Embeddium | 0.3.31+mc1.20.1 | No combinar con Sodium/Rubidium; driver local no probado. | Pendiente |
| Radium | 0.12.4 | Versión e incompatibilidad Canary deben verificarse contra archivos exactos. | Pendiente |
| ModernFix | 5.28.0+mc1.20.1 | Dynamic Resources false; archivo exacto pendiente. | Pendiente |
| FerriteCore | 6.0.1 | Compatibilidad del pack pendiente. | Pendiente |
| Entity Culling | 1.12.1-1.20.1 | Licencia personalizada; no redistribuir JAR fuera de términos. | Pendiente |
| ImmediatelyFast | 1.5.5 | Archivo/versión exactos pendientes. | Pendiente |
| Dynamic FPS | 3.7.7 | Archivo/dependencias exactos pendientes. | Pendiente |
| Particle Core | 0.3.3+1.20.1+forge | Opcional; probar aisladamente si se justifica. | Pendiente |

## Casos de prueba (sin resultados aún)

Guardar logs, crash reports, versiones e hashes de los archivos usados localmente.

| ID | Caso | Resultado | Evidencia/log | Incidencias |
|---|---|---|---|---|
| C-01 | Arranque de juego + loader sin optimizadores | Pendiente | | |
| C-02 | Arranque con dependencias mínimas aprobadas | Pendiente | | |
| C-03 | Llegada al menú sin errores bloqueantes | Pendiente | | |
| C-04 | Crear/cargar mundo de prueba | Pendiente | | |
| C-05 | Recorrido de chunks existentes | Pendiente | | |
| C-06 | Generación de chunks nuevos | Pendiente | | |
| C-07 | Modelos, recursos, entidades y contenido RPG | Pendiente | | |
| C-08 | Cambio de dimensión, si aplica | Pendiente | | |
| C-09 | Reinicio y segunda carga | Pendiente | | |
| C-10 | Cierre normal | Pendiente | | |

## Incidencias

| ID | Fecha | Archivos exactos | Síntoma reproducible | Pasos | Log | Mitigación probada | Estado |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Criterio de compatibilidad

Marcar “Compatible en prueba” solo al documentar Minecraft, Java, loader y archivos exactos; dependencias verificadas; arranque al menú y carga de mundo sin fallo bloqueante; sistemas relevantes del pack; incidencias/advertencias; logs conservados. Evaluar rendimiento por separado en `PERFORMANCE.md`.