# Arquitectura

> **Estado:** propuesta documental; pendiente de aprobación e implementación. No hay código ni integración confirmada. Las alternativas/mods y sus APIs permanecen **[SIN VERIFICAR]**.

## Límites generales

Se propone un único mod propio modular, con responsabilidades separadas; no son nombres definitivos. Elegir un propietario para niveles/estadísticas, un árbol de habilidades base y un sistema de misiones. Evitar guardar el mismo estado duplicado entre módulos y sistemas externos. Modelo de progreso (jugador, mundo/equipo o mixto) pendiente. Mantener regiones compactas, transiciones controladas y ningún requisito de dimensión procedural. No subir archivos de mods de terceros.

## Mods propios candidatos

| Módulo candidato | Responsabilidad / datos | Configuración prevista | Alternativas externas (no selección aprobada) | Dificultad / riesgo cualitativo |
|---|---|---|---|---|
| **Núcleo de campaña** | Decisiones, hitos, testimonios, ayudas y situación persistente. | Identificadores de estados y condiciones declarativas; requisitos de desenlace por definir. | Un sistema de misiones: Questlog o FTB Quests. Integración/API no verificada. | Media-alta; riesgo de ejecución esperado bajo si actualiza solo por eventos, no medido. |
| **Reputación de facciones** | Valores separados para Liga, Cartógrafos, Hermandad y Flota; cambios por decisiones/misiones. | Escala, cambios y efectos en servicios, comercio, testimonios y apoyos. Sin umbrales de finales aún. | Village Diplomacy se refiere a aldeas según auditoría, no reemplaza estas facciones. | Media; pocos datos/cambios puntuales; riesgo no medido. |
| **Rutas y accesos controlados** | Estados de transiciones disponibles/usadas, habilitadas por campaña. | Referencias a transiciones construidas y estados de acceso; sin generación procedural. | Registro de misiones puede mostrar objetivos, pero la lógica física sería propia. | Media; activación al interactuar/cambiar ruta; no medido. |
| **Clases y habilidades de campaña** | Clase seleccionada y rangos; tres perfiles y ramas sin bloquear misiones. | Bonificaciones, rangos, requisitos y balance ajustables; evitar progresión duplicada. | Como máximo un árbol externo entre Simply Skills y Skill Tree (RPG Series), o implementación propia. No se verificó API ni equivalencia. | Alta para árbol completo; media para selección/bonificaciones sencillas; riesgo no medido. |
| **Niveles y estadísticas (alternativa)** | Ser propietario de nivel, XP, puntos y Vigor, Técnica, Percepción, Temple solo si no se elige un proveedor externo adecuado. | Nivel máximo, curva, fuentes de XP y límites, sujetos a pruebas. | PlayerEX como candidato; escoger un único propietario, no duplicar atributos/puntos. | Media-alta por integración de combate/guardado; riesgo local no medido. |
| **Encuentros y seis jefes** | Fases, ataques señalados, victoria, recompensas y estado de jefe. Las decisiones narrativas son del Núcleo. | Daño, ventanas, fases, límites de entidades/reflejos, recompensas y señales pendientes de pruebas. | Better Combat solo para parte del combate cuerpo a cuerpo si se valida. Bosses of Mass Destruction y Remnants no sustituyen los encuentros; Remnants añadiría dimensión no requerida. Todo candidato/no verificado. | Alta; riesgo medio previsto, alto y localizado para reflejos/IA/efectos del Almirante; no medido. |
| **Objetos narrativos y recompensas controladas** | Piezas únicas, recompensas de jefe, planos y equipo ligado a misiones/decisiones; prevenir duplicados si aplica. | Función, rareza fija y obtención por acto. Sin tiers aleatorios no aprobados. | RPG Inventory para espacios y Reforged para tiers según auditoría; sus usos no equivalen a contenido narrativo. No combinar sin función diferenciada/pruebas. | Baja-media para contenido estático; no medido. |
| **Integración de misiones** | Conectar objetivos con campaña, reputación, rutas y recompensas únicamente si el sistema elegido lo permite. | Mapeos declarativos; conservar fuente única de texto/objetivos y no duplicar editor. | Elegir Questlog o FTB Quests. API, dependencias, integración y licencia de distribución por verificar. | Media-alta por incertidumbre de integración; carga por eventos esperada baja, no medida. |

## Dependencias y cuestiones por resolver

- No se ha verificado una API entre Questlog, FTB Quests, PlayerEX, Simply Skills o Skill Tree y el diseño.
- Definir ámbito de guardado de campaña/reputación y comportamiento en mundos compartidos.
- Elegir propietarios únicos para progresión, árbol y misiones antes de implementar.
- Las condiciones mecánicas de los cuatro desenlaces, XP por actividad, rangos/costes de nodos y recompensas específicas no están definidos.
- Candidatos, compatibilidad, versiones, dependencias, licencias y rendimiento del conjunto siguen pendientes. No inferir coste medido a partir de tamaño de archivo o etiquetas del mod.
- Validar en instancia autorizada y hardware objetivo antes de estimar rendimiento. No añadir dimensión nueva ni multitudes permanentes.
