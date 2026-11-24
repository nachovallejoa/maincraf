# Contexto del proyecto

> Misión 1: documentación de investigación inicial. Estado: **en revisión**; propuestas técnicas pendientes de aprobación. La información de hardware procede de la entrada recibida y no se midió independientemente.

## Objetivo y filosofía

Documentar una base técnica para evaluar Minecraft con contenido RPG y optimización en el equipo declarado, sin afirmar compatibilidad o rendimiento no medidos. Mantener trazabilidad de fuentes, versiones y decisiones; separar propuestas de hechos y preservar los datos ausentes como pendientes. No diseñar contenido RPG en esta etapa.

## Hardware declarado

| Componente | Dato recibido | Estado |
|---|---|---|
| CPU | AMD Athlon 5150, 4 núcleos, 1,6 GHz | No verificado independientemente |
| Gráficos | Radeon R3 integrada; hasta 2 GB compartidos según la entrada | No verificado; memoria compartida no equivale a VRAM dedicada |
| RAM | 12 GB instalados; ~9,9 GB utilizables declarados | No verificado |
| Almacenamiento | HDD | No verificado |
| Resolución | 1280×720 declarada | No verificada |
| Sistema operativo | Windows; versión/build no indicada | Pendiente |
| Driver y API gráfica | No indicados | Pendiente; OpenGL/Vulkan no verificados |

AMD clasifica la familia Athlon con Radeon R3 como legacy y no planea nuevos drivers para ella. Esto no establece la API gráfica expuesta por esta instalación. Fuente: https://www.amd.com/en/resources/support-articles/faqs/GPU-630.html

## Reglas de autonomía controlada y autorización

- Se permite investigar, documentar y proponer; no se considera una propuesta como decisión aprobada.
- No instalar, quitar, sustituir ni redistribuir mods sin autorización expresa y verificación de archivo, loader, compatibilidad y licencia.
- No inventar valores, mediciones, manifiestos, dependencias, resultados ni contenido cuando una fuente no devolvió datos; registrar `NO DATA` y qué fuente faltó.
- No ejecutar benchmarks ficticios ni extrapolar FPS. Conservar logs y condiciones al probar.
- Mantener loaders y ramas de prueba aislados; no mezclar Fabric y Forge.
- Nunca subir JARs de mods de terceros.
- No sobrescribir trabajo ajeno: esta misión se documenta en una rama propia, sin cambios en `main`.

## Estado recibido del repositorio

La investigación entregada informó rama por defecto `main`, repositorio vacío y sin commits, árbol raíz vacío y README 404. En esta misión se consultó GitHub: repositorio `nachovallejoa/maincraf`, rama por defecto `main`; lista de ramas vacía y contenido de raíz vacío. El contenido sigue sin archivos previos. La revisión original reporta: `INCOMPLETE: 0 archivos revisados; árbol del repositorio y README, because el repositorio está vacío y no tiene commits (el README devolvió 404).`

## Decisiones propuestas

- Probar primero Minecraft 1.20.1 + Fabric en instancia aislada: propuesta de investigación, no decisión aprobada ni superioridad de FPS demostrada.
- Java 17 es la recomendación de Fabric para Minecraft 1.17–1.20.4: https://wiki.fabricmc.net/install
- Base mínima candidata para ensayar: Sodium 0.5.13 + Lithium 0.11.4 + FerriteCore 6.0.1; compatibilidad con el pack y Radeon R3 pendiente de pruebas. Sodium exige oficialmente driver compatible con OpenGL 4.5: https://modrinth.com/mod/sodium
- Alternativa 1.20.1 + Forge solo si el manifiesto RPG lo requiere. No mezclar pilas.
- `-Xmx4G` es un valor inicial propuesto, no medido ni aprobado.
- No hay FPS, 1% low, frametimes, RAM, CPU/GPU ni tiempos de carga disponibles.

## Pendientes de aprobación y datos

1. Aprobar o rechazar 1.20.1 + Fabric.
2. Entregar manifiesto exacto del pack RPG y sus requisitos de loader.
3. Confirmar launcher, Windows/build, driver AMD y OpenGL/Vulkan expuestos.
4. Aprobar mods y archivos exactos tras verificar dependencias/licencias.
5. Ejecutar pruebas funcionales y benchmarks controlados en el equipo real.
6. Definir objetivo prioritario: FPS, estabilidad/frametimes, memoria o equilibrio.
7. Autorizar explícitamente cualquier incorporación, retirada o sustitución de mods.

Ver también `ROADMAP.md`, `MOD_AUDIT.md`, `MOD_COMPATIBILITY.md`, `PERFORMANCE.md` y `TECH_DECISIONS.md`.