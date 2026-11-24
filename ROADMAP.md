# Hoja de ruta

## Metodología: 13 etapas secuenciales

1. **Inventario del repositorio y fuentes** — registrar archivos reales y límites de acceso. Estado: inventario recibido; la revisión actual no inspecciona todo de forma independiente.
2. **Perfil del equipo** — recoger hardware, sistema y APIs, distinguiendo declaraciones de mediciones. Estado: equipo declarado; driver/OpenGL/Vulkan pendientes.
3. **Definición del objetivo RPG** — acordar alcance y criterios sin crear contenido antes de autorización. Estado: pendiente.
4. **Inventario del pack RPG** — obtener manifiesto, versiones, loader y dependencias. Estado: bloqueada por ausencia de manifiesto/JARs en el material recibido.
5. **Comparativa de versiones y loaders** — documentar evidencia y límites. Estado: comparativa documental inicial; selección final pendiente de aprobación.
6. **Auditoría de mods** — verificar builds, licencias, dependencias e interacciones. Estado: candidatos documentales; auditoría integral pendiente.
7. **Diseño de perfiles aislados** — preparar instancias limpia/base/alternativas, sin mezclar loaders. Estado: pendiente de autorización y manifiesto.
8. **Configuración inicial** — proponer ajustes y validar formato en instancia. Estado: no hay valores/configuraciones nuevas verificados; no precargar.
9. **Pruebas de carga** — arranque, menú, mundo y logs incrementales. Estado: pendiente.
10. **Pruebas funcionales y compatibilidad** — validar contenido RPG, progresión y conflictos. Estado: bloqueada por falta de pack/manifiesto.
11. **Benchmark controlado** — medir escenarios reproducibles, no estimar. Estado: pendiente; sin mediciones.
12. **Decisiones y autorización** — presentar evidencia, riesgos y cambios al usuario. Estado: pendiente.
13. **Documentación y cierre** — conservar resultados, decisiones, changelog y tareas. Estado: documentación inicial actualizada; cierre final pendiente.

Las etapas se ejecutan secuencialmente. Una etapa documental no equivale a validación técnica.

## Tablero

| Pendientes | En desarrollo | Revisión | Bloqueadas | Completadas |
|---|---|---|---|---|
| Etapa 2 (pruebas locales), 3, 7, 8, 9, 11, 12 | Ninguna | **Etapa 2: propuesta de versión, loader y mods — revisión documental, pendiente de aprobación** | Etapa 4: manifiesto/JARs no disponibles; etapa 10: pack/manifiesto ausentes | Etapa 1: inventario informado; etapa 5: comparativa documental inicial; etapa 6: candidatos y riesgos documentados; etapa 13: documentación inicial (sin cierre final) |

## Criterios de avance

- No confundir existencia de archivo/build con compatibilidad probada.
- Registrar `NO DATA` junto a la fuente que no aportó el dato.
- Conservar logs y métodos reproducibles cuando haya pruebas autorizadas.
- Obtener autorización antes de cambiar mods o aprobar decisiones técnicas finales.
- No subir JARs/binarios de terceros.
- Mantener ramas aisladas; no modificar `main` ni `mision-1-investigacion` desde la rama de etapa dos.
- Orden de dependencias: manifiesto/requisitos/builds/licencias → pruebas funcionales → benchmark. No medir un pack hipotético.

## Segunda etapa en revisión

Propuesta documental pendiente de aprobación: Minecraft 1.20.1 + Fabric como candidata provisional, tomando la ficha de Prominence II como referencia; alternativa 1.21.1 + Fabric **[SIN VERIFICAR como conservación de contenido]**; mods candidatos, límites, dependencias y licencias pendientes de confirmar con manifiesto/JARs y hardware local. No se instalaron mods, no se editó configuración y no se ejecutaron pruebas. Resultados: **NO DATA**.

Siguiente paso de revisión: recibir manifiesto/JARs y comprobar driver/OpenGL/Java/launcher/sistema local; después validar artefactos exactos y permisos. No crear configuraciones de mods: no hay ajustes nuevos verificados.

Referencias de detalle: `TECH_DECISIONS.md`, `MOD_AUDIT.md`, `MOD_COMPATIBILITY.md` y `MODS_MANIFEST.md`.
