# PROJECT_CONTEXT

## Modo autónomo

El usuario aprobó todo y delegó todas las decisiones al equipo. No quiere cuestionarios ni conocer el contenido del modpack; el trabajo se realiza de forma autónoma y se comunican los resultados de integración.

Hardware actualizado: 12 GB instalados, unos 10 GB disponibles; Windows usa unos 500 MB. Launcher del usuario: TLauncher en Windows.

## Estado del paquete Mar de Nubes

- Perfil objetivo Minecraft `1.20.1`; Loader declarado `0.20.1` según Fabric Meta.
- El manifiesto contiene el subconjunto documental de mods con datos de versiones verificables. No se afirma que esté listo para instalar mientras dependencias obligatorias sigan sin resolverse.
- JAR, compatibilidad completa, configuraciones y rendimiento conjunto: [SIN VERIFICAR].
- No se suben JAR de mods de terceros.
- La configuración específica de mods no se incorpora sin validación contra los JAR exactos.
- `-Xmx4G` es una recomendación operativa aportada, no una medición validada.

## Mods propios

El núcleo de campaña usa Fabric y persistencia `PersistentState`. Las firmas Yarn mencionadas para 1.20.1+build.10 se consultaron, pero la compilación no se ejecutó. La configuración `guardarCampana` no está conectada al guardado persistente. El comportamiento del gestor ante datos de esquema futuro está [SIN VERIFICAR]. Balance, contenido frente a una especificación aprobada y dependencias finales permanecen sin validar.

## Integración y pruebas

TLauncher para Windows es el objetivo prioritario de instalación. Los constructores obtienen versiones y hashes desde las APIs durante el build; los archivos de terceros se descargan en el equipo del usuario, nunca se versionan ni distribuyen como JAR en el repositorio.

La compilación Gradle y el empaquetado deben comprobarse en GitHub Actions. La prueba de juego queda pendiente de que el usuario instale y ejecute el paquete.

## Pendientes por datos no disponibles

- El contenido original de `pack/mods.json` no estaba disponible en la revisión; el manifiesto actual es una reconstrucción documental.
- No se recibió una lista completa de JAR instalados ni conteo final/incomplete a conservar; se mantiene la nota pendiente tal como fue entregada en el resumen del paquete.
- No hay pruebas de ejecución de la compilación ni del juego en la máquina destino.
