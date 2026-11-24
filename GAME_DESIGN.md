# Diseño de juego

> **Pendiente: etapas futuras.** Esta misión no diseña mecánicas ni contenido RPG; el modpack y sus requisitos siguen sin datos.

- Objetivos de diseño: pendientes.
- Bucle de juego y progresión: pendientes.
- Sistemas/reglas: pendientes.
- Misiones, dificultad y balance: pendientes.
- Criterios de aceptación: pendientes de acordar con el usuario.

## Pilares RPG por propuesta de identidad

> Las propuestas están **pendientes de elección**. Todo mod o versión es candidato por investigar, no una recomendación aprobada ni combinación comprobada. Plataforma candidata para las tres: Minecraft 1.20.1 + Fabric **[SIN VERIFICAR; pendiente de aprobación]**. No se han aportado fuentes para verificar disponibilidad de archivos, versiones, dependencias, licencias, compatibilidad o rendimiento. Ningún archivo de mod se incorpora aquí.

### La Cartografía de la Ceniza — pendiente de elección

| Pilar | Diseño RPG propuesto | Candidatos y brechas (todos [SIN VERIFICAR]) |
|---|---|---|
| Progresión | Avanzar por capítulos restaurando faros, recuperando fragmentos del atlas y ganando acceso a rutas y asentamientos; premiar exploración y decisiones, no solo niveles. | Remnants / RPG Attribute System `5.0.0+fabric-1.20.1`; Skill Tree (RPG Series) `1.6.1+1.20.1-fabric`. No está acreditada su integración con capítulos, faros, decisiones o rutas. |
| Clases y habilidades | Builds de exploración, protección de caravanas y apoyo/control; la facción no determina la clase. | Rogues & Warriors (RPG Series) `3.1.3+1.20.1-fabric`, Wizards (RPG Series) `3.1.3+1.20.1-fabric`, Skill Tree `1.6.1+1.20.1-fabric`; Simply Skills, versión exacta 1.20.1 no acreditada. No se verifica clase de cartógrafo ni compatibilidad conjunta. |
| Equipamiento y rarezas | Herramientas de navegación y supervivencia, equipo ligado a asentamientos; rarezas que indiquen procedencia/especialización y recompensen ayudar a comunidades. | Tierify, versión exacta 1.20.1 no acreditada; RPG Inventory `1.5.2`. No se acredita equipo narrativo ni integración de rarezas. La licencia ARR atribuida a assets de Tierify requiere fuente. |
| Jefes | Guardián de faro que prueba lectura del terreno; criatura de mapas que plantea rastreo/emboscada; Custodio como culminación del conflicto. | Bosses of Mass Destruction `1.7.5-1.20.1`: no se acredita que incluya esos jefes ni su vínculo con campaña y decisiones. |
| Exploración | Cuenca Gris, bosque de ceniza y ciudad enterrada; faros como hitos. Caminos cambiantes son objetivo de diseño, no característica confirmada. | BetterEnd y When Dungeons Arise, versiones exactas 1.20.1 no acreditadas. No se verifica que creen las regiones, lugares reaparecidos o rutas alteradas por decisiones. |
| Misiones y narrativa | Cartografiar, recuperar marcas, escoltar caravanas e investigar asentamientos; consecuencias de mediación legibles. | Questlog `3.1.0-1.20.1-fabric`; FTB Quests Optimizer `1.1.5-1.20.1` y disponibilidad/dependencias de FTB Quests: no verificados. No se acredita solución para diálogos, facciones o consecuencias en el mundo. |
| Combate | Posicionamiento, defensa de caravanas y uso de habilidades, subordinados a la exploración. | Better Combat `1.9.0+1.20.1-fabric`: equilibrio con clases, jefes y campaña no acreditado. |

**Brechas de diseño/implementación:** conectar capítulos y decisiones con faros/rutas; dar consecuencias persistentes a facciones; crear jefes propios solo si se convierte en requisito. Cualquier mod propio es posibilidad futura, no decisión.

### La Marea de los Mil Soles — pendiente de elección

| Pilar | Diseño RPG propuesto | Candidatos y brechas (todos [SIN VERIFICAR]) |
|---|---|---|
| Progresión | Expediciones, acceso a diques y señales, decisiones sobre la estación; alianzas deberían desbloquear refugios/suministros y no ser solo reputación. | Remnants / RPG Attribute System `5.0.0+fabric-1.20.1`; Skill Tree (RPG Series) `1.6.1+1.20.1-fabric`. No se acredita integración con mareas, diques, alianzas o accesos. |
| Clases y habilidades | Roles de expedición: buceador/salvador, guardián de rutas y magia/control; especialización sin dictar la facción. | Rogues & Warriors (RPG Series) `3.1.3+1.20.1-fabric`, Wizards (RPG Series) `3.1.3+1.20.1-fabric`, Skill Tree `1.6.1+1.20.1-fabric`; Simply Skills, versión exacta 1.20.1 no acreditada. No se verifican habilidades de buceo, navegación, rescate o mareas. |
| Equipamiento y rarezas | Equipo para ruinas y zonas anegadas, piezas de puertos y recompensas que habiliten builds; rareza comunica procedencia/utilidad. | Tierify, versión exacta 1.20.1 no acreditada; RPG Inventory `1.5.2`. No se acredita equipo que afecte navegación/acceso acuático ni integración de rarezas. Licencia de assets pendiente de fuente. |
| Jefes | Centinela de coral protege compuerta; bestia asociada a expedición; Almirante culmina la decisión sobre el ciclo. | Bosses of Mass Destruction `1.7.5-1.20.1`: enemigos y vínculo con compuertas, ciclo o decisiones no acreditados. |
| Exploración | Archipiélago Salobre, ruinas y observatorio; rutas seguras según señales, diques y alianzas. No se presupone inundación dinámica. | BetterEnd y When Dungeons Arise, versiones exactas 1.20.1 no acreditadas. No se verifica archipiélago, ciclos de marea ni rutas por decisiones. |
| Misiones y narrativa | Recuperar objetos, reparar señales, negociar acceso y elegir rescates; consecuencias legibles en suministros, refugios o rutas. | Questlog `3.1.0-1.20.1-fabric`; FTB Quests Optimizer `1.1.5-1.20.1`, FTB Quests y dependencias: no verificados. Diálogos, facciones y consecuencias de rescates no acreditados. |
| Combate | Encuentros en ruinas y defensa de rutas, con objetivos de entorno; no sustituir rescates/expediciones. | Better Combat `1.9.0+1.20.1-fabric`, Rogues & Warriors y Wizards: equilibrio e integración con encuentros anegados/mareas/alianzas no acreditados. |

**Brechas de diseño/implementación:** conectar estación, diques y facciones con rutas/zonas; decidir si mareas dinámicas son requisito esencial; diseñar reglas de jefes solo si se requieren. Los candidatos no cubren estas funciones de forma acreditada.

### El Invierno que Recuerda — pendiente de elección

| Pilar | Diseño RPG propuesto | Candidatos y brechas (todos [SIN VERIFICAR]) |
|---|---|---|
| Progresión | Investigar recuerdos y testimonios, proteger hogares y descubrir caminos del pasado; hitos narrativos pueden abrir rutas o cambiar ayuda comunitaria. | Remnants / RPG Attribute System `5.0.0+fabric-1.20.1`; Skill Tree (RPG Series) `1.6.1+1.20.1-fabric`. No se acredita integración con recuerdos, confianza o rutas temporales. |
| Clases y habilidades | Builds de protección, rastreo y magia/apoyo; habilidades ayudan a investigar o defender sin resolver automáticamente los misterios. | Rogues & Warriors (RPG Series) `3.1.3+1.20.1-fabric`, Wizards (RPG Series) `3.1.3+1.20.1-fabric`, Skill Tree `1.6.1+1.20.1-fabric`; Simply Skills, versión exacta 1.20.1 no acreditada. Habilidades para recuerdos, voces o defensa de hogares no verificadas. |
| Equipamiento y rarezas | Equipo invernal, objetos heredados y recompensas ligadas a testimonios/lugares; rareza señala antigüedad o comunidad, no solo combate. | Tierify, versión exacta 1.20.1 no acreditada; RPG Inventory `1.5.2`. Propiedades según recuerdos, comunidad o decisiones no acreditadas. Licencia de assets pendiente de fuente. |
| Jefes | Guardián repite patrones de viajeros; criatura imitadora amenaza con voces; Reina culmina el conflicto entre romper ciclo y conservar pasado. | Bosses of Mass Destruction `1.7.5-1.20.1`: jefes, patrones y vínculos narrativos no acreditados. |
| Exploración | Valle de los Hogares, bosque de nombres y paso en tormenta; recuerdos podrían abrir caminos/revelar peligros como objetivo, no cambio automático confirmado. | BetterEnd y When Dungeons Arise, versiones exactas 1.20.1 no acreditadas. Regiones, caminos temporales y cambios por recuerdos no acreditados. |
| Misiones y narrativa | Reunir testimonios, reconstruir escenas, proteger hogares y decidir secretos; confianza/ayuda deben ser consecuencias legibles, aunque inicialmente se expresen mediante objetivos/recompensas. | Questlog `3.1.0-1.20.1-fabric`; FTB Quests Optimizer `1.1.5-1.20.1`, FTB Quests y dependencias: no verificados. Diálogos, testimonios ramificados, reputación y cambios de habitantes no acreditados. |
| Combate | Observar patrones, sobrevivir al frío y proteger a otros; reservar espacio para investigación. | Better Combat `1.9.0+1.20.1-fabric`, Rogues & Warriors y Wizards: integración con patrones de recuerdos, peligro invernal y progreso narrativo no acreditada. |

**Brechas de diseño/implementación:** vincular recuerdos con confianza, rutas y comunidades; decidir si hacen falta diálogos ramificados; definir mecánicas específicas de jefes solo si son requisito. Los candidatos no acreditan esas integraciones.

## Riesgos y verificaciones comunes

- Todos los mods/versiones son candidatos **[SIN VERIFICAR]**; no hay fuentes citadas para archivos, versiones, dependencias, licencias o compatibilidad. No son una lista de instalación.
- Minecraft 1.20.1 + Fabric está **[SIN VERIFICAR]** y pendiente de aprobación.
- No hay pruebas en Athlon 5150/Radeon R3 ni mediciones con HDD. Peso desconocido; no se asegura compatibilidad con Sodium. FPS, frametime, memoria, carga y estabilidad **[SIN VERIFICAR]**. No aprobar para ese equipo hasta verificar artefactos/dependencias y hacer pruebas locales reproducibles.
- Originalidad frente a Prominence II **[SIN VERIFICAR]**: no se aportó descripción, fuente ni comparación.
