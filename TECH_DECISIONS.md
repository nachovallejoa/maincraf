# Decisiones técnicas y del director

- **Rama aislada `etapa-7-modpack`:** continuar la etapa de empaquetado sobre su rama existente, sin modificar `main` ni etapas anteriores.
- **Manifiesto de mods reducido:** excluir ImmediatelyFast porque el artefacto señalado corresponde a Minecraft 1.20.4; corregir el ID de ModernFix a `rPmgLeZC`; no incluir Skill Tree ni otros mods con dependencias obligatorias sin cerrar. Evitar que una lista incompleta aparente ser instalable.
- **Minecraft 1.20.1 y Loader declarado 0.20.1:** conservar las versiones indicadas por el material recibido; esto no demuestra Loader instalado ni compatibilidad total.
- **Sin JAR de terceros en Git:** generadores e instalador resuelven los datos y descargan archivos de Modrinth al ejecutar; no se redistribuyen binarios de terceros.
- **Sin configuraciones no validadas:** no escribir overrides de mods porque no fueron contrastados con los JAR exactos.
- **TLauncher Windows como ruta de instalación objetivo:** incluir un instalador local que consulta lista de archivos y hashes generada por el builder, mantiene respaldo y descarga terceros en el equipo.
- **Memoria:** conservar `-Xmx5G` solo como punto operativo solicitado, marcado sin verificación; no afirmar que esté optimizado ni añadir argumentos JVM.
- **Persistencia propia:** fijar `PersistentState` con Yarn 1.20.1+build.10 según las firmas documentadas; llamar `markDirty()` al crear un perfil. Marcar incierto el manejo del gestor ante esquemas futuros.
- **No inventar huecos:** compatibilidad colectiva, dependencias completas, JAR exactos, compilación Gradle, balance y rendimiento quedan pendientes si las fuentes disponibles no los verifican.
- **Acción automática:** el workflow debe guardarse al final de los archivos de la entrega, para no iniciar Actions antes de que estén los insumos.
