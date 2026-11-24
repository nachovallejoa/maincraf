# Hoja de ruta

## Metodología: 13 etapas secuenciales

1. **Inventario del repositorio y fuentes** — registrar archivos reales y límites de acceso. Estado: inventario inicial informado; revisión actual no inspeccionó todo independientemente.
2. **Perfil del equipo** — recopilar hardware, sistema y API, distinguiendo declaraciones de mediciones. Estado: hardware declarado; driver/OpenGL/build pendientes.
3. **Definición del objetivo RPG** — acordar alcance y criterios sin crear contenido antes de autorización. Estado: pendiente.
4. **Inventario del pack RPG** — obtener manifiesto, versiones, loader y dependencias. Estado: bloqueada por falta de manifiesto/JARs.
5. **Comparativa de versiones/loaders** — documentar evidencia y límites. Estado: investigación inicial documentada; selección final pendiente.
6. **Auditoría de mods** — verificar builds, licencias, dependencias e interacciones. Estado: candidatos documentados; auditoría integral pendiente.
7. **Diseño de perfiles aislados** — preparar instancia limpia/base/alternativas con loaders separados. Estado: pendiente de autorización y manifiesto.
8. **Configuración inicial** — proponer ajustes y validar formato en instancia. Estado: propuestas no precargables; prueba pendiente.
9. **Pruebas de carga** — arranque, menú, mundo y logs incrementales. Estado: pendiente.
10. **Pruebas funcionales y compatibilidad** — validar sistemas RPG, progresión y conflictos. Estado: bloqueada por pack/manifiesto.
11. **Benchmark controlado** — medir escenarios reproducibles sin estimar resultados. Estado: pendiente; no hay mediciones.
12. **Decisiones y autorización** — presentar evidencia, riesgos y cambios al usuario. Estado: pendiente.
13. **Documentación y cierre** — conservar resultados, decisiones, changelog y tareas siguientes. Estado: documentación inicial actualizada; cierre final pendiente.

Las etapas se ejecutan una tras otra, no en paralelo. Una etapa documental no equivale a validación técnica.

## Tablero

| Pendientes | En desarrollo | Revisión | Bloqueadas | Completadas |
|---|---|---|---|---|
| Etapas 2 (verificación local), 3, 7, 8 (validación), 9, 11 y 12 | Ninguna | **Misión 1: investigación y documentación inicial corregida** (sin pruebas de Minecraft) | Etapa 4: falta manifiesto del pack; etapa 10: falta pack/manifiesto | Etapas 1 (inventario informado), 5 (comparativa documental inicial), 6 (candidatos/riesgos iniciales), 13 (documentación inicial; cierre no final) |

## Criterios de avance

- No confundir existencia de archivo/build con compatibilidad probada.
- Registrar `NO DATA` y la fuente que no devolvió datos.
- Conservar logs y método reproducible.
- Obtener autorización antes de cambiar mods o aceptar decisiones técnicas finales.
- No subir JARs de terceros.
- Mantener las ramas de prueba separadas y no modificar `main`.
- Orden de dependencias: manifiesto y requisitos → builds/dependencias/licencias → pruebas funcionales → benchmark; no medir un pack hipotético.
