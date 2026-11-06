---
id: "INT-CONOCIMIENTO"
version: "1.0"
actualizado_en: "2026-11-06"
estado: "aprobado"
audiencia: "interno"
tipo: "guia"
origen: "escenario_ficticio"
responsable: "Operador de práctica"
---

# Gestión del conocimiento

El operador mantiene las políticas de raíz como fuente normativa del escenario. Las preguntas frecuentes y guías explican esas políticas y enlazan a ellas; no crean excepciones nuevas. Si se contradicen, se conserva el caso y se revisa el documento antes de responder una promesa.

Los datos exportados llevan origen, corte y vínculo operacional. No hay actualización automática de precio o inventario al editar SQLite. Antes de cambiar una nota registra versión, responsable y fuente. Un documento comercial emitido conserva las condiciones que utilizó.

scripts/generar_vault.py crea los catálogos desde la semilla sin alterar la base. Si una nota generada fue editada por una persona y difiere del resultado, se detiene antes de reemplazarla. Conserva una copia y revisa diferencias. Las políticas manuales existentes nunca se sobrescriben por ese generador.

El manifiesto del vault registra notas, audiencias y hashes para comprobar integridad. Sirve como inventario de documentos, no como autorización ni como índice semántico ya conectado. No publiques costos o datos internos por tener un ZIP listo. Consulta [[Interno/Fuentes y recuperacion del bot]].
