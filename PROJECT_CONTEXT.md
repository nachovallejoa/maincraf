# PROJECT_CONTEXT

## Modo autónomo

El usuario aprobó todo y delegó todas las decisiones al equipo. No quiere cuestionarios ni conocer el contenido del modpack; se trabaja autónomamente y se comunican los resultados de integración.

Hardware actualizado: 12 GB instalados, unos 10 GB disponibles; Windows usa unos 500 MB. Launcher del usuario: TLauncher en Windows.

## Estado del paquete Deriva

- Perfil objetivo Minecraft `1.20.1`; Loader declarado `0.20.1` según Fabric Meta.
- El manifiesto contiene un subconjunto. No se declara listo para instalar mientras dependencias obligatorias sigan sin resolverse.
- JAR, compatibilidad completa, configuraciones y rendimiento conjunto: [SIN VERIFICAR].
- No se suben JAR de mods de terceros.
- La configuración específica de mods no se incorpora sin validación contra los JAR exactos.
- `-Xmx4G` es recomendación operativa aportada, no una medición validada.

## Mods propios

El núcleo de campaña usa Fabric y persistencia `PersistentState`. Las firmas Yarn mencionadas para 1.20.1+build.10 se consultaron, pero la compilación no se ejecutó. La configuración `guardarCampana` no está conectada al guardado persistente. El comportamiento del gestor ante datos de esquema futuro está [SIN VERIFICAR]. Balance, contenido frente a una especificación aprobada y dependencias finales permanecen sin validar.

## Integración y pruebas

TLauncher para Windows es el objetivo prioritario de instalación. Los constructores obtienen versiones y hashes desde las APIs durante el build; los archivos de terceros se descargan en el equipo del usuario, nunca se versionan ni distribuyen como JAR en el repositorio.

La compilación Gradle y el empaquetado deben comprobarse en GitHub Actions. La prueba de juego queda pendiente de que el usuario instale y ejecute el paquete.
