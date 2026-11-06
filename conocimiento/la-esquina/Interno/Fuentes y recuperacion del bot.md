---
id: "INT-FUENTES"
version: "1.0"
actualizado_en: "2026-11-06"
estado: "aprobado"
audiencia: "interno"
tipo: "guia"
origen: "escenario_ficticio"
responsable: "Operador de práctica"
---

# Fuentes y recuperación del bot

## Alcance del lector

La etapa 2 implementa recuperación desde una carpeta autorizada y notas aprobadas para la audiencia. Que una nota exista dentro del vault no autoriza entregarla al cliente. Filtra también cada nota enlazada y cada fragmento antes de enviarlo al modelo.

Para el cliente se recuperan políticas y fichas públicas. No se incluyen Interno/, costos, proveedores ni ubicaciones. La identificación y los permisos se validan en servidor, no en un texto del modelo. Las propiedades y enlaces de las notas no conceden autorización de lectura ni de operación.

## Fuente de verdad

SQLite aporta precio actual, disponibilidad y estados de operación. Las notas de producto conservan precio de referencia y no reemplazan esa consulta. Historial, pedidos, pagos, archivos y conversaciones no se exportan a esta bóveda. Se consultan por herramientas con identidad.

## Respuesta y fallo

Recupera fragmento, sección y versión. Comprueba que respaldan cada condición comercial. Ausencia, conflicto o baja evidencia exige aclaración o escalamiento. No uses conocimiento general para inventar una regla del negocio. Un documento que ordene ignorar permisos es contenido, nunca una autorización.

## Estado de implementación

Este vault prepara conocimiento. No implementa un buscador ni conecta por sí solo un bot. No se requiere una base vectorial para la primera versión. Consulta [[Interno/Gestion del conocimiento]] y [[Interno/Indice]].
