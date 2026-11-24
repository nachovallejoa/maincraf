# Auditoría RPG de mods — perfil provisional

> **Perfil:** Minecraft 1.20.1 + Fabric, pendiente de aprobación. Auditoría documental basada solo en fichas/enlaces suministrados; no acredita instalación, interoperabilidad ni funcionamiento local. “No verificado” no significa incompatible. No se recibieron JAR/manifiesto de instancia; no se inspeccionó ni redistribuyó software de terceros.

## Conclusión

Hay candidatos para progresión, combate, equipo, misiones y jefes genéricos. Ninguno implementa por sí mismo las tres clases, reputación de cuatro facciones, decisiones persistentes y rutas concretas. Planear un módulo propio o integración demostrada. Solapamientos: Skill Tree/Simply Skills; PlayerEX/estadísticas propias; Questlog/FTB Quests; RPG Inventory/Reforged con funciones distintas por verificar. Remnants añade dimensión no necesaria. Village Diplomacy cubre aldeas, no estas facciones.

## Fichas de candidatos RPG documentados

### Skill Tree (RPG Series)
- Build citada: **1.6.1+1.20.1-fabric**, cliente/servidor. Página atribuye 200+ nodos para clases RPG Series, especializaciones y modificadores; no acredita Guardacorrientes, Vigía o Rompeanclas.
- Dependencias: Pufferfish’s Skills 0.16.7+1.20 y versión emparejada de Spell Engine. Build Fabric 1.20.1 exacta de Pufferfish 0.16.7 no verificada; la ficha aportada de Skills muestra 0.13.2, no acredita requisito 0.16.7.
- Solapamiento con Simply Skills y PlayerEX. Autor advierte emparejar RPG Series/Spell Engine; Sodium y conjunto no probados. ARR; redistribución no verificada.
- Adaptación de clases narrativas no comprobada. Rendimiento: **NO DATA**; no se midió FPS, memoria o carga.
- Fuentes aportadas: [build](https://modrinth.com/mod/skill-tree/version/Bf3op7OA), [Skills 0.13.2](https://modrinth.com/mod/skills/version/XffZOSrD), [proyecto](https://modrinth.com/mod/skill-tree).

### Simply Skills
- Build: **1.3.2+1.20.1**, Fabric cliente/servidor. Árbol/especializaciones genéricas, no confirma clases del proyecto.
- Requiere Spell Power Attributes, Spell Engine, Cloth Config API, Pufferfish’s Skills; RPG Series y otros complementos opcionales según ficha.
- Se solapa directamente con Skill Tree; no combinar sin propietario claro de builds. Combinación con Sodium no probada. Licencia Timefall Development License 1.2; redistribución del archivo no verificada.
- Adaptación de historia no verificada. Impacto de rendimiento: **NO DATA**.
- Fuente: [versión 1.3.2](https://modrinth.com/mod/simply-skills/version/1.3.2+1.20.1).

### PlayerEX: Directors Cut
- Build: **4.0.5+1.20.1**, Fabric/Quilt. Atributos RPG; detalles de niveles/puntos descritos en build 3.7 no se trasladan automáticamente a todos los detalles de 4.0.5.
- Dependencias visibles/citadas para 4.0.5: oωo, Fabric API, Ranged Weapon API, Fabric Language Kotlin; cadena completa exacta no verificada. Página anterior también menciona Data Attributes y Cloth Config.
- Solapamiento de niveles/atributos/puntos con árboles y sistema propio. Licencia MIT indicada; comprobar archivo y avisos. Build publicada 2025; configuración detallada 4.0.5 pendiente.
- Build anterior dice “minor performance tweaks”, no benchmark de esta build/hardware. Rendimiento actual: **NO DATA**.
- Fuentes: [4.0.5](https://modrinth.com/mod/playerex-directors-cut/version/vELn14ZA), [3.7.0](https://modrinth.com/mod/playerex-directors-cut/version/3.7.0+1.20.1).

### RPG Inventory
- Build **1.8.0 Fabric 1.20.1**, cliente/servidor; añade espacios de equipo y mecánicas de inventario, no rarezas por sí mismo.
- Trinkets y Cloth Config API obligatorias; Stamina Attributes y Food Overhaul opcionales según ficha. Posible solapamiento de espacios de accesorios. Licencia MIT indicada; redistribución conforme licencia/avisos, verificar archivo.
- Adaptación a rarezas narrativas no verificada. Rendimiento: **NO DATA**.
- Fuente: [1.8.0](https://modrinth.com/mod/rpg-inventory/version/1.8.0).

### Reforged (formerly Tiered)
- Build **1.20.1-1.0.9-Fabric**, Fabric/Quilt, cliente/servidor. Modificadores/tiers para equipo y configuración data-driven según ficha; no progresión por facción.
- UnionLib obligatoria según build consultada. Puede solaparse con sistemas de estadísticas de objetos/rareza. MIT indicada; revisar archivo. Adaptación de datos del proyecto no comprobada.
- Rendimiento: **NO DATA**.
- Fuentes: [build](https://modrinth.com/mod/tiered/version/1.20.1-1.0.9-Fabric), [proyecto](https://modrinth.com/mod/tiered).

### Better Combat
- Build **1.9.0+1.20.1-fabric**, cliente/servidor; sistema de combate cuerpo a cuerpo/animaciones, no fases narrativas del jefe final.
- Dependencias nominales exactas de esta build: **[SIN VERIFICAR: la ficha consultada no las estableció]**. No inferir las de una build anterior. Solapamiento posible con otro reemplazo de ataques/daño; combinación completa no probada. ARR; permiso de redistribución no verificado.
- Rendimiento: **NO DATA**.
- Fuente: [build](https://modrinth.com/mod/better-combat/version/OtwNg4r4).

### Remnants | The Eclipsed Realm
- Build exacta citada **3.0.0+fabric-1.20.1**. Jefes/arenas propios, diario, configuración; no son los seis encuentros de campaña. Añade dimensión/biomas, no requeridos por diseño.
- GeckoLib, JAuml y Fabric API (Fabric) obligatorias según ficha. Posible conflicto con mods que reemplacen interfaz completa de barras; la ficha permite desactivar barras personalizadas. Sodium no verificado.
- Apache-2.0 indicada; respetar licencia/avisos. No benchmark. Coste local: **NO DATA**.
- Fuentes: [build](https://modrinth.com/mod/remnants-eclipsed-realm/version/3.0.0+fabric-1.20.1), [proyecto](https://modrinth.com/mod/remnants-eclipsed-realm).

### Bosses of Mass Destruction
- Build **1.7.5-1.20.1 Fabric**, cuatro jefes genéricos, no los seis diseñados.
- Dependencias citadas: Cloth Config API, GeckoLib, Fabric Language Kotlin, Fabric API, Cardinal Components API. Solapa con otros mods de jefes; no implementa arenas controladas de campaña. LGPL-3.0-only indicada; verificar obligaciones. Mantenimiento reciente no verificado.
- Rendimiento: **NO DATA**.
- Fuentes: [build](https://modrinth.com/mod/bosses-of-mass-destruction/version/yoCCX4Cc), [proyecto](https://modrinth.com/mod/bosses-of-mass-destruction).

### Village Diplomacy
- Build **1.4.0 Fabric 1.20.1**, reputación/relaciones con aldeas, no cuatro facciones narrativas.
- Dependencias nominales obligatorias no suficientemente identificadas: **[SIN VERIFICAR]**. Solapamiento con reputación de aldeas; no acredita facciones personalizadas. ARR; redistribución no verificada.
- Rendimiento: **NO DATA**.
- Fuente: [build](https://modrinth.com/mod/village-diplomacy/version/xzUOqXuO).

### FTB Quests (Fabric)
- Build **2001.4.22**, Fabric 1.20.1, sistema de misiones por equipos. Ramas exclusivas descritas en evidencia de build 2001.4.13; no atribuir automáticamente iguales funciones a 2001.4.22. No equivale a diálogo ramificado ni lógica física de rutas.
- Suite con FTB Library/FTB Teams; páginas de Teams listan Architectury API y Fabric API. Versiones mínimas conjuntas no verificadas. Progreso individual divergente requiere verificar ámbito de equipo.
- Alternativa solapada con Questlog; escoger uno. ARR según auditoría; no redistribuir JAR sin autorización expresa. “Lightweight” de página no es medición.
- Impacto local: **NO DATA**.
- Fuentes: [2001.4.22](https://www.curseforge.com/minecraft/mc-mods/ftb-quests-fabric/files/8078537), [ramas exclusivas 2001.4.13](https://www.curseforge.com/minecraft/mc-mods/ftb-quests-fabric/files/6431736), [Library](https://www.curseforge.com/minecraft/mc-mods/ftb-library-fabric), [Teams/dependencias](https://www.curseforge.com/minecraft/mc-mods/ftb-teams-fabric/relations/dependencies).

### Questlog
- Build **3.3.2-1.20.1-fabric**, misiones tipo libro/lista y datos JSON; ficha atribuye prerrequisitos, objetivos, recompensas/globales en builds recientes. No acredita selección exclusiva equivalente a FTB Quests ni reputación/rutas integradas.
- Dependencias nominales completas de esta build: **[SIN VERIFICAR]**; una ficha antigua cita Cloth Config, no asumir cadena completa. Alternativa solapada con FTB Quests. Apache-2.0 indicada; aplicar avisos/condiciones.
- Rendimiento: **NO DATA**.
- Fuentes: [build](https://modrinth.com/mod/questlog/version/qN2sUxYM), [proyecto/modelo](https://modrinth.com/mod/ufQYCY6N).

## Medición local

No hay ejecución ni benchmarks aportados para Athlon 5150, Radeon R3 y HDD. No se midió ninguna combinación RPG ni base de comparación.

| Métrica | Resultado |
|---|---|
| FPS | **NO DATA — benchmark no ejecutado** |
| Frametime | **NO DATA — no medido** |
| RAM | **NO DATA — no medido** |
| CPU/GPU | **NO DATA — no medido** |
| Arranque | **NO DATA — no medido** |
| Carga | **NO DATA — no medido** |
| Compatibilidad/estabilidad del conjunto | **NO DATA — instancia no probada** |

Un dato vacío no significa cero ni resultado favorable. Para completar mediciones se requiere instancia autorizada, escenario repetible y consentimiento; esta auditoría no instala ni redistribuye mods.
