# Protocolo de benchmarks de rendimiento

## Estado

- Protocolo; resultados **NO DATA**: no se ejecutó Minecraft ni se midieron FPS, frametimes, RAM, CPU/GPU, disco o cargas. Fuente: entrada de revisión indica que no hay resultados; el equipo/instancia tampoco fue probado en esta misión.
- Hardware declarado, no verificado independientemente: AMD Athlon 5150 (4 núcleos/1,6 GHz), 12 GB RAM (~9,9 GB utilizables declarados), Radeon R3 integrada, HDD, Windows, 1280×720.
- Driver local y APIs reportadas **NO DATA**: no se entregó versión/controlador ni lectura OpenGL/Vulkan.
- Manifiesto/JARs **NO DATA** según inventario recibido; benchmark del pack completo bloqueado.

## Objetivo

Comparar de forma repetible juego limpio, base de optimización, grupos de mods y pack completo solo después de auditarlo. Separar renderizado, lógica/CPU, memoria, carga, frametimes, HDD y generación de chunks. No atribuir el efecto de un conjunto a un mod individual sin prueba aislada.

## Herramientas candidatas

Usar una sola herramienta de captura de frametimes por serie. Confirmar disponibilidad y compatibilidad local. No asumir que todos los sensores de Radeon R3 están disponibles.

| Herramienta | Uso | Estado |
|---|---|---|
| CapFrameX | Capturas de frametimes/FPS | Candidata; no ejecutada |
| PresentMon | Captura de presentación/frame | Candidata; no ejecutada |
| HWiNFO | Sensores disponibles | Candidata; no ejecutada |
| Task Manager | CPU, RAM, disco y GPU básicos | Candidata; no ejecutada |
| WPR/WPA | Diagnóstico ETW separado | Candidata; no ejecutada |

Si una lectura no está disponible, anotar “no disponible”; no deducir memoria gráfica compartida ni causa del cuello de botella.

## Variables constantes

Registrar y mantener iguales Minecraft, Java, loader, launcher, driver, resolución, modo de pantalla, VSync/límite FPS, heap, argumentos JVM, opciones de vídeo, mundo/semilla/dimensión, posición/orientación/ruta, packs de recursos, shaders y estado de programas en segundo plano.

## Secuencia

| Orden | Etapa | Estado |
|---:|---|---|
| 1 | Minecraft limpio + loader requerido | Pendiente |
| 2 | Base candidata, tras auditar dependencias | Pendiente |
| 3 | Grupos de mods, añadiendo uno por vez | Pendiente |
| 4 | Pack completo, tras recibir manifiesto/JARs y aprobar compatibilidad | Bloqueado por falta de manifiesto |

## Escenarios y repeticiones

- **Chunks existentes:** copia idéntica de mundo ya generado; misma posición, cámara, ruta y acciones. Restaurar copia sin cambios antes de cada repetición.
- **Chunks nuevos:** mismo mundo/semilla y zona no generada; copia limpia por repetición. No mezclar capturas de zona generada con nueva.
- **Arranque/carga:** definir hitos de inicio/fin; registrar primera carga y posteriores por separado. La aparición de una pantalla no necesariamente significa que terminó la carga.
- FPS/frametimes: al menos tres capturas válidas por configuración/escenario.
- Arranque, carga y chunks nuevos: tres repeticiones por configuración/categoría comparada, restaurando el estado.
- Conservar capturas individuales, intentos inválidos y motivo. Las repeticiones son protocolo, no resultados ni predicción.

## Métricas

| Métrica | Registro |
|---|---|
| FPS medio | Por captura; vacío hasta medir. |
| 1% low | Herramienta y definición; no asumir definiciones intercambiables. |
| Frametime/stutter | Distribución, gráfico y picos observados. |
| CPU | Uso total/por núcleo y herramienta. |
| RAM | Proceso Java y/o sistema; indicar columna exacta. |
| GPU/memoria gráfica | Solo si hay lectura disponible y utilizable. |
| Inicio/carga de mundo | Tiempo por repetición e hitos. |
| Chunks nuevos | Mismo recorrido; registrar solo lo medido. |
| HDD | Lecturas disponibles; no inferir causa por sí sola. |
| Logs/archivos | Ruta, fecha y hash de capturas/logs; no subir JARs. |

## Registro de ejecución (plantilla)

| Campo | Valor |
|---|---|
| ID/fecha/responsable | |
| Etapa y mods exactos | |
| Minecraft/Java/loader | |
| Manifiesto y hash | |
| Driver/versión | |
| Resolución/VSync/límite | |
| Distancias de render/simulación | |
| Ajustes gráficos | |
| Heap/JVM | |
| Mundo/semilla/dimensión/copia | |
| Escenario/ruta | |
| Calentamiento/caché | |
| Herramienta/versión | |
| Sensores disponibles | |
| Capturas/logs | |
| Incidencias | |

## Resultados por repetición — tabla vacía; aún no hay mediciones

| Etapa | Configuración | Escenario | Repetición | FPS medio | 1% low | Frametime | CPU | RAM | GPU si disponible | Inicio | Mundo | Chunks nuevos | Captura/log | Notas |
|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| | | | 1 | | | | | | | | | | | |
| | | | 2 | | | | | | | | | | | |
| | | | 3 | | | | | | | | | | | |

## Resumen — sin resultados

| Caso | Escenario | Repeticiones válidas | FPS/frametimes | RAM/CPU/GPU/disco | Compatibilidad | Decisión/aprobador |
|---|---|---:|---|---|---|---|
| | | | | | | |

## Validez y decisión

Repetir y conservar el dato original si cambió escena/ajustes, hubo actividad excepcional del sistema, pérdida de captura, pausa/cambio de ventana o estado de chunks distinto. No declarar mejora con una captura ni solo con FPS medio. Completar decisión únicamente con mediciones, diferencias repetibles, regresiones funcionales/visuales, limitaciones y aprobación responsable.

| Campo | Resultado |
|---|---|
| Configuración elegida | |
| Evidencia | |
| Limitaciones | |
| Capturas/logs conservados localmente | |
| Aprobación del responsable y fecha | |
