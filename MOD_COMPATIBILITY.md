# Matriz de compatibilidad de mods

## Estado y alcance

- Registro documental, no certificación de compatibilidad.
- Propuesta principal provisional: Fabric 1.20.1; Forge 1.20.1 solo como alternativa condicional al manifiesto.
- Manifiesto y JARs de la instalación no recibidos; el juego no se ejecutó en el equipo.
- No marcar compatible hasta validar versiones exactas, dependencias, arranque, mundo, logs y sistemas relevantes del pack. Compatibilidad no equivale a rendimiento aprobado.
- No subir JARs de terceros.

## Entorno por completar

| Campo | Valor |
|---|---|
| Identificador de instancia / fecha / responsable |  |
| Sistema operativo y build |  |
| CPU / núcleos / hilos |  |
| RAM instalada/utilizable |  |
| GPU / memoria compartida |  |
| Driver y versión |  |
| OpenGL/Vulkan reportado |  |
| Resolución/Hz |  |
| Minecraft |  |
| Java: distribución/versión/arquitectura |  |
| Loader y versión |  |
| Launcher y versión |  |
| Manifiesto y hash |  |
| Heap y argumentos JVM |  |
| `latest.log` y hash |  |

## Estados

| Estado | Significado |
|---|---|
| Pendiente | No probado o faltan datos esenciales. |
| Compatible en prueba | Solo casos registrados en esa instancia concreta superados. |
| Compatible con limitaciones | Funciona con incidencia/limitación documentada. |
| Incompatible | Falla reproducible en combinación exacta con evidencia. |
| No evaluado | No corresponde probar aún o no está seleccionado. |

## Inventario por completar

| Componente | Versión declarada | Archivo instalado | SHA-256 local | Fuente | Dependencias verificadas | Estado |
|---|---|---|---|---|---|---|
| Minecraft | 1.20.1 candidata |  |  |  |  | Pendiente |
| Java | 17 asociado documentalmente a MC 1.20.1 |  |  |  |  | Pendiente |
| Loader | Fabric candidato / Forge condicional |  |  |  |  | Pendiente |
| Modpack/manifiesto | No disponible en inventario recibido |  |  |  |  | Pendiente |
| Driver gráfico | No disponible |  |  |  |  | Pendiente |

## Candidatos Fabric 1.20.1

| Mod | Build candidata documental | Condición conocida | Estado |
|---|---|---|---|
| Sodium | `0.5.13` **[SIN VERIFICAR: build exacta]** | GPU R3/driver y pack sin verificar. La guía oficial indica que Indium puede ser necesario para compatibilidad con otros mods en Sodium 0.5.x con Minecraft 1.20 o anterior. No están verificados aquí los mínimos atribuidos a esa build. | Pendiente |
| Lithium | `0.11.4` **[SIN VERIFICAR: detalles de build]** | Dependencias y compatibilidad del pack pendientes. | Pendiente |
| ModernFix | `5.25.2+mc1.20.1` | No aplicar `mixin.perf.dynamic_resources=false`; clave no verificada para build exacta. Pack no probado. | Pendiente |
| FerriteCore | `6.0.1` | Pack pendiente. Supuesto conflicto con Hydrogen mencionado previamente, no verificado en esta revisión. | Pendiente |
| Entity Culling | `1.12.1-1.20.1` | Cliente. Coste/beneficio CPU y compatibilidad visual no probados; alertas específicas **[SIN VERIFICAR]**. | Pendiente |
| ImmediatelyFast | `1.2.1+1.20.1` | La ficha declara incompatibilidad con MemoryLeakFix `<=1.1.1`; comprobar manifiesto/JAR exacto. | Pendiente |
| BadOptimizations | `2.1.4` | El ID suministrado `GydKiUd0` corresponde a 2.1.4 (1.20.1), no 2.4.1. | Pendiente |
| Sodium Extra | `0.5.9` | Ficha consultada requiere Sodium y Fabric API; compatibilidad conjunta no comprobada. | Pendiente |
| Dynamic FPS | `3.9.5` | Requiere Fabric API según ficha; Cloth Config opcional. No inferir aceleración en primer plano. | Pendiente |
| Fabric API | `0.92.6+1.20.1` **[SIN VERIFICAR]** | Añadir solo si dependencia confirmada; build/licencia no verificadas en esta revisión. | Pendiente |
| Indium | No fijada | La guía de Sodium menciona posible necesidad con Sodium 0.5.x para compatibilidad; no es requisito universal verificado para esta combinación. | No evaluado |
| Iris | No fijada | No se valida el mínimo 1.7.6+ que se había atribuido a Sodium 0.5.13. Añadir solo si se requiere. | No evaluado |
| Reese’s Sodium Options | No fijada | Opcional en ficha de Sodium Extra consultada; necesidad/build de instancia pendientes. | No evaluado |
| Cloth Config API | No fijada | Opcional en ficha de Dynamic FPS; necesidad/build exactas pendientes. | No evaluado |

## Candidatos Forge 1.20.1

Forge solo si el manifiesto lo exige. No combinar renderizadores equivalentes.

| Mod | Versión de entrada previa | Estado documental en esta revisión |
|---|---|---|
| Embeddium | `0.3.31+mc1.20.1` | Candidato Forge; driver Radeon R3 y rendimiento local sin probar. Licencia exacta del archivo no verificada aquí. |
| Radium | `0.12.4` | Build y compatibilidad citadas deben verificarse contra archivos exactos. No afirmar incompatibilidad con Canary sin fuente/build concreta. |
| ModernFix | `5.28.0+mc1.20.1` | Candidato distinto del Fabric; build/licencia exactas no verificadas aquí. No asumir Dynamic Resources. |
| FerriteCore | `6.0.1` | MIT indicado para ficha consultada; pack no probado. |
| Entity Culling | `1.12.1-1.20.1` | Licencia personalizada; no redistribuir fuera de términos aplicables. Compatibilidad no probada. |
| ImmediatelyFast | `1.5.5` | Archivo y versión exactos pendientes de verificar. |
| Dynamic FPS | `3.7.7` | Archivo/dependencias exactas pendientes de verificar. |
| Particle Core | `0.3.3+1.20.1+forge` | Opcional; no incluir en núcleo. Build/licencia exactas pendientes. |

## Combinaciones y hechos de compatibilidad documentados

- Sodium 0.5.x en Minecraft 1.20 o anterior: la guía oficial dice que Indium puede ser necesario para compatibilidad con otros mods; no confirma un mínimo exacto para Sodium `0.5.13` en este pack. Desde Sodium 0.6.x Indium deja de ser necesario según la guía.
- ImmediatelyFast `1.2.1+1.20.1`: la ficha consultada declara incompatibilidad con MemoryLeakFix `<=1.1.1`; confirmar si esa build está en la instalación.
- Sodium Extra `0.5.9`: su ficha consultada requiere Sodium y Fabric API; Reese’s Sodium Options e Iris se enumeran como opcionales.
- Dynamic FPS `3.9.5`: su ficha consultada requiere Fabric API y enumera Cloth Config API como opcional.
- No se ha probado compatibilidad conjunta entre estos candidatos, pack, driver ni JARs locales.
- No afirmar conflicto FerriteCore/Hydrogen, solapamiento Particle Core/Sodium Extra, ni incompatibilidades de More Culling, C2ME, Noisium/Noisiumed o LazyDFU: las razones citadas previamente siguen **[SIN VERIFICAR]** en esta revisión.
- Prominence II lista Entity Culling en el contenido actual según el material recibido, pero no prueba que cualquier versión candidata sea compatible con una instancia concreta. Pack ARR: no redistribuir sin autorización.
- No se ha demostrado incompatibilidad local de Sodium con Radeon R3 ni el OpenGL efectivo. Sodium documenta soporte oficial con drivers compatibles con OpenGL 4.5+ y referencia Radeon HD 7000 o posteriores; la GPU indicada no cae dentro de la referencia, pero esto no demuestra fallo de arranque. Driver/OpenGL pendientes.

## Casos de prueba (sin resultados aún)

Guardar logs, crash reports, versiones y hashes localmente; no publicar binarios.

| ID | Caso | Resultado | Evidencia/log | Incidencias |
|---|---|---|---|---|
| C-01 | Arranque con loader, sin optimizadores | Pendiente |  |  |
| C-02 | Arranque con dependencias mínimas aprobadas | Pendiente |  |  |
| C-03 | Llegada al menú sin errores bloqueantes | Pendiente |  |  |
| C-04 | Crear/cargar mundo de prueba | Pendiente |  |  |
| C-05 | Recorrido de chunks existentes | Pendiente |  |  |
| C-06 | Generación de chunks nuevos | Pendiente |  |  |
| C-07 | Modelos, recursos, entidades y contenido RPG | Pendiente |  |  |
| C-08 | Cambio de dimensión, si aplica | Pendiente |  |  |
| C-09 | Reinicio y segunda carga | Pendiente |  |  |
| C-10 | Cierre normal | Pendiente |  |  |

## Incidencias

| ID | Fecha | Archivos exactos | Síntoma reproducible | Pasos | Log | Mitigación probada | Estado |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## Criterio de compatibilidad

Marcar “Compatible en prueba” solo después de registrar Minecraft, Java, loader y archivos exactos; dependencias verificadas; arranque al menú y carga de mundo sin fallo bloqueante; sistemas relevantes del pack; incidencias y logs. Evaluar rendimiento por separado en `PERFORMANCE.md`. Todos los resultados actuales son **NO DATA**.
