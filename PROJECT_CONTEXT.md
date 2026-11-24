# Contexto del proyecto

> **Misión 1 — investigación inicial. Estado: revisión.** Esta misión documenta hallazgos y propuestas; no instala Minecraft ni mods, no ejecuta pruebas y no modifica la rama principal. Ninguna recomendación de plataforma o rendimiento está aprobada.

## Objetivo y filosofía

Documentar una base técnica para evaluar Minecraft con contenido RPG y optimización en el equipo declarado, sin sacrificar los mods requeridos. Mantener trazabilidad de fuentes/versiones; distinguir hechos, propuestas, decisiones aprobadas y datos no verificados. No diseñar contenido RPG en esta etapa. Las secciones sin datos quedan explícitamente pendientes y nunca se rellenan con estimaciones.

## Hardware declarado

| Componente | Dato recibido | Estado |
|---|---|---|
| CPU | AMD Athlon 5150 | No verificado independientemente |
| Gráficos | Radeon R3 integrada | No verificado; API/controlador local pendiente |
| RAM | 12 GB instalados; ~9,9 GB utilizables declarados | No verificado |
| Almacenamiento | HDD | No verificado |
| Sistema | Windows; versión/build no indicada | Pendiente |
| Resolución | 1280×720 declarada | No verificada |
| OpenGL/controlador/estado térmico | Sin datos | **Pendiente de comprobación local** |

## Autonomía controlada y autorización

- Se permite investigar, documentar y proponer; una propuesta no es decisión aprobada salvo autorización explícita.
- No instalar, quitar, sustituir ni redistribuir mods sin autorización expresa y revisión de archivo, loader, compatibilidad y licencia.
- No inventar métricas, manifiestos, dependencias ni resultados. Registrar `NO DATA` y la fuente que no devolvió datos.
- No ejecutar benchmarks ficticios ni extrapolar FPS de otros equipos.
- Mantener loaders/ramas de prueba aislados; no mezclar Fabric y Forge.
- Nunca subir JARs ni otros archivos de mods de terceros.
- No sobrescribir trabajo ajeno. La documentación de esta misión se mantiene en `mision-1-investigacion`, sin escribir en `main`.
- La investigación recibida indica ejecución secuencial de pasos, no paralela.

## Equipo y responsabilidades

- **Director del proyecto:** coordina investigación, trazabilidad y separación de propuestas/decisiones.
- **Diseñador RPG:** identifica requisitos; no crea sistemas/contenido RPG en esta misión.
- **Guionista:** registra necesidades narrativas pendientes; no redacta lore/trama.
- **Programador Java:** revisa riesgos técnicos; no programa mods/código.
- **Especialista Minecraft:** verifica versiones/loaders/fuentes; no instala ni modifica.
- **Optimizador:** documenta opciones/protocolo; no ejecuta optimizaciones ni benchmarks.
- **Auditor de mods:** organiza evidencia, licencias, dependencias; no instala ni aprueba mods.
- **Tester:** define pruebas/datos necesarios; no las ejecuta.
- **Revisor independiente:** comprueba que hechos, propuestas y pendientes se distingan.
- Incorporar especialistas adicionales solo si el alcance lo requiere.

## Repositorio y alcance revisado

- Repositorio `nachovallejoa/maincraf`; rama por defecto `main`; trabajo documental aislado en `mision-1-investigacion`.
- La entrada revisada describe 12 archivos existentes: 10 documentos y dos archivos de configuración. El README no fue encontrado en los árboles/referencias consultados; las consultas devolvieron 404. Ese 404 no demuestra inexistencia fuera de lo consultado.
- La revisión no instaló ni ejecutó Minecraft, no inspeccionó equipo físico, no midió rendimiento ni modificó el repositorio.
- Manifiesto RPG, JARs, logs y mediciones: **no disponibles en el material revisado**.

## Propuestas técnicas iniciales — pendientes de aprobación

1. Minecraft 1.20.1 + Fabric como plataforma candidata a ensayo, por coincidencia documental de versiones; no se afirma superioridad de rendimiento.
2. Forge 1.20.1 solo como alternativa si el manifiesto lo exige.
3. Base candidata de prueba: Sodium 0.5.13, Lithium 0.11.4, FerriteCore 6.0.1, ModernFix 5.25.2+mc1.20.1 e ImmediatelyFast 1.5.5+1.20.4-fabric (la ficha de este último declara rango 1.20–1.20.4). Ninguno está aprobado/instalado.
4. Java 17 es adecuado para Minecraft 1.20.1; la GPU/controlador/OpenGL de la máquina siguen sin verificar.
5. No precargar `sodium-options.json`; el esquema exacto para esa versión no está demostrado en esta revisión. ModernFix queda en valores predeterminados en el primer ensayo.
6. No redistribuir binarios por citar su licencia. Revisar condiciones y avisos aplicables por archivo.

## Pendientes de aprobación/datos

- Obtener manifiesto completo del pack RPG, loader exigido, dependencias y archivos exactos.
- Confirmar si se acepta una instancia aislada 1.20.1 + Fabric; no equivale a aprobar instalación final.
- Confirmar si Forge es requisito del contenido.
- Obtener comprobación local de Java, GPU/controlador, OpenGL y apertura de Minecraft limpio.
- Autorizar, tras revisión de licencia, cualquier redistribución eventual.
- Decidir límite de FPS, resolución y ajustes tras pruebas, no por la plantilla.
- Evaluar `-Xmx4G` como propuesta previa, no como valor óptimo medido.
- Ejecutar el protocolo y aportar logs, capturas y resultados; ninguna medición existe actualmente.
- Resolver el conteo histórico solo si se actualiza la fuente de revisión: el detalle indica 12 archivos existentes; README 404 no cuenta como archivo.

## Enlaces documentales

Ver `ROADMAP.md`, `MOD_AUDIT.md`, `MOD_COMPATIBILITY.md`, `PERFORMANCE.md` y `TECH_DECISIONS.md`.
