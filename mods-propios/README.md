# Mods propios de Deriva

El build contiene dos subproyectos Fabric para Minecraft 1.20.1:

- `deriva-core`: configuración externa, estado de campaña persistente y API compartida.
- `deriva-progression`: selección de clase, consulta de estado y servicio de XP que otros módulos pueden invocar.

## Compilación

Desde esta carpeta, con JDK 17 y una instalación de Gradle compatible con Loom 1.10.5:

```text
gradle build
```

No se incluye Gradle Wrapper. No se han ejecutado ni compilado estos archivos en esta entrega.

## Uso actual

- La configuración por defecto se crea en `config/deriva.properties` al iniciar el juego.
- El estado de campaña se guarda como datos persistentes del mundo en el almacenamiento de datos del Overworld.
- Los comandos de jugador son `/deriva estado` y `/deriva clase <clase>`.
- La selección puede cambiarse mientras se desarrollan las reglas de reinicio y las habilidades; todavía no hay habilidades implementadas.
- Los módulos futuros pueden otorgar XP mediante la API `CampaignProgression.grantExperience`. No se fija una fuente de XP porque la documentación de mecánicas no aprobó ninguna.

## Versiones declaradas

Minecraft 1.20.1, Fabric Loader 0.20.1, Yarn `1.20.1+build.10` y Fabric API `0.92.2+1.20.1`. Loom está fijado en `1.10.5` en `settings.gradle`.
