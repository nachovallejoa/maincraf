# Changelog

## 2026-11-24 — Etapa 7: integración y entrega del modpack

- Reducido `pack/mods.json` a Sodium (`OihdIimA`) y BadOptimizations (`DIugITgU`), los dos mods documentados en el paquete final recibido. Ambos se registran como cliente.
- Fijado Fabric Loader `0.20.1` para Minecraft `1.20.1`, conforme a la revisión de Fabric Meta recibida.
- Añadido `pack/overrides/options.txt` con opciones de Minecraft 1.20.1 orientadas a rendimiento; no se declara una ganancia medida.
- Actualizado `scripts/build_mrpack.py` para resolver los archivos referenciados en Modrinth y producir el `.mrpack`, sin añadir JARs de terceros al repositorio.
- Actualizadas las instrucciones de instalación y los documentos de contexto, decisiones, manifiesto de mods y hoja de ruta.
- Registrado modo autónomo aprobado y hardware declarado por el usuario: 12 GB instalados, unos 10 GB disponibles y Windows usa unos 500 MB; no son mediciones independientes.
- Dejadas como pendientes las consultas incompletas de candidatos, las licencias no proporcionadas, la build automática y la prueba real del juego.
- No se recibió código de mods propios y no se añadió contenido inventado ni se afirmó compilación o prueba.

**Estado:** integración y entrega en revisión; compilación de GitHub y juego real pendientes. No afirmar que el paquete fue probado o que sea un manifiesto de servidor.
