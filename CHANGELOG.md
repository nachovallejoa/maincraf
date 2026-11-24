# Changelog

## 2026-11-24 — Etapa 7: integración y entrega del modpack (en revisión)

- Añadido `pack/mods.json` con Minecraft 1.20.1 y los cuatro mods base seleccionados: Sodium `OihdIimA`, Lithium `iEcXOkz4`, FerriteCore `unerR5MN` y ModernFix `rPmgLeZC`; se conserva `fabric_loader_version: null` porque no se proporcionó una versión exacta verificable.
- Añadido `scripts/build_mrpack.py`, que verifica datos de versiones/archivos de Modrinth, construye un `.mrpack` y no descarga los JARs de terceros al repositorio. El build termina con error explícito mientras Loader siga sin fijarse.
- Añadido `INSTALL.md` con instrucciones de importación, requisitos y límites de validación.
- Actualizados `PROJECT_CONTEXT.md`, `TECH_DECISIONS.md`, `MODS_MANIFEST.md` y `ROADMAP.md`: modo autónomo, hardware declarado, selección, enlaces, licencias pendientes, motivos y estado de pruebas.
- No se añadieron archivos bajo `pack/overrides/`: contenido de configuración completo no verificado; se conservan los valores predeterminados.
- No se entregó código ni archivos de `mods-propios/`: la entrada no proporciona proyecto o fuentes implementables; autorización específica y compilación no verificables. No se inventó contenido.
- Sin JARs de terceros, sin configuración parcial supuesta y sin afirmar que la instancia está lista o validada.

**Pendiente:** fijar Fabric Loader desde una fuente verificable; ejecutar el workflow/build en GitHub; revisar su resultado y luego importar, iniciar y jugar en el equipo real. Compatibilidad conjunta, rendimiento, consumo y licencias individuales permanecen sin verificación suficiente. La guía de memoria `-Xmx6G` es una orientación condicionada, no una medición.

## 2026-11-24 — Aprobación de mecánicas y preferencias del usuario

- Registrada la aprobación general del diseño revisado: clases, árboles/builds como parámetros de prueba, progresión/XP, rarezas y recompensas fijas, combate, seis jefes y facciones con escala propuesta. El detalle permanece en `GAME_DESIGN.md`.
- Registrada la preferencia de evitar cuestionarios, tomar decisiones creativas según prioridades comunicadas y preservar el descubrimiento narrativo sin spoilers. No se inventaron giros narrativos.
- Registrado hardware declarado por el usuario: aproximadamente 10 GB disponibles y unos 500 MB usados por el sistema operativo; benchmarks siguen **NO DATA**. En esta entrega el usuario actualizó el dato a 12 GB instalados.
- No se asignaron estados individuales a módulos propios ni se seleccionaron mods concretos de la pregunta 9: no se inventaron esas decisiones.
- Desarrollo de mods propios no autorizado explícitamente en la fuente previa; no se inició nueva implementación.
- Actualizados `ARCHITECTURE.md`, `MODS_MANIFEST.md`, `PROJECT_CONTEXT.md` y `ROADMAP.md` para reflejar límites y estados.
- Cambios mantenidos en `etapa-5-mecanicas`; no se fusionaron ramas ni se subieron binarios de terceros.

## 2026-11-24 — Mecánicas: propuesta documental en revisión

- Consolidado `GAME_DESIGN.md` como diseño de mecánicas para *La Marea de los Mil Soles*, con clases/atributos, ramas y builds, niveles y XP, equipo/rarezas, combate, seis jefes, reputación/facciones, progresión por actos y misiones.
- Registradas cifras propuestas sin presentarlas como balance probado. Presupuesto XP por acto, atributos iniciales, balance/builds, costes definitivos y efectos cuantificados siguen pendientes.
- Conservada como **[SIN VERIFICAR]** la correspondencia con una fuente independiente de historia aprobada y la relación Almirante Sumergido–Veyr; no se inventaron datos para completar esos huecos.
- Añadida en `ARCHITECTURE.md` la selección de módulos propios candidatos, sin código ni APIs presumidas.
- Actualizados `MOD_AUDIT.md` y `MODS_MANIFEST.md` con candidatos RPG, versiones/enlaces/licencias/dependencias tal como fueron aportados. Autoría o compatibilidad no suministrada marcada **[SIN VERIFICAR]**; no se aprobaron instalaciones ni se subieron JARs/binarios de terceros.
- Mediciones locales de FPS, frametime, memoria, CPU/GPU, arranque, carga, estabilidad y compatibilidad: **NO DATA**; no se ejecutaron benchmarks.
- Actualizado `ROADMAP.md`: etapa 8 — Mecánicas aprobada; no autoriza implementación, pruebas, instalación, compatibilidad ni fusión de ramas.

## 2026-11-24 — Misión 1: investigación inicial corregida (en revisión)

- Integrado el paquete corregido de revisión: alcance documental, equipo, límites de autonomía, autorizaciones y hardware declarado con su estado de verificación.
- Registradas las 13 etapas secuenciales; la misión permanece en revisión y no equivale a validación técnica final.
- Actualizada la comparación: Minecraft 1.20.1 + Fabric como candidato documental principal; Forge 1.20.1 condicionado a lo que requiera el manifiesto. No se registra aprobación técnica definitiva.
- Corregidas cautelas y estados de licencias/builds candidatos; datos no verificados permanecen explícitamente pendientes.
- Registrada discrepancia previa entre versiones de Entity Culling e ImmediatelyFast: resolver con manifiesto/JARs, no por intuición.
- Conservados criterios prudentes de configuración: sin JSON manual/preset completo de Sodium ni overrides no validados.
- Mediciones y pruebas vacías: Minecraft no se ejecutó; no hay resultados locales.
- Reforzada regla de no subir JARs/binarios de terceros y revisar licencias antes de redistribuir.
- Arquitectura, biblia narrativa y diseño continúan como documentos pendientes; no se creó contenido RPG técnico.
- `README` no encontrado: lectura devolvió 404 (Not Found). No se inventó ni creó su contenido.
- Cambios de Misión 1 documentados en `mision-1-investigacion`; no se describe fusión ni modificación de `main`.

## 2026-11-24 — Segunda etapa: propuesta documental en revisión

- Incorporada propuesta pendiente de aprobación: Minecraft 1.20.1 + Fabric como candidata condicional; 1.21.1 + Fabric marcada como conservación **[SIN VERIFICAR como conservación de contenido]**; Forge 1.20.1 sujeta al manifiesto.
- Actualizadas fichas candidatas y discrepancias de versiones; dependencias, compatibilidad y licencias condicionadas a los artefactos exactos.
- Documentados solapamientos no demostrados; no se propuso instalar/configurar mods ni ejecutar pruebas.
- Mediciones locales de FPS, frametime, RAM, arranque, carga y compatibilidad: **NO DATA**.
- Actualizados documentos de decisiones técnicas y auditoría sin añadir JARs/binarios.

## 2026-11-24 — Etapa de identidad RPG: elección registrada

- Registrada en `STORY_BIBLE.md` la opción D: base de *La Marea de los Mil Soles*, trasladada del océano al cielo y combinada con elementos/candidatos RPG de A; B como base, A como reserva/fuente y C no elegida. No se desarrolló la historia completa.
- Actualizado `GAME_DESIGN.md` con misterio/aventura oscura, peligro, combate/exploración, clases, niveles/estadísticas, ramas/builds y dificultad equilibrada.
- Añadido a `PROJECT_CONTEXT.md` el acuerdo de desarrollar historia.
- Actualizado `ROADMAP.md`: identidad RPG completada; historia pendiente y autorizada para etapa posterior.
- Mods/combinaciones continúan como candidatos; disponibilidad, dependencias, licencias, compatibilidad, rendimiento y mecánicas no se verificaron.
- No se fusionaron ramas ni se inició otra etapa.
