---
id: "INT-RECUPERACION"
version: "1.0"
actualizado_en: "2026-11-06"
estado: "aprobado"
audiencia: "interno"
tipo: "guia"
origen: "escenario_ficticio"
responsable: "Operador de práctica"
---

# Recuperación y evidencias

## Resultado incierto

Antes de repetir consulta caso, pedido y propuesta por ID. Si la ejecución ya persistió, recupera su resultado con la misma clave. Si no hubo commit, verifica que no hay efectos parciales antes de reintentar. Si cambió una versión, pide revisión nuevamente.

## Reinicio

La persistencia conserva IDs, versiones, propietarios y relaciones. Un reinicio puede exigir otra sesión; no debe recrear el negocio a partir del chat. Recupera base y archivos juntos desde respaldo privado, con la app detenida. No borres la práctica para ocultar un error.

## Evidencia y medición

Conserva actor, paso, fuente y versión, herramienta, resultado, error, duración y consumo disponible. Separa API real, mocks y fallas inyectadas. Un consumo desconocido no es cero. La tarifa monetaria necesita verificación y fecha. No registres secretos ni imágenes privadas enteras en las trazas.

Este documento describe el procedimiento a construir y comprobar. La bóveda no ejecuta recuperaciones, pruebas ni escrituras. Consulta [[Interno/Procedimientos operativos]] y [[escalamiento]].
