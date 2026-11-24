# Contexto del proyecto

> **Misión 1 — investigación inicial. Estado: revisión.** Paquete corregido recibido el 2026-11-24. Esta actualización documental no implica inspección ni ejecución independiente de Minecraft. No modificar la rama principal.

## Objetivo y filosofía

Documentar una base técnica para evaluar Minecraft con contenido RPG y optimización en el equipo declarado, sin sacrificar mods requeridos. Mantener trazabilidad entre fuentes, builds, propuestas, decisiones autorizadas y datos pendientes. Separar hechos comprobados documentalmente, propuestas, decisiones aprobadas y pendientes. Las secciones sin datos deben indicar la fuente que no los proporcionó; no completar huecos con estimaciones. No crear contenido RPG en esta etapa.

## Hardware declarado (no verificado independientemente)

| Componente | Dato recibido | Estado |
|---|---|---|
| CPU | AMD Athlon 5150 | No verificado |
| Gráficos | Radeon R3 integrada | Controlador, API y OpenGL local pendientes |
| RAM | 12 GB instalados; ~9,9 GB utilizables declarados | No verificado |
| Almacenamiento | HDD | No verificado |
| Sistema | Windows, versión/build no indicada | Pendiente |
| Resolución | 1280×720 declarada | No verificada |
| Java/launcher | Sin datos | Pendiente |

## Autonomía controlada y autorización

- Se permite investigar, documentar y proponer; una propuesta no es decisión aprobada.
- No instalar, retirar, sustituir, modificar ni redistribuir mods sin autorización expresa y revisión del archivo, loader, compatibilidad y licencia.
- No inventar manifiestos, dependencias, métricas ni resultados; registrar `NO DATA` y la fuente que no entregó los datos.
- No ejecutar benchmarks ficticios ni extrapolar FPS de otros equipos.
- Mantener ramas/perfiles aislados: no escribir en `main`, no sobrescribir trabajo ajeno y no fusionar sin autorización.
- Nunca subir JARs ni otros archivos binarios de mods de terceros.
- El flujo de esta misión se ejecuta secuencialmente, no en paralelo.
- La licencia de un mod no implica por sí sola permiso universal de redistribución.

## Equipo y responsabilidades

- **Director del proyecto:** coordina alcance, trazabilidad y aprobaciones.
- **Diseñador RPG:** recopila requisitos pendientes; no diseña contenido RPG en esta misión.
- **Guionista:** registra definiciones narrativas pendientes; no crea lore ni trama.
- **Programador Java:** revisa requisitos técnicos/dependencias; no programa mods.
- **Especialista Minecraft:** documenta versiones, loaders y datos de instalación pendientes.
- **Optimizador:** define mediciones; no declara rendimiento sin pruebas.
- **Auditor de mods:** registra versiones, licencias, dependencias y riesgos como candidatos, no como aprobados.
- **Tester:** prepara pruebas reproducibles; no ejecuta juego ni benchmarks aquí.
- **Revisor independiente:** contrasta evidencia, límites y estados de aprobación.
- **Especialistas adicionales:** no se identifican como necesarios ahora.

## Estado documental y propuestas

La rama de misión contiene la documentación de investigación. Según el inventario recibido, el manifiesto y los JARs no se encontraron; las listas de mods son candidatas documentales y hay discrepancias de versiones por resolver. `README` no aparece en las estructuras consultadas y su lectura devolvió 404; no se inventa ni se crea su contenido. La descripción del inventario no equivale a verificación independiente de esos archivos.

**Ninguna decisión técnica final está aprobada.** Candidata principal: Minecraft 1.20.1 + Fabric, condicionada al manifiesto, driver y pruebas. Forge 1.20.1 es alternativa solo si el manifiesto lo exige. No hay instalación ni configuración probada. ModernFix `dynamic_resources=false` es un override documental propuesto; Lithium puede quedarse sin overrides. No precargar `options.txt` ni JSON de Sodium sin esquema verificado. No hay benchmarks; las tablas permanecen vacías.

La revisión recibida confirma documentalmente ciertos metadatos de candidatos (incluidos Sodium 0.5.13, Lithium 0.11.4, ImmediatelyFast 1.2.21 y Entity Culling 1.12.1-1.20.1), con los límites y licencias anotados en `MOD_AUDIT.md`. Otras versiones exactas siguen marcadas sin verificar. Entity Culling tiene licencia personalizada: no redistribuir su JAR fuera de los términos aplicables. No subir binarios de mods.

## Decisiones pendientes

- Obtener/seleccionar manifiesto RPG y JARs exactos; resolver discrepancias de versiones y loader mediante dependencias reales.
- Confirmar launcher, Java local y arquitectura, Windows/build, driver Radeon y APIs gráficas expuestas.
- Aprobar candidatos para instancia aislada y política/plataforma de distribución; revisar licencia por archivo.
- Ejecutar pruebas funcionales y benchmarks reproducibles con autorización; conservar logs, capturas y hashes locales, sin subir JARs.
- Aprobar/rechazar la base técnica tras revisar la evidencia.
- README: pendiente; fuente consultada devolvió 404.
- Benchmarks y compatibilidad local: pendientes; no se entregaron resultados.

No se ha descrito fusión a `main`; esta actualización pertenece exclusivamente a `mision-1-investigacion`.