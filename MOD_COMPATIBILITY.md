# Matriz de compatibilidad de mods — segunda etapa

## Estado y alcance

- Este documento registra compatibilidad documentada, no certificación de una instancia concreta.
- Propuesta provisional: Fabric 1.20.1; Forge 1.20.1 únicamente si lo exige el manifiesto.
- No se recibió manifiesto ni JARs; Minecraft no se ejecutó en el equipo.
- No marcar compatible/incompatible sin builds exactas, dependencias, arranque, mundo, logs y sistemas relevantes.
- No subir JARs de terceros. No instalar ni modificar sin autorización.

## Entorno pendiente de completar

| Campo | Valor |
|---|---|
| Identificador de instancia / fecha / responsable | NO DATA |
| Sistema operativo y build | NO DATA |
| CPU / núcleos / hilos | NO DATA |
| RAM instalada/utilizable | NO DATA |
| GPU / memoria compartida | Radeon R3 indicada; modelo y datos locales SIN VERIFICAR |
| Driver y versión | NO DATA |
| OpenGL / Vulkan reportado | NO DATA |
| Resolución / Hz | NO DATA |
| Minecraft / Java (distribución, versión, arquitectura) | NO DATA |
| Loader / versión | NO DATA |
| Launcher / versión | NO DATA |
| Manifiesto / hash | NO DATA — manifiesto no recibido |
| Heap y argumentos JVM | NO DATA |
| `latest.log` y hash | NO DATA — no se ejecutó prueba |

## Significado de estados

| Estado | Significado |
|---|---|
| Pendiente | No probado o faltan datos esenciales. |
| Compatible en prueba | Solo los casos registrados en esa instancia concreta superaron los criterios. |
| Compatible con limitaciones | Funciona con incidencia o limitación documentada. |
| Incompatible | Falla reproducible con evidencia en la combinación exacta. |
| No evaluado | No corresponde probar aún o no seleccionado. |

## Inventario por completar

| Componente | Versión declarada | Archivo instalado | SHA-256 local | Fuente | Dependencias verificadas | Estado |
|---|---|---|---|---|---|---|
| Minecraft | 1.20.1 candidata | NO DATA | NO DATA | Propuesta recibida | NO DATA | Pendiente |
| Java | 17 asociada documentalmente a MC 1.20.1 | NO DATA | NO DATA | Propuesta recibida | NO DATA | Pendiente |
| Loader | Fabric candidato / Forge condicional | NO DATA | NO DATA | Propuesta recibida | NO DATA | Pendiente |
| Modpack/manifiesto | No disponible; manifiesto no recibido | NO DATA | NO DATA | NO DATA | NO DATA | Pendiente |
| Driver gráfico | No disponible | NO DATA | NO DATA | NO DATA | NO DATA | Pendiente |

## Candidatos Fabric 1.20.1

Los enlaces y versiones describen artefactos candidatos de la propuesta; no prueban instalación ni coexistencia. Las dependencias por verificar se mantienen como pendientes.

| Mod | Versión candidata | Compatibilidad / condición documentada | Estado conjunto |
|---|---|---|---|
| Sodium | `0.5.13` | Ficha candidata para Fabric 1.20.1. Radeon R3/driver, OpenGL y pack sin probar. La guía indica posible necesidad de Indium con mods que usen Fabric Rendering API en Sodium 0.5.x; no es necesidad universal. | Pendiente |
| Lithium | `0.11.4` | Artefacto consultado para 1.20.1; dependencias y compatibilidad del pack por cotejar. | Pendiente |
| FerriteCore | `6.0.1` | Ficha consultada indica Fabric/Quilt y MC 1.20–1.20.2. Pack no probado. | Pendiente |
| ModernFix | `5.25.2+mc1.20.1` | Ficha consultada para Fabric 1.20.1. No aplicar `mixin.perf.dynamic_resources=false`: clave y valor no verificados. | Pendiente |
| Sodium Extra | `0.5.9` | Ficha consultada para versión candidata; dependencia/compatibilidad conjunta no comprobadas aquí. | Pendiente |
| ImmediatelyFast | `1.2.21+1.20.1` | Proyecto consultado advierte incompatibilidad conocida con OptiFine/OptiFabric; artefacto exacto, dependencias y coexistencia pendientes. | Pendiente |
| BadOptimizations | `2.4.1` propuesta | Build exacta indicada en propuesta; cotejo de artefacto y compatibilidad pendientes. | Pendiente |
| Dynamic FPS | `3.9.5` | Ficha consultada para Fabric 1.20–1.20.1; dependencia requerida Fabric API no acreditada: SIN VERIFICAR. Función de segundo plano, no aumento de FPS enfocado. | Pendiente |
| Fabric API | `0.92.6+1.20.1` condicional | Añadir solo si manifiesto/mod elegido lo requiere; necesidad exacta pendiente. | No evaluado |
| Indium | `1.0.36` o posterior condicional | Solo si un mod requiere Fabric Rendering API con Sodium 0.5.x; requiere Fabric API; no compatible con Sodium 0.6.0+. Versión/licencia exactas pendientes. | No evaluado |

## Hechos e incompatibilidades documentados (alcance limitado)

- Indium es necesario solo en el caso condicional de mods que requieran Fabric Rendering API con Sodium anterior a 0.6; no es compatible con Sodium 0.6.0 o posterior. Cotejar artefactos exactos antes de elegir. Fuente: [Indium](https://modrinth.com/mod/indium).
- La documentación de Sodium declara soporte oficial para tarjetas con controladores actualizados compatibles con OpenGL 4.5 o superior. GPU más antiguas pueden funcionar sin garantía ni soporte. OpenGL expuesto por Radeon R3 local: **[SIN VERIFICAR]**. Esto es límite de soporte oficial, no prueba de imposibilidad de ejecución. Fuente: [Sodium](https://github.com/CaffeineMC/sodium).
- ImmediatelyFast declara incompatibilidades conocidas con OptiFine/OptiFabric en la página consultada. No se confirmó que estén presentes en el pack. Fuente: [ImmediatelyFast](https://modrinth.com/mod/immediatelyfast).
- Sodium Extra 0.5.9: su ficha consultada confirma versión/licencia y compatibilidad Minecraft, pero no se cotejaron en esta revisión todas las dependencias del artefacto. No cerrar Fabric API como requisito del conjunto sin manifiesto.
- No hay evidencia para declarar incompatibilidad de FerriteCore/ModernFix, Sodium Extra/Particle Core, More Culling/Entity Culling, C2ME u otros pares candidatos. Solapamiento de función o hipótesis no equivale a conflicto demostrado.
- No se probó compatibilidad conjunta de ningún candidato con el pack ni con el equipo.

## Candidatos Forge 1.20.1, solo si manifiesto lo exige

No combinar renderizadores equivalentes. Las referencias previas no se verifican como conjunto ni para el hardware local.

| Mod | Versión indicada previamente | Estado |
|---|---|---|
| Embeddium | `0.3.31+mc1.20.1` | Candidato Forge; Radeon R3 y rendimiento sin probar; licencia del archivo exacto pendiente. |
| Radium | `0.12.4` | Build y compatibilidad se deben cotejar contra artefacto exacto. |
| ModernFix | `5.28.0+mc1.20.1` | Candidato distinto de Fabric; build/licencia y configuración exactas pendientes. |
| FerriteCore | `6.0.1` | MIT según ficha citada; pack no probado. |
| Entity Culling / ImmediatelyFast / Dynamic FPS / Particle Core | Builds previas citadas | Archivo, dependencias y compatibilidad exacta pendientes; no formar base inicial. |

## Candidatos pospuestos

- Entity Culling: costo CPU/beneficio y advertencias concretas de la propuesta recibida **[SIN VERIFICAR]**; licencia personalizada pendiente.
- Particle Core junto a Sodium Extra: posible solapamiento, no conflicto probado; versión/dependencias exactas pendientes.
- More Culling, C2ME, Noisium/Noisiumed y LazyDFU: compatibilidad/razones previas **[SIN VERIFICAR]** para los archivos exactos.
- Hydrogen/FerriteCore: no afirmar incompatibilidad sin fuente aplicable y prueba.
- ScalableLux: release Fabric 1.20.1 no comprobada.

## Protocolo de prueba pendiente

Solo tras autorización expresa y en instancia aislada con respaldo: registrar versiones y hashes localmente; probar primero loader/base; verificar dependencias confirmadas; añadir un candidato a la vez. Guardar logs/crash reports localmente, no publicar binarios. Probar arranque, menú, mundo existente, chunks, generación, contenido RPG, cambio de dimensión y cierre normal. Comparar rendimiento por separado en condiciones reproducibles; los resultados corresponden en `PERFORMANCE.md`.

| ID | Caso | Resultado | Evidencia / incidencias |
|---|---|---|---|
| C-01 | Arranque con loader, sin optimizadores | Pendiente | NO DATA |
| C-02 | Arranque con dependencias mínimas aprobadas | Pendiente | NO DATA |
| C-03 | Llegada al menú sin error bloqueante | Pendiente | NO DATA |
| C-04 | Crear/cargar mundo de prueba | Pendiente | NO DATA |
| C-05 | Recorrido de chunks existentes | Pendiente | NO DATA |
| C-06 | Generación de chunks nuevos | Pendiente | NO DATA |
| C-07 | Modelos, recursos, entidades y contenido RPG | Pendiente | NO DATA |
| C-08 | Cambio de dimensión, si aplica | Pendiente | NO DATA |
| C-09 | Reinicio y segunda carga | Pendiente | NO DATA |
| C-10 | Cierre normal | Pendiente | NO DATA |

## Registro de incompatibilidades

No hay incompatibilidades locales reproducidas en esta revisión.

| ID | Fecha | Archivos exactos | Síntoma reproducible | Pasos | Log | Mitigación probada | Estado |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Criterio de compatibilidad

Marcar “Compatible en prueba” solo después de registrar Minecraft, Java, loader, archivos exactos, dependencias, arranque hasta menú, carga de mundo y contenido relevante sin falla bloqueante, además de logs e incidencias. Evaluar rendimiento por separado en `PERFORMANCE.md`. Estado actual de todos los candidatos: **Pendiente / NO DATA**.
