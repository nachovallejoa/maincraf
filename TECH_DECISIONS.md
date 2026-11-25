# Decisiones técnicas y del director

## Decisiones técnicas

- **Rama aislada `etapa-7-modpack`:** guardar la etapa del modpack en su propia rama, sin modificar `main` ni ramas anteriores.
- **Minecraft `1.20.1` y Fabric Loader `0.20.1`:** conservar el objetivo aprobado y la versión estable más reciente consignada desde Fabric Meta.
- **Inventario base:** Sodium, Lithium, FerriteCore e ImmediatelyFast tienen IDs Modrinth confirmados según los hallazgos entregados; Fabric API `0.92.5+1.20.1` se incorpora porque es la API fijada por la base de desarrollo aprobada.
- **Sin prueba conjunta implícita:** las consultas de versiones individuales no certifican arranque conjunto ni compatibilidad de la instancia completa.
- **No incluir JAR de terceros:** mantener solo manifiesto/metadata para que el usuario descargue binarios desde sus fuentes; no versionar ni redistribuir dichos JAR.
- **No precargar ajustes no verificados:** mantener options.txt únicamente como referencia, no introducir configuraciones especulativas para Sodium, FerriteCore o ImmediatelyFast; conservar Lithium sin overrides, con el encabezado consignado.
- **TLauncher en Windows:** es el objetivo de instalación prioritaria; la instalación y ejecución real quedan pendientes de prueba.
- **Memoria/JVM:** conservar la recomendación `-Xms2G -Xmx6G` sin argumentos extra de GC; la configuración de memoria no es una medición de rendimiento.
- **Código propio entregado:** copiar los archivos suministrados, sin completar módulos ausentes ni inventar implementaciones. `nucleo-campana` referencia una clase no recibida y `decisiones-campana` no tiene fuentes recibidas.
- **Pendientes:** arranque conjunto, dependencias adicionales, compilación, instalación TLauncher, persistencia, migraciones y rendimiento se mantienen sin afirmar hasta disponer de pruebas.
- **Automatización:** el workflow de compilación y empaquetado se deja para el paso posterior que debe crear los archivos de `.github/workflows/`.

## Decisiones narrativas del director

- Nombre del paquete: **Mar de Nubes**, versión `1.0.0`.
- Alcance: pack ligero de rendimiento base; no agregar contenido RPG opcional descartado/no aprobado.
- ModernFix se excluyó al no acreditarse variante Fabric compatible; Dynamic FPS y los mods RPG enumerados se excluyeron por decisión documental.
- Indium e Iris no se agregaron, dado que no son dependencias obligatorias declaradas por el inventario.
- El usuario aprobó el trabajo y delegó decisiones; no se le hacen cuestionarios ni se le expone el contenido del modpack.