# Decisiones técnicas y del director

- **Rama aislada `etapa-7-modpack`:** continuar la etapa de empaquetado en su rama existente, sin modificar `main` ni ramas previas.
- **Manifiesto de mods reducido:** mantener los seis mods de optimización seleccionados y versiones indicadas en el paquete final. ImmediatelyFast se fija en la versión escogida para Minecraft 1.20.1 y Dynamic FPS en la compatible declarada; no incluir mods adicionales sin cierre verificado de dependencias.
- **Minecraft 1.20.1 y Loader 0.20.1:** conservar las versiones de destino indicadas en el material, sin inferir que el Loader esté instalado ni que exista compatibilidad total.
- **Sin JAR de terceros en Git:** constructores e instalador consultan metadatos y hashes de Modrinth y descargan los archivos en el equipo del usuario; no se redistribuyen binarios de terceros.
- **Sin configuraciones no validadas:** no crear overrides para mods porque no se contrastaron con los JAR exactos.
- **TLauncher Windows como destino prioritario:** incluir instalador local que usa manifiesto de archivos/hash, genera respaldo y descarga mods de terceros en el equipo.
- **Memoria:** `-Xmx4G -XX:+UseG1GC` es la pauta inicial documentada; no afirmar optimización ni añadir más argumentos JVM sin medición.
- **Persistencia propia:** emplear `PersistentState` con Yarn 1.20.1+build.10 conforme a las firmas documentadas; la compilación aún debe probarse. Las normalizaciones/cambios de datos deben marcar el estado como sucio.
- **No inventar huecos:** compatibilidad colectiva, dependencias completas, compilación Gradle, balance y rendimiento permanecen pendientes cuando las fuentes disponibles no los verificaron.
- **Acción automática:** guardar el workflow de build al final de la secuencia de escritura para que el primer disparo ya encuentre los archivos de entrega.
