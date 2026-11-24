# Hoja de ruta

## Etapas y estado

Las etapas previas permanecen en sus ramas aisladas. Esta rama registra la integración documental del modpack; no implica que haya superado pruebas técnicas.

| Área | Estado | Pendiente / criterio |
|---|---|---|
| Selección y manifiesto | Documentada con pendientes | Minecraft documental 1.20.1 y Fabric Loader 0.20.1. La selección recibida incluye versiones/IDs nulos y dependencias obligatorias sin versiones verificadas. |
| Integración | En revisión | Revisar manifiesto y constructor; la entrada advierte que faltan IDs, artefactos y dependencias verificadas. No publicar como paquete instalable mientras existan esos bloqueos. |
| Entrega | En revisión | Instrucciones y proceso documentados como provisionales; no afirmar que el paquete esté completo, probado ni listo para instalar. La ruta TLauncher sigue [SIN VERIFICAR]. |
| Mods propios | Revisión de fuentes pendiente | El código proporcionado refiere a `mareas-core`, mientras el árbol del repositorio tiene el módulo `venas-core`; no se inventa código ni se declara compilación. |
| Pruebas | Pendiente | Esperar la compilación automática de GitHub y que el usuario importe, inicie y juegue. Registrar resultados y logs cuando existan; no anticiparlos. |
| Rendimiento | Pendiente | No hay mediciones en el equipo. Los datos declarados de hardware no equivalen a benchmark. |
| Licencias | Pendiente | Las fuentes recibidas no proporcionaron licencias verificadas para los mods listados. Comprobar fuentes oficiales antes de cualquier redistribución pertinente. |

## Pendientes por fuente no concluyente

Las consultas recibidas no devolvieron suficientes metadatos y dependencias obligatorias para Sodium, Remnants, Village Diplomacy y FTB Quests; también quedaron sin cerrar dependencias de Better Combat y Bosses of Mass Destruction. Para Better Combat se marcó INCOMPLETE el proyecto `gedNE4y2`: slug, versión compatible, artefacto y licencia no fueron verificados. No completar estos huecos por inferencia.

## Próximos hitos

1. La compilación automática debe ejecutarse al guardar el workflow; revisar el resultado real.
2. Completar únicamente los metadatos y dependencias que puedan confirmarse en fuentes autorizadas, sin introducir JARs de terceros en Git.
3. Resolver errores de build usando evidencia, sin inventar versiones o código.
4. El usuario importa e inicia la instancia y juega; registrar el resultado solo después de ocurrir.
5. Mantener compatibilidad, rendimiento y licencias como pendientes hasta tener evidencia.
