# Decisiones técnicas y del director

- **Rama aislada `etapa-7-modpack`:** continuar la etapa de empaquetado en su rama existente, sin modificar `main` ni ramas anteriores.
- **Manifiesto vacío de mods:** `mods: []` porque no hay mods instalables aprobados con IDs de versión Modrinth/dependencias obligatorias incluidos. Los cuatro mods citados como verificados son candidatos individuales; su disponibilidad no demuestra compatibilidad conjunta ni autoriza instalación.
- **Minecraft 1.20.1 y Fabric Loader 0.20.1:** conservar los valores objetivo entregados; no inferir que el Loader esté instalado ni que la instancia tenga compatibilidad completa.
- **No incluir JAR de terceros:** los constructores consultan metadatos y hashes de Modrinth y los descargadores obtienen los archivos en el equipo del usuario; los binarios de terceros no se versionan en Git.
- **No añadir configuraciones de mods no verificadas:** el manifiesto no tiene mods y las opciones de vídeo se limitan a las claves/rangos documentados; no se afirma que `options.txt` se haya probado en juego.
- **TLauncher Windows como destino prioritario:** incluir guía e instalador local con manifiesto de archivos/hashes, respaldo y descargas de terceros en el equipo.
- **Memoria y JVM:** no fijar argumentos JVM en el manifiesto por falta de validación del runtime de destino. La recomendación documental de memoria es inicial, no una optimización probada.
- **Persistencia propia:** usar `PersistentState` y las firmas consultadas para Yarn 1.20.1+build.10; compilación y pruebas reales continúan pendientes. Las migraciones indican el estado como sucio cuando corresponde.
- **No inventar datos faltantes:** compatibilidad conjunta, dependencias completas, compilación Gradle, balance y rendimiento permanecen pendientes donde las fuentes no los verificaron.
- **Acción automática:** guardar el workflow de build al final de la secuencia de archivos para que el primer disparo encuentre antes los artefactos de entrada.

## Decisiones narrativas del director

- Nombre del paquete: **Mar de Nubes**.
- Alcance aprobado: paquete documental reconstruido, no instancia probada.
- Se conservan las marcas `[SIN VERIFICAR]` y `[INCOMPLETE]` como pendientes; no se rellenan huecos con versiones o fuentes inventadas.
- El usuario aprobó el trabajo y delegó las decisiones al equipo; no se solicitan cuestionarios ni se expone contenido que el usuario no quiere conocer.
