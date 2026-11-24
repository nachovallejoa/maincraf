# Instalacion

## TLauncher en Windows

1. Descarga el ZIP `-tlauncher.zip` desde Releases o el artefacto `tlauncher-package` de Actions.
2. Descomprime el ZIP completo.
3. Ejecuta `INSTALAR.bat`. Por defecto instala en `%APPDATA%\.minecraft`; puedes indicar otra carpeta como argumento.
4. Abre TLauncher y selecciona la version Fabric instalada.

El instalador descarga los mods de terceros en el equipo y comprueba sus SHA1. Los JAR de terceros no se guardan en este repositorio ni se distribuyen dentro del ZIP. La carpeta `mods/` existente y la configuracion se respaldan antes de copiar los componentes del paquete.

## Prism Launcher o Modrinth App

Importa el `.mrpack` desde la interfaz del launcher. El paquete contiene metadatos para que el launcher descargue los mods desde sus fuentes.

## Memoria

Recomendacion operativa aportada: `-Xmx5G`. **[SIN VERIFICAR]** No hay mediciones del uso real de memoria ni validacion en el hardware. No se agregan argumentos JVM adicionales.

## Limites conocidos

El manifiesto es reducido y no se declara listo para instalar: quedan dependencias requeridas sin cerrar y algunas versiones, nombres de archivo, JAR y compatibilidad del conjunto **[SIN VERIFICAR]**. No se han incorporado configuraciones de mods no validadas. La compilacion del mod propio no se ha ejecutado ni confirmado.
