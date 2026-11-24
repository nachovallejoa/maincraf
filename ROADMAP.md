# Hoja de ruta

## Metodología: 13 etapas secuenciales

1. **Inventario del repositorio y fuentes** — registrar archivos reales y límites de acceso. Estado: inventario recibido; la revisión actual no inspecciona todo de forma independiente.
2. **Perfil del equipo** — recoger hardware, sistema y APIs, distinguiendo declaraciones de mediciones. Estado: equipo declarado; driver/OpenGL/Vulkan pendientes.
3. **Definición del objetivo RPG** — acordar alcance y criterios sin crear contenido antes de autorización. Estado: preferencias de identidad y pilares registradas; historia completa autorizada para etapa futura.
4. **Inventario del pack RPG** — obtener manifiesto, versiones, loader y dependencias. Estado: bloqueada por ausencia de manifiesto/JARs en el material recibido.
5. **Comparativa de versiones y loaders** — documentar evidencia y límites. Estado: comparativa documental inicial; selección final pendiente de aprobación.
6. **Auditoría de mods** — verificar builds, licencias, dependencias e interacciones. Estado: candidaturas documentales; auditoría integral pendiente.
7. **Diseño de perfiles aislados** — preparar instancias limpia/base/alternativas, sin mezclar loaders. Estado: pendiente de autorización y manifiesto.
8. **Configuración inicial** — proponer ajustes y validar formato en instancia. Estado: sin valores/configuraciones nuevas verificados; no precargar.
9. **Pruebas de carga** — arranque, menú, mundo y logs incrementales. Estado: pendiente.
10. **Pruebas funcionales y compatibilidad** — validar contenido RPG, progresión y conflictos. Estado: bloqueada por falta de pack/manifiesto.
11. **Benchmark controlado** — medir escenarios reproducibles, no estimar. Estado: pendiente; sin mediciones.
12. **Decisiones y autorización** — presentar evidencia, riesgos y cambios al usuario. Estado: pendiente para decisiones técnicas. La autorización narrativa de etapa de Historia está registrada en contexto; no implica inicio automático.
13. **Documentación y cierre** — conservar resultados, decisiones, changelog y tareas. Estado: documentación inicial actualizada; cierre final pendiente.

Las etapas se ejecutan secuencialmente. Una etapa documental no equivale a validación técnica.

## Tablero

| Pendientes | En desarrollo | Revisión | Bloqueadas | Completadas |
|---|---|---|---|---|
| Etapas 2 (pruebas locales), 3 (Historia autorizada para después), 7, 8, 9, 11, 12, 13; inventario/validación técnica posteriores | Ninguna | Etapa 5 (comparativa documental; aprobación pendiente) | Etapa 4 (manifiesto/JARs no disponibles); etapa 10 (pack/manifiesto ausentes) | Etapa 1 (inventario informado); etapa 3 (identidad RPG registrada) |

## Criterios de avance

- No confundir existencia de archivo/build con compatibilidad probada.
- Registrar `NO DATA` junto a la fuente que no aportó el dato.
- Conservar logs y métodos reproducibles cuando haya pruebas autorizadas.
- Obtener autorización antes de cambiar mods o aprobar decisiones técnicas finales.
- No subir JARs/binarios de mods de terceros.
- Mantener ramas aisladas; no modificar `main` ni fusionar sin autorización.
- Orden de dependencias: manifiesto/requisitos/builds/licencias → pruebas funcionales → benchmark. No medir un pack hipotético.

## Segunda etapa en revisión

Propuesta documental pendiente de aprobación: Minecraft 1.20.1 + Fabric como candidata provisional, tomando la ficha de Prominence II como referencia; alternativa 1.21.1 + Fabric **[SIN VERIFICAR como conservación de contenido]**; mods candidatos, límites, dependencias y licencias pendientes de confirmar con manifiesto/JARs y hardware local. No se instalaron mods, no se editó configuración y no se ejecutaron pruebas. Resultados: **NO DATA**.

Siguiente paso de revisión: recibir manifiesto/JARs y comprobar driver/OpenGL/Java/launcher/sistema local; después validar artefactos exactos y permisos. No crear configuraciones sin ajustes nuevos verificados.

Referencias detalladas: `TECH_DECISIONS.md`, `MOD_AUDIT.md`, `MOD_COMPATIBILITY.md` y `MODS_MANIFEST.md`.

## Etapa 6: Identidad RPG — completada

El usuario eligió una mezcla con base en **La Marea de los Mil Soles**, trasladada del océano al cielo, y pidió combinar los mods candidatos de B con los de A. El cuestionario también registra tono de misterio/aventura y más oscuro/peligroso; enfoque combate y exploración; progresión mediante árbol de habilidades/builds, niveles/estadísticas y clases definidas; dificultad equilibrada. La etapa de identidad RPG queda **completada** por decisión documentada.

La etapa de Historia permanece **pendiente**. El usuario autorizó explícitamente desarrollar la historia completa de la propuesta elegida (respuesta 6A), por lo que queda **autorizada para más adelante**, pero no se inicia aquí. Mods/candidatos, mundo técnico, compatibilidad, funciones previstas, originalidad frente a Prominence II y rendimiento permanecen sin verificar. No se fusiona ninguna rama ni se inicia una etapa nueva.
