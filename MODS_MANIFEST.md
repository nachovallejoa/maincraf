# Manifiesto de mods — La Marea de los Mil Soles

El manifiesto técnico (`pack/mods.json`) contiene solo los dos mods cuya identificación, versiones y compatibilidad se documentaron en los hallazgos recibidos. Los hallazgos no aportaron licencia confirmada para cada archivo/proyecto; se marca como **[SIN VERIFICAR]** en vez de inferirla.

| Mod / slug | Versión | ID de versión Modrinth | Licencia | Enlace de Modrinth | Entorno |
|---|---|---|---|---|---|
| Sodium (`sodium`) | `mc1.20.1-0.5.13-fabric` | `OihdIimA` | [SIN VERIFICAR] — la consulta recibida no aportó licencia | [Proyecto](https://modrinth.com/mod/sodium) · [versión](https://modrinth.com/mod/sodium/version/OihdIimA) | Cliente |
| BadOptimizations (`badoptimizations`) | `2.4.1` | `DIugITgU` | [SIN VERIFICAR] — la consulta recibida no aportó licencia | [Proyecto](https://modrinth.com/mod/badoptimizations) · [versión](https://modrinth.com/mod/badoptimizations/version/DIugITgU) | Cliente |

## Dependencias y límites

- Los hallazgos indican que BadOptimizations no declara dependencias.
- Sodium señala dependencias condicionales para Indium e Iris; ninguno está incluido en este manifiesto. No se afirman como requisitos obligatorios.
- Minecraft `1.20.1`, Fabric Loader `0.20.1`; la versión estable exacta del loader se conserva en `pack/mods.json`.
- Los archivos JAR de terceros no se incluyen en Git. El constructor obtiene los archivos referenciados desde Modrinth al crear el paquete.
- La revisión no afirma inicio del juego, prueba conjunta, rendimiento medido ni autorización de redistribución. Confirmar licencias en las fichas oficiales antes de cualquier redistribución que las requiera.

## Candidatos fuera del manifiesto

Los candidatos no auditados quedan fuera, sin afirmar incompatibilidad ni asignarles IDs o versiones. INCOMPLETE: no se recibieron resultados suficientemente verificados de metadatos de proyecto y dependencias obligatorias para Lithium, FerriteCore, ModernFix, Sodium Extra, ImmediatelyFast, Simply Skills y Better Combat; la identificación y verificación de FTB Quests y del Remnants propuesto tampoco quedó resuelta en las consultas disponibles.
