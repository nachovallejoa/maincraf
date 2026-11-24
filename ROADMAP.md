# Hoja de ruta

## Metodología: 13 etapas secuenciales

1. **Inventario del repositorio y fuentes** — registrar archivos reales y límites de acceso. Estado: inventario recibido; revisión actual no inspecciona todo independientemente.
2. **Perfil del equipo** — hardware/sistema/APIs, distinguir declaraciones de mediciones. Estado: equipo declarado; drivers/OpenGL/Vulkan pendientes.
3. **Definición del objetivo RPG** — alcance y criterios. Estado: identidad/pilares registrados; autorización narrativa registrada.
4. **Inventario del pack RPG** — manifiesto, versiones, loader/dependencias. Estado: bloqueada por ausencia de manifiesto/JARs.
5. **Comparativa de versiones/loaders** — evidencia y límites. Estado: comparativa documental; selección final pendiente.
6. **Auditoría de mods** — builds, licencias, dependencias/interacción. Estado: candidatos documentados; auditoría integral pendiente.
7. **Historia** — propuesta narrativa y consecuencias. Estado: **completada y aprobada sin cambios**, según registro de rama anterior; no implica implementación.
8. **Mecánicas** — diseño de clases, niveles/estadísticas, habilidades/builds, equipo, combate, jefes, reputación, progresión y misiones. Estado: **en revisión en el tablero; propuesta documentada pendiente de aprobación final e implementación**.
9. **Configuración inicial** — ajustes y validación en instancia. Estado: pendiente; no preconfigurar.
10. **Pruebas de carga** — arranque, menú, mundo/logs incrementales. Estado: pendiente; pack/manifiesto no disponibles.
11. **Pruebas funcionales y compatibilidad** — progresión, contenido y conflictos. Estado: bloqueada por pack/manifiesto.
12. **Benchmark controlado** — escenarios reproducibles. Estado: pendiente; no hay mediciones.
13. **Decisiones y documentación de cierre** — evidencia, riesgos y cambios. Estado: pendiente.

Las etapas son secuenciales; documentación no equivale a validación técnica.

## Tablero

| Pendientes | En desarrollo | Revisión | Bloqueadas | Completadas |
|---|---|---|---|---|
| Etapas 2, 4–6 y 8–13 según dependencias | Ninguna | **Etapa 8 — Mecánicas: propuesta de diseño en revisión; autorizada como diseño, aprobación final pendiente** | Etapa 4 (manifiesto/JAR ausentes); etapas 10–11 (pack/manifiesto ausentes) | Etapa 1 (inventario informado); etapa 3 (identidad RPG registrada); etapa 7 (historia aprobada sin cambios) |

La autorización previa permite diseñar mecánicas como propuesta; no autoriza implementación, pruebas, instalación, compatibilidad, fusión de ramas ni cambio de rama por defecto. No se debe confundir presencia de archivo/build con compatibilidad probada. Registrar **NO DATA** cuando la fuente/medición no aporta resultado.

## Etapa 7 — Historia aprobada

La historia se registró aprobada sin cambios y se mantienen las elecciones acordadas. Diseño y mecánicas no alteran esa aprobación. Correspondencia detallada de mecánicas con la fuente narrativa deberá verificarse si la fuente no acompaña la revisión.

## Etapa 8 — Mecánicas: revisión

La propuesta de **La Marea de los Mil Soles** queda en revisión. Incluye tres clases no afiliadas, tres ramas propuestas por clase, curva XP hasta nivel 30, estadísticas, equipo/rareza, combate, seis encuentros, cuatro relaciones de facción, rangos por acto y misiones principales/secundarias. Conserva decisiones aprobadas y señala pendientes explícitos: balance/viabilidad solitaria, XP por actividad, asignación inicial, nodos y requisitos, recompensas sin especificar, condiciones mecánicas de finales, ámbito de guardado y relación Almirante Sumergido–Veyr **[SIN VERIFICAR]**.

Los mods RPG son candidatos auditados documentalmente, no aprobados ni compatibles como conjunto. Sin pruebas locales. No se suben binarios/JARs de terceros. La revisión del tablero no cambia la rama principal ni etapas previas.

## Criterios de avance

- No confundir existencia de archivo/build con compatibilidad probada.
- Registrar **NO DATA** junto con la fuente que no devolvió datos; no convertir en cero/estimación.
- Conservar logs y métodos reproducibles solo tras pruebas autorizadas.
- Obtener aprobación antes de cambiar selección técnica o comenzar implementación.
- No subir binarios de mods de terceros; revisar términos/licencias.
- Mantener ramas aisladas; no modificar rama por defecto ni ramas de etapas anteriores.
