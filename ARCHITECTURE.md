# Arquitectura

> **Estado:** propuesta documental. Sin código ni integración externa confirmada. El usuario aprobó el diseño revisado de mecánicas y expresó que quiere que el asistente asuma decisiones creativas sin cuestionarios y mantenga la historia futura sin spoilers. Esto no equivale a autorización explícita para iniciar la etapa de Desarrollo de mods propios. Versiones, APIs, compatibilidad, licencias e instancia permanecen por verificar.

## Límites generales

Se propone un único mod propio modular, con responsabilidades separadas y fuente de estado coherente. Evitar estado duplicado entre módulos y sistemas externos. Regiones compactas y transiciones controladas; no incorporar binarios/JAR de terceros al repositorio.

## Mods propios candidatos y estado de decisión

La expresión general «apruebo todo» aplica claramente a las propuestas del cuestionario de mecánicas. En la pregunta 10 se exigía clasificar cada módulo como Aprobar/Aplazar/Descartar; el usuario no dio esas clasificaciones. Por fidelidad, **ningún módulo individual se marca como aprobado, aplazado ni descartado**. Quedan sin clasificación explícita y no autorizan implementación.

1. **Núcleo de campaña y persistencia — sin clasificación explícita.** Propuesta: estado de campaña, guardado/recuperación, migraciones e IDs antirrepetición.
2. **Clases, atributos, niveles y builds — sin clasificación explícita.** Propuesta: clases opcionales, curva XP, puntos y habilidades; evitar bloquear contenido principal.
3. **Decisiones, facciones y accesos — sin clasificación explícita.** Propuesta: estados narrativos, reputación, pruebas, rutas, misiones y condiciones de finales; sin requisito de reputación única.
4. **Encuentros y seis jefes — sin clasificación explícita.** Propuesta de mayor coste: fases, señales, límites de enemigos y resultados narrativos.
5. **Rarezas, recompensas y equipo — sin clasificación explícita.** Propuesta: objetos de campaña y recompensas fijas.
6. **Adaptador opcional de misiones — sin clasificación explícita.** Solo si luego se selecciona y verifica un sistema externo.

## Autonomía creativa y experiencia sin spoilers

El usuario pidió que no se le formulen más cuestionarios, que el asistente tome decisiones creativas usando sus prioridades ya expresadas y que no se le revele por adelantado qué descubrirá en el modpack. En el trabajo narrativo futuro, preservar la historia aprobada existente y comunicar progreso sin revelar giros, escenas o sorpresas. Este pedido no determina estados técnicos ni permite inventar respuestas a decisiones explícitas por módulo. La solicitud de que el modpack esté hecho en la próxima interacción es una expectativa del usuario, no una garantía de que pueda completarse sin acceso a la instancia, dependencias y verificaciones.

## Criterios técnicos previos a implementar

Confirmar instancia, versión y loader; comprobar dependencias y licencias; diseñar persistencia y migraciones; probar que clase/nivel/reputación/secundarias no bloquean historia; prevenir recompensas duplicadas y estados contradictorios; validar campaña sin farmeo con presupuesto XP; limitar entidades y actividad de arenas; medir en el hardware objetivo. Hardware comunicado por el usuario: 10 GB RAM disponibles, sistema operativo usa 500 MB (sin verificación independiente). No se dispone de SO, configuración completa ni benchmarks.
