# Diseño de juego

> **Estado: propuesta de diseño pendiente de aprobación e implementación.** No certifica contenido de Minecraft, disponibilidad o compatibilidad de mods, ni rendimiento.

## Identidad RPG elegida

Se conserva como base **La Marea de los Mil Soles**, fantasía oscura y misterio en un archipiélago celeste, combinada con la preferencia del usuario por progresión RPG. La Cartografía de la Ceniza queda en reserva. La identidad y las preferencias no son una selección técnica de mods.

### Pilares y preferencias

| Pilar | Dirección de diseño | Estado |
|---|---|---|
| Combate y exploración | Ambos importantes; explorar rutas, testimonios y reflejos, y combatir guardianes con dificultad equilibrada. | Preferencia; balance sin pruebas. |
| Progresión | Clases definidas y opcionales, niveles/estadísticas y árboles/builds como objetivos. | Sistemas y cifras pendientes. |
| Supervivencia | Riesgo moderado; no convertir cada desplazamiento en castigo. | Calibración pendiente. |
| Mundo | Islas y regiones compactas conectadas por rutas controladas. | Propuesta; generación e implementación no confirmadas. |
| Consecuencias | Decisiones alteran confianza, rutas, refugios, suministros y condiciones de desenlace. | Estados y lógica pendientes. |

Perfiles narrativos opcionales: Guardacorrientes (resistencia/protección), Vigía del Prisma (observación/rutas) y Rompeanclas (combate/mecanismos). Ninguna clase debería bloquear misiones principales.

## Impacto de la historia en el juego

Lo siguiente describe el efecto jugable deseado si la historia se implementa; no afirma que esté disponible. Las zonas se plantean acotadas, sin multitudes, generación procedural pesada, movimiento automático de islas ni cambios masivos de bloques. Jefes con arena controlada y pocos enemigos simultáneos. Son precauciones para el Athlon 5150, Radeon R3 integrada, 12 GB instalados (aprox. 9,9 GB utilizables según datos recibidos) y HDD, no garantías: no hay benchmarks locales.

| Elemento narrativo | Impacto deseado en el juego | Dependencias / implementación pendiente |
|---|---|---|
| Archipiélago, venas y Mar de Nubes | Zonas compactas, rutas desbloqueables y transiciones; riesgo moderado de navegación. | Minecraft 1.20.1 + Fabric perfil provisional **[SIN VERIFICAR]**. BetterEnd y When Dungeons Arise **[SIN VERIFICAR]**; no se presupone que provean estas regiones. Posible construcción/configuración propia. |
| Trama de Anclas y ciclos de Marea | Estados narrativos abren/cierran rutas y presentan hitos; no hacen falta clima dinámico ni movimiento físico de islas. | Questlog y FTB Quests **[SIN VERIFICAR]** como candidatos de misiones. Flags, transiciones y lógica podrían requerir contenido propio. |
| Facciones (Liga, Cartógrafos, Hermandad, Flota) | Confianza/apoyo desbloquea suministros, refugios, contactos y alternativas; no exige alineamiento único para terminar. | Reputación y estados persistentes no confirmados; candidatos de quests no equivalen a reputación. Posible sistema propio. |
| Evacuación de Cabo | La prioridad elegida determina quién recibe suministros y contacto para viajar a Oria. | Flags de campaña y consecuencias: implementación propia o sistema compatible por verificar. Evitar simular multitudes. |
| Ancla de Oria | Conservar mantiene ruta/suministro de Liga pero riesgo local; modificar equilibra; abandonar requiere traslado y reduce suministro. Semillas pueden abrir ayuda posterior. | Misiones/flags de Questlog o FTB Quests **[SIN VERIFICAR]**; lógica de dependencias posiblemente propia. |
| Dársena y pruebas | Publicar registros mejora confianza comunitaria; negociar conserva canal con Tavia y demora difusión. Planos habilitan opciones posteriores. | Estados de campaña y servicios requieren implementación; no se confirma mod candidato que cubra todos los efectos. |
| Fosa y Ballena | Refugios/testimonios abren recursos y diálogo con tripulaciones; evitar la criatura deja ruta más larga, vencerla despeja paso. | Regiones/encuentros son contenido propuesto. Bosses of Mass Destruction **[SIN VERIFICAR]**, sin atribuirle la Ballena. Si no hay solución compatible, jefe y lógica propios. |
| Nimbo y reflejos | Registros muestran futuros posibles, nunca certezas; compartir aumenta transparencia e informa a Veyr, reservar reduce transparencia. | Mapas, decisiones y estados narrativos son contenido propio pendiente; ningún candidato confirmado. |
| Jefes | Mastín, Madre de los Zarcillos, Custodio, Ballena, Corista y Veyr protegen lugares/decisiones con patrones legibles y encuentros acotados. | Bosses of Mass Destruction **[SIN VERIFICAR]** y no se afirma que contenga ninguno. Posibles jefes propios, sin archivos de mods de terceros. |
| Eventos de Marea | Hitos narrativos pueden alterar acceso o presentar decisiones; no implican clima dinámico ni cambios físicos automáticos. | Scripts/flags/eventos propios potenciales; compatibilidad y carga sin probar. |
| Perfiles, niveles y builds | Opciones RPG con rutas distintas, campaña completable por cualquier perfil. | Skill Tree/RPG Series, Tierify y RPG Inventory **[SIN VERIFICAR]**; no se confirma que implementen clases, niveles o estadísticas requeridas. Sistema propio solo tras decisión y verificación. |
| Misiones y objetivos | Principales y secundarias desbloquean rutas, refugios, recursos, testimonios o condiciones finales, evitando recompensas repetitivas. | Questlog y FTB Quests **[SIN VERIFICAR]**; no se confirma soporte de estados y bifurcaciones necesarios. Puede requerirse contenido/configuración propia. |
| Desenlaces | Cielo inmóvil, medido, libre o Marea pactada alteran rutas, servicios, refugios y relaciones. El pactado exige pruebas y participación comunitaria. | Requisitos y persistencia son propuestas narrativas; implementación propia o sistema validado pendiente. |

### Desenlaces y requisitos propuestos

- **Cielo inmóvil:** rutas principales más estables y servicios de la Liga; comunidades fuera de red aisladas, pérdida de recuerdos y menos rutas secundarias.
- **Cielo medido:** rutas previsibles y servicios de Cartógrafos; control compartido solo con pruebas y acuerdos.
- **Cielo libre:** nodos rotos, menos accesos bajo control, más rutas/refugios móviles; algunas comunidades pierden hogares.
- **Marea pactada:** testimonios y participación permiten separar nodos que trasladan el peligro y dejar mecanismos locales voluntarios; no elimina el riesgo.

## Decisiones del usuario sobre la historia

La historia fue aprobada como base sin cambios. Las respuestas de impacto jugable registradas son:

- **Pregunta 4 — Desenlaces: 4A.** Mantener los cuatro; el pactado es más exigente, no un final perfecto.
- **Pregunta 5 — Jefes: 5A.** Mantener los seis propuestos.
- **Pregunta 6 — Misiones secundarias: 6B.** Peso medio: algunas desbloquean rutas, recursos, testimonios o apoyos para el final.

Las opciones son decisiones narrativas del usuario, no aprobación técnica ni compromiso de implementación. Los sistemas de progresión, compatibilidad de mods, versiones y rendimiento continúan pendientes.

## Desenlaces: consecuencias previstas

- **Cielo inmóvil:** rutas principales más estables y servicios de Liga; comunidades fuera de red aisladas, recuerdos perdidos y menos rutas secundarias.
- **Cielo medido:** rutas previsibles y servicios de Cartógrafos; control compartido solo si existen pruebas y acuerdos.
- **Cielo libre:** nodos rotos, menos accesos controlados y más rutas/refugios móviles; algunas comunidades pierden hogares.
- **Marea pactada:** pruebas y participación permiten separar nodos que trasladan peligro y mantener mecanismos locales voluntarios; el riesgo permanece.

## Candidatos, verificación y límites

Skill Tree/RPG Series, Tierify, RPG Inventory, Bosses of Mass Destruction, BetterEnd, When Dungeons Arise, Questlog y FTB Quests están **[SIN VERIFICAR]** para este proyecto. No se dispone de manifiesto ni archivos exactos; no se afirma versión, función, licencia, compatibilidad mutua, con loader o equipo. Minecraft 1.20.1 + Fabric sigue pendiente de verificación. La ambientación y mecánicas descritas son propuestas, no características técnicas confirmadas. No hay benchmarks locales.
