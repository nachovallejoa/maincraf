# Decisiones técnicas — modpack final

## Decisiones del director y motivos

| Decisión | Motivo | Límite/estado |
|---|---|---|
| Mantener La Marea de los Mil Soles en Minecraft 1.20.1 y Fabric Loader `0.20.1` | La revisión recibida confirma que `0.20.1` es la entrada estable más reciente de Fabric Meta para Minecraft 1.20.1. | Valor exacto conservado como texto. No se afirma que el paquete haya sido instalado o probado. |
| Limitar el manifiesto a Sodium y BadOptimizations | Los hallazgos identifican sus IDs Modrinth (`OihdIimA`, `DIugITgU`), versiones, compatibilidad 1.20.1/Fabric y lado cliente. | No añadir candidatos restantes sin la verificación suficiente de metadatos, dependencias y compatibilidad. |
| Mantener ambos mods como solo cliente | Las fuentes consultadas los describen como mods de cliente; no constituyen una selección de servidor. | `env: client` en el manifiesto. |
| No incluir Indium ni Iris | Sodium declara dependencias condicionales para esos mods y no están incluidos aquí; la revisión no afirma que sean requisitos obligatorios para esta selección. | No agregar dependencias supuestas. |
| No subir archivos JAR de terceros | El paquete debe obtener esos artefactos de sus fuentes autorizadas en la instalación/build. | No almacenar ni redistribuir binarios de terceros en el repositorio. |
| Añadir `options.txt` con valores orientados a rendimiento | Las claves corresponden al formato de Minecraft 1.20.1 y son una propuesta razonada. | No es benchmark ni garantiza mejora; el usuario puede ajustar valores. |
| No añadir configuración de mods | Sodium recomienda no editar manualmente `sodium-options.json`; la configuración de BadOptimizations no se verificó para la versión exacta. | No inventar contenido por defecto ni archivos parciales. |
| Dejar argumentos JVM avanzados sin cambios; considerar `-Xmx5G` solo como referencia condicional | Hardware declarado: 12 GB instalados, unos 10 GB disponibles y Windows usando unos 500 MB; no hay medición independiente ni prueba del perfil. | No añadir `-Xms` ni banderas de GC. No presentar el heap como resultado medido. |
| No implementar mods propios en esta entrega | No se recibieron archivos de código; la entrada indica que la implementación no está autorizada/establecida y no fija Fabric API. | No inventar código, proyecto Gradle ni APIs. No se afirma compilación. |
| Documentar pruebas como pendientes | No se ha confirmado ejecución del workflow, compilación, inicio del juego ni mediciones. | La build en GitHub y la prueba real de juego siguen pendientes. |

## Pendientes de verificación

- La consulta no aportó metadatos y dependencias obligatorias suficientes para Lithium, FerriteCore, ModernFix, Sodium Extra, ImmediatelyFast, Simply Skills y Better Combat.
- La identificación/verificación de FTB Quests y del Remnants propuesto no quedó resuelta en los resultados disponibles.
- Los demás candidatos descartados no tienen en esta revisión metadatos completos; su exclusión no significa incompatibilidad.
- No se proporcionaron licencias confirmadas para los dos mods incluidos; consultar las páginas/proyectos oficiales antes de redistribución cuando corresponda.
- No hay resultado de compilación GitHub ni prueba de inicio, juego o rendimiento.
