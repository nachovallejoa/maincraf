# Protocolo de rendimiento — Minecraft 1.20.1

## Estado

No hay resultados de benchmark: no se ejecutó Minecraft ni se midieron FPS, 1% low, frametimes, RAM, CPU, GPU, disco o cargas. Tablas vacías intencionalmente. Hardware declarado en la entrada: Athlon 5150, Radeon R3 integrada, 12 GB RAM, HDD, Windows y 1280×720; no verificado independientemente. Controlador/OpenGL local: **[SIN VERIFICAR]**.

## Objetivo y etapas

Comparar bajo variables controladas: (G0) juego limpio; (G1) base mínima autorizada y builds exactas; (G2+) candidatos uno por vez; (G-final) pack real con manifiesto. Loader es una variable distinta; no tratar Fabric y Forge como comparación de una sola variable. Separar chunks existentes de generación nueva.

## Herramientas candidatas

CapFrameX/PresentMon/RTSS para frametimes; HWiNFO o AMD Software para sensores; herramientas Windows para proceso/memoria/disco; cronómetro para cargas. Disponibilidad y sensores de Radeon R3: **[SIN VERIFICAR]**. Process Monitor es diagnóstico puntual, no captura rutinaria de FPS por su overhead. Si un sensor falta, anotar “no disponible”, no inferirlo.

## Variables y procedimiento

Registrar Windows/build, launcher, Minecraft, loader, Java, driver, lista de mods/versiones/hashes locales, configs, recursos, heap y argumentos JVM, resolución/modo/gráficos, plan de energía, procesos de fondo, ubicación de instancia/mundo y herramientas. No subir JARs.

Usar instancia aislada y copias de mundos. Mantener constantes mundo/seed/dimensión/ruta/orientación/acciones/duración. Separar carga de proceso, menú, entrada al mundo y generación de chunks. Para terreno nuevo, restaurar estado inicial equivalente; no mezclar lectura de chunks existentes con generación. Mantener ModernFix en defaults, salvo que una prueba autorizada contraste otra configuración en perfil separado.

Fijar warm-up, duración y número de repeticiones antes de ver resultados. La propuesta recibida sugiere cinco repeticiones válidas; registrar número real, exclusiones y motivo, conservar todas las corridas. No cambiar mods/ajustes a mitad de serie. Guardar logs/capturas originales.

## Métricas

- FPS medio, 1% low y método de cálculo.
- Frametime y stutters con umbral definido antes de medir.
- CPU de proceso/total y por núcleo si está disponible.
- Heap Java usado/máximo y memoria total del proceso/sistema por separado.
- GPU y memoria gráfica solo si sensores fiables están expuestos.
- Actividad de disco del dispositivo donde se alojan juego, instancia y mundo.
- Tiempos de arranque, menú, mundo jugable y generación separados.

No confundir heap máximo con memoria total del proceso ni memoria compartida con VRAM física. No extrapolar rendimiento desde textos promocionales u otros equipos.

## Seguridad y validez

Detener ante crash, corrupción/pérdida, funciones ausentes, regresión visual, falta de memoria o alerta térmica considerada insegura. Usar respaldos. Marcar inválidas las corridas interrumpidas explicando el motivo; repetir sin borrar registro. Un resultado aislado no demuestra mejora universal.

## Tabla por repetición — vacía, sin mediciones

| ID | Fecha | Etapa/mods exactos | Loader/Java | Escenario | Mundo/seed/coords | Repetición | FPS medio | 1% low/método | Frametime | CPU | RAM sistema | Heap usado/máximo | GPU/sensor | Disco | Proceso→menú | Entrada→jugable | Chunks nuevos | Validez/notas |
|---|---|---|---|---|---|---:|---:|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Resumen — vacío

| Caso | Escenario | Repeticiones válidas | FPS/frametimes | RAM/CPU/GPU/disco | Compatibilidad | Decisión/aprobador |
|---|---|---:|---|---|---|---|
|  |  |  |  |  |  |  |

## Conclusión pendiente

Completar solo con mediciones: comparación control/base, diferencias repetibles, regresiones visuales/funcionales, limitación respaldada por sensores, estabilidad RPG y decisión autorizada. Hasta entonces no atribuir mejora ni aprobar combinación.
