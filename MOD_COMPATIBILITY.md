# Compatibilidad de mods

## Estado

- Estado inicial recibido: repositorio sin manifiesto ni lista de mods RPG.
- La consulta inicial de esta misión encontró raíz vacía; no hay mods del proyecto que probar.
- `NO DATA: mods RPG del proyecto — árbol reportado vacío; README reportado 404; no hay manifiesto ni lista de mods.`
- Compatibilidad de cualquier base candidata con un pack RPG concreto: **SIN VERIFICAR**.
- No se ejecutó Minecraft; ninguna carga o función se marca como probada.

## Estados válidos

- No verificado
- Carga probada
- Función probada
- Conflicto reproducido
- No aplica

La existencia de un archivo o declaración de su proyecto no equivale a prueba de carga/función.

## Matriz candidata Fabric 1.20.1

| Componente | Versión/archivo propuesto | Dependencia o nota comprobada | Pack RPG | Carga | Función | Evidencia |
|---|---|---|---|---|---|---|
| Minecraft | 1.20.1 | Java 17 recomendado por Fabric para 1.17–1.20.4 | No verificado | No verificado | No verificado | https://wiki.fabricmc.net/install |
| Fabric Loader | Pendiente | Fijar tras conocer el pack | No verificado | No verificado | No verificado | — |
| Fabric API | Versión pendiente | Dynamic FPS 3.9.5 la requiere; versión común exacta pendiente | No verificado | No verificado | No verificado | https://modrinth.com/mod/dynamic-fps/version/D9mrJwm0 |
| Sodium | 0.5.13 Fabric | Indium ≥1.0.36 o Iris ≥1.7.6 solo si se usan; OpenGL 4.5 en driver actualizado para soporte oficial | No verificado; Radeon R3 sin verificación de API | No verificado | No verificado | https://modrinth.com/mod/sodium/version/mc1.20.1-0.5.13-fabric |
| Lithium | 0.11.4 Fabric | Proyecto dice que Fabric API no es requerida | No verificado | No verificado | No verificado | https://www.curseforge.com/minecraft/mc-mods/lithium/files/7268114 |
| FerriteCore | 6.0.1 Fabric | Hydrogen conflict [SIN VERIFICAR] | No verificado | No verificado | No verificado | https://modrinth.com/mod/ferrite-core/version/6.0.1 |
| ModernFix | 5.25.2+mc1.20.1 Fabric | Compatibilidad específica pendiente | No verificado | No verificado | No verificado | https://www.curseforge.com/minecraft/mc-mods/modernfix/files/7306748 |
| Entity Culling | 1.12.1 Fabric | Uso de CPU libre descrito por proyecto; revisar rendimiento con CPU cargada | No verificado | No verificado | No verificado | https://modrinth.com/mod/entityculling/version/xM6y5W1N |
| ImmediatelyFast | 1.2.4 propuesto | Artefacto exacto [SIN VERIFICAR]; revisar OptiFine/OptiFabric y MemoryLeakFix antiguo | No verificado | No verificado | No verificado | https://modrinth.com/mod/immediatelyfast |
| BadOptimizations | 2.2.3 (1.20.1) | Sin dependencia obligatoria según ficha consultada | No verificado | No verificado | No verificado | https://www.curseforge.com/minecraft/mc-mods/badoptimizations/files/6673591 |
| Particle Core | 0.3.3+1.20.1 Fabric | Validar efectos personalizados | No verificado | No verificado | No verificado | https://www.curseforge.com/minecraft/mc-mods/particle-core/files/7581167 |
| Dynamic FPS | 3.9.5 Fabric | Fabric API requerida; Cloth Config opcional | No verificado | No verificado | No verificado | https://modrinth.com/mod/dynamic-fps/version/D9mrJwm0 |
| Mods RPG | NO DATA | Inventario/manifiesto no entregado | No verificable | No verificado | No verificado | Árbol reportado vacío; README 404 |

## Matriz alternativa Forge 1.20.1

No mezclar con la matriz Fabric. Versiones candidatas recibidas, pendientes de validación integral:

| Componente | Propuesta | Estado |
|---|---|---|
| Minecraft / Java | 1.20.1 / Java 17 orientativo | Loader y perfil final pendientes |
| Forge | Versión pendiente | No verificado |
| Embeddium | 0.3.31+mc1.20.1 | Versión/compatibilidad [SIN VERIFICAR] |
| Radium | 0.12.4 | No combinar con Canary según información recibida; archivo exacto pendiente |
| FerriteCore / ModernFix | Versiones citadas en entrada | Compatibilidad RPG [SIN VERIFICAR] |
| Entity Culling / ImmediatelyFast | Versiones citadas | Artefactos y compatibilidad completa [SIN VERIFICAR] |
| Particle Core | 0.3.3+1.20.1+forge | Probar función RPG |
| Dynamic FPS | 3.9.2 Forge propuesto | [SIN VERIFICAR] |
| Mods RPG | NO DATA | Sin manifiesto |

## Reglas de prueba

1. Respaldar perfil y mundo.
2. Registrar Minecraft, Java, loader, mods y dependencias con versiones exactas.
3. Probar primero carga del pack RPG sin optimizadores.
4. Añadir un mod/grupo cada vez, conservar logs y verificar funciones.
5. No instalar simultáneamente pilas Fabric y Forge.
6. No equiparar carga exitosa con compatibilidad funcional total.
7. No retirar ni reemplazar mods sin autorización expresa.
8. Medir solo después de estabilidad y con el protocolo de `PERFORMANCE.md`.
