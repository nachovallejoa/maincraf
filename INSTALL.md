# Instalacion

## TLauncher en Windows

### Requisitos

- Windows y una version reciente de TLauncher.
- Conexion a Internet para que TLauncher descargue los componentes de Minecraft que falten.
- Java 17 para Minecraft 1.20.1. TLauncher puede administrar el runtime segun su configuracion; si aparece una seleccion de Java, usa Java 17.
- Memoria suficiente para Windows, TLauncher y el juego. La recomendacion de memoria esta al final de este documento.

### Descargar el paquete

1. Abre la seccion **Releases** del repositorio y descarga el archivo cuyo nombre termina en `-tlauncher.zip`. Tambien puedes descargarlo desde **Actions**, abriendo una ejecucion completada y descargando el artefacto `tlauncher-package`.
2. Extrae el ZIP completo: clic derecho sobre el archivo y selecciona **Extraer todo**.
3. El ZIP contiene una sola carpeta de version. Copia esa carpeta completa a:
   `%APPDATA%\.minecraft\versions`
4. Para abrir esa ruta, pulsa **Win+R**, escribe `%APPDATA%\.minecraft\versions` y pulsa **Enter**.
   Tambien puedes abrir la carpeta de Minecraft desde el icono de carpeta de TLauncher y entrar en `versions`.
5. Comprueba que la carpeta copiada contiene un archivo JSON cuyo nombre coincide con el de la carpeta. No muevas solo los archivos de dentro: la carpeta completa debe quedar dentro de `versions`.

### Seleccionar y ejecutar

1. Abre TLauncher y elige la nueva version en la lista.
2. En los ajustes de TLauncher, asigna la memoria recomendada al juego.
3. Si los ajustes de tu TLauncher muestran una opcion de carpetas separadas por version, dejala activada para que el perfil use su carpeta propia. **[SIN VERIFICAR]** La documentacion oficial consultada explica que los mundos de modpacks se guardan dentro de la carpeta de cada version, pero no documenta el nombre ni el comportamiento de un ajuste con esa etiqueta. Si no ves esa opcion, no cambies otras opciones del launcher por esta guia.
4. El perfil de Fabric hereda de Minecraft 1.20.1. Si TLauncher pide la version vanilla heredada o no descarga los archivos necesarios para iniciar, instala/ejecuta Minecraft 1.20.1 una vez desde TLauncher y vuelve a elegir el perfil Fabric.
5. Los mods y los archivos de configuracion incluidos quedan dentro de la carpeta de esta version. Los mundos nuevos se guardan dentro de su subcarpeta `saves`. Esto separa esos archivos de otras carpetas de version, siempre que TLauncher ejecute esta version usando su directorio correspondiente.

Para desinstalar el modpack, cierra el juego y borra solamente la carpeta de esta version dentro de `.minecraft\\versions`. Haz antes una copia de `saves` si quieres conservar mundos.

**[SIN VERIFICAR]** No se genera ni se incluye `TLauncherAdditional.json`: la pagina oficial consultada indica que el archivo puede aparecer despues de iniciar una version personalizada, pero no documenta un formato completo ni establece que sea necesario para lanzar un perfil Fabric heredado. No se incluye un JAR de Minecraft de Mojang; el perfil usa `inheritsFrom` y TLauncher debe resolver la version base.

## Opcional: Prism Launcher o Modrinth App

TLauncher no instala archivos `.mrpack` desde este procedimiento. Si usas Prism Launcher o Modrinth App, puedes importar el archivo `.mrpack` descargado de **Releases** o del artefacto `mrpack-package` en **Actions**. Sigue el flujo de importacion del launcher que hayas elegido.

## Memoria y argumentos JVM

El manifiesto recomienda `-Xms2G -Xmx6G`. Es una recomendacion del paquete, no una medicion del equipo. En TLauncher configura hasta 6 GB para el juego solo si el sistema tiene memoria disponible suficiente; deja memoria para Windows y otros programas. No se recomienda copiar argumentos adicionales de GC.

**[SIN VERIFICAR]** No se ha medido la memoria fisica o disponible del equipo del usuario. Si la memoria disponible es menor, reduce la memoria asignada; no asignes al juego toda la memoria del sistema.

## Si el juego no arranca

- Confirma que copiaste la carpeta completa y que el JSON esta directamente dentro de ella.
- Comprueba que Minecraft 1.20.1 se haya instalado/ejecutado desde TLauncher si el launcher no resuelve la version heredada.
- Revisa los registros en `logs/` y los informes de error en `crash-reports/` dentro de la carpeta del modpack. Si todavia no existe `crash-reports/`, busca tambien los registros generales de Minecraft que haya creado TLauncher.
- Verifica que TLauncher este usando Java 17 para Minecraft 1.20.1.
- Si el problema continua, guarda una copia del registro y del informe de error antes de borrar o volver a instalar archivos.
