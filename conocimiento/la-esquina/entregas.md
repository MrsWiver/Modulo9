---
id: POL-ENTREGAS
version: "1.0"
vigente_desde: 2026-11-06
estado: aprobado
audiencia: cliente
responsable: Operador de práctica
origen: escenario_ficticio
---

# Entrega y recogida

El recorrido base usa recogida en tienda, gratuita, para mantener compatibilidad con el contrato de venta heredado. La política ofrece además un piloto de domicilio gratuito en la zona ficticia «Zona A». Un destino fuera de esa zona requiere cotización administrativa de transporte y plazo. No se emite como firme un total o plazo desconocido.

| Modalidad | Plazo del escenario | Inicio del plazo |
| --- | --- | --- |
| Recogida | Listo para recoger al finalizar el siguiente día hábil de práctica | Confirmación comercial del pedido |
| Domicilio Zona A | Entrega entre el segundo y el tercer día hábil de práctica | Confirmación comercial del pedido |
| Otro destino | Por definir con el operador | Según condiciones de la nueva cotización |

Para el calendario ficticio, día hábil significa lunes a viernes, sin festivos en este escenario. El día de confirmación es día cero y los siguientes días hábiles se cuentan desde el siguiente día local. Esta convención debe estar visible en la cotización. Prueba confirmación en viernes y cambio de día en Bogotá. La aplicación calcula y guarda el intervalo esperado al confirmar; una novedad puede cambiar la estimación solo mediante actualización registrada del operador, con motivo y aviso visible al consultar.

Las fechas estimadas no prueban que un envío ocurrió. Guía, transportadora y eventos provienen del operador. Sin integración externa, la fuente se muestra como «registro interno de práctica». Un operador registra listo para recoger, despacho, retiro o entrega; el modelo y el cliente no pueden hacerlo.

La vista del cliente muestra estado, última actualización, modalidad/destino, intervalo esperado y novedades. No muestra ubicación GPS ni promete llegada a una hora que no está registrada.
