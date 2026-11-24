# Hoja de ruta

## Metodología: 13 etapas

1. **Inventario del repositorio y fuentes** — identificar archivos reales y límites de acceso. Estado de inventario inicial documentado; 12 archivos existentes descritos en la revisión recibida.
2. **Perfil del equipo** — recoger hardware/sistema/API y distinguir declaraciones de mediciones. Hardware declarado; controlador/OpenGL/build pendiente.
3. **Definición del objetivo RPG** — acordar alcance y criterios sin diseñar contenido antes de autorización. Pendiente.
4. **Inventario del pack RPG** — conseguir manifiesto, versiones, loader y dependencias. Bloqueada por falta de manifiesto.
5. **Comparativa de versiones/loaders** — documentar evidencia y límites. Investigación inicial documentada; elección final pendiente del manifiesto y pruebas.
6. **Auditoría de mods** — verificar builds, licencias, dependencias e interacciones. Candidatos investigados; auditoría integral pendiente.
7. **Diseño de perfiles aislados** — instancia limpia, base y alternativas; loaders separados. Pendiente de aprobación y manifiesto.
8. **Configuración inicial** — proponer ajustes y validar formato en una instancia. Fragmento documentado; validación en juego pendiente.
9. **Pruebas de carga** — arranque/mundo/logs incrementales. Pendiente.
10. **Pruebas funcionales y compatibilidad** — contenido RPG/progresión/conflictos. Bloqueada por falta de pack/manifiesto.
11. **Benchmark controlado** — mediciones repetibles sin estimar resultados. Pendiente; no hay mediciones.
12. **Decisiones y autorización** — presentar evidencia, riesgos y cambios al usuario. Preferencias iniciales registradas; decisiones finales pendientes.
13. **Documentación y cierre** — conservar resultados, decisiones, changelog y siguientes tareas. Documentación inicial actualizada; cierre/mediciones pendientes.

## Tablero

| Pendientes | En desarrollo | Revisión | Bloqueadas | Completadas |
|---|---|---|---|---|
| Etapas 2 (verificación local), 3, 7, 8 (validación), 9, 11 y 12 (aprobación final) | Ninguna | **Misión 1: investigación y documentación inicial** (hallazgos revisados; aún no validación técnica) | Etapa 4: falta manifiesto RPG; etapa 10: falta pack/manifiesto | Etapa 1: inventario inicial documental; etapa 5: comparativa inicial documentada; etapa 6: candidatos y riesgos documentados; etapa 13: documentación inicial/changelog, no cierre final |

## Criterios de avance

- No tratar existencia de un archivo/build como compatibilidad probada.
- Registrar `NO DATA` junto con la fuente que no devolvió datos.
- Conservar logs originales y método reproducible.
- Obtener autorización antes de cambiar mods o adoptar decisiones técnicas finales.
- No subir archivos de mods de terceros.
- Secuenciar las acciones, no ejecutarlas en paralelo.
- Orden de dependencias: manifiesto y requisitos → verificar builds/dependencias/licencias → prueba funcional → benchmark; no medir con pack hipotético.
