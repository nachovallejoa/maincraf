# Diseño de mecánicas — La Marea de los Mil Soles

> **Estado: propuesta de diseño pendiente de aprobación final e implementación.** No confirma compatibilidad de mods ni correspondencia independiente con la historia aprobada. Las afirmaciones sobre nombres, escenas, decisiones y desenlaces quedan **[SIN VERIFICAR]** cuando la fuente de historia no está incluida. Los mods son candidatos, no selecciones aprobadas.

## Alcance, principios y pendientes

- Diseño revisado consolidado en esta versión. Clase, nivel, reputación o victoria en combate no deciden por sí solos rutas principales ni finales; las condiciones narrativas y el resultado de encuentro se guardan como estados distintos.
- Clases opcionales; ninguna clase pierde pruebas, decisiones, información necesaria o rutas principales. Pueden cambiar el modo de obtener o interpretar información.
- Regiones compactas, arenas controladas y pocos enemigos simultáneos. Evitar generación procedural pesada, movimiento físico de islas, cambios masivos de bloques, lógica continua por tick, entidades y efectos innecesarios.
- Minecraft 1.20.1 + Fabric es perfil provisional, pendiente de aprobación y verificación de instancia. Compatibilidad de mods, APIs y rendimiento: **[SIN VERIFICAR]**. Equipo objetivo declarado: Athlon 5150, Radeon R3 y HDD; RAM, sistema operativo, configuración completa y benchmarks no proporcionados.
- Valores de equilibrio y rendimiento no se presuponen. Propuesta autorizada como diseño, no como implementación.

## 1. Clases y atributos

Las clases describen estilos, no afiliaciones y no cambian por sí solas reputación, misiones o finales.

| Clase | Papel | Atributos que aprovecha | Vínculo temático, no afiliación |
|---|---|---|---|
| **Guardacorriente** | Defensa, protección y control del espacio; crea momentos seguros para observar o avanzar. | Vigor y Temple. | Afinidad temática con la Liga del Lastre; elegirla no apoya sus cierres ni altera relación. |
| **Vigía del Prisma** | Observación, movilidad y lectura de señales, terreno e información. | Percepción y Agilidad. | Afinidad temática con los Cartógrafos; no restringe el acceso a conocimiento ni implica apoyo. |
| **Rompeanclas** | Combate directo, presión contra guardianes y manipulación de mecanismos, con mayor riesgo. | Agilidad y Temple. | Afinidad temática con quienes cuestionan o alteran la Trama; no decide destruir nodos ni una postura narrativa. |

Atributos comunes propuestos:
- **Vigor:** salud y resistencia a interrupciones.
- **Agilidad:** recuperación entre acciones y movilidad de combate.
- **Percepción:** lectura de señales, oportunidades y elementos explorables.
- **Temple:** acciones técnicas, control de mecanismos y resistencia a efectos de combate.

Valores iniciales, límites, fórmulas, efectos cuantificados y coste/política de reinicio: pendientes; no inventados. Atributos y clases deben variar la respuesta, no eliminar pruebas ni información necesaria.

## 2. Árboles de habilidades y builds

Cada clase tiene tres ramas propuestas de cinco nodos (mejoras menores, técnica activa y especialización final como objetivo). No son llaves de misión. Se conservan los 29 puntos de habilidad propuestos y, como **parámetro inicial de pruebas**, se propone coste de tres puntos por nodo: 15 nodos costarían 45 puntos por clase, por lo que no se completan con 29. No es balance probado ni se presupone mezclar árboles de clases diferentes.

**Guardacorriente**
- **Baluarte:** mitiga presión al mantener posición y protege aliado/interacción. Build: *Muro de ruta*.
- **Ancla móvil:** recuperación tras esquiva/bloqueo y reposicionamiento. Build: *Escolta*.
- **Señal de repliegue:** técnica activa que interrumpe o distrae brevemente, gana espacio, no elimina grupos. Build: *Rescatista*.

**Vigía del Prisma**
- **Lectura de reflejos:** vuelve legibles algunas señales; los reflejos no son predicciones ciertas. Build: *Intérprete*.
- **Paso de corriente:** esquiva y reposicionamiento para atacar tras apertura. Build: *Navegante*.
- **Cartografía de campo:** señala pistas, rutas o mecanismos disponibles tras observar; no abre rutas contra condiciones narrativas. Build: *Explorador*.

**Rompeanclas**
- **Golpe de fractura:** premia atacar aperturas del guardián o mecanismo. Build: *Desestabilizador*.
- **Pulso de mecanismo:** mejora interacciones previstas en el encuentro, sin conceder acceso principal fuera de condiciones narrativas. Build: *Técnico*.
- **Ruptura controlada:** potencia concentrada tras una apertura con menor tolerancia al error. Build: *Asaltante*.

Se puede concentrar la inversión en una rama o repartirla entre dos; no se presupone completar las tres. Técnicas legibles y con recuperación clara. Todas las clases necesitan una respuesta viable en todos los encuentros; información o interacción imprescindible debe seguir accesible sin habilidad concreta.

## 3. Niveles, estadísticas y experiencia

- Nivel máximo propuesto: **30**.
- Un punto de atributo en cada nivel par del 2 al 30: **15 puntos**.
- Un punto de habilidad por cada subida tras nivel 1: **29 puntos** al nivel 30.
- XP para pasar de nivel L al siguiente: **100 + 25 × (L − 1)**. Suma para pasar de nivel 1 a 30: **13.050 XP**.
- No se requiere nivel para misiones principales, relación con facciones ni finales. La campaña principal debería dejar una build funcional sin secundarias, pero falta presupuesto de XP por acto; es objetivo por verificar, no garantía.
- No definidos: valores iniciales, límites y fórmulas de atributos, XP inicial, coste de reinicio y efectos cuantificados.

Fuentes propuestas: hitos principales, jefes o resolución alternativa válida, exploración relevante y secundarias de peso medio. Combate ordinario da XP menor y no debe ser fuente eficiente repetible. Intervalos iniciales de prueba: hito principal 450–700 XP; encuentro de jefe 500–800 XP; secundaria 150–300 XP; pista relevante 40–90 XP. No validados. Cada hito recompensa una sola vez; alternativa narrativa válida al jefe debe dar igual XP de encuentro que derrotarlo.

## 4. Equipamiento y rarezas

Equipo amplía opciones sin reemplazar progresión narrativa ni requerir repetición. Rarezas propuestas, no escala de poder validada:
1. **Corriente:** equipo común, estadística base, sin efecto extra.
2. **Afinado:** mejora pequeña o utilidad situacional.
3. **Singular:** efecto temático fijo, ligado a exploración, decisión o reto concreto.
4. **Reliquia de ancla:** objeto narrativo único; uso y adquisición deben respetar decisiones del acto.

Recompensas fijas y no repetibles; ningún objeto imprescindible depende de botín aleatorio. No se fijan magnitudes, límites ni efectos cuantificados por falta de balance. El equipo inicial puede seguir útil para una build adecuada.

- Prólogo/Cabo: equipo común y primera pieza Afinada posible por evacuación/faro/suministros; pieza de Trama narrativa, no botín aleatorio.
- Oria: utilidad de raíces/cultivos y posible Singular opcional ligada a investigación o encuentro.
- Dársena: herramientas/protección de archivos y refugios; recompensar pruebas y planes.
- Fosa: movilidad/supervivencia y recursos no repetibles.
- Nimbo: Singular ligado a registros/testimonios y expedición de Lena.
- Corona: mejoras de utilidad por rutas/nodos; Reliquia puede participar en resolución sin forzar final.

No duplicar pieza narrativa de Trama como recompensa del Mastín salvo que lo establezca la historia aprobada (**[SIN VERIFICAR]**). RPG Inventory se excluye del requisito inicial: añade ranuras, no rarezas. Tierify/TieredZ no seleccionados; versiones exactas y compatibilidad no verificadas.

## 5. Combate

Combate de señales legibles, posicionamiento y ventanas; errores ocasionales tolerables, desplazamiento sin penalización constante y sin escalado ilimitado de salud. Roles: hostigadores (flancos/reposición), defensores (bloqueo/protección), interrumpidores (ataque fuerte anunciado), vigías/apoyos (preparan ataques o alteran espacio), guardianes de mecanismo (protegen interacción, pueden tener alternativas contextuales). Encuentros ordinarios compactos, como máximo dos roles simultáneos.

- Guardacorriente: sostiene posición, protege interacción o crea repliegue.
- Vigía: reconoce señales y usa movilidad; no tiene visión infalible.
- Rompeanclas: interrumpe o concentra daño en apertura, con menos margen para combate prolongado.

Cada encuentro debe tener respuesta viable para las tres clases y alternativa no dependiente de técnica concreta. Better Combat y demás interoperabilidad no verificados.

## 6. Seis jefes propuestos

Son contenido propio propuesto, no mecánicas implementadas por mods. Arenas delimitadas, fases legibles, enemigos simultáneos acotados. Victoria no decide automáticamente consecuencias narrativas.

1. **Mastín de Lastre — Cabo de las Campanas:** guardián peligroso, no necesariamente maligno; carga anunciada y placas con apertura; mecanismo del faro puede frenar carga. XP y pista de rastreo de Flota. Consecuencias de evacuación sobre suministros, apoyo y contactos separadas del combate. Recompensa narrativa exacta **[SIN VERIFICAR]**.
2. **Madre de los Zarcillos Aéreos — Jardines de Oria:** raíces con ataques telegrafiados y aperturas; responder a criatura o entorno expone vínculo con ancla. XP/testimonio o recurso; no decide conservar, modificar o abandonar el ancla.
3. **Custodio de Remaches — Dársena:** defensa por sectores, patrón y arena abren oportunidades. Preparación, refugio y pruebas aportan contexto/alternativas. XP y acceso a archivo/refugio/prueba según preparación; victoria no automatiza decisión.
4. **Ballena de Lastre — Fosa:** corrientes atrapadas y restos alteran espacio; contención/interacción o combate; no es subordinada de Veyr ni necesariamente maligna. Despejar habilita ruta segura; dejarla permite avanzar por ruta más larga viable, sin bloquear acto. Relación de tripulaciones independiente.
5. **Corista Ciego — Nimbo:** señales y reflejos inciertos; distinguir aperturas sin asumir veracidad de escenas. XP y registros sobre expedición de Lena; decisión de compartir/reservar sigue separada.
6. **Almirante Sumergido / Veyr — Corona:** arena delimitada, fases claras y pocos enemigos; presión sobre nodos/Trama. Condiciones previas pueden permitir matar a Veyr, apartarlo del núcleo o persuadirlo para soltar la Trama. XP final; no fija por sí solo uno de los cuatro finales. Relación con Flota es un estado aparte; conexión histórica Almirante–Veyr **[SIN VERIFICAR]**.

Bosses of Mass Destruction añade jefes distintos y no sustituye estos encuentros; su uso no se recomienda para cubrir la campaña.

## 7. Reputación y facciones

Escala propuesta −2 a +2 para cuatro facciones, sin cambios por matar enemigos. Cambios por decisión y umbrales no definidos: hasta documentarlos, reputación no es requisito de ruta/final ni autoridad única. Registrar rutas, refugios, pruebas, testimonios y condiciones como estados específicos.

- **Liga del Lastre — Tavia Renn:** apoyo puede facilitar refugios/suministros/rutas seguras; cierres pueden trasladar peligro.
- **Cartógrafos del Prisma — Maela Orin:** cooperación facilita mapas/testimonios; compartir puede ayudar y concentrar poder.
- **Hermandad del Vaivén — Saira Nume:** confianza facilita rutas/decisiones comunitarias, no garantiza supervivencia universal.
- **Flota Sumergida — Ilyan Veyr:** estado refleja divisiones de tripulaciones; no las convierte a todas en enemigas/aliadas. Separar relación con tripulaciones, condiciones narrativas y resultado del encuentro final.

Efectos posibles: comercio moderado no imprescindible; refugios con descanso/información/apoyo no obligatorio; rutas facilitadas pero no controladas por una sola facción; reputación puede aportar apoyo/testimonios/legitimidad, nunca determinar final sola. Village Diplomacy se refiere a aldeas/villagers, no es equivalente a estas facciones.

Cuatro finales propuestos; correspondencia con canon **[SIN VERIFICAR]** por falta de historia aprobada independiente:
- **Cielo inmóvil:** Liga fija rutas; reduce peligro inmediato, puede excluir comunidades y costar recuerdos.
- **Cielo medido:** control compartido de Cartógrafos con pruebas y acuerdos; reputación no sustituye evidencia.
- **Cielo libre:** romper nodos devuelve corriente natural; no requiere enemistad con todas las facciones, implica rutas/refugios móviles y posibles hogares perdidos.
- **Marea pactada:** testimonios compartidos, comunidades afectadas y condiciones técnicas pendientes; reputación no garantiza pacto.

## 8. Progresión por actos

Bandas orientativas, no requisitos de acceso ni resultados garantizados. Falta suma de XP por acto y prueba de campaña sin secundarias.

| Parte | Nivel orientativo | Foco y dificultad prevista |
|---|---:|---|
| Prólogo — Cabo de las Campanas | 1–4 | Evacuación, faro, pieza, Mastín y rastreo; baja-moderada, enseñar señales/entorno. |
| I — Jardines de Oria | 4–8 | Raíces, ancla y elección; moderada, amenazas localizadas. |
| II — Dársena de los Remaches | 8–12 | Mapas, archivos, refugio, planes/pruebas ante Custodio; moderada. |
| III — Fosa de Marea | 12–17 | Tripulación, barrios y Ballena; ruta segura o larga viable; moderada con picos breves, sin enjambres. |
| IV — Nimbo de Vidrio | 17–22 | Lena, registros y Corista; moderada, señales ambiguas legibles. |
| V — Corona de Espejos | 22–30 | Nodos, Veyr y finales; moderada/final, arena y presión acotadas. |

## 9. Misiones principales y secundarias

Correspondencia con historia aprobada independiente **[SIN VERIFICAR]**. Principales propuestas: (1) evacuar Cabo, explorar faro, resolver Mastín y rastrear Flota; (2) investigar raíces/ancla y escoger conservar, modificar o abandonar; (3) obtener mapas, pruebas, refugio y alternativas ante Custodio; (4) descender a Fosa, conocer tripulación y decidir Ballena/ruta larga; (5) recuperar registros de Lena y decidir compartir/reservar; (6) llegar a Corona, resolver nodos/Veyr y final por condiciones acumuladas.

Dos a cuatro secundarias por acto, de funciones distintas: abrir ruta/refugio no obligatorio, aportar testimonio/registro, recurso no imprescindible, apoyo comunitario, relación con personaje/facción y desacuerdos internos. Sin encargos repetidos de recolección/combate como XP eficiente. Secundarias cambian estados/apoyos/información, no son necesarias para terminar ni imponen una opción “correcta”. Acto V sin objetivos concretos documentados: quedan pendientes, no se inventan.

Ember’s Questing y Mebahel’s RPG son candidatos parcialmente solapados; no se propone instalarlos juntos ni otorgar autoridad duplicada sobre diario, flags o recompensas. Requisitos y compatibilidad: **[SIN VERIFICAR]**.

## 10. Implementación y criterio de aceptación

Mantener el estado narrativo actualizado por eventos, no revisión continua. Antes de implementar: confirmar instancia Fabric/versiones; verificar persistencia y migración; ninguna clase/nivel/reputación/secundaria bloquea historia; impedir recompensas duplicadas/estados contradictorios; presupuestar XP y probar campaña sin secundarias y sin farmear; respetar límites de arenas y actividad; escoger un único responsable del diario/recompensas; medir incrementalmente en equipo objetivo. No hay benchmarks ni garantías de FPS, carga o compatibilidad.

Pendientes explícitos: contrastar nombres/escenas/facciones/finales con historia aprobada (fuente no incluida); aclarar relación Almirante–Veyr; definir atributos iniciales, XP por acto y XP por actividad, balance/builds solitarias, costes/requisitos de nodos, recompensas concretas, condiciones técnicas de finales, secundarias del Acto V, ámbito de guardado, versiones/dependencias/licencias/APIs y pruebas locales.
