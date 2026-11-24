# Contexto del proyecto

> Misión 1: documentación de investigación inicial. Estado: **decisiones iniciales registradas; la validación del pack y el rendimiento siguen pendientes**. La información de hardware procede de la entrada recibida y no se midió independientemente.

## Objetivo y filosofía

Documentar una base técnica para evaluar Minecraft con contenido RPG y optimización en el equipo declarado, sin afirmar compatibilidad o rendimiento no medidos. Mantener trazabilidad de fuentes, versiones y decisiones; separar propuestas de hechos y preservar los datos ausentes como pendientes. No diseñar contenido RPG en esta etapa.

## Hardware declarado

| Componente | Dato recibido | Estado |
|---|---|---|
| CPU | AMD Athlon 5150, 4 núcleos, 1,6 GHz | No verificado independientemente |
| Gráficos | Radeon R3 integrada; hasta 2 GB compartidos según la entrada | No verificado; memoria compartida no equivale a VRAM dedicada |
| RAM | 12 GB instalados; ~9,9 GB utilizables declarados | No verificado |
| Almacenamiento | HDD | No verificado |
| Resolución | 1280×720 declarada | No verificada |
| Sistema operativo | Windows; versión/build no indicada | Pendiente |
| Driver y API gráfica | No indicados | Pendiente; OpenGL/Vulkan no verificados |

AMD clasifica la familia Athlon con Radeon R3 como legacy y no planea nuevos drivers para ella. Esto no establece la API gráfica expuesta por esta instalación. Fuente: https://www.amd.com/en/resources/support-articles/faqs/GPU-630.html

## Reglas de autonomía controlada y autorización

- Se permite investigar, documentar y proponer; una propuesta no se considera una decisión aprobada salvo respuesta explícita.
- No instalar, quitar, sustituir ni redistribuir mods sin autorización expresa y verificación de archivo, loader, compatibilidad y licencia.
- No inventar valores, mediciones, manifiestos, dependencias, resultados ni contenido cuando una fuente no devolvió datos; registrar `NO DATA` y qué fuente faltó.
- No ejecutar benchmarks ficticios ni extrapolar FPS. Conservar logs y condiciones al probar.
- Mantener loaders y ramas de prueba aislados; no mezclar Fabric y Forge.
- Nunca subir JARs de mods de terceros.
- No sobrescribir trabajo ajeno: esta misión se documenta en su propia rama, sin cambios en `main`.

## Estado recibido del repositorio

La investigación entregada informó rama por defecto `main`, repositorio vacío y sin commits, árbol raíz vacío y README 404. En esta misión se consultó GitHub: repositorio `nachovallejoa/maincraf`, rama por defecto `main`; lista de ramas vacía y contenido de raíz vacío. El contenido sigue sin archivos previos. La revisión original reporta: `INCOMPLETE: 0 archivos revisados; árbol del repositorio y README, because el repositorio está vacío y no tiene commits (el README devolvió 404).`

## Propuestas técnicas iniciales

- **Versión:** Minecraft 1.20.1 fue la propuesta investigada. La respuesta 1D solicita escoger la versión que ofrezca mejor rendimiento sin sacrificar mods; no designa una versión concreta, por lo que la elección queda pendiente de conocer/evaluar el pack RPG y sus mods.
- **Loader:** Fabric es preferido (respuesta 2A), sin convertirlo en requisito absoluto. La versión y loader finales deben preservar los mods del pack; si son incompatibles, revisar opciones antes de decidir. Forge solo se había considerado como alternativa según requisitos.
- **Base optimizadora:** la respuesta 3C pide investigar más mods de optimización, pero no especificó cuáles añadidos de la lista ni aprobó una selección concreta. Sodium 0.5.13 + Lithium 0.11.4 + FerriteCore 6.0.1 siguen siendo candidatos de investigación, no mods aprobados o instalados. Investigar opciones adicionales sin sacrificar mods del pack y verificar compatibilidad/licencia/versiones. ImmediatelyFast exacto sigue sin verificarse.
- **Configuraciones precargables:** respuesta 4A acepta el fragmento vanilla y JSON de Sodium como propuestas iniciales, sujetos a revisión en juego; se podrán considerar más configuraciones/mods en el futuro, por ejemplo Sodium Extra, sin aprobación de instalación ahora. El fragmento vanilla no es archivo completo y el JSON no es una optimización medida.
- Java 17 es recomendación de Fabric para Minecraft 1.17–1.20.4: https://wiki.fabricmc.net/install
- Sodium requiere oficialmente driver compatible con OpenGL 4.5: https://modrinth.com/mod/sodium. La API disponible en el equipo no está comprobada.
- No hay FPS, 1% low, frametimes, RAM, CPU/GPU ni tiempos de carga medidos.

## Decisiones de la primera misión

1. **Versión objetivo — respuesta 1D:** elegir la versión que ofrezca el mejor rendimiento sin sacrificar mods. No se indicó número de versión; queda aplazada la elección concreta hasta identificar y verificar el pack RPG y sus mods. 1.20.1 permanece como propuesta, no como decisión.
2. **Loader — respuesta 2A:** preferencia por Fabric. Es una preferencia inicial, condicionada a que soporte todos los mods requeridos; falta el manifiesto para confirmar el loader final.
3. **Optimización — respuesta 3C:** investigar si hay más opciones de optimización. No se nombraron añadidos concretos entre los candidatos y no queda aprobada una lista final ni instalación. Investigar más opciones y compatibilidad con el pack, procurando no sacrificar sus mods.
4. **Configuraciones — respuesta 4A:** aceptar el fragmento vanilla y el JSON de Sodium como propuestas iniciales, revisándolos en juego; valorar opciones adicionales en el futuro, por ejemplo Sodium Extra. No implica instalación ni que sean mediciones optimizadas.
5. **Benchmarks — respuesta 5B:** realizarlos después de añadir y validar el pack RPG final. No hay mediciones por ahora.
6. **Fusión — respuesta 6A:** autorizada la fusión de `mision-1-investigacion` en `main` con el contenido actual. Esta autorización se registra; esta actualización no realiza la fusión.
7. **Siguiente etapa — respuesta 7B:** autorizada avanzar, pero solo empezando por revisar la propuesta de versión, loader y mods. No iniciar ahora esa etapa; queda pendiente.

## Pendiente de aprobación y datos

1. Concretar versión de Minecraft con el manifiesto y los mods del pack, atendiendo al mejor rendimiento sin sacrificar mods.
2. Confirmar loader a partir del pack (preferencia declarada: Fabric).
3. Investigar candidatos adicionales de optimización y compatibilidad; el usuario no especificó cuáles ni autorizó instalación.
4. Entregar manifiesto exacto del pack RPG y requisitos de loader.
5. Confirmar launcher, Windows/build, driver AMD y OpenGL/Vulkan expuestos.
6. Aprobar mods y archivos exactos tras verificar dependencias/licencias.
7. Realizar pruebas funcionales y benchmarks controlados en el equipo después de validar el pack RPG final.

Ver también `ROADMAP.md`, `MOD_AUDIT.md`, `MOD_COMPATIBILITY.md`, `PERFORMANCE.md` y `TECH_DECISIONS.md`.