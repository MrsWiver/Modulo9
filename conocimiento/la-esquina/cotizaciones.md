---
id: POL-COTIZACIONES
version: "1.0"
vigente_desde: 2026-11-06
estado: aprobado
audiencia: cliente
responsable: Operador de práctica
origen: escenario_ficticio
---

# Cotizaciones

| Condición | Regla de práctica |
| --- | --- |
| Vigencia | 7 días calendario desde emisión; guardar instante exacto de vencimiento y mostrarlo en Bogotá |
| Precios | COP, desde catálogo; los valores del piloto se tratan como precios finales, sin inventar base ni tarifa de impuestos |
| Desglose tributario | Mostrar «incluido en precio final; desglose no disponible en esta práctica» si el catálogo no tiene detalle; no añadir un porcentaje supuesto |
| Cantidades | Positivas, en unidad del catálogo; en el recorrido base, cantidades enteras |
| Descuentos | Cero en el recorrido base; cualquier excepción requiere decisión del operador y ampliación comprobada del contrato comercial |
| Disponibilidad | Consultada en inventario y confirmada por operador antes del pedido; la consulta o cotización no reserva existencias |
| Cambios | Editar genera una versión nueva; no conserva aceptación anterior |
| Aceptación | Acción explícita del cliente identificado sobre ID y versión vigente |
| Precio cambiado | Al preparar o ejecutar el pedido, si el precio vigente difiere, detener y solicitar nueva cotización y aceptación; no cambiar silenciosamente el importe |
| Alcance | Cotización y orden comercial no son factura fiscal |

La cotización contiene negocio, cliente, ID, versión, emisión y vencimiento; códigos, nombres, unidades, cantidades, precios y subtotales; tratamiento de impuestos, descuentos, transporte y total; destino o recogida; forma de pago; plazo y evento de inicio; disponibilidad y condiciones; políticas utilizadas y canal interno de aclaración.

Una cotización con datos faltantes permanece como borrador. La vigencia no puede prorrogarse editando la fecha a escondidas: se emite una nueva versión. La aceptación no es una venta ni demuestra pago.
