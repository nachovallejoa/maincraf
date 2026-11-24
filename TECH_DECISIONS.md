# Decisiones técnicas: propuestas pendientes

> No hay decisiones finales aprobadas en la misión 1. La tabla conserva comparación de alto nivel recibida; disponibilidad de mods no constituye benchmark ni compatibilidad con el equipo.

## Comparativa de versiones y loaders

| Minecraft + loader | Java orientativa | Optimización citada | Contexto RPG citado | Evaluación / estado |
|---|---|---|---|---|
| 1.19.2 + Fabric | Java 17 (Fabric recomienda para 1.17–1.20.4) | Sodium/Lithium disponibles; conjunto exacto no probado | Packs actuales no comparados | Ventaja sobre 1.20.1 [SIN VERIFICAR] |
| 1.19.2 + Forge | Java 17 | Embeddium y candidatos Forge mencionados | Packs RPG citados en entrada | Equilibrio mantenimiento/rendimiento [SIN VERIFICAR] |
| 1.19.2 + NeoForge | Java 17 orientativa; requisito exacto de loader pendiente | Combinaciones no verificadas | Disponibilidad/calidad no comprobada | No priorizar sin mod exclusivo |
| 1.20.1 + Fabric | Java 17 | Sodium 0.5.13, Lithium 0.11.4, FerriteCore 6.0.1 y ModernFix 5.25.2 tienen archivos/versiones citados | Prominence II citado como pack Fabric 1.20.1 | **Preferencia de investigación propuesta**, no decisión ni FPS medidos; GPU compatible [SIN VERIFICAR] |
| 1.20.1 + Forge | Java 17 | Embeddium/Radium y otros candidatos; pila no probada | Pack Forge citado en entrada | Alternativa si manifiesto exige Forge; compatibilidad/rendimiento pendientes |
| 1.20.1 + NeoForge | Java 17 orientativa | Candidatos citados, combinación no validada | Packs citados, no evaluados | No elegir sin necesidad concreta |
| 1.21.1 + Fabric | Java 21 (Minecraft requiere Java 21 desde 1.20.5) | Candidatos 1.21.x sin validación individual aquí | Comparación RPG pendiente | Sin ventaja probada para este equipo |
| 1.21.1 + Forge | Java 21 | Renderer equivalente y archivos no verificados en la entrada | Disponibilidad alta no comprobada | No priorizar sin manifiesto |
| 1.21.1 + NeoForge | Java 21 | Candidatos de ecosistema citados | Pack citado | Radeon R3 y compatibilidad [SIN VERIFICAR] |

Fuentes: Fabric/Java https://wiki.fabricmc.net/install ; Java 21 desde 1.20.5 https://www.minecraft.net/en-us/article/minecraft-java-edition-1-20-5 ; AMD legacy https://www.amd.com/en/resources/support-articles/faqs/GPU-630.html . Sodium requiere soporte oficial de driver OpenGL 4.5: https://modrinth.com/mod/sodium . No se conoce API de esta instalación.

## Registro de propuestas

| ID | Propuesta | Justificación disponible | Estado |
|---|---|---|---|
| TD-01 | Ensayar primero 1.20.1 + Fabric, aislado | Hay archivos de varios optimizadores para esta versión y un pack RPG Fabric citado; Fabric recomienda Java 17 | Pendiente de aprobación y pruebas; no se afirma superioridad |
| TD-02 | Usar 1.20.1 + Forge solo si lo requiere el pack | Loader depende del manifiesto y las pilas no son intercambiables | Pendiente del manifiesto |
| TD-03 | Base de prueba Sodium + Lithium + FerriteCore; añadir grupos incrementalmente | Reduce variables; compatibilidad del pack y GPU no probadas | Propuesta pendiente; Sodium OpenGL 4.5 puede ser limitante |
| TD-04 | No fijar aún Loader/API exactos | Falta manifiesto completo y versión común verificada | Pendiente |
| TD-05 | Conservar defaults de Sodium 0.5.13 hasta prueba | Esquema cotejado con código versionado; no hay mediciones para ajustar hilos | Propuesta pendiente |
| TD-06 | No incorporar flags JVM experimentales; `-Xmx4G` solo como punto inicial | No hay evidencia de beneficio en el equipo | Pendiente y sujeto a medición |
| TD-07 | Revisar licencia del artefacto antes de distribución | Hay licencias distintas y Entity Culling limita redistribución directa del JAR | Pendiente antes de empaquetar; nunca subir JARs aquí |
| TD-08 | No ejecutar FPS estimados ni declarar ganancias | No existe captura/benchmark | Regla vigente |

## Pendientes del usuario

- Aprobar o rechazar 1.20.1 + Fabric.
- Entregar manifiesto exacto y requisitos RPG/loader.
- Confirmar launcher, Windows/build, driver y OpenGL/Vulkan de la máquina.
- Aprobar archivos/mods concretos después de revisar licencias y dependencias.
- Definir objetivo y autorizar pruebas/cambios.
