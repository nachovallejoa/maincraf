# Hoja de ruta

## Metodología: 13 etapas secuenciales

1. **Inventario del repositorio y fuentes** — registrar archivos reales y límites de acceso. Estado: inventario recibido; revisión actual no inspecciona todo independientemente.
2. **Perfil del equipo** — hardware/sistema/APIs y separar declaraciones de mediciones. Estado: equipo declarado; datos de sistema/mediciones pendientes.
3. **Definición del objetivo RPG** — alcance y criterios. Estado: identidad/pilares registrados; autorización narrativa previa.
4. **Inventario del pack RPG** — manifiesto, versiones, loader/dependencias. Estado: bloqueada por ausencia de manifiesto/JARs.
5. **Comparativa de versiones/loaders** — evidencia y límites. Estado: documental; selección final pendiente.
6. **Auditoría de mods** — builds/licencias/dependencias/interacciones. Estado: candidatos documentados; auditoría integral pendiente.
7. **Historia** — propuesta narrativa y consecuencias. Estado: completada y aprobada según registro anterior, sin que esto certifique una fuente independiente en esta revisión.
8. **Mecánicas** — clases, niveles/estadísticas, habilidades/builds, equipo, combate, jefes, reputación, progresión y misiones. Estado: **en revisión en el tablero**; diseño documental pendiente de aprobación final e implementación. No autoriza instalación, pruebas, implementación ni compatibilidad.
9. **Configuración inicial** — ajustes y validación en instancia. Estado: pendiente; no preconfigurar.
10. **Pruebas de carga** — arranque, menú, mundo/logs incrementales. Estado: pendiente; pack/manifiesto no disponible.
11. **Pruebas funcionales y compatibilidad** — progresión, contenido y conflictos. Estado: bloqueada por selección/pack.
12. **Benchmark controlado** — escenarios reproducibles. Estado: pendiente; sin mediciones.
13. **Decisiones y documentación de cierre** — evidencia, riesgos y cambios. Estado: pendiente.

Las etapas son secuenciales; documentación no equivale a validación técnica.

## Tablero

| Pendientes | En desarrollo | Revisión | Bloqueadas | Completadas |
|---|---|---|---|---|
| Etapas 2, 4–6 y 9–13 según dependencias | Ninguna | **Etapa 8 — Mecánicas: propuesta documentada, pendiente de aprobación final e implementación** | Etapas 10–11 por pack/manifiesto ausentes; validación de historia mecánica contra fuente independiente pendiente | Etapa 1 (inventario informado); etapa 3 (identidad RPG); etapa 7 (historia aprobada según registro) |

La autorización previa permite diseñar mecánicas como propuesta, no autoriza implementación, pruebas, instalación, compatibilidad, fusión de ramas ni cambio de rama por defecto. No confundir existencia de archivo/build con compatibilidad probada. Registrar **NO DATA** cuando fuente/medición no aporta resultado; no inferir cero ni resultado favorable. No subir binarios de mods de terceros.

## Etapa 7 — Historia aprobada

La historia se registra como aprobada según el historial de proyecto. Mecánicas no deben alterar esa aprobación. La correspondencia detallada de nombres, escenas, decisiones y desenlaces requiere contrastar fuente independiente si no está incluida en el material de revisión.

## Etapa 8 — Mecánicas: revisión

El diseño revisado de *La Marea de los Mil Soles* conserva las clases opcionales, progreso propuesto hasta nivel 30, cuatro atributos, ramas, equipo/rarezas, combate, seis encuentros, cuatro facciones, bandas por acto y misiones. Parámetros aritméticos propuestos se distinguen de valores validados. Se mantienen pendientes: coherencia con historia aprobada independiente (**[SIN VERIFICAR]**); balance/viabilidad en solitario; presupuesto de XP por acto y XP por actividad; asignación inicial; nodos/costes/requisitos; recompensas sin magnitudes; condiciones técnicas de finales; secundarias concretas del Acto V; ámbito de guardado; selección y verificación de versiones/dependencias/licencias/APIs; compatibilidad local y rendimiento.

Los mods RPG solo son candidatos documentales, no selección aprobada. Medidas locales de FPS, frametime, memoria, arranque/carga y estabilidad: **NO DATA**. No se incorporan JARs/binarios de terceros. La rama principal y ramas de etapas anteriores permanecen sin cambios por este registro.

## Criterios de avance

- No confundir archivo/build existente con compatibilidad probada.
- Registrar **NO DATA** junto a la fuente que no devolvió datos; no convertir huecos en cero/estimación.
- Conservar logs/métodos reproducibles solo tras pruebas autorizadas.
- Obtener aprobación antes de cambiar selección técnica o empezar implementación.
- No subir binarios de mods de terceros; revisar licencias antes de cualquier distribución.
- Mantener ramas aisladas; no modificar ramas anteriores ni principal por defecto.
