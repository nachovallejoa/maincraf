# Decisiones técnicas — propuestas pendientes

> No hay decisiones técnicas finales aprobadas en la misión 1. Disponibilidad de build no es benchmark, compatibilidad integral ni validación en el equipo.

## Comparativa de versiones/loaders

| Minecraft + loader | Java | Gráficos/API Radeon R3 | Evidencia disponible | Estado y riesgos |
|---|---|---|---|---|
| **1.20.1 + Fabric** | Java 17; mínimo documentado para 1.20.1 y recomendado por Fabric para 1.17–1.20.4. | OpenGL/controlador local [SIN VERIFICAR]. Sodium 0.5.13 ofrece soporte oficial con drivers OpenGL 4.5+, pero advierte que hardware antiguo puede funcionar sin ese nivel sin garantía. | Sodium 0.5.13, Lithium 0.11.4, FerriteCore 6.0.1 e ImmediatelyFast 1.5.5 (rango declarado 1.20–1.20.4) tienen builds/fichas pertinentes. ModernFix 5.25.2+mc1.20.1. | **Candidata principal a ensayo**, no decisión final ni afirmación de FPS. Compatibilidad RPG y hardware local [SIN VERIFICAR]. |
| **1.20.1 + Forge** | Java 17 para Minecraft 1.20.1. | [SIN VERIFICAR]; Embeddium no resuelve por sí mismo la incertidumbre API/controlador local. | Embeddium/FerriteCore/ModernFix aparecen como candidatos recibidos. | Alternativa solo si manifiesto exige Forge; pila y pack completos pendientes. No mezclar loaders. |
| **1.20.1 + NeoForge** | Combinación exacta no verificada en evidencia recibida. | [SIN VERIFICAR]. | No hay conjunto completo validado para el pack. | No elegir sin requisito; recomendación citada en la entrada requiere nueva consulta si se vuelve relevante. |
| **1.20.4 + Fabric** | Java 17, recomendación Fabric para 1.17–1.20.4. | [SIN VERIFICAR]. | No se proporciona matriz completa de mods RPG aplicable. | Alternativa para proyecto [SIN VERIFICAR]; sin comparativa de rendimiento local. |
| **1.20.4 + NeoForge** | Java 17 según familia en información recibida; validar la combinación exacta. | [SIN VERIFICAR]. | Compatibilidad integral RPG [SIN VERIFICAR]. | No seleccionada. |
| **1.21.1 + Fabric** | Java 21 desde Minecraft 1.20.5. | [SIN VERIFICAR]. | No se verificó conjunto exacto compatible con RPG. | No priorizar sin requisito de manifiesto; ninguna ventaja local probada. |
| **1.21.1 + NeoForge** | Java 21. | [SIN VERIFICAR]. | Candidato Alpha C2ME en registro, no evidencia de estabilidad del pack. | No seleccionada sin requisito; pack/API local pendientes. |

### Lectura recomendada

Propuesta: probar primero 1.20.1 + Fabric por coincidencia documental de builds y Java adecuado, no porque se haya probado más rápida. Forge 1.20.1 solo si el manifiesto lo exige. Antes de decidir: obtener manifiesto, confirmar Java/GPU/controlador/OpenGL, verificar archivos/dependencias y hacer pruebas repetibles.

## Registro de propuestas pendientes de aprobación

| ID | Propuesta | Justificación limitada | Estado/condiciones |
|---|---|---|---|
| TD-01 | Ensayar primero 1.20.1 + Fabric en instancia aislada. | Builds pertinentes publicadas; Java 17 adecuado. | Pendiente de aprobación, manifiesto RPG y comprobación GPU/API. No afirma superioridad FPS. |
| TD-02 | Forge 1.20.1 solo si lo exige manifiesto. | Loader depende del pack; pilas no intercambiables. | Pendiente de manifiesto y validación de archivos Forge. |
| TD-03 | Probar base Sodium + Lithium + FerriteCore + ModernFix + ImmediatelyFast. | Candidatos publicados para la rama; reduce variables iniciales. | Pendiente de verificación de builds/dependencias, compatibilidad pack y medición local. |
| TD-04 | Mantener ModernFix predeterminado al inicio. | Opción dinámica consultada falsa por defecto; pack no validado. | Propuesta pendiente; no añadir override en base. |
| TD-05 | No precargar `sodium-options.json`. | Esquema exacto no demostrado en esta revisión; evitar preset no validado para Radeon R3. | Dejar que Sodium genere archivo en instancia; pendiente de prueba. |
| TD-06 | Mantener candidatos opcionales fuera de base inicial. | Evitar variables/solapamientos. | Añadir individualmente tras definir hipótesis y autorización. |
| TD-07 | Considerar `-Xmx4G` solo como punto inicial propuesto. | No es resultado óptimo medido. | Pendiente de autorización y evaluación de uso RAM; no imponer flags JVM. |

## Pendientes de usuario/datos

- Aprobar o rechazar 1.20.1 + Fabric como instancia aislada de ensayo.
- Aportar manifiesto RPG y confirmar si Forge es requisito.
- Confirmar launcher, Windows/build, Java, GPU/controlador y OpenGL/Vulkan local.
- Aprobar archivos concretos solo tras revisar dependencias/licencias.
- Decidir autorización de pruebas/cambios y política de redistribución.
- Evaluar resolución, límite FPS y ajustes tras medir.
- Decidir si se ensayan opciones adicionales; entregar resultados del protocolo `PERFORMANCE.md`.
- No distribuir JARs por defecto; revisión de licencias no equivale a autorización legal global.

## Fuentes citadas en la revisión recibida

[Java Edition 1.20.1](https://minecraft.wiki/w/Java_Edition_1.20.1) · [Fabric install](https://wiki.fabricmc.net/install) · [Sodium hardware](https://modrinth.com/mod/sodium) · [Sodium 0.5.13](https://modrinth.com/mod/sodium/version/mc1.20.1-0.5.13-fabric) · [Lithium 0.11.4](https://www.curseforge.com/minecraft/mc-mods/lithium/files/7268114) · [FerriteCore 6.0.1](https://modrinth.com/ferrite-core/version/6.0.1) · [ImmediatelyFast 1.5.5](https://modrinth.com/mod/immediatelyfast/version/1.5.5%2B1.20.4-fabric) · [ModernFix 5.25.2](https://modrinth.com/mod/modernfix/version/5.25.2%2Bmc1.20.1).
