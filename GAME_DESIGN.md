# Diseño de juego — La Marea de los Mil Soles

> **Estado: propuesta de diseño pendiente de aprobación e implementación.** No confirma compatibilidad entre mods, rendimiento ni correspondencia independiente con la historia aprobada. Los datos marcados **[SIN VERIFICAR]** o pendientes no se completan por inferencia.

## Alcance y principios

Se conservan regiones compactas, transiciones controladas, seis encuentros de jefe, secundarias de peso medio y cuatro desenlaces según la propuesta. Las clases son perfiles, no facciones, y ninguna bloquea misiones. La Ballena no está subordinada a Veyr; las visiones no son certezas; el equipo no determina por sí solo un desenlace. La conexión entre el Almirante Sumergido y Veyr queda **[SIN VERIFICAR]**. Tratar la Ballena como encuentro de jefe/decisión, no como combate obligatorio.

Un único propietario para niveles/estadísticas, un solo árbol de habilidades como base y un sistema de misiones. Reputación, decisiones persistentes, rutas y jefes específicos requieren implementación o integración aún no verificada. Los mods son candidatos, no selecciones aprobadas.

## Clases

| Clase | Función | Estadísticas principales | Relación narrativa |
|---|---|---|---|
| **Guardacorrientes** | Defensa, protección y control de espacio; aguanta presión, cubre aliados y crea oportunidades para mecanismos. | Vigor y Temple. | Puede colaborar con la Liga del Lastre; no implica pertenencia ni prioridades compartidas. |
| **Vigía del Prisma** | Observación, precisión y lectura del campo; detecta señales y orienta exploración. | Percepción y Técnica. | Afinidad temática con mapas/registros de los Cartógrafos, sin membresía obligatoria. |
| **Rompeanclas** | Combate directo y manipulación de mecanismos mediante fuerza, herramientas u oficio. | Técnica y Vigor. | Encaja con maquinaria y nodos, sin imponer afiliación ni violencia como solución universal. |

Diferenciación a probar: Guardacorrientes prioriza defensa/apoyo; Rompeanclas, presión y acciones comprometidas; Vigía, precisión e información. Deben ser viables en solitario. La lectura del Vigía no da daño gratis ni resuelve automáticamente encuentros.

## Árboles de habilidades y arquetipos

Tres ramas propuestas por clase; nodos, rangos, costes y requisitos concretos pendientes. Las habilidades no son requisitos exclusivos de misiones; obstáculos principales admiten interacción alternativa, objeto o ruta.

### Guardacorrientes
- **Baluarte:** reducir daño, proteger a un aliado cercano, resistir interrupciones y sostener posición ante ataques telegrafiados.
- **Control de corriente:** frenar/apartar enemigos, interrumpir cargas señaladas y crear zonas seguras breves.
- **Vigilia del refugio:** recuperación entre encuentros, detección de rutas peligrosas y opciones defensivas al usar mecanismos.
- Arquetipos no balanceados: **Baluarte** (aguante/protección, menos daño), **Interdictor** (interrupción/espacio dependientes de lectura), **Escolta** (protección y utilidad).

### Vigía del Prisma
- **Lectura del reflejo:** marcar vulnerabilidades, distinguir señales y revelar pistas de orientación; no convierte visiones en certeza.
- **Tiro de precisión:** ataques fiables contra blancos marcados y herramientas para ventanas breves.
- **Cartografía práctica:** buscar desvíos, mecanismos y testimonios sin revelar automáticamente la solución.
- Arquetipos: **Tirador** (precisión a un objetivo, vulnerable si no aprovecha ventanas), **Analista** (información/apoyo, daño moderado), **Explorador** (observación, rutas y combate).

### Rompeanclas
- **Impacto:** golpes comprometidos contra armaduras, piezas expuestas y mecanismos vulnerables.
- **Desmontaje:** interrumpir acciones mecánicas y abrir oportunidades al manipular dispositivos.
- **Oficio de campo:** reparar, forzar o activar dispositivos durante exploración y encuentros.
- Arquetipos: **Quebrador** (oportunidad contra protegidos, más exposición), **Ingeniero** (mecanismos/guardianes, menos daño directo), **Vanguardia** (presión y supervivencia en espacios cerrados).

## Niveles y estadísticas

Nivel máximo propuesto: 30. XP para pasar de nivel L al siguiente: **100 + 35 × (L − 1)**. Ejemplos: 1→2 = 100 XP; 10→11 = 415 XP. La suma de umbrales 1→30 (niveles 1 a 29) es **17.110 XP**. Cada nivel ganado concede 1 punto de estadística y 1 punto de habilidad. Asignación inicial en nivel 1: pendiente, no presupuesta.

La campaña principal debe bastar para progresar; secundarias son alternativas y no requisitos de nivel obligatorio. No XP repetible por matar indefinidamente enemigos comunes. XP por misión, descubrimiento, encuentro y jefe no está especificada, por lo que no se garantiza alcanzar nivel 30 sin repetición.

- **Vigor:** salud máxima y resistencia a daño físico.
- **Técnica:** eficacia de armas, herramientas y acciones contra mecanismos.
- **Percepción:** precisión, lectura de señales y detección de oportunidades.
- **Temple:** estabilidad ante interrupciones y eficacia defensiva/de apoyo.

Fuentes propuestas: objetivos principales, secundarias, descubrimientos relevantes, resolución de encuentros con recompensa fija moderada y primera victoria de jefe con recompensa importante. Beneficios y curva requieren pruebas; no hay cifras que demuestren equilibrio o viabilidad solitaria.

## Equipo y rarezas

Rarezas fijas y legibles; cambian principalmente la función, no multiplican daño:
- **Común:** equipo inicial fiable y reparable.
- **Mejorado:** ventaja clara y moderada.
- **Raro:** habilidad/especialización reconocible.
- **Reliquia:** pieza singular ligada a decisión, jefe o descubrimiento; no superior para todas las builds.

Equipo relevante por misiones, exploración controlada, comercio o jefes, no por farmeo aleatorio. Progresión por acto: Prólogo, equipo común y mejora sencilla ligada al faro/evacuación y pieza del Mastín; Oria, supervivencia, plaga, cultivos y ancla; Dársena, equipo mecánico/defensivo, comercio o planos; Fosa, rutas peligrosas, comunidad y comercio de flota; Nimbo, observación y registros; Acto V, mejoras finales de nodos, misiones y preparación. Las decisiones cambian recursos/apoyos descritos, no cierran facciones ni determinan desenlace. Objetos, estadísticas y cantidades no especificados siguen pendientes.

## Combate

Encuentros normales con pocos enemigos simultáneos, espacio para leer señales y, si corresponde, salida o solución contextual. Roles de diseño (no mobs atribuidos a mods): hostigador, defensor, tirador/lanzador, mecánico y guardián pesado. Ataques anunciados y cobertura/alternativas legibles.

- Guardacorrientes sostiene línea, protege durante señales y crea ventana segura; menor daño sostenido que Rompeanclas.
- Vigía identifica blancos/señales, castiga a distancia y evita algunos peligros; más vulnerable acorralado. Información no resuelve automáticamente.
- Rompeanclas presiona objetivos resistentes y altera dispositivos asumiendo riesgo.

Todos los jefes deben poder abordarse en solitario con cada clase: objetivo de diseño por probar, no balance verificado. Sin cifras de vida, daño, recursos o ventanas no se demuestra la dificultad.

## Seis encuentros de jefe propuestos

No se adjunta una fuente independiente de historia para verificar nombres/eventos; la correspondencia queda **[SIN VERIFICAR]**. Mecánicas y recompensas son diseño, no contenido de mods. Recompensas aportan progreso, no seleccionan desenlace.

1. **Mastín de Lastre — Cabo de las Campanas.** Guardián peligroso, no necesariamente maligno. Carga señalada, presión frontal y placas con abertura breve; mecanismo del faro puede frenar una carga. Fases: aprender patrón, luego gestionar ventanas menores sin carrera de daño. Recompensa descrita: pieza del mecanismo y materiales de mejora temprana; decidir quién conserva pieza es narrativo. Avanza investigación del faro/flota.
2. **Madre de los Zarcillos Aéreos — Jardines de Oria.** Protectora de raíces ligadas al ancla. Zonas de raíces señaladas; atacar apertura, reposicionarse o usar anclaje para pausa; no es obligatorio dañar raíces indiscriminadamente. Foco: control espacial y anclaje. Recompensa: testimonios/recursos del ancla; no decide su destino. Avance a registros/rutas de Oria.
3. **Custodio de Remaches — Dársena.** Seguridad de la Liga llevada al extremo. Pistones anunciados, defensa frontal y remaches desactivables/expuestos en pausa; ángulo, bloqueo o mecanismo. Foco: defensa frontal y ciclo mecánico, diferenciado de Madre. Recompensa: planos/materiales. No obliga a publicar pruebas o negociar primero.
4. **Ballena de Lastre — Fosa.** Criatura afectada por corrientes atrapadas, no subordinada a Veyr. Encuentro de contención/decisión, no matar obligatoriamente. Trayectorias cambian espacio seguro; señales permiten refugiarse, abrir paso o retirarse. Resolver por interacción o combate contenido. Recompensa: ruta elegida e información; ayudar comunidad abre comercio/misiones de flota descritas. Ahuyentarla implica ruta más larga.
5. **Corista Ciego — Nimbo de Vidrio.** Guardián de registros que muestran que las visiones no son certezas. Pulsos sonoros y reflejos; leer ritmo, dirección o cobertura, sin asumir veracidad de escenas. Fases de aprender pulsos y combinar lectura/aperturas con señales contradictorias. Recompensa: registros y comparación con testimonios; avance a tres futuros posibles y elección de destinatario.
6. **Almirante Sumergido — Corona de Espejos/Atrio.** Antagonista final que pretende fijar una versión del mundo. Relación con Veyr: **[SIN VERIFICAR]**. Arena delimitada; reflejos/entidades acotados. Fases: órdenes y ataques, interrumpir/sobrevivir mando, disputar núcleo en ventanas anunciadas. Apoyos previos abren ayudas sin sustituir combate. Recompensa: acceso a la elección descrita (matar a Veyr, apartarlo del núcleo o persuadirlo para soltar Trama); no elige opción. Requisitos de los cuatro desenlaces pendientes.

La Madre y el Custodio comparten mecanismos/interrupción pero sus focos difieren como arriba. Recompensas más concretas para Mastín y Corista; no inventar objetos/estadísticas/cantidades para otros. Sin multitudes permanentes; riesgo de entidades/IA/efectos finales requiere medir.

## Reputación y facciones

Cuatro valores separados propuestos: Liga del Lastre (incl. Tavia Renn), Cartógrafos del Prisma (Maela Orin), Hermandad del Vaivén (Saira Nume), Flota Sumergida (lealtades diversas, no bloque enemigo). Escala 0–100 solo formato provisional; valores, cambios y umbrales pendientes. Una decisión puede alterar relaciones distintas, sin enemistad automática.

Efectos propuestos: comercio y suministros moderados; servicios/refugios/testimonios; apoyos o información para transiciones controladas; apoyo final condicionado a misiones/decisiones pero no universalmente obligatorio. Nunca impedir equipo básico/campaña. No hay umbral de reputación fijado para final. Ámbito de guardado (jugador, mundo/equipo o mixto) pendiente.

Se conservan cuatro nombres de propuesta: **Cielo inmóvil, Cielo medido, Cielo libre y Marea pactada**. Testimonios y decisiones de varios actos pueden contribuir; requisitos cuantificados no definidos y no se derivan automáticamente de reputación, equipo o victoria. Correspondencia con historia aprobada **[SIN VERIFICAR]**.

## Progresión por actos y dificultad orientativa

| Acto | Rango orientativo | Progresión | Dificultad prevista (objetivo, no prueba) |
|---|---:|---|---|
| Prólogo — Cabo | 1–4 | Evacuación, faro, Mastín, pieza y flota. | Baja-moderada; señales sencillas, pocos enemigos. |
| I — Jardines de Oria | 4–9 | Cultivos, ancla, plaga y registros; elección altera consecuencias locales/suministros. | Moderada; espacio y peligros localizados. |
| II — Dársena | 9–15 | Refugio, comercio, Liga, planos, pruebas o negociación. | Moderada; defensores/mecanismos con opciones de evitar/interrumpir. |
| III — Fosa | 15–21 | Ballena, comunidad, reconstrucción de la Noche. | Moderada-alta controlada; posición/rutas, sin enjambres. |
| IV — Nimbo | 21–26 | Corista, comparación de futuros y compartir hallazgos. | Moderada-alta; señales contradictorias sin azar injusto. |
| V — Corona/Atrio | 26–30 | Nodos, rutas, apoyos, confrontación y desenlace. | Alta dentro del equilibrio objetivo; fases legibles y presión acotada. |

Rangos se solapan como transición y no son niveles obligatorios. No exigir secundarias ni repetir enemigos para entrar en actos. Campaña principal debe bastar en XP; recompensas XP por actividad pendientes. Rutas por estados/transiciones controladas; sin generación procedural ni dimensión nueva.

## Misiones y secundarias

Registro presenta objetivos, pistas y consecuencias sin declarar una decisión correcta. Decisiones persistentes afectan refugios, suministros, testimonios y apoyos. Modelo de guardado individual/equipo/mixto pendiente.

- **Prólogo:** evacuar y priorizar; explorar faro; vencer Mastín y decidir pieza; rastrear flota/contacto.
- **Acto I:** cultivos resistentes; hallar ancla; contener plaga; decisión con Madre; comparar registros de Lena.
- **Acto II:** investigar zonas afectadas; asegurar refugio; desactivar Custodio/planos; pruebas o negociación con Tavia.
- **Acto III:** llegar a Fosa; ayudar comunidad; abrir/evitar paso Ballena; versiones de flota; reconstruir Noche y decidir revelar coste.
- **Acto IV:** ruta real entre reflejos; ocultación de expedición de Lena; registros Corista; comparar tres futuros y decidir destinatario.
- **Acto V:** llegada conjunta o alternativa; activar/desviar/destruir nodos; comprender red; reconstruir sacrificio; detener a Veyr y elegir futuro.

Secundarias de peso medio, no obligatorias: Oria — *Huerto de nombres*, *Cosecha compartida*, *Luz prestada*; Dársena — *Grúa de nadie*, *Una pieza, dos promesas*, *Nombres del registro*; Fosa — *Nombre del barco*, *Precio del oxígeno*, *Puerta que sube*; Nimbo — *Árbol que recuerda mal*, *Expedición incompleta*, *Mapa para todos*. Acto V lista temas por facción (Liga: emergencia/anclas/guardia expuesta; Cartógrafos: mapas/luz de Lena/límites cristal; Hermandad: convoy/refugio/ruta regreso; Flota: orden/promesa Veyr/guardia Kest), pero nombres/objetivos concretos no provistos: pendientes, no inventados.

Questlog y FTB Quests son alternativas candidatas, solapadas; elegir uno. Integración con estados de campaña no verificada. La auditoría suministrada indica que FTB Quests 2001.4.22 no queda acreditada con las mismas funciones que la evidencia de ramas exclusivas 2001.4.13; dependencias/API/licencia de redistribución requieren verificar. No afirmar equivalencia con diálogo ramificado o campaña lista.

## Mods, validación y límites

Candidatos, versiones, funciones, dependencias, licencias, compatibilidad y API solo según auditoría aportada; no son instalación/selección aprobada. Skill Tree y Simply Skills: escoger como máximo un árbol externo, ninguno acredita estas clases. PlayerEX y sistema propio: un propietario de progresión. Questlog/FTB Quests: uno. RPG Inventory/Reforged: no combinar sin función diferenciada y pruebas. Bosses of Mass Destruction/Remnants no sustituyen encuentros; Remnants añade dimensión no necesaria. Village Diplomacy no representa las cuatro facciones. No hay API de integración confirmada.

No hay mediciones en Athlon 5150, Radeon R3 ni HDD: FPS, frametime, memoria, carga, arranque, estabilidad y compatibilidad **[SIN VERIFICAR]**. Regiones compactas, pocos enemigos y arenas delimitadas se mantienen; jefe final con reflejos/IA/efectos es riesgo principal, aún sin cuantificar. Implementar jefes, estados, reputación, rutas y clases es trabajo de desarrollo importante, no simple configuración de árbol/misiones. No subir archivos de mods de terceros.

Pendientes explícitos: contrastar nombres/eventos/facciones/desenlaces con historia aprobada adjunta; aclarar relación Almirante-Veyr; definir asignación inicial nivel 1, XP por actividad y balance; definir nodos/requisitos de ramas; recompensas específicas aún no descritas; condiciones mecánicas de cuatro finales; secundarias Acto V; ámbito de guardado; verificar builds/dependencias/licencias/APIs y probar rendimiento antes de aprobación/implementación.
