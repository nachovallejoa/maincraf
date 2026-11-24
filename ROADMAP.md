# Hoja de ruta

## Metodología: 13 etapas secuenciales

1. **Inventario del repositorio y fuentes** — registrar archivos reales y límites de acceso. Estado: inventario recibido; la revisión actual no inspecciona todo de forma independiente.
2. **Perfil del equipo** — recoger hardware, sistema y APIs, distinguiendo declaraciones de mediciones. Estado: equipo declarado; driver/OpenGL/Vulkan pendientes.
3. **Definición del objetivo RPG** — acordar alcance y criterios sin crear contenido antes de autorización. Estado: pendiente.
4. **Inventario del pack RPG** — obtener manifiesto, versiones, loader y dependencias. Estado: bloqueada por ausencia de manifiesto/JARs según el inventario recibido.
5. **Comparativa de versiones y loaders** — documentar evidencia y límites. Estado: investigación inicial documentada; selección final pendiente de aprobación.
6. **Auditoría de mods** — verificar builds, licencias, dependencias e interacciones. Estado: candidatos documentados; auditoría integral pendiente.
7. **Diseño de perfiles aislados** — preparar instancia limpia/base/alternativas, separando loaders. Estado: pendiente de autorización y manifiesto.
8. **Configuración inicial** — proponer ajustes y validar formato en instancia. Estado: propuestas documentales no probadas; no precargar formatos no verificados.
9. **Pruebas de carga** — arranque, menú, mundo y logs incrementales. Estado: pendiente.
10. **Pruebas funcionales y compatibilidad** — validar sistemas RPG, progresión y conflictos. Estado: bloqueada por pack/manifiesto.
11. **Benchmark controlado** — medir escenarios reproducibles sin estimar resultados. Estado: pendiente; no hay mediciones.
12. **Decisiones y autorización** — presentar evidencia, riesgos y cambios al usuario. Estado: pendiente.
13. **Documentación y cierre** — conservar resultados, decisiones, changelog y tareas. Estado: documentación inicial actualizada; cierre final pendiente.

Las etapas se ejecutan una tras otra, no en paralelo. Una etapa documental no equivale a validación técnica.

## Tablero

| Pendientes | En desarrollo | Revisión | Bloqueadas | Completadas |
|---|---|---|---|---|
| Etapas 2 (verificación local), 3, 7, 8 (validación), 9, 11, 12 | Ninguna | **Misión 1: investigación y documentación inicial corregida; sin pruebas de Minecraft ni benchmarks** | Etapa 4: manifiesto/JARs ausentes; etapa 10: falta pack/manifiesto | Etapa 1: inventario informado; etapa 5: comparativa documental inicial; etapa 6: candidatos y riesgos iniciales; etapa 13: documentación inicial (no cierre final) |

## Criterios de avance

- No confundir existencia de archivo/build con compatibilidad probada.
- Registrar `NO DATA` junto con la fuente que no entregó el dato.
- Conservar logs y métodos reproducibles.
- Obtener autorización antes de cambiar mods o aprobar decisiones técnicas finales.
- No subir JARs de terceros.
- Mantener ramas de trabajo aisladas; no modificar `main` ni sobrescribir trabajo ajeno.
- Orden de dependencias: manifiesto/requisitos/builds/licencias → pruebas funcionales → benchmark; no medir un pack hipotético.
