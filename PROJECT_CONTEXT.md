# Contexto del proyecto

> **Misión 1 — investigación inicial. Estado: revisión.** Este documento registra el paquete corregido recibido el 2026-11-24. No se inspeccionó Minecraft ni se ejecutaron pruebas durante esta misión. No se modificará la rama principal.

## Objetivo y filosofía

Documentar una base técnica para evaluar Minecraft con contenido RPG y optimización en el equipo declarado, sin sacrificar mods requeridos. Mantener trazabilidad de fuentes/versiones y separar hechos comprobados, propuestas, decisiones autorizadas y datos pendientes. No crear contenido RPG en esta etapa. Las secciones sin datos se mantienen expresamente pendientes, sin estimaciones inventadas.

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
- No instalar, retirar, sustituir ni redistribuir mods sin autorización expresa y revisión de archivo, loader, compatibilidad y licencia.
- No inventar manifiestos, dependencias, métricas ni resultados. Registrar `NO DATA` junto a la fuente que no entregó el dato.
- No ejecutar benchmarks ficticios ni extrapolar FPS de otros equipos.
- Mantener ramas y perfiles aislados; no escribir en `main` ni sobrescribir trabajo ajeno.
- Nunca subir JARs u otros archivos de mods de terceros.
- La investigación recibida prescribe ejecución secuencial de pasos, no paralela.
- La licencia de un mod no garantiza por sí sola permiso de redistribución.

## Equipo y responsabilidades

- **Director del proyecto:** coordina alcance, trazabilidad y aprobaciones.
- **Diseñador RPG:** identifica requisitos pendientes; no diseña contenido en esta misión.
- **Guionista:** registra definiciones narrativas faltantes; no crea lore ni trama.
- **Programador Java:** revisa requisitos técnicos; no programa mods.
- **Especialista Minecraft:** documenta versiones/loaders y pendientes de instalación.
- **Optimizador:** prepara criterios de medición; no afirma rendimiento sin pruebas.
- **Auditor de mods:** registra versiones, licencias, dependencias y riesgos como candidatos.
- **Tester:** define pruebas reproducibles; no ejecuta juego ni benchmarks aquí.
- **Revisor independiente:** comprueba evidencia, límites y estado de aprobación.

No se requiere equipo adicional para esta investigación inicial según la información disponible.

## Decisiones/propuestas registradas

No hay decisiones técnicas finales aprobadas. Propuestas pendientes:

1. Evaluar primero Minecraft 1.20.1 + Fabric por la evidencia documental más directa, sujeto al manifiesto del pack y autorización.
2. Considerar Forge 1.20.1 solo si el manifiesto lo exige; Embeddium aparece publicado para Forge/NeoForge, sin demostrar compatibilidad local.
3. No afirmar rendimiento hasta ejecutar pruebas reproducibles en el equipo.
4. Mantener ModernFix Dynamic Resources en `false` hasta auditar el pack.
5. No precargar Sodium JSON ni fragmento vanilla `options.txt` como configuración probada; el esquema/valores exactos no quedaron verificados para el propósito.
6. Mantener candidatos condicionales fuera de la base hasta identificar necesidad y obtener autorización.
7. No redistribuir archivos binarios sin revisar términos y método de distribución.

## Decisiones y datos pendientes

- Modpack RPG exacto, manifiesto, loader y versión.
- Lista real de JARs y hashes (sin subir los JARs).
- Java Runtime, launcher, Windows/build, controlador Radeon y OpenGL local.
- Requisitos RPG imprescindibles y autorización para probar en instancia de respaldo.
- Autorización de benchmarks y cambios visuales.
- Política de uso privado/redistribución y revisión de licencias.
- Aprobación o rechazo de la base técnica propuesta.

## Estado del repositorio

Según el inventario aportado (no reinspección integral): `main` es la rama por defecto; la documentación de investigación vive en `mision-1-investigacion`. README no se encontró en el inventario descrito. No se registra fusión. La presente actualización se realiza exclusivamente en `mision-1-investigacion`.
