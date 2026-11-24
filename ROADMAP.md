# Hoja de ruta

## Metodología: 13 etapas secuenciales

1. **Inventario del repositorio y fuentes** — registrar archivos reales y límites de acceso. Estado: inventario recibido; revisión actual no inspecciona todo independientemente.
2. **Perfil del equipo** — hardware/sistema/APIs y separar declaraciones de mediciones. Estado: usuario informa 10 GB RAM disponibles y 500 MB usados por SO; SO/configuración completa y mediciones pendientes.
3. **Definición del objetivo RPG** — alcance y criterios. Estado: identidad/pilares registrados; autorización narrativa previa.
4. **Inventario del pack RPG** — manifiesto, versiones, loader/dependencias. Estado: bloqueada por ausencia de manifiesto/JARs.
5. **Comparativa de versiones/loaders** — evidencia y límites. Estado: documental; selección técnica final pendiente.
6. **Auditoría de mods** — builds/licencias/dependencias/interacciones. Estado: candidatos documentados; auditoría integral pendiente.
7. **Historia** — propuesta narrativa y consecuencias. Estado: historia registrada como aprobada en etapa previa; preservar sin spoilers.
8. **Mecánicas** — clases, niveles/estadísticas, habilidades/builds, equipo, combate, jefes, reputación, progresión y misiones. **Estado: aprobada por el usuario como diseño revisado.** Decisiones aprobadas están registradas en `GAME_DESIGN.md`. Candidatos externos y módulos propios individuales no quedaron clasificados; verificaciones técnicas, balance y rendimiento siguen pendientes. Esto no autoriza por sí solo instalación o implementación.
9. **Configuración inicial** — ajustes y validación en instancia. Estado: pendiente; no reconfigurar.
10. **Pruebas de carga** — arranque, menú, mundo/logs incrementales. Estado: pendiente; no hay pack/manifiesto.
11. **Pruebas funcionales y compatibilidad** — progresión, contenido y conflictos. Estado: bloqueada por selección/pack.
12. **Benchmark controlado** — escenarios reproducibles. Estado: pendiente; sin mediciones.
13. **Decisiones y documentación de cierre** — evidencia, riesgos y cambios. Estado: pendiente.

Las etapas son secuenciales; la documentación no equivale a validación técnica.

## Tablero

| Pendientes | En desarrollo | En revisión | Bloqueadas | Completadas |
|---|---|---|---|---|
| Etapas 2, 4–6, 9–13 según dependencias; clasificación de módulos y candidatos RPG; verificaciones técnicas | Ninguna | Ninguna | Etapas 10–11 por ausencia de pack/manifiesto y selección técnica | Etapa 1 (inventario informado); Etapa 3 (identidad registrada); Etapa 7 (historia aprobada); **Etapa 8 (Mecánicas aprobada)** |

### Siguiente etapa: Desarrollo de mods propios

**Pendiente y no autorizada explícitamente.** La respuesta «apruebo todo» no asignó Aprobar/Aplazar/Descartar a cada módulo de la pregunta 10 ni eligió la opción de autorización explícita de la pregunta 11. No iniciar etapa nueva ni implementar módulos por inferencia. Los módulos continúan sin clasificación individual, documentada en `ARCHITECTURE.md`.

## Registro de estado y confidencialidad

El usuario pidió que no se le formulen más cuestionarios, que el asistente asuma decisiones creativas según sus prioridades y que se preserve el descubrimiento de la historia sin revelar contenido por adelantado. Evitar spoilers al comunicar el trabajo; no eludir aprobaciones técnicas formales ni licencias. La solicitud de tener el modpack hecho en la próxima ocasión no significa que el pack ya exista ni que las verificaciones puedan omitirse. No fusionar ramas ni empezar automáticamente una nueva etapa.

Rendimiento local: **NO DATA**. El hardware comunicado por el usuario no se ha verificado independientemente; no declarar rendimiento ni compatibilidad.
