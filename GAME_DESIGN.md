# Diseño de juego

> **Estado: propuesta de diseño pendiente de aprobación e implementación.** No certifica contenido de Minecraft, disponibilidad o compatibilidad de mods, ni rendimiento.

## Identidad RPG elegida

Se conserva como base **La Marea de los Mil Soles**, fantasía oscura y misterio en un archipiélago celeste, combinada con la preferencia del usuario por progresión RPG. La Cartografía de la Ceniza queda en reserva. La identidad y las preferencias no son una selección técnica de mods.

### Pilares y preferencias

| Pilar | Dirección de diseño | Estado |
|---|---|---|
| Combate y exploración | Ambos importantes; explorar rutas, testimonios y reflejos y combatir guardianes con dificultad equilibrada. | Preferencia; balance pendiente de pruebas. |
| Progresión | Clases definidas y opcionales, niveles/estadísticas y árboles/builds como objetivos. | Sistemas y cifras pendientes. |
| Supervivencia | Riesgo moderado; sin convertir cada desplazamiento en castigo. | Calibración pendiente. |
| Mundo | Islas flotantes y regiones compactas conectadas por rutas controladas. | Propuesta; no se confirma generación o implementación. |
| Consecuencias | Decisiones alteran confianza, rutas, refugios, suministros y condiciones de desenlace. | Estados persistentes y lógica pendientes. |

Perfiles narrativos opcionales: Guardacorrientes (resistencia/protección), Vigía del Prisma (observación/rutas) y Rompeanclas (combate/mecanismos). Ninguna clase debería bloquear misiones principales.

## Impacto de la historia en el juego

Todo lo siguiente describe el efecto jugable que se busca si la historia se implementa; no afirma que esté disponible. Las zonas se plantean acotadas, sin multitudes, generación procedural pesada, movimiento automático de islas ni cambios masivos de bloques. Jefes con arena controlada y pocos enemigos simultáneos. Son precauciones para el Athlon 5150, Radeon R3 integrada, 12 GB instalados (aprox. 9,9 GB utilizables según datos recibidos) y HDD, no garantías: no hay benchmarks locales.

| Elemento narrativo | Impacto deseado en el juego | Dependencias / implementación pendiente |
|---|---|---|
| Archipiélago, venas y Mar de Nubes | Zonas compactas, rutas desbloqueables y transiciones; riesgo moderado de navegación. | Minecraft 1.20.1 + Fabric es perfil provisional **[SIN VERIFICAR]**. BetterEnd y When Dungeons Arise **[SIN VERIFICAR]**; no se presupone que provean estas regiones. Posible construcción/configuración propia. |
| Trama de Anclas y ciclos de Marea | Estados narrativos abren/cierran rutas y presentan hitos; no hace falta clima dinámico o movimiento físico de islas. | Questlog y FTB Quests **[SIN VERIFICAR]** como candidatos de misiones. Flags, transiciones y lógica podrían requerir contenido propio. |
| Facciones (Liga, Cartógrafos, Hermandad, Flota) | Confianza/apoyo desbloquea suministros, refugios, contactos y alternativas; no exige alineamiento único para terminar. | Reputación y estados persistentes no confirmados. Candidatos de quests no equivalen a reputación; posible sistema propio. |
| Evacuación de Cabo | Decisión de prioridad determina grupo que recibe suministros y contacto para viajar a Oria. | Flags de campaña y consecuencias: implementación propia o sistema compatible por verificar. Evitar simular multitudes. |
| Ancla de Oria | Conservar mantiene ruta/suministro de Liga pero riesgo local; modificar equilibra; abandonar implica traslado y menos suministro. Semillas pueden abrir ayuda posterior. | Misiones/flags de Questlog o FTB Quests **[SIN VERIFICAR]**; lógica de dependencias entre encargos posiblemente propia. |
| Dársena y pruebas | Publicar registros mejora confianza comunitaria; negociar primero conserva canal con Tavia y demora difusión. Planos habilitan opciones de nodos/Fosa. | Estados de campaña y servicios requieren implementación; no se confirma mod candidato que cubra todos los efectos. |
| Fosa y Ballena | Refugios y testimonios abren recursos y diálogo con tripulaciones; dejar criatura conduce a ruta más larga, vencerla despeja paso. | Regiones/encuentros son contenido propuesto. Bosses of Mass Destruction **[SIN VERIFICAR]**, sin atribuirle la Ballena. Si no existe solución compatible, jefe y lógica propios. |
| Nimbo y reflejos | Registros revelan futuros posibles, nunca certezas; divulgar da transparencia y también información a Veyr. | Mapas, decisiones y estados narrativos son contenido propio pendiente; ningún candidato está confirmado para ello. |
| Jefes | Mastín, Madre de los Zarcillos, Custodio, Ballena, Corista y Veyr protegen lugares/decisiones; patrones legibles, encuentros acotados. | Bosses of Mass Destruction **[SIN VERIFICAR]** para este proyecto y no se afirma que contenga ninguno. Posibles jefes propios, sin archivos de mods terceros. |
| Eventos de Marea | Hitos narrativos pueden alterar acceso o presentar decisiones; no implican clima dinámico ni cambios físicos automáticos. | Script/flags/eventos propios potenciales; compatibilidad y carga sin probar. |
| Perfiles, niveles y builds | Opciones RPG con rutas distintas pero campaña completables por cualquier perfil. | Skill Tree/RPG Series, Tierify y RPG Inventory **[SIN VERIFICAR]**; no se confirma que implementen clases, niveles o estadísticas requeridas. Sistema propio solo tras decisión y verificación. |
| Misiones y objetivos | Principales y secundarias desbloquean rutas, refugios, recursos, testimonios o condiciones finales, evitando recompensas repetitivas. | Questlog y FTB Quests **[SIN VERIFICAR]**; no se confirma que soporten estados y bifurcaciones necesarias. Puede requerir configuración/contenido propio. |
| Desenlaces | Cielo inmóvil, medido, libre o pactado cambian rutas, servicios, refugios y relaciones; final pactado exige testimonios y participación. | Requisitos de desenlace y persistencia son propuesta narrativa; implementación propia o sistema validado pendiente. |

### Desenlaces: consecuencias previstas

- **Cielo inmóvil:** rutas principales más estables y servicios de Liga; comunidades fuera de red aisladas, pérdida de recuerdos y menos rutas secundarias.
- **Cielo medido:** rutas principales previsibles y servicios de Cartógrafos; control compartido solo si hubo pruebas y acuerdos.
- **Cielo libre:** se rompen nodos; menos accesos bajo control y más rutas/refugios móviles; algunas comunidades pierden hogares.
- **Marea pactada:** testimonios y participación permiten separar nodos que trasladan peligro, dejando mecanismos locales voluntarios; conserva rutas/refugios diversos sin eliminar el riesgo.

## Candidatos, verificación y límites

Skill Tree/RPG Series, Tierify, RPG Inventory, Bosses of Mass Destruction, BetterEnd, When Dungeons Arise, Questlog y FTB Quests están **[SIN VERIFICAR]** para este proyecto. No se dispone de manifiesto ni archivos exactos; no se afirma versión, función, licencia, compatibilidad entre sí, con loader o con el equipo. Minecraft 1.20.1 + Fabric sigue pendiente de verificación. La propuesta no sube ni incorpora archivos de mods de terceros. No hay benchmarks locales. La ambientación y mecánicas descritas son diseño pendiente, no características técnicas confirmadas.
