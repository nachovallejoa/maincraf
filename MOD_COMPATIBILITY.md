# Matriz de compatibilidad de mods

**Estado:** borrador; ninguna combinación instalada ni probada. Manifiesto RPG: no disponible en el paquete revisado. Plataforma candidata: Minecraft 1.20.1 + Fabric; Forge solo si lo requiere el manifiesto.

## Estados

- **Candidato:** existe evidencia de versión/plataforma publicada; no prueba local.
- **No verificado:** falta evidencia de combinación concreta.
- **Carga probada / función probada:** solo tras registrar launcher, MC, loader, Java, mods/config exactos y resultado reproducible.
- **Conflicto confirmado:** evidencia reproducible o aviso del autor aplicable al caso.
- No mezclar JARs Fabric y Forge. Nunca subir JARs de terceros.

## Matriz candidata Fabric 1.20.1

| Mod | Build/alcance registrado | Pack RPG | Estado |
|---|---|---|---|
| Minecraft/Java | MC 1.20.1; Java 17 documentado/recomendado por Fabric para 1.17–1.20.4 | Manifiesto ausente | Java adecuado como referencia; configuración local no verificada. |
| Fabric Loader/API | Versión exacta pendiente | Manifiesto ausente | No verificado; API solo si build requiere. |
| Sodium | 0.5.13 Fabric 1.20.1 | Sin manifiesto | Candidato. OpenGL/controlador Radeon R3 [SIN VERIFICAR]; soporte oficial OpenGL 4.5+ no permite inferir fallo/éxito local. |
| Lithium | 0.11.4 Fabric 1.20.1 | Sin manifiesto | Candidato; carga/función no probadas. |
| FerriteCore | 6.0.1 Fabric, MC 1.20–1.20.2 | Sin manifiesto | Candidato. FerriteCore declara incompatibilidad con Hydrogen en 1.18+; no combinarlos en 1.20.1. |
| ModernFix | 5.25.2+mc1.20.1 Fabric | Sin manifiesto | Candidato; configuración predeterminada inicialmente. |
| ImmediatelyFast | 1.5.5+1.20.4 Fabric, rango declarado 1.20–1.20.4 | Sin manifiesto | Candidato; versión 1.20.1 dentro del rango publicado; integración completa no probada. |
| Entity Culling | 1.12.1-1.20.1 (entrada recibida) | Sin manifiesto | Opcional, archivos exactos pendientes; probar entidades/NPCs y CPU. |
| Particle Core | 0.2.5+1.20.1 (entrada recibida) | Sin manifiesto | Opcional, archivos exactos pendientes; comprobar solapamiento de partículas. |
| Noisium | 2.3.0+mc1.20-1.20.1 (entrada recibida) | Sin manifiesto | Opcional, archivo/estado actuales por verificar; solo escenario de generación. |
| Dynamic FPS | 3.9.5 (entrada recibida) | Sin manifiesto | Opcional para segundo plano; dependencias exactas pendientes, no candidato de FPS activo. |
| LightSpeedRe | 2.0.7 Fabric 1.20.1 (entrada recibida) | Sin manifiesto | Experimental; dependencias/licencia pendientes; comparar individualmente con ModernFix. |

## Alternativa Forge 1.20.1

Embeddium, FerriteCore y ModernFix aparecen como candidatos recibidos. Versiones/builds completas, dependencias e integración RPG no verificadas. No combinar con matriz Fabric; elegir únicamente si el manifiesto exige Forge.

## Interacciones que requieren prueba

| Relación | Evidencia/estado | Precaución |
|---|---|---|
| Sodium + Radeon R3 | API/controlador local sin verificar. Sodium 0.5.13 publicado para MC 1.20.1; OpenGL 4.5+ para soporte oficial. | Probar primero Minecraft limpio; registrar API/controlador; comparar sin Sodium solo si falla. No asumir que Embeddium resuelve API. |
| Sodium + ImmediatelyFast | No hay prueba con el pack. | Revisar arranque, render y logs. |
| Sodium + Indium | Ficha Sodium indica 1.0.36+ si se usa. | No añadir sin dependencia explícita. |
| Sodium + Iris | Ficha Sodium indica 1.7.6+ si se usa. | Shaders/Iris no forman parte de base propuesta. |
| FerriteCore + Hydrogen | Incompatibilidad declarada por FerriteCore para MC 1.18+. | No combinar en 1.20.1. |
| ModernFix dinámico | Falso por defecto según código consultado. | No añadir override inicial; generar config propia. |
| Activar `mixin.perf.dynamic_resources` | Opción existente; pack no disponible para validación. | Solo en copia, con logs y revisión de recursos. |
| ModernFix + LightSpeedRe | Solapamiento potencial, combinación sin verificar. | Ensayar individualmente. |
| Entity Culling + NPCs RPG | Sin inventario de entidades. | Revisar visibilidad/función y exclusiones si se prueba. |
| Particle Core + partículas nativas | Solapamiento posible. | Probar por separado. |
| Noisium + mundo existente | No se acredita mejora de lectura de chunks existentes. | Separar generación nueva y mundo guardado. |

## Registro de pruebas (vacío: no se ejecutaron pruebas)

| Fecha | MC/loader exactos | Java | Mods/versiones/hash local | Configuración/mundo | Carga | Función | Logs/errores | Estado |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
