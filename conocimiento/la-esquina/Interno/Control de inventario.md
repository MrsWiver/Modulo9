---
id: "INT-INVENTARIO"
version: "1.0"
actualizado_en: "2026-11-06"
estado: "aprobado"
audiencia: "interno"
tipo: "guia"
origen: "escenario_ficticio"
responsable: "Operador de práctica"
---

# Control de inventario

## Procedencia y límites

Las 827 filas son una fotografía de la semilla de la aplicación, con estado y fechas originales. No hay sincronización de este vault con SQLite ni disponibilidad en tiempo real. Las notas internas documentan lote, ubicación, cantidades y origen; no deben recuperarse para un cliente.

## Comprobación antes de prometer

Consulta el código correcto, unidad, existencia operacional, fecha y condiciones del lote. Un estado histórico VIGENTE o POR VENCER puede ser incoherente con su fecha al corte actual. Conserva el dato original y registra la discrepancia para revisión. No presentes stock bruto como utilizable cuando hay alertas.

No sumes registros de referencias diferentes o unidades incompatibles. Ausencia de fila significa dato no disponible. Fecha anterior al corte o estado VENCIDO impiden usar ese registro como evidencia suficiente de disponibilidad. Fecha igual al corte requiere criterio del operador.

## Operación del taller

El inventario es de lectura. La confirmación del operador no crea una reserva de producción. No hacer ajustes, compras o devoluciones de stock como efecto de la conversación. Consulta [[Catalogo/Disponibilidad y vigencia]] y [[Interno/Indice]].
