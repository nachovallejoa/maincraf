# Contexto del proyecto

> Misión 1 — investigación inicial. Estado: revisión. Paquete corregido recibido el 2026-11-24. La documentación no implica inspección ni ejecución independiente de Minecraft. No modificar la rama principal.

## Objetivo y filosofía

Documentar una base técnica para evaluar Minecraft con contenido RPG y optimización en el equipo declarado, manteniendo trazabilidad entre fuentes, builds, propuestas, decisiones autorizadas y datos pendientes. No completar vacíos con estimaciones. No crear contenido RPG técnico fuera del alcance autorizado. Las decisiones narrativas aprobadas se conservan; las mecánicas no deben alterarlas.

## Hardware declarado y no verificado independientemente

El usuario comunicó para esta revisión que tiene **12 GB de RAM instalados**, con **unos 10 GB disponibles**, y que **Windows usa unos 500 MB**. Es información declarada por el usuario, no una medición o verificación independiente. Sistema operativo, configuración completa, RAM física total y benchmarks siguen pendientes.

## Modo autónomo

El usuario aprobó todo, delegó todas las decisiones al equipo y no quiere cuestionarios ni conocer el contenido del modpack. El equipo debe tomar las decisiones necesarias, mantener en secreto las sorpresas narrativas y entregar el modpack para que el usuario lo descubra jugando. Esta autonomía no permite inventar datos de compatibilidad, dependencias, licencias, resultados de pruebas o mediciones. No instalar, retirar, sustituir, modificar ni redistribuir archivos de mods de terceros; tampoco subir sus JARs al repositorio.

## Límites y responsabilidades

- Mantener ramas aisladas; no escribir en `main` ni alterar ramas de etapas anteriores.
- No declarar una compilación, prueba de lanzamiento o compatibilidad efectiva sin evidencia.
- Registrar `NO DATA`, `INCOMPLETE` y `[SIN VERIFICAR]` como pendientes indicando qué fuente no proporcionó los datos.
- No subir JARs de terceros. Los artefactos solo pueden descargarse desde sus fuentes autorizadas durante el build.
- La versión exacta de Fabric Loader para el paquete queda pendiente; el manifiesto mantiene `null` y la instancia no se declara validada.

## Registro conservador de decisiones previas

Las propuestas de historia y mecánicas aprobadas se mantienen según los documentos de diseño existentes. La selección RPG opcional y los módulos propios planificados continúan sujetos a revisión técnica. La revisión no los declara incompatibles ni autoriza por sí sola implementación de código propio.

## Decisiones de la etapa de modpack

Minecraft 1.20.1 se conserva como base. La selección mínima incluye Sodium, Lithium, FerriteCore y ModernFix, según los IDs y archivos de versión de Modrinth proporcionados en los hallazgos. No se agrega Fabric API porque las respuestas consultadas no declaran dependencias obligatorias para las versiones seleccionadas. Sodium es solo cliente y los otros tres mods funcionan en cliente y servidor.

La configuración permanece por defecto, sin overrides. El heap máximo sugerido `-Xmx6G` es solo un punto de partida condicionado a la memoria disponible; no constituye medición del consumo del pack. No se añaden `-Xms` ni argumentos de GC adicionales. La compilación del `.mrpack` queda pendiente de fijar Fabric Loader: el script debe detenerse expresamente si el valor continúa en `null`.

Los módulos propios planificados son núcleo de campaña y persistencia; clases, atributos, niveles y builds; decisiones, facciones y accesos; encuentros y jefes; rarezas, recompensas y equipo; adaptador opcional de misiones. No hay código entregado, autorización explícita documentada para implementarlo ni proyecto Gradle que permita afirmar que compile.

Los candidatos RPG y opcionales de rendimiento no incluidos quedan fuera por auditoría insuficiente, no por incompatibilidad demostrada.
