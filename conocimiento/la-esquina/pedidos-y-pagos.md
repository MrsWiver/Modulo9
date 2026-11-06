---
id: POL-PEDIDOS-PAGOS
version: "1.0"
vigente_desde: 2026-11-06
estado: aprobado
audiencia: cliente
responsable: Operador de práctica
origen: escenario_ficticio
---

# Pedido y aceptación del comprobante

La orden de compra es el pedido del cliente a La Esquina. No registra adquisición a un proveedor. Solo una cotización vigente aceptada puede originarla; el operador confirma disponibilidad sin escribir inventario. No hay reserva de stock ni garantía de concurrencia de inventario de producción: no se descuentan existencias en esta práctica.

El pedido autorizado queda `pendiente_soporte`. Adjuntar una imagen lo lleva a soporte en revisión, sin confirmarlo. El sistema confirma comercialmente cuando se ejecuta la propuesta revisada y aprobada que cumple estos requisitos:

1. El pedido pertenece al cliente de la sesión y su versión coincide con las condiciones aceptadas y autorizadas.
2. El original está conservado; la extracción es válida y el operador dejó revisión y procedencia de correcciones.
3. La operación corresponde a cobro, no a gasto ni financiación; COP fue confirmado explícitamente.
4. El monto aplicado cubre exactamente el total del pedido del recorrido base. Valores parciales, mayores o discrepantes van a revisión; no se declara confirmación automática ni se crea un cambio a favor.
5. Las referencias disponibles no están aplicadas a otra operación. Si no son legibles, el operador compara evidencia y confirma singularidad, dejando motivo. Un hash solo identifica el mismo archivo.
6. La fecha documental es compatible con la orden: no anterior a su creación y no posterior al día local de revisión, en el escenario de prueba usado. Una discrepancia se escala; no se modifica la extracción para hacerla encajar.
7. Los datos comerciales vienen del pedido y del catálogo, no se deducen de la imagen. No se inventa cliente, factura o mercancía.
8. La versión exacta de la propuesta tiene autorización humana de servidor. Un booleano o una respuesta del modelo no autoriza operaciones.

Registrar venta, líneas, operación, vínculo y confirmación de pedido es una operación compuesta sin efectos parciales. La ejecución repetida devuelve el resultado existente. Debe impedirse que dos propuestas diferentes creen dos ventas para el mismo pedido.

La confirmación guarda `motivo=aceptacion_de_soporte` y `estado_financiero=no_verificado`. No consulta un banco ni demuestra autenticidad. Dos candidatos por el mismo importe requieren selección y revisión; una coincidencia no identifica por sí sola la venta.

Un soporte diferente del mismo pago se adjunta a la operación ya identificada tras revisión y nunca suma dinero. No se admite usar el mismo pago para confirmar dos pedidos. Si el posible duplicado no puede resolverse, el caso queda pendiente de persona.

El caso base no admite modificar un pedido confirmado. Una corrección posterior abre un caso administrativo; no edita su historial ni borra su venta. Una nueva cotización para un pedido pendiente requiere una nueva aceptación y deja la anterior como reemplazada con sus relaciones conservadas.
