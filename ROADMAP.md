# Hoja de ruta

## Metodología: 13 etapas

1. **Inventario del repositorio y fuentes** — identificar archivos reales y límites de acceso. Estado: completada para la revisión inicial; 0 archivos de proyecto revisados porque el árbol estaba vacío.
2. **Perfil del equipo** — recoger hardware, sistema, driver y APIs gráficas; separar declaraciones de mediciones. Estado: hardware declarado; Windows/build, driver y API gráfica pendientes.
3. **Definición del objetivo RPG** — acordar estilo, contenido y criterios de éxito sin diseñar contenido antes de autorización. Estado: pendiente; se debe preservar el conjunto de mods deseado.
4. **Inventario del pack RPG** — obtener manifiesto exacto, versiones, dependencias y loader. Estado: bloqueada por falta de manifiesto.
5. **Comparativa de Minecraft y loaders** — comparar opciones con fuentes y distinguir disponibilidad de rendimiento medido. Estado: primera investigación documentada; decisión de versión concreta pendiente del pack. Fabric es preferido, no confirmado como loader final.
6. **Auditoría de mods** — validar archivos, licencia, dependencias, incompatibilidades y clasificación con evidencia. Estado: candidatos en revisión; no instalados.
7. **Diseño de perfiles aislados** — establecer instancia limpia, base mínima y alternativas exigidas por el pack; no mezclar loaders. Estado: pendiente de aprobación y manifiesto.
8. **Configuración inicial** — fusionar opciones por versión sin sobrescribir archivos completos y verificar esquemas. Estado: propuestas/fragementos documentados, revisión en juego pendiente.
9. **Pruebas de carga** — verificar arranque, carga del mundo y logs incrementalmente. Estado: pendiente.
10. **Pruebas funcionales/compatibilidad** — comprobar funciones RPG, progresión y conflictos. Estado: bloqueada por falta del pack/manifiesto.
11. **Benchmark controlado** — medir limpio, base optimizada, grupos incrementales y pack final; sin estimar resultados. Estado: pendiente; usuario realizará tras añadir y validar el pack RPG final.
12. **Decisiones y autorización** — presentar evidencia, riesgos y cambios para aprobación explícita. Estado: preferencias iniciales registradas; selección técnica final pendiente. Autorización de fusionar rama registrada, no ejecutada.
13. **Documentación y cierre de misión** — preservar resultados, decisiones, changelog y tareas siguientes. Estado: documentación inicial actualizada; mediciones y cierre final pendientes.

## Tablero

| Pendientes | En desarrollo | Revisión | Bloqueadas | Completadas |
|---|---|---|---|---|
| Etapas 3, 4, 6, 7, 9, 10, 11, 12; completar etapa 13 tras validación | — | **Primera misión: investigación y documentación inicial; decisiones registradas, no se declara cerrada la validación técnica** (etapas 1, 5, 8, 13) | Etapa 4: manifiesto RPG; etapa 10: pack no identificado | Etapa 1: inventario inicial (0 archivos de proyecto revisables) |

## Estado de decisiones y secuencia

- Objetivo de versión: elegir la que dé el mejor rendimiento sin sacrificar mods; número concreto pendiente de conocer el pack. 1.20.1 sigue siendo propuesta.
- Loader: preferencia por Fabric; confirmar según requisitos y compatibilidad del pack.
- Optimización: investigar candidatos adicionales, sin selección final de añadidos ni instalación autorizada.
- Configuración: aceptadas como propuestas para revisar el fragmento vanilla y JSON de Sodium; se pueden evaluar opciones futuras como Sodium Extra.
- Benchmarks: después de añadir y validar el pack RPG final; no existen mediciones.
- Fusión: el usuario autorizó fusionar esta rama con el contenido actual. No se fusiona mediante esta actualización.
- Siguiente etapa: el usuario autorizó pasar a ella **solo después de revisar la propuesta de versión, loader y mods**. Está en pendientes y no se inicia en este cambio.

## Criterios de avance

- Ningún candidato se trata como instalado ni compatible por la mera existencia de un archivo.
- Registrar `NO DATA` con la fuente que no proporcionó datos.
- Mantener pruebas reproducibles y guardar logs originales.
- Obtener autorización antes de cambios en mods o decisiones técnicas finales.
- No subir archivos de mods de terceros.
- Respetar la secuencia: revisar propuesta técnica; concretar pack/manifiesto; validar versiones, dependencias y compatibilidad; luego instalar/probar; benchmarks únicamente tras validación del pack final.
