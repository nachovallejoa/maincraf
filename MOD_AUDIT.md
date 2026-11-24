# Auditoría de mods RPG — mecánicas

> **Alcance:** auditoría documental basada en fichas/enlaces aportados; perfil candidato Minecraft 1.20.1 + Fabric pendiente de aprobación y verificación de instancia. La presencia de una build publicada no prueba instalación ni funcionamiento local. No se recibieron JARs/manifiestos de instancia ni se inspeccionó o redistribuyó software de terceros. Ningún candidato queda aprobado por esta tabla. Autoría, dependencia, licencia y compatibilidad se anotan solo según evidencia indicada; cualquier dato que no se aportó permanece **[SIN VERIFICAR]**. No se suben archivos de mods.

## Resumen de decisión

Candidatos para árboles, progresión, inventario/tiers, combate, jefes, reputación y misiones; ninguno implementa por sí solo todas las mecánicas narrativas. No combinar sistemas solapados sin asignar una única autoridad para puntos, equipo, diario y recompensas. Versiones exactas, APIs y compatibilidad deben comprobarse contra artefactos/manifiesto antes de seleccionar. Mods de rendimiento no aprobados y sus cruces con estos candidatos: no verificados.

## Fichas

### Skill Tree (RPG Series)
- **Build citada:** `1.6.1+1.20.1-fabric`, cliente/servidor.
- **Función/cobertura:** árbol de 200+ nodos para clases del ecosistema RPG Series; no acredita Guardacorriente, Vigía o Rompeanclas ni opcionalidad narrativa.
- **Dependencias:** Pufferfish’s Skills `0.16.7+1.20` y mods de clases RPG Series indicados por proyecto; emparejar versiones/Spell Engine. Build exacta del requisito no confirmada por el material recibido.
- **Solapamiento/riesgos:** Simply Skills y PlayerEX/progresión propia. Advertencia de incompatibilidad entre generaciones antiguas de RPG Series/Spell Engine. Sodium y conjunto local: no verificado.
- **Licencia/redistribución:** ARR indicada; redistribución no autorizada/verificada.
- **Fuente:** [build](https://modrinth.com/mod/skill-tree/version/Bf3op7OA), [proyecto](https://modrinth.com/mod/skill-tree), [Pufferfish build citada](https://modrinth.com/mod/skills/version/XfFZOSrD).
- **Mediciones locales:** FPS **NO DATA**; frametime **NO DATA**; RAM **NO DATA**; CPU/GPU **NO DATA**; arranque/carga **NO DATA**; estabilidad/compatibilidad **NO DATA**. No se midió en Athlon 5150/Radeon R3/HDD.

### Simply Skills
- **Build citada:** `1.3.2+1.20.1` Fabric, cliente/servidor.
- **Función:** pasivas, especializaciones y habilidades activas; no confirma clases propias de campaña.
- **Dependencias citadas:** Spell Power Attributes, Spell Engine, Cloth Config API y Pufferfish’s Skills; otros complementos según ficha. Cadena completa del artefacto no verificada aquí.
- **Solapamiento:** directo con Skill Tree; no usar ambos sin propietario claro.
- **Licencia:** Timefall Development License 1.2 indicada; redistribución no verificada.
- **Fuente:** [versión](https://modrinth.com/mod/simply-skills/version/1.3.2+1.20.1), [proyecto](https://modrinth.com/mod/simply-skills).
- **Mediciones locales:** FPS **NO DATA**; frametime **NO DATA**; RAM **NO DATA**; CPU/GPU **NO DATA**; arranque/carga **NO DATA**; estabilidad/compatibilidad **NO DATA**.

### PlayerEX: Directors Cut
- **Build citada:** `4.0.5+1.20.1`, Fabric/Quilt.
- **Función:** atributos RPG. La ficha previa 3.7 contenía detalles de niveles/puntos que no se trasladan automáticamente a 4.0.5.
- **Dependencias:** lista completa exacta de 4.0.5 **[SIN VERIFICAR]**.
- **Solapamiento:** niveles, atributos y puntos propios; escoger un único propietario. Licencia MIT indicada, revisar licencia/avisos del artefacto.
- **Fuente:** [build](https://modrinth.com/mod/playerex-directors-cut/version/vELn14ZA), [proyecto](https://modrinth.com/mod/playerex-directors-cut).
- **Mediciones locales:** FPS **NO DATA**; frametime **NO DATA**; RAM **NO DATA**; CPU/GPU **NO DATA**; arranque/carga **NO DATA**; estabilidad/compatibilidad **NO DATA**.

### RPG Inventory
- **Build:** `1.8.0`, Fabric 1.20.1, cliente/servidor.
- **Función:** slots y mecánicas de inventario; no implementa rarezas.
- **Dependencias/solapamiento:** Trinkets y Cloth Config API citados como requeridos; Stamina Attributes/Food Overhaul opcionales según evidencia. Posible solapamiento de slots.
- **Licencia:** MIT indicada; comprobar artefacto/avisos.
- **Fuente:** [build](https://modrinth.com/mod/rpg-inventory/version/1.8.0).
- **Mediciones locales:** FPS **NO DATA**; frametime **NO DATA**; RAM **NO DATA**; CPU/GPU **NO DATA**; arranque/carga **NO DATA**; estabilidad/compatibilidad **NO DATA**.

### Reforged (formerly Tiered)
- **Build:** `1.20.1-1.0.9-Fabric`.
- **Función:** modificadores/tiers de equipo, configuración data-driven; no reputación ni progresión narrativa.
- **Dependencias:** UnionLib indicada para build consultada; verificar en artefacto.
- **Solapamiento/licencia:** se puede solapar con tiers/atributos de objetos; MIT indicada, verificar avisos. Adaptación de datos de campaña no probada.
- **Fuente:** [build](https://modrinth.com/mod/tiered/version/1.20.1-1.0.9-Fabric), [proyecto](https://modrinth.com/mod/tiered).
- **Mediciones locales:** FPS **NO DATA**; frametime **NO DATA**; RAM **NO DATA**; CPU/GPU **NO DATA**; arranque/carga **NO DATA**; estabilidad/compatibilidad **NO DATA**.

### Better Combat
- **Build citada:** `1.9.0+1.20.1-fabric`.
- **Función:** combate cuerpo a cuerpo/animaciones; no fases narrativas de jefes.
- **Dependencias:** exactas para esta build **[SIN VERIFICAR]** en ficha leída.
- **Solapamiento/licencia:** posibles reemplazos de ataque/daño; combinación completa no probada. ARR indicada; redistribución no verificada.
- **Fuente:** [build](https://modrinth.com/mod/better-combat/version/OtwNg4r4), [proyecto](https://modrinth.com/mod/better-combat).
- **Mediciones locales:** FPS **NO DATA**; frametime **NO DATA**; RAM **NO DATA**; CPU/GPU **NO DATA**; arranque/carga **NO DATA**; estabilidad/compatibilidad **NO DATA**.

### Remnants | The Eclipsed Realm
- **Build:** `3.0.0+fabric-1.20.1`.
- **Función:** jefes/arenas propios, diario y configuración; añade dimensión/biomas, no requerido para los seis jefes de campaña.
- **Dependencias:** GeckoLib, JAuML y Fabric API citadas; verificar artefacto.
- **Solapamiento/licencia:** no sustituye elenco de campaña; posible conflicto con interfaces completas de barras. Apache-2.0 indicada, cumplir avisos.
- **Fuente:** [build](https://modrinth.com/mod/remnants-eclipsed-realm/version/3.0.0+fabric-1.20.1), [proyecto](https://modrinth.com/mod/remnants-eclipsed-realm).
- **Mediciones locales:** FPS **NO DATA**; frametime **NO DATA**; RAM **NO DATA**; CPU/GPU **NO DATA**; arranque/carga **NO DATA**; estabilidad/compatibilidad **NO DATA**.

### Bosses of Mass Destruction
- **Build:** `1.7.5-1.20.1` Fabric.
- **Función:** cuatro jefes genéricos distintos de los seis encuentros de campaña.
- **Dependencias citadas:** Cloth Config API, GeckoLib, Fabric Language Kotlin, Fabric API, Cardinal Components API.
- **Solapamiento/licencia:** no sustituye jefes/arenas narrativas; LGPL-3.0-only indicada, revisar obligaciones.
- **Fuente:** [build](https://modrinth.com/mod/bosses-of-mass-destruction/version/yoCCX4Cc), [proyecto](https://modrinth.com/mod/bosses-of-mass-destruction).
- **Mediciones locales:** FPS **NO DATA**; frametime **NO DATA**; RAM **NO DATA**; CPU/GPU **NO DATA**; arranque/carga **NO DATA**; estabilidad/compatibilidad **NO DATA**.

### Village Diplomacy
- **Build citada:** `1.4.0`, Fabric 1.20.1.
- **Función:** relaciones/reputación de aldeas; no modela cuatro facciones narrativas.
- **Dependencias:** exactas **[SIN VERIFICAR]**.
- **Solapamiento/licencia:** solo apropiado para reputación de aldeas; ARR indicada, redistribución no verificada.
- **Fuente:** [build](https://modrinth.com/mod/village-diplomacy/version/xzUOqXuO).
- **Mediciones locales:** FPS **NO DATA**; frametime **NO DATA**; RAM **NO DATA**; CPU/GPU **NO DATA**; arranque/carga **NO DATA**; estabilidad/compatibilidad **NO DATA**.

### FTB Quests (Fabric)
- **Build citada:** `2001.4.22`, MC 1.20.1.
- **Función:** misiones para equipo. Ramas exclusivas citadas con evidencia de build `2001.4.13`; no atribuir automáticamente igual funcionalidad a 2001.4.22. No equivale a diálogo ramificado o lógica física de rutas.
- **Dependencias:** suite FTB Library/Teams; versiones mínimas exactas no verificadas.
- **Solapamiento/licencia:** alternativa a Questlog; ARR según auditoría, no redistribuir JAR sin autorización expresa.
- **Fuente:** [2001.4.22](https://www.curseforge.com/minecraft/mc-mods/ftb-quests-fabric/files/8078537), [build con evidencia de ramas](https://www.curseforge.com/minecraft/mc-mods/ftb-quests-fabric/files/6431736), [Library](https://www.curseforge.com/minecraft/mc-mods/ftb-library-fabric), [Teams/dependencias](https://www.curseforge.com/minecraft/mc-mods/ftb-teams-fabric/relations/dependencies).
- **Mediciones locales:** FPS **NO DATA**; frametime **NO DATA**; RAM **NO DATA**; CPU/GPU **NO DATA**; arranque/carga **NO DATA**; estabilidad/compatibilidad **NO DATA**.

### Questlog
- **Build:** `3.3.2-1.20.1-fabric`.
- **Función:** misiones tipo libro/lista y datos JSON; no acredita ramas exclusivas ni reputación/rutas integradas.
- **Dependencias:** lista exacta de esta build **[SIN VERIFICAR]**; no inferir desde build antigua.
- **Solapamiento/licencia:** alternativa a FTB Quests; Apache-2.0 indicada, verificar avisos/archivo.
- **Fuente:** [build](https://modrinth.com/mod/questlog/version/qN2sUxYM), [proyecto/modelo](https://modrinth.com/mod/ufQYCY6N).
- **Mediciones locales:** FPS **NO DATA**; frametime **NO DATA**; RAM **NO DATA**; CPU/GPU **NO DATA**; arranque/carga **NO DATA**; estabilidad/compatibilidad **NO DATA**.

## Mediciones locales

No hubo ejecución ni benchmark aportado para Athlon 5150, Radeon R3 y HDD. No se midieron FPS, frametime, RAM, CPU/GPU, arranque, carga, estabilidad ni compatibilidad del conjunto. Cada resultado permanece **NO DATA**, no equivale a cero ni a resultado favorable. Requiere instancia autorizada, escenario repetible y consentimiento; esta auditoría no instala ni redistribuye mods.
