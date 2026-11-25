# Decisiones técnicas y del director

- **Rama aislada `etapa-7-modpack`:** continuar la etapa de empaquetado en su rama existente, sin modificar `main` ni ramas anteriores.
- **Manifiesto con los cuatro mods comprobados según la entrada:** conservar Sodium, Lithium, FerriteCore e ImmediatelyFast con IDs de versión Modrinth y los datos entregados. El conjunto no implica una prueba integral de arranque.
- **Minecraft 1.20.1 y Fabric Loader 0.20.1:** conservar los valores objetivo entregados; no inferir que el Loader esté instalado ni que la instancia tenga compatibilidad completa.
- **No incluir JAR de terceros:** los constructores consultan metadatos y hashes de Modrinth y los descargadores obtienen archivos en el equipo del usuario; los binarios de terceros no se versionan en Git.
- **No añadir configuraciones no verificadas:** solo se contempla el archivo vacío de Lithium, descrito en la entrada como válido para sus valores predeterminados. No se inventan opciones de Sodium, FerriteCore o ImmediatelyFast.
- **TLauncher en Windows como destino prioritario:** documentar e incluir el instalador local con manifiesto de archivos/hashes, respaldo y descarga de mods de terceros en el equipo. La instalación y ejecución real en TLauncher permanecen **[SIN VERIFICAR]**.
- **Memoria y JVM:** recomendar `-Xmx6G` según la entrada, sin fijar `-Xms` ni flags GC; la adecuación real al hardware es **[SIN VERIFICAR]**.
- **Modificaciones propias:** no añadir módulos, fuentes ni JAR propios porque la entrada indica que no recibió archivos fuente/configuración. APIs, compilación, balance y funcionamiento quedan pendientes por falta de datos.
- **No inventar datos faltantes:** compatibilidad de conjunto, dependencias adicionales y ejecución quedan pendientes si las fuentes no los demuestran.
- **Automatización:** colocar el workflow al final de la secuencia de integración, después de los archivos que necesita el build.

## Decisiones narrativas del director

- Nombre del paquete: **Mar de Nubes**, versión `1.0.0`.
- Alcance: paquete de rendimiento base y ligero; no se añaden RPG ni contenido de terceros opcional porque no fueron evaluados y la decisión del director prioriza ligereza.
- Deriva Core y Deriva Progression se mantienen fuera porque sus versiones/artefactos descargables no se pudieron verificar.
- ModernFix 5.25.2+mc1.20.1 se excluye por no estar acreditada una variante Fabric compatible; Dynamic FPS 3.9.0 y el contenido RPG enumerado se excluyen por decisión documental.
- Núcleo Campaña y Decisiones Campaña no se seleccionan por el solapamiento señalado; Venas Core no se selecciona porque el árbol documentado no muestra fuente Java.
- El usuario aprobó el trabajo y delegó las decisiones; no se solicitan cuestionarios ni se revela contenido que el usuario no quiere conocer.
