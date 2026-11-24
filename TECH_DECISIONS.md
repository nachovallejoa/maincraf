# Decisiones técnicas y del director

- **Rama aislada `etapa-7-modpack`:** continuar la etapa de empaquetado en su rama existente, sin modificar `main` ni ramas anteriores.
- **Manifiesto de mods reducido:** incluir únicamente Sodium, Lithium, FerriteCore e ImmediatelyFast con los ids release indicados en el paquete. Los restantes candidatos se excluyen cuando no existe evidencia suficiente de variante Fabric compatible o de cadena release completa.
- **Minecraft 1.20.1 y Fabric Loader 0.20.1:** conservar las versiones objetivo indicadas en el material de entrega; no inferir que el Loader esté instalado ni que la instancia tenga compatibilidad total.
- **Sin JAR de terceros en Git:** los constructores consultan metadatos y hashes de Modrinth y el instalador descarga los archivos en el equipo del usuario; no se redistribuyen binarios de terceros en el repositorio.
- **Sin configuraciones no validadas:** no crear overrides de mods porque las opciones no se contrastaron contra los JAR exactos.
- **TLauncher para Windows como destino prioritario:** incluir instalador local con manifiesto de archivos/hash, respaldo y descarga de mods de terceros en el equipo.
- **Memoria y argumentos JVM:** no se fijan en el manifiesto por falta de verificación del runtime de destino. La memoria sugerida en documentación permanece como recomendación inicial, no como optimización probada.
- **Persistencia propia:** emplear `PersistentState` con Yarn 1.20.1+build.10 conforme a las firmas consultadas; la compilación y pruebas reales siguen pendientes. Las migraciones marcan el estado como sucio cuando corresponda.
- **No inventar datos faltantes:** compatibilidad colectiva, dependencias completas, compilación Gradle, balance y rendimiento quedan pendientes donde las fuentes no los verificaron.
- **Acción automática:** guardar el workflow de build al final de la secuencia de archivos para que el primer disparo encuentre primero los artefactos de entrega.

## Decisiones narrativas del director

- Nombre del paquete: **Mar de Nubes**.
- Se conserva la decisión de alcance de esta entrega: paquete documental reconstruido y no instancia probada.
- Se conservan las marcas `[SIN VERIFICAR]` y `INCOMPLETE` como pendientes; no se completan huecos de fuentes ni se inventan versiones.
- El usuario aprobó el trabajo y delegó las decisiones al equipo; no se solicitan cuestionarios ni se le expone contenido que indicó no querer conocer.
