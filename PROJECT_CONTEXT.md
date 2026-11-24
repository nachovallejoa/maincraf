# Contexto del proyecto

> **Misión 1 — investigación inicial. Estado: revisión.** Paquete corregido recibido el 2026-11-24. La documentación no implica inspección ni ejecución independiente de Minecraft. No modificar la rama principal.

## Objetivo y filosofía

Documentar una base técnica para evaluar Minecraft con contenido RPG y optimización en el equipo declarado, manteniendo trazabilidad entre fuentes, builds, propuestas, decisiones autorizadas y datos pendientes. No completar vacíos con estimaciones. No crear contenido RPG técnico fuera del alcance autorizado. Las decisiones narrativas aprobadas se conservan; las mecánicas no deben alterarlas.

## Hardware declarado y no verificado independientemente

El usuario comunicó para esta revisión que tiene **10 GB de RAM disponibles** y que el sistema operativo usa **500 MB**. Es información declarada por el usuario, no una medición o verificación independiente. Sistema operativo, configuración completa, RAM física total y benchmarks siguen pendientes. La información anterior del perfil no se sustituye por una inferencia sobre el total instalado.

## Autonomía controlada y autorización

- Se permite investigar, documentar y proponer; una propuesta no es decisión aprobada.
- El usuario pidió dejar de recibir cuestionarios, que el asistente tome decisiones creativas usando prioridades ya expresadas y que mantenga en secreto el contenido narrativo futuro para que pueda descubrirlo al jugar. Evitar spoilers en futuras comunicaciones; no divulgar giros o contenido sorpresa.
- La solicitud de tener el modpack hecho en la próxima interacción expresa una expectativa, no certifica que el pack esté construido ni elimina verificaciones de instancia, mods, licencias o dependencias.
- No instalar, retirar, sustituir, modificar ni redistribuir mods sin autorización expresa y revisión de archivo, loader, compatibilidad y licencia. No inventar manifiestos, dependencias, métricas ni resultados.
- Mantener ramas aisladas; no escribir en `main`, no fusionar ni iniciar etapa nueva por defecto.
- No subir JARs ni binarios de mods de terceros.

## Equipo y responsabilidades

- **Director del proyecto:** coordina alcance, trazabilidad y aprobaciones.
- **Diseñador RPG:** recopila requisitos; no diseña contenido sin autorización de etapa.
- **Guionista:** registra definiciones narrativas autorizadas; preservar confidencialidad y no crear lore por iniciativa ajena al alcance vigente.
- **Programador Java:** revisa requisitos técnicos/dependencias; no programa mods sin autorización.
- **Especialista Minecraft:** documenta versiones, loaders y datos de instalación pendientes.
- **Optimizador:** define mediciones; no declara rendimiento sin pruebas.
- **Auditor de mods:** registra versiones, licencias, dependencias y riesgos como candidatos, no aprobados.
- **Tester:** prepara pruebas reproducibles; no ejecuta juego ni benchmarks aquí.

## Decisiones de la etapa de Mecánicas

El usuario respondió: «apruebo todo, pero quiero que dejes de hacerme cuestionarios y hagas vos la historia, no quiero saber yo lo que va a tener el modpack, quiero vivirlo sin saberlo e ir descubriendo cosas asi que toma decisiones por vos mismo, ya sabes mis prioridades. mi pc tiene 10gb de ram disponibles y el sistema operativo usa 500mb nada mas. todo lo demas hacelo vos, procesa todo lo necesario. quiero que la proxima vez tengas el modpack hecho ya».

Registro conservador de las preguntas del cuestionario único:

1. **Diseño general revisado — aprobado** por «apruebo todo», respetando pendientes y límites indicados.
2. **Clases — aprobadas** las tres propuestas: Guardacorriente, Vigía del Prisma y Rompeanclas.
3. **Árboles/builds — aprobado** el esquema de tres ramas y cinco nodos, coste de 3 puntos como parámetro inicial de prueba; no es balance validado.
4. **Niveles/estadísticas — aprobada como base de pruebas** la propuesta nivel 30, curva, 15 puntos de atributo y 29 de habilidad; efectos cuantificados siguen pendientes.
5. **Equipo/rareza — aprobadas** cuatro rarezas y recompensas fijas, sin ranuras adicionales por ahora.
6. **Combate — aprobado** el enfoque de señales legibles, grupos compactos y respuestas viables para todas las clases.
7. **Jefes — aprobados como propuestas sujetas a pruebas** los seis encuentros nombrados en `GAME_DESIGN.md`.
8. **Reputación — aprobadas** las cuatro facciones y escala propuesta −2 a +2, sin que reputación decida rutas/finales por sí sola.
9. **Candidatos de mods RPG — sin selección individual registrada.** «Apruebo todo» no identifica opciones de auditoría, retiros o adiciones de la pregunta 9. Ningún candidato se marca como aceptado, quitado o añadido por decisión del usuario; siguen candidatos sin verificación.
10. **Módulos propios — sin clasificación individual registrada.** La pregunta 10 requería aprobar/aplazar/descartar cada módulo. La respuesta general no especificó estados por módulo. Todos permanecen sin clasificación explícita en `ARCHITECTURE.md`.
11. **Desarrollo de mods propios — no autorizado explícitamente.** No hubo respuesta específica a la pregunta 11. El pedido de procesar todo y tener el modpack hecho no se convierte en autorización inequívoca para iniciar una etapa nueva.

**Decisiones aplazadas o no determinadas:** clasificación de cada módulo propio; selección individual de mods candidatos; valores/balance y pruebas; compatibilidad, versiones, APIs, licencias, configuración y rendimiento. No se registran como aprobados ni rechazados los puntos no contestados de forma específica.

La petición de tomar decisiones creativas se registra como preferencia para la dirección narrativa futura, sin revelar al usuario las sorpresas. No cambia por sí sola el estado formal de aprobaciones técnicas ni altera la historia independiente ya aprobada.

## Decisiones de la etapa de Mecánicas

Las decisiones detalladas de aprobación de mecánicas, clasificación pendiente de candidatos, estado de autorización y contexto de hardware están registradas arriba. El diseño sigue aislado en `etapa-5-mecanicas`; no iniciar ni fusionar otra etapa por defecto.
