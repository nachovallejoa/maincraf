# Contexto del proyecto

> **Misión 1 — investigación inicial. Estado: revisión.** Paquete corregido recibido el 2026-11-24. Esta actualización documental no implica inspección ni ejecución independiente de Minecraft. No modificar la rama principal.

## Objetivo y filosofía

Documentar una base técnica para evaluar Minecraft con contenido RPG y optimización en el equipo declarado, sin sacrificar mods requeridos. Mantener trazabilidad entre fuentes, builds, propuestas, decisiones autorizadas y datos pendientes. Separar hechos comprobados documentalmente, propuestas, decisiones aprobadas y pendientes. Las secciones sin datos deben indicar la fuente que no los proporcionó; no completar huecos con estimaciones. No crear contenido RPG técnico fuera del alcance autorizado.

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
- No inventar manifiestos, dependencias, métricas ni resultados; registrar «NO DATA» y la fuente que no entregó los datos.
- No ejecutar benchmarks ficticios ni extrapolar FPS de otros equipos.
- Mantener ramas/perfiles aislados: no escribir en `main`, no sobrescribir trabajo ajeno y no fusionar sin autorización.
- Nunca subir JARs ni otros binarios de mods de terceros.
- El flujo de etapas se ejecuta secuencialmente; una autorización no implica fusionar ramas ni iniciar automáticamente otra etapa.
- La licencia de un mod no implica por sí sola permiso universal de redistribución.

## Equipo y responsabilidades

- **Director del proyecto:** coordina alcance, trazabilidad y aprobaciones.
- **Diseñador RPG:** recopila requisitos pendientes; no diseña contenido RPG sin autorización de etapa.
- **Guionista:** registra definiciones narrativas autorizadas; no crea lore/trama por iniciativa propia.
- **Programador Java:** revisa requisitos técnicos/dependencias; no programa mods.
- **Especialista Minecraft:** documenta versiones, loaders y datos de instalación pendientes.
- **Optimizador:** define mediciones; no declara rendimiento sin pruebas.
- **Auditor de mods:** registra versiones, licencias, dependencias y riesgos como candidatos, no como aprobados.
- **Tester:** prepara pruebas reproducibles; no ejecuta juego ni benchmarks aquí.
- **Revisor independiente:** contrasta evidencia, límites y estados de aprobación.
- **Especialistas adicionales:** no se identifican como necesarios ahora.

## Estado documental y propuestas

La rama de misión contiene documentación de investigación. Según el inventario recibido, el manifiesto y los JARs no se encontraron; las listas de mods son candidaturas documentales y hay discrepancias de versiones por resolver. `README` no aparece en las estructuras consultadas y su lectura devolvió 404; no se inventa ni crea su contenido en esta entrada.

**Ninguna decisión técnica final está aprobada.** Candidata principal técnica: Minecraft 1.20.1 + Fabric, condicionada al manifiesto, driver y pruebas. Forge 1.20.1 es alternativa solo si el manifiesto lo exige. No hay instalación ni configuración probada.

La revisión recibida confirma documentalmente ciertos metadatos de candidatos (incluidos Sodium 0.5.13, Lithium 0.11.4, ImmediatelyFast 1.2.21 y Entity Culling 1.12.1-1.20.1), con límites y licencias anotados en `MOD_AUDIT.md`. Otras versiones exactas siguen marcadas sin verificar. Entity Culling tiene licencia personalizada: no redistribuir su JAR fuera de los términos aplicables. No subir binarios.

## Decisiones de la etapa de identidad RPG

Respuestas expresas del usuario al cuestionario, registradas en la rama etapa 3. La identidad se registra como preferencia narrativa/RPG; no desarrolla la historia completa ni aprueba técnicamente mods.

1. **Propuesta elegida — D, mezcla:** La Marea de los Mil Soles como base (B) con mods candidatos de B y A. No es lista de mods aprobada ni instalada.
2. **Tono — B y D:** misterio y aventura, tono más oscuro y peligroso.
3. **Enfoque principal — A y B:** combate y exploración.
4. **Progresión/clases — B, C y D:** árboles/builds, niveles y estadísticas como ejes; clases definidas.
5. **Dificultad — B:** equilibrada, reto moderado en combate y supervivencia.
6. **Autorización — A:** autorizó desarrollar la historia completa de la propuesta elegida en la etapa de Historia. Esa autorización queda registrada; no iniciaba por sí misma esa etapa.

**Decisiones aplazadas:** ninguna marcada `después`. Los detalles concretos de historia, mundo y reglas quedaron para desarrollo; verificación de mods, versiones, dependencias, licencias, compatibilidad y rendimiento no forma parte de ese cuestionario y sigue pendiente.

## Decisiones de la etapa de Historia

Respuestas expresas del usuario al cuestionario de aprobación y ajustes. La historia general quedó aprobada tal como estaba; no se solicitaron cambios narrativos. Las elecciones registradas son decisiones sobre la historia, no confirmaciones técnicas ni implementación.

1. **Aprobación general — 1A:** aprueba la historia general como base del proyecto, tal como está.
2. **Almirante Veyr — 2A:** mantenerlo como antagonista trágico convencido de que sacrificar recuerdos evitará más catástrofes.
3. **Facciones y personajes — 3A:** mantenerlos como están.
4. **Desenlaces — 4A:** mantener los cuatro; el pactado es una opción más exigente, no un final perfecto.
5. **Jefes — 5A:** mantener los seis propuestos.
6. **Misiones secundarias — 6B:** peso medio; algunas desbloquean rutas, recursos, testimonios o apoyos para el final.
7. **Etapa de Mecánicas — 7A:** autorizó avanzar con clases, niveles, estadísticas, habilidades/builds, combate y progresión como propuestas de diseño. Esta autorización habilita el diseño de la etapa, pero no implica compatibilidad con mods, implementación, fusión de ramas ni inicio automático de una etapa nueva.

**Decisiones aplazadas:** ninguna pregunta se dejó pendiente explícitamente. Los datos técnicos no verificados (perfil, mods, compatibilidad, implementación y rendimiento) continúan en estado pendiente; no se convierten en aprobaciones por la aprobación de la historia.
