# Hoja de ruta

## Metodología: 13 etapas

1. **Inventario del repositorio y fuentes** — identificar archivos reales y límites de acceso. Estado: completada para la revisión inicial; 0 archivos de proyecto revisados porque el árbol estaba vacío.
2. **Perfil del equipo** — recoger hardware, sistema, driver y APIs gráficas; separar declaraciones de mediciones. Estado: en revisión, hardware declarado y datos de driver/API pendientes.
3. **Definición del objetivo RPG** — acordar estilo, contenido y criterios de éxito sin diseñar contenido antes de autorización. Estado: pendiente.
4. **Inventario del pack RPG** — obtener manifiesto exacto, versiones, dependencias y loader. Estado: bloqueada por falta de manifiesto.
5. **Comparativa de Minecraft y loaders** — comparar opciones con fuentes y distinguir disponibilidad de rendimiento medido. Estado: en revisión (primera misión).
6. **Auditoría de mods** — validar archivos, licencia, dependencias, incompatibilidades y clasificación con evidencia. Estado: en revisión (primera misión; candidatos, no instalados).
7. **Diseño de perfiles aislados** — establecer instancia limpia, base mínima y alternativa exigida por el pack; no mezclar loaders. Estado: pendiente de aprobación.
8. **Configuración inicial** — fusionar opciones por versión sin sobrescribir archivos completos y verificar esquemas. Estado: en revisión; fragmentos propuestos, no instalados.
9. **Pruebas de carga** — verificar arranque, carga del mundo y logs en etapas incrementales. Estado: pendiente.
10. **Pruebas funcionales/compatibilidad** — probar funciones RPG, progresión y conflictos. Estado: bloqueada por falta del pack/manifiesto.
11. **Benchmark controlado** — medir limpio, base optimizada, grupos incrementales y pack final, sin estimar resultados. Estado: pendiente; no hay mediciones.
12. **Decisiones y autorización** — presentar evidencia, riesgos y cambios para aprobación explícita. Estado: pendiente.
13. **Documentación y cierre de misión** — conservar resultados, decisiones, changelog y tareas siguientes. Estado: en revisión (primera misión).

## Tablero

| Pendientes | En desarrollo | Revisión | Bloqueadas | Completadas |
|---|---|---|---|---|
| Etapas 3, 7, 9, 11, 12 | — | **Primera misión: investigación y documentación inicial** (etapas 1, 5, 6, 8, 13) | Etapa 4: manifiesto RPG; etapa 10: pack no identificado | — |

## Criterios de avance

- Ningún candidato se trata como instalado ni compatible por mera existencia de un archivo.
- Registrar `NO DATA` con la fuente que no proporcionó datos.
- Mantener pruebas reproducibles y guardar logs originales.
- Obtener autorización antes de cambios en mods o decisiones técnicas finales.
- No subir archivos de mods de terceros.
