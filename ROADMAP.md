# Hoja de ruta

## Metodología: 13 etapas secuenciales

1. **Inventario del repositorio y fuentes** — registrar archivos reales y límites de acceso. Estado: inventario recibido; la revisión actual no inspecciona todo de forma independiente.
2. **Perfil del equipo** — recoger hardware, sistema y APIs, distinguiendo declaraciones de mediciones. Estado: equipo declarado; driver/OpenGL/Vulkan pendiente.
3. **Definición del objetivo RPG** — acordar alcance y criterios sin crear contenido antes de autorización. Estado: preferencias de identidad y pilares registradas; historia completa autorizada para desarrollo documental, pendiente de aprobación.
4. **Inventario del pack RPG** — obtener manifiesto, versiones, loader y dependencias. Estado: bloqueada por ausencia de manifiesto/JARs en el material recibido.
5. **Comparativa de versiones y loaders** — documentar evidencia y límites. Estado: comparativa documental inicial; selección final pendiente.
6. **Auditoría de mods** — verificar builds, licencias, dependencias e interacciones. Estado: candidaturas documentales; auditoría integral pendiente.
7. **Historia** — desarrollar la propuesta narrativa autorizada y documentar alcance, consecuencias e incógnitas, sin afirmar implementación ni compatibilidad. Estado: **en revisión**; propuesta completa en `STORY_BIBLE.md` y efectos de diseño en `GAME_DESIGN.md`, ambos pendientes de aprobación. Requiere revisar contenido y mantener mods/sistemas **[SIN VERIFICAR]**.
8. **Diseño de perfiles aislados** — preparar instancias limpia/base/alternativas sin mezclar loaders. Estado: pendiente de autorización y manifiesto.
9. **Configuración inicial** — proponer ajustes y validar formato en instancia. Estado: sin valores/configuraciones nuevas verificadas; no precargar.
10. **Pruebas de carga** — arranque, menú, mundo y logs incrementales. Estado: pendiente.
11. **Pruebas funcionales y compatibilidad** — validar contenido RPG, progresión y conflictos. Estado: bloqueada por falta de pack/manifiesto.
12. **Benchmark controlado** — medir escenarios reproducibles, no estimar. Estado: pendiente; sin mediciones.
13. **Decisiones y documentación de cierre** — presentar evidencia, riesgos y cambios al usuario. Estado: pendiente para decisiones técnicas; esta etapa narrativa sigue en revisión, no aprobada.

Las etapas se ejecutan secuencialmente. Una etapa documental no equivale a validación técnica.

## Tablero

| Pendientes | En desarrollo | Revisión | Bloqueadas | Completadas |
|---|---|---|---|---|
| Etapas 2 (pruebas locales), 8, 9, 11, 12, 13; inventario/validación técnica posterior | Ninguna | **Etapa 7 (Historia): propuesta La Marea de los Mil Soles pendiente de aprobación; mods y sistemas sin verificar** | Etapa 4 (manifiesto/JARs no disponibles); etapa 10 (pack/manifiesto ausente) | Etapa 1 (inventario informado); etapa 3 (identidad RPG registrada); etapa 5 (comparativa documental, aprobación pendiente); etapa 6 (candidaturas documentales, auditoría integral pendiente) |

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

El usuario eligió una mezcla con base en **La Marea de los Mil Soles**, trasladada del océano al cielo, y pidió combinar candidatos RPG de A con B. También registró misterio/aventura más oscura, enfoque en combate y exploración, clases definidas, niveles/estadísticas, árboles/builds y dificultad equilibrada. La Cartografía de la Ceniza no queda elegida.

La etapa de Historia se encuentra ahora en revisión: la propuesta completa está documentada como pendiente de aprobación. Esta actualización no inicia otra etapa técnica ni declara implementado el contenido. Mods/candidatos, Minecraft 1.20.1 + Fabric, funciones previstas, compatibilidad, originalidad absoluta y rendimiento continúan sin verificar. No se fusiona ninguna rama.
