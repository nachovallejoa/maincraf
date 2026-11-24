# Arquitectura

> **Estado:** propuesta documental, pendiente de aprobación e implementación. No contiene código ni integración confirmada. Alternativas externas, versiones y APIs quedan **[SIN VERIFICAR]**.

## Límites generales

Se propone un único mod propio modular, con responsabilidades separadas y fuente de estado coherente. Los nombres son candidatos, no definitivos. Evitar estado duplicado entre módulos y sistemas externos. Modelo de progreso (jugador, mundo/equipo o mixto) pendiente. Regiones compactas y transiciones controladas; sin generación procedural pesada. Nunca incorporar binarios/JAR de terceros al repositorio.

## Mods propios candidatos

Las dificultades y riesgos son valoraciones cualitativas, no calendarios ni benchmarks.

### 1. Núcleo de campaña y persistencia
- **Responsabilidad:** fuente compartida para estado de campaña, identificar partida/jugador, guardar y recuperar progreso; no contiene todas las reglas narrativas.
- **Estado:** versión de formato/migración; nivel, XP y puntos si progresión activa; clase/habilidades; reputación; decisiones, misiones, pruebas, rutas, refugios, encuentros y final; IDs de hitos/recompensas ya concedidos; estado mínimo de encuentro solo si se necesita restauración.
- **Configuración:** módulos activables, política de guardado/restauración/reinicio, diagnóstico y validación, migraciones con copia antes de cambios potencialmente destructivos. Herramientas administrativas solo si se definen y protegen; no deben cambiar finales silenciosamente.
- **Convivencia:** puede proveer estados a Ember’s Questing o Mebahel’s RPG, sin integración presumida. Un único responsable del diario visible; evitar seguimiento duplicado. APIs/versiones **[SIN VERIFICAR]**.
- **Dificultad:** media; coherencia ante migraciones y mods aumenta esfuerzo.
- **Riesgo:** bajo con actualizaciones por eventos/guardados agrupados; medio si consulta condiciones cada tick o recorre entidades/regiones continuamente (evitarlo).

### 2. Clases, atributos, niveles y builds
- **Responsabilidad:** clases opcionales, cuatro atributos, nivel máximo 30, curva XP y ramas; ninguna elección impide completar una misión principal.
- **Estado:** clase o sin clase; nivel/XP; Vigor, Agilidad, Percepción, Temple y puntos; nodos/ramas; técnicas y recuperación solo si requiere persistencia; inicialización para no duplicar puntos.
- **Configuración:** máximo/curva; puntos por nivel; XP por hito, jefe, exploración y secundaria; límites/efectos/reinicio; clases/árboles/técnicas; coste y recuperación. No asumir balance.
- **Convivencia:** se solapa con Skill Tree (RPG Series), Pufferfish’s Skills, Simply Skills y Skillbound-RPG. No combinar proveedores de nivel/puntos/árbol sin decidir un propietario único. Versiones/APIs **[SIN VERIFICAR]**.
- **Dificultad:** alta si integra atributos con salud/combate; media-alta si puntos, desbloqueos y efectos simples.
- **Riesgo:** bajo-medio; cálculo de nivel no necesita ser continuo. Aumenta con recalcular atributos cada tick o generar efectos/entidades.

### 3. Decisiones, facciones y accesos
- **Responsabilidad:** estados explícitos de pruebas, reputación, testimonios, rutas, refugios, misiones y disponibilidad de finales; no mover islas ni modificar geografía dinámicamente.
- **Estado:** reputación propuesta −2 a +2 de cuatro facciones; decisiones de Oria, Ballena, Lena y Corona; pruebas/testimonios/apoyo/condiciones técnicas; rutas/refugios; misiones relevantes; condiciones acumuladas para cuatro finales sin decidir por una barra; IDs de recompensas compartidos con núcleo.
- **Configuración:** cambios de reputación, condiciones de rutas/información/diálogo/finales, requisitos de evidencia/apoyo, visibilidad de misiones, traducciones y validación de referencias/requisitos imposibles.
- **Convivencia:** Ember’s Questing, Mebahel’s RPG y QuestTome se solapan parcialmente; Village Diplomacy corresponde a aldeas, no a las facciones. Probar como máximo un sistema externo de quests. Integración **[SIN VERIFICAR]**.
- **Dificultad:** media-alta; principal trabajo es prevenir dependencias contradictorias y validar combinaciones.
- **Riesgo:** bajo si se evalúa al completar acciones/solicitar misión; medio si inspecciona misiones, entidades o bloques continuamente.

### 4. Encuentros, enemigos y seis jefes
- **Responsabilidad:** seis encuentros propios, fases, señales, límite de enemigos y resultados; separar victoria de combate y consecuencias narrativas.
- **Estado:** encuentro/fase/finalización, objetivos y señales persistentes si hacen falta, recompensas concedidas, estados comunicados al núcleo, referencias de arena/salidas si el mundo las necesita y progreso de mecanismos solo durante encuentro.
- **Configuración:** salud/daño/avisos/aperturas; límite y composición simultánea; XP/recursos/información; alternativas/resultados; límites de aparición/actividad. Sin dependencia de generación pesada.
- **Convivencia:** Bosses of Mass Destruction solo se evaluaría para conservar sus jefes, tras comprobar conflictos; no hace falta para implementar los seis. Better Combat y otros cambios de combate **[SIN VERIFICAR]**.
- **Dificultad:** alta por comportamiento, sincronización, persistencia y pruebas finales.
- **Riesgo:** medio, con picos medio-altos por acumulación de entidades, IA, proyectiles, efectos o actualizaciones de arena. Limitar enemigos, arena y lógica por eventos; medir en hardware objetivo.

### 5. Rarezas, recompensas y equipo
- **Responsabilidad:** cuatro rarezas/objetos fijos y recompensas controladas por acto, ruta y decisión; no sumar ranuras salvo necesidad probada.
- **Estado:** IDs de recompensa única entregada, recetas/intercambios si existen, propiedades no derivables del objeto y origen narrativo para impedir doble concesión.
- **Configuración:** efectos/magnitudes Afinado/Singular, fuentes/requisitos/cantidades, Reliquias, nombres/descripciones/iconos/localización (permisos de recursos por verificar). Tiers solo si se elige un mod tras identificar alcance.
- **Convivencia:** RPG Inventory se consideraría para ranuras solo si son necesarias y tras revisar Trinkets; Tierify/TieredZ se solapan. No combinar sistemas de rareza. Licencias/versiones **[SIN VERIFICAR]**.
- **Dificultad:** baja-media con recompensas fijas/efectos pocos; media-alta con botín generado o amplia compatibilidad.
- **Riesgo:** bajo con pocos efectos al equipar/usar; medio si recorre inventario o recalcula constantemente.

### 6. Adaptador opcional de misiones
- **Responsabilidad:** si se selecciona un único mod externo, reflejar hitos indispensables y recibir confirmaciones si API lo permite; no ser requisito de campaña.
- **Estado:** mapeos de IDs internos/externos, sincronización mínima antirrepetición de recompensas, versión del adaptador/datos.
- **Configuración:** sistema elegido, mapeos de hitos/misiones/recompensas/textos, desactivación con aviso si falta el mod, validación de referencias/recompensas duplicadas.
- **Convivencia:** elegir Ember’s Questing o Mebahel’s RPG, no asumir ambos. QuestTome se describe como encargos tipo bounty, no campaña ramificada. APIs/formato **[SIN VERIFICAR]**.
- **Dificultad:** media-alta si expone condiciones; alta con sincronización bidireccional de misiones, estado, recompensa y guardado.
- **Riesgo:** bajo con eventos; medio si consulta estado externo periódicamente.

## Orden de alcance sugerido

Priorizar núcleo de persistencia y estados narrativos, después progresión mínima y condiciones de misiones. Definir presupuesto XP por acto antes de prometer ritmo sin secundarias. Jefes tras prueba de alcance en versión/hardware; son el componente de mayor coste. Empezar con equipo fijo y pocos efectos. Evaluar un sistema externo de misiones cada vez. No declarar ligereza ni rendimiento sin medición.

## Criterios previos a implementación

Confirmar instancia Minecraft 1.20.1 + Fabric y dependencias; probar persistencia/migración; asegurar que clase/nivel/reputación/secundaria no bloquean la historia; evitar decisiones/recompensas duplicadas; validar campaña principal sin farmear con presupuesto XP; limitar entidades/actividad de arenas; escoger una autoridad para diario y recompensas; medir en hardware objetivo. Memoria, sistema operativo, configuración y benchmarks no disponibles: no inventar resultados.
