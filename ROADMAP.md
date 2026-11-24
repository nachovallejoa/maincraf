# Hoja de ruta

## Metodología: 13 etapas secuenciales

1. **Inventario del repositorio y fuentes** — registrar archivos reales y límites de acceso. Estado: inventario recibido; la revisión actual no inspecciona todo de forma independiente.
2. **Perfil del equipo** — recoger hardware, sistema y APIs, distinguiendo declaraciones de mediciones. Estado: equipo declarado; driver/OpenGL/Vulkan pendientes.
3. **Definición del objetivo RPG** — acordar alcance y criterios sin crear contenido antes de autorización. Estado: preferencias de identidad y pilares registradas; autorización de desarrollo narrativo registrada.
4. **Inventario del pack RPG** — obtener manifiesto, versiones, loader y dependencias. Estado: bloqueada por ausencia de manifiesto/JARs en el material recibido.
5. **Comparativa de versiones y loaders** — documentar evidencia y límites. Estado: comparativa documental inicial; selección final pendiente.
6. **Auditoría de mods** — verificar builds, licencias, dependencias e interacciones. Estado: candidaturas documentales; auditoría integral pendiente.
7. **Historia** — desarrollar la propuesta narrativa autorizada y documentar alcance, consecuencias e incógnitas, sin afirmar implementación ni compatibilidad. Estado: **completada; historia aprobada por el usuario sin cambios**. `STORY_BIBLE.md` registra aprobación; `GAME_DESIGN.md` recoge sus decisiones con impacto de juego. Mods y sistemas técnicos siguen **[SIN VERIFICAR]**.
8. **Diseño de perfiles aislados** — preparar instancias limpia/base/alternativas sin mezclar loaders. Estado: pendiente de autorización y manifiesto.
9. **Configuración inicial** — proponer ajustes y validar formato en instancia. Estado: sin valores/configuraciones nuevas verificadas; no precargar.
10. **Pruebas de carga** — arranque, menú, mundo y logs incrementales. Estado: pendiente; pack/manifiesto ausente.
11. **Pruebas funcionales y compatibilidad** — validar contenido RPG, progresión y conflictos. Estado: bloqueada por falta de pack/manifiesto.
12. **Benchmark controlado** — medir escenarios reproducibles, sin estimar. Estado: pendiente; no hay mediciones.
13. **Decisiones y documentación de cierre** — presentar evidencia, riesgos y cambios al usuario. Estado: pendiente para decisiones técnicas.

Las etapas se ejecutan secuencialmente. Una etapa documental no equivale a validación técnica.

## Tablero

| Pendientes | En desarrollo | Revisión | Bloqueadas | Completadas |
|---|---|---|---|---|
| Etapas 2 (verificación del equipo), 4–6 (inventario y auditoría técnica), 8–13 según dependencias; **Etapa de Mecánicas: pendiente de ejecución, expresamente autorizada por 7A para diseñar clases, niveles, estadísticas, habilidades/builds, combate y progresión como propuestas**. La autorización no implica iniciar automáticamente una etapa, implementar ni confirmar compatibilidad. | Ninguna | Ninguna | Etapa 4 (manifiesto/JARs no disponibles); etapa 10 (pack/manifiesto ausente); etapa 11 (falta pack/manifiesto) | Etapa 1 (inventario informado); etapa 3 (identidad RPG registrada); **etapa 7 (Historia: completada y aprobada sin cambios)** |

## Criterios de avance

- No confundir existencia de archivo/build con compatibilidad probada.
- Registrar `NO DATA` junto a la fuente que no aportó el dato.
- Conservar logs y métodos reproducibles cuando haya pruebas autorizadas.
- Obtener autorización antes de cambiar mods o aprobar decisiones técnicas finales.
- No subir JARs/binarios de mods de terceros.
- Mantener ramas aisladas; no modificar `main` ni fusionar sin autorización.
- Orden de dependencias: manifiesto/requisitos/builds/licencias → pruebas funcionales → benchmark. No medir un pack hipotético.

## Segunda etapa en revisión

Propuesta documental pendiente de aprobación: Minecraft 1.20.1 + Fabric como candidata principal; alternativa 1.21.1 + Fabric marcada **[SIN VERIFICAR como conservación de contenido]**; Forge 1.20.1 sujeto al manifiesto. No se instalaron mods, editaron configuraciones ni ejecutaron pruebas. Resultado local: **NO DATA**.

## Etapa 6: Identidad RPG — completada por decisión documentada

El usuario eligió una mezcla con base en **La Marea de los Mil Soles**, trasladada del océano al cielo, y pidió combinar candidatos RPG de A con B. También registró misterio/aventura más oscuro, combate y exploración, clases definidas, niveles/estadísticas y árboles/builds como ejes, y dificultad equilibrada. Eligió autorizar el desarrollo de la historia completa como propuesta en la etapa de Historia. La Cartografía de la Ceniza no fue elegida.

La etapa de Historia terminó aprobada sin cambios; esto no inicia etapa técnica ni valida mods, compatibilidad u originalidad absoluta. No se fusiona ninguna rama.

## Historia — aprobada

El usuario respondió 1A y aprobó la historia general tal como estaba. También eligió 2A (mantener Veyr), 3A (mantener facciones/personajes), 4A (mantener cuatro desenlaces, con el pactado más exigente y no perfecto), 5A (mantener los seis jefes), 6B (misiones secundarias con peso medio: algunas desbloquean rutas, recursos, testimonios o apoyos para el final). No se solicitaron ajustes; los detalles técnicos continúan pendientes de verificación.

## Etapa de Mecánicas — pendiente; autorizada para diseño

El usuario eligió 7A: autoriza avanzar con clases, niveles, estadísticas, habilidades/builds, combate y progresión **como propuestas de diseño**. Estado en el tablero: pendiente de ejecución; no se empieza automáticamente una etapa nueva aquí. No implica implementación, compatibilidad de mods, fusión de ramas ni modificación de `main`.

No hay fusión a `main`; esta actualización pertenece exclusivamente a `etapa-4-historia`.
