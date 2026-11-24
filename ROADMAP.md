# Hoja de ruta

## Etapas y estado

Las etapas previas permanecen en sus ramas aisladas. Esta rama registra la integración del modpack y su entrega documental; no implica validación técnica final.

| Área | Estado | Pendiente / criterio |
|---|---|---|
| Selección y manifiesto | Documentalmente actualizado | Dos mods verificados incluidos: Sodium y BadOptimizations. Loader `0.20.1` indicado según Fabric Meta. |
| Integración | En revisión | Revisar el manifiesto, el constructor y el workflow tras la compilación automática. |
| Entrega | En revisión | Instrucciones y proceso de empaquetado documentados; no llamar al paquete probado o listo antes de comprobar la build. |
| Mods propios | Sin implementación en esta entrega | No se recibieron fuentes de código ni detalle técnico suficiente; no se inventaron módulos. |
| Pruebas | Pendiente | Esperar compilación automática en GitHub y que el usuario importe, inicie y juegue. Registrar logs/resultados; no afirmar pruebas por adelantado. |
| Rendimiento | Pendiente | No hay benchmark ni mediciones locales. Las opciones son una propuesta de configuración, no una ganancia comprobada. |
| Licencias | Pendiente | La entrada no proporcionó licencias confirmadas para los mods; verificar antes de redistribución. |

## Pendientes por fuente no verificada

INCOMPLETE: las consultas disponibles no devolvieron metadatos de proyecto y dependencias obligatorias suficientes para Lithium, FerriteCore, ModernFix, Sodium Extra, ImmediatelyFast, Simply Skills y Better Combat. Tampoco quedó verificada la identificación de FTB Quests y del Remnants propuesto. No incorporarlos al manifiesto ni inferir incompatibilidad mientras no haya datos.

## Próximos hitos

1. La compilación automática de GitHub debe ejecutarse al guardar el workflow y su resultado debe revisarse.
2. Resolver cualquier error de build sin incorporar versiones o código no verificados.
3. El usuario importa la instancia, la inicia y juega; registrar el resultado solo cuando ocurra.
4. Mantener pruebas de compatibilidad, rendimiento y licencias como pendientes hasta obtener evidencia.
