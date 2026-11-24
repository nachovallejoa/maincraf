# Hoja de ruta

## Metodología: 13 etapas secuenciales

1. **Inventario del repositorio y fuentes** — Registrar archivos reales y límites de acceso. Estado: inventario recibido; revisiones documentales no equivalen a inspección independiente completa.
2. **Perfil del equipo** — Hardware/sistema/APIs y separar declaraciones de mediciones. Estado: usuario declara 12 GB instalados, unos 10 GB disponibles y Windows usa unos 500 MB; mediciones independientes pendientes.
3. **Definición del objetivo RPG** — Alcance y criterios. Estado: identidad/pilares registrados; autorización narrativa previa.
4. **Inventario del pack RPG** — Manifiesto, versiones, loader/dependencias. Estado: selección mínima documentada; Loader exacto, licencias y validación pendientes.
5. **Comparativa de versiones/loaders** — Evidencia y límites. Estado: documentación de Minecraft 1.20.1/Fabric seleccionada para esta entrega; Loader no fijado.
6. **Auditoría de mods** — Builds/licencias/dependencias/interacciones. Estado: cuatro mods base verificados según revisión; auditoría de licencias y prueba conjunta pendientes. Candidatos opcionales/RPG excluidos por falta de auditoría suficiente.
7. **Historia** — Propuesta narrativa y consecuencias. Estado: historia registrada como aprobada en etapa previa; preservar sin spoilers.
8. **Mecánicas** — Clases, niveles/estadísticas, habilidades/builds, equipo, combate, jefes, reputación, progresión y misiones. Estado: diseño aprobado como propuesta; implementación y verificación técnica pendientes.
9. **Configuración inicial** — Ajustes y validación en instancia. Estado: pendiente; no se añaden overrides ni configuraciones no verificadas.
10. **Pruebas de carga** — Arranque, menú, mundo/logs incrementales. Estado: pendiente.
11. **Pruebas funcionales y compatibilidad** — Progresión, contenido y conflictos. Estado: pendiente.
12. **Benchmark controlado** — Escenarios reproducibles. Estado: pendiente; no hay mediciones.
13. **Decisiones y documentación de cierre** — Evidencia, riesgos y cambios. Estado: pendiente.

Las etapas son secuenciales; la documentación no equivale a validación técnica.

## Tablero de la entrega del modpack

| Área | Estado | Criterio / pendiente |
|---|---|---|
| Selección y manifiesto base | Completada documentalmente | Cuatro versiones y archivos de Modrinth registrados; sin JARs de terceros en el repositorio. |
| Integración | En revisión | Revisar rama, workflow, script e índice generado; `fabric_loader_version` sigue `null`. |
| Entrega | En revisión | Instrucciones añadidas, pero no declarar paquete listo hasta tener compilación exitosa con Loader exacto. |
| Pruebas | Pendiente | Build en GitHub tras fijar Loader y luego que el usuario importe, lance y juegue; registrar logs/resultado. |
| Configuración | Pendiente | Mantener valores predeterminados hasta fuente completa y prueba específica. |
| Rendimiento | Pendiente | Sin medición local; `-Xmx6G` es solo orientación condicionada, no benchmark. |

## Seguimiento posterior

Los módulos propios planificados permanecen sin código y sin proyecto Gradle recibido; no afirmar compilación. Candidatos RPG fuera de selección hasta completar auditoría de versión, dependencias, licencia e interacciones.

## Registro de estado y confidencialidad

El usuario aprobó el modo autónomo: evitar cuestionarios y decisiones creativas innecesarias, y preservar sorpresas narrativas al comunicar avances. Esta preferencia no elimina verificación técnica, licencias o pruebas. No subir ni redistribuir JARs de terceros.
