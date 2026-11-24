# Protocolo de rendimiento reproducible

**Estado:** protocolo; no contiene resultados. No se instaló ni ejecutó Minecraft y no se realizaron benchmarks en esta misión. Las tablas de medición siguen vacías.
**Hardware declarado:** Athlon 5150, Radeon R3, 12 GB RAM (~9,9 GB utilizables declarados), HDD, Windows, 1280×720; no verificado independientemente. API/controlador gráfico local: [SIN VERIFICAR].

## Objetivo y casos

Comparar Minecraft 1.20.1 limpio, base candidata, candidatos incrementales y —cuando se disponga— el pack RPG real. No reemplazar la etapa del pack por uno hipotético.

1. Instancia limpia sin optimizadores ni contenido RPG.
2. Base candidata Fabric, builds exactas verificadas previamente: Sodium 0.5.13, Lithium 0.11.4, FerriteCore 6.0.1, ModernFix 5.25.2+mc1.20.1, ImmediatelyFast 1.5.5+1.20.4-fabric (rango publicado 1.20–1.20.4).
3. Comparar cada candidato por separado con la base; opcionales nunca todos juntos al inicio.
4. Pack RPG completo solo con manifiesto real. Sin manifiesto, declarar etapa pendiente.

## Condiciones y procedimiento

- Crear perfiles aislados y respaldar mundos; registrar MC, loader, Java, argumentos, mods exactos, configuraciones, hashes locales si disponibles y logs. No subir binarios de mods.
- Confirmar GPU/controlador/API local antes de atribuir un resultado a Sodium.
- Mantener constantes mundo/semilla, ruta, orientación, resolución, ajustes, launcher, Java, energía, procesos de fondo y duración. Registrar herramientas/versiones.
- Separar chunks existentes y nuevos. Para generación nueva, restaurar la misma copia/estado inicial; no confundir con lectura de regiones ya generadas.
- Medir arranque, menú, entrada/carga del mundo y generación como eventos separados; distinguir caché fría de caliente.
- ModernFix en predeterminados en la base; cualquier override solo en perfil copia.
- Usar una herramienta principal de frametimes en toda la serie. Guardar CSV/logs/capturas originales. No ejecutar capturadores concurrentes.
- Objetivo: cinco repeticiones válidas por caso; anotar número real y exclusiones. No cambiar mods y ajustes gráficos a la vez.
- FPS medio, frametimes y 1% low deben incluir método/definición; registrar RAM del juego/sistema, CPU, GPU, disco, inicio y carga. Si un sensor no está disponible, marcar “no disponible”, no estimar.
- CapFrameX/PresentMon, RTSS, HWiNFO, AMD Software o PerfMon son herramientas candidatas, no resultados; comprobar disponibilidad local.

## Tabla por repetición (sin datos; ninguna medición recibida)

| Caso/ID | Escenario | Repetición | MC/loader/Java | Mods exactos | FPS medio | 1% low y método | Frametime | CPU | RAM juego/sistema | GPU/disco | Inicio/mundo/generación | Incidencias/archivo |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |

## Resumen (pendiente de mediciones)

| Caso | Escenario | Repeticiones válidas | FPS/frametimes | RAM/CPU/GPU/disco | Compatibilidad | Conclusión autorizada |
|---|---|---:|---|---|---|---|
| | | | | | | |
| | | | | | | |

## Límites

- Un resultado de una escena no demuestra mejora universal ni permite extrapolar a la Radeon R3 sin medición local.
- Separar generación de chunks nuevos de lectura de chunks guardados.
- No inferir rendimiento desde textos promocionales o benchmarks de otros equipos.
- No retirar/reemplazar mods solo por FPS; considerar compatibilidad, mantenimiento, calidad y autorización explícita.
- Dejar vacías las métricas que no se midan e indicar la limitación.
