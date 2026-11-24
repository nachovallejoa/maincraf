# Protocolo de rendimiento

## Estado de datos

- No hay capturas ni resultados disponibles; no se ejecutó Minecraft ni benchmark.
- No se informan FPS estimados ni ganancias atribuidas.
- El hardware siguiente es declarado en la entrada, no medido independientemente.
- Sensores OpenGL/Vulkan, GPU y memoria gráfica disponibles en esta instalación: **SIN VERIFICAR**.

## Equipo declarado

| Dato | Valor recibido | Estado |
|---|---|---|
| CPU | AMD Athlon 5150, 4 núcleos, 1,6 GHz | No verificado |
| RAM | 12 GB instalados; ~9,9 GB utilizables declarados | No verificado |
| GPU | Radeon R3 integrada | No verificado |
| Memoria gráfica | Hasta 2 GB compartidos según entrada | Sensor no verificado; no equivale a VRAM dedicada |
| Disco | HDD | No verificado |
| Resolución | 1280×720 | Declarada, no verificada |
| Windows/build | Pendiente | No informado |
| Driver/API gráfica | Pendiente | No informado |
| Java/Minecraft/loader | Pendiente | Aún no se fijó perfil |

## Comparaciones separadas

1. Minecraft limpio.
2. Base optimizada mínima.
3. Grupos añadidos uno a uno.
4. Pack RPG final con manifiesto real.

Si no se proporciona manifiesto, la etapa 4 queda pendiente; no se sustituye por un pack hipotético.

## Condiciones controladas

Registrar y mantener constantes versión de juego, loader, Java, heap/flags, resolución, modo de pantalla, ajustes de vídeo, mundo/semilla, posición y recorrido, duración, aplicaciones en segundo plano y estado de energía. Anotar herramienta y versión.

Separar escenarios de chunks generados y chunks nuevos; restaurar una copia del mundo antes de cada repetición de generación. Medir inicio y carga de mundo por separado, no como FPS.

## Procedimiento

- Confirmar inicio, entrada al mundo y funciones relevantes antes de medir.
- Usar una sola herramienta principal de frametimes en toda la serie.
- Guardar CSV/logs originales y versiones de herramientas.
- Objetivo: cinco repeticiones válidas por escenario; registrar exclusiones y motivo.
- Mantener idénticos recorrido y duración.
- Sensores no disponibles: marcar “No disponible”; no estimar.
- No cambiar mods y ajustes gráficos a la vez.
- No interpretar ausencia de un escenario activador como efecto cero.

## Herramientas candidatas, pendientes de validar

CapFrameX, PresentMon, HWiNFO, AMD Software o PerfMon. Registrar versión y disponibilidad efectiva; las métricas OpenGL/sensores de esta Radeon R3 siguen sin verificar. No ejecutar capturadores PresentMon concurrentes.

## Tabla de mediciones (vacía: aún no hay datos)

| Configuración | Escenario | Repetición | FPS medio | 1% low | Frametime | Heap/RAM | CPU | GPU/memoria | Inicio | Carga | Captura/log |
|---|---|---:|---:|---:|---|---|---|---|---|---|---|
| | Chunks existentes | | | | | | | | | | |
| | Chunks nuevos | | | | | | | | | | |

## Conclusiones posteriores (pendientes)

- Mejor en chunks existentes:
- Mejor generando chunks:
- Diferencias medidas y método:
- Sensores no disponibles:
- Conflictos/logs:
- Limitaciones:
- Decisión del usuario:
- Evidencia adjunta:
