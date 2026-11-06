# Políticas y datos para la práctica de Comercial La Esquina

Estas reglas ficticias permiten construir y probar los recorridos del [taller](modulo-9-taller.md). Se aplican a datos de demostración; no describen políticas reales de una empresa ni constituyen reglas legales. Los números son decisiones del escenario pedagógico. El mentor puede cambiarlos antes de implementar; los cambios posteriores requieren nueva versión y pruebas.

## Identidad y documentos

Negocio de demostración: Comercial La Esquina. Moneda: COP. Zona horaria: America/Bogota. Responsable de las políticas: operador de práctica. Versión inicial: 1.0. Fecha de versión: 6 de noviembre de 2026. Para escenarios históricos con reloj controlado se usa una copia de política marcada como fixture, sin atribuirle vigencia histórica real.

Crea notas separadas en `conocimiento/la-esquina/`. Cada una contiene identificador estable, título, versión, vigencia, responsable, origen ficticio y contenido. Los documentos comerciales conservan una copia de las condiciones aplicadas y su huella, para poder explicarlos aunque luego se edite la nota.

Identifica cliente y negocio como ficticios en documentos imprimibles. Usa nombres Ana y Bruno para cuentas locales. No inventes NIT, facturas fiscales, contactos, transportadoras o guías reales. Los identificadores de cotización, pedido y caso se generan en servidor.

## Registro y acceso de clientes

El cliente puede consultar políticas y catálogo sin registrarse. Para aceptar cotizaciones, generar pedidos y acceder a historial, soportes o expedientes necesita una cuenta y sesión propias. El registro solicita nombre, correo y contraseña y crea un cliente_id estable con rol cliente. No concede rol operador ni asigna compras antiguas por coincidencias de texto.

El correo debe ser único bajo una normalización documentada. La contraseña se ingresa en el formulario de acceso y no pasa por el chat, las trazas o los documentos. Se conserva un hash seguro, nunca su texto. Cerrar sesión invalida el acceso privado hasta volver a autenticarse. Las cuentas de Ana y Bruno sirven para pruebas, sin sustituir el registro de una cuenta nueva.

La práctica es local con datos ficticios: no incorpora verificación de correo ni recuperación por email. Una dirección ingresada no acredita identidad sobre compras anteriores. Las asociaciones históricas requieren revisión administrativa explícita. Si se crea una cotización anónima, su posible vinculación al registrarse exige pertenecer a la misma sesión previa y confirmación, sin buscar borradores de otras personas.

## Cotizaciones

Identificador de nota: POL-COTIZACIONES.

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

## Entrega y recogida

Identificador de nota: POL-ENTREGAS.

El recorrido base usa recogida en tienda, gratuita, para mantener compatibilidad con el contrato de venta heredado. La política ofrece además un piloto de domicilio gratuito en la zona ficticia «Zona A». Un destino fuera de esa zona requiere cotización administrativa de transporte y plazo. No se emite como firme un total o plazo desconocido.

| Modalidad | Plazo del escenario | Inicio del plazo |
| --- | --- | --- |
| Recogida | Listo para recoger al finalizar el siguiente día hábil de práctica | Confirmación comercial del pedido |
| Domicilio Zona A | Entrega entre el segundo y el tercer día hábil de práctica | Confirmación comercial del pedido |
| Otro destino | Por definir con el operador | Según condiciones de la nueva cotización |

Para el calendario ficticio, día hábil significa lunes a viernes, sin festivos en este escenario. El día de confirmación es día cero y los siguientes días hábiles se cuentan desde el siguiente día local. Esta convención debe estar visible en la cotización. Prueba confirmación en viernes y cambio de día en Bogotá. La aplicación calcula y guarda el intervalo esperado al confirmar; una novedad puede cambiar la estimación solo mediante actualización registrada del operador, con motivo y aviso visible al consultar.

Las fechas estimadas no prueban que un envío ocurrió. Guía, transportadora y eventos provienen del operador. Sin integración externa, la fuente se muestra como «registro interno de práctica». Un operador registra listo para recoger, despacho, retiro o entrega; el modelo y el cliente no pueden hacerlo.

La vista del cliente muestra estado, última actualización, modalidad/destino, intervalo esperado y novedades. No muestra ubicación GPS ni promete llegada a una hora que no está registrada.

## Pedido y aceptación del comprobante

Identificador de nota: POL-PEDIDOS-PAGOS.

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

## Historial y recompra

Identificador de nota: POL-HISTORIAL.

Solo se muestran compras con una relación de propiedad establecida en servidor. El nombre del cliente escrito en una venta antigua no es prueba de identidad. Un operador puede preparar relaciones ficticias explícitas en los fixtures, con procedencia.

La recompra conserva la referencia al origen y toma códigos y cantidades como selección inicial. Reconsulta precios, productos y disponibilidad; reconfirma destino y modalidad. Los cambios se presentan antes de emitir una nueva cotización. No copia pago, aprobación ni promesa de entrega. Si un producto ya no existe, se solicita elección; no se sustituye en silencio.

## Reclamaciones y devoluciones

Identificador de nota: POL-POSVENTA.

El cliente puede abrir una reclamación sobre una compra propia por daño, faltante, producto equivocado, demora u otra inconformidad. Solicita ID de compra o permite escogerla del historial; recoge línea, cantidad, relato, fecha y evidencias disponibles. Una evidencia faltante permite guardar y continuar; no obliga a inventarla.

Como regla orientativa ficticia, las solicitudes por daño o producto equivocado dentro de los 7 días calendario desde entrega pasan a evaluación ordinaria. Para probar el borde se compara la fecha local de solicitud con la fecha local de entrega: diferencia de 0 a 7 inclusive. Fuera de esa ventana, sin fecha de entrega o por otro motivo, la solicitud se registra y se escala como excepción; no se afirma rechazo automático ni pérdida de derechos.

El operador autoriza la devolución con cantidad y motivo. La cantidad acumulada autorizada/recibida no puede superar la comprada, descontando cancelaciones registradas. La recepción requiere acción distinta y evidencia administrativa. Un envío de devolución no equivale a recepción. No se reintegra inventario ni se altera la venta original.

## Reembolso administrativo

Identificador de nota: POL-REEMBOLSOS.

El cliente solicita; una persona revisa y decide. La aprobación de devolución no aprueba automáticamente un reembolso. En el escenario ordinario de devolución de producto, se exige recepción registrada antes de aprobar el reembolso. Una excepción requiere motivo explícito del operador.

El monto usa cantidades elegibles y precio realmente vendido. En el piloto sin descuentos y recogida gratuita: monto de productos = cantidad aprobada × precio unitario de la venta. No se añade de nuevo un impuesto incluido. No se reembolsa un transporte no cobrado. Otros ajustes o cargos requieren ampliar el desglose y probarlo antes de utilizarlos.

El saldo administrativo disponible es el monto de cobro aplicado a la venta, menos los reembolsos aprobados o remitidos aún vigentes. Los aprobados reservan ese saldo y la comprobación es atómica. Esta es una cuenta administrativa basada en soportes aceptados, no un saldo bancario verificado. Una revocación autorizada antes de remitir libera su reserva y conserva la decisión y motivo; después de remitir, una corrección exige expediente adicional, sin liberar automáticamente el saldo.

Estados: `solicitado`, `en_revision`, `aprobado_administrativamente`, `rechazado`, `revocado`, `remitido_a_pago_externo`. La transición a `revocado` exige autorización del operador antes de la remisión y conserva el historial. La remisión guarda responsable, fecha y referencia administrativa. El caso puede cerrarse por remisión, indicando «trámite administrativo remitido; pago externo pendiente». Nunca mostrar «dinero devuelto» ni un estado `pagado` en esta práctica. No se recogen cuentas bancarias ni se ejecutan transferencias.

## Escalamiento

Identificador de nota: POL-ESCALAMIENTO.

Se escala por solicitud del cliente, información insuficiente, condiciones fuera de política, disponibilidad sin confirmar, discrepancia de pago, posible duplicidad, novedad de entrega o decisión administrativa. Una intervención no implica fracaso: puede ser el resultado correcto de la regla.

El destino es una bandeja interna. No se promete notificación por correo o mensajería. El expediente conserva caso, motivo, resumen, hechos, faltantes, fuentes y relaciones. Una falla del modelo no debe impedir guardar los IDs y el motivo.

Solo una persona puede estar asignada como responsable activa de un caso. Mientras atiende, el agente permite consultas y recogida de información, pero pausa acciones que cambien el negocio. El operador registra respuesta y decide reanudar o cerrar. La conversación conserva identidad y origen humano o agente.

## Datos para pruebas reproducibles

No cambies la semilla heredada para producir casos. Construye fixtures sobre SQLite y archivos temporales. Cada fixture lleva origen, propietario, fecha y propósito, separado de cualquier llamada real.

| Fixture | Preparación | Resultado comprobable |
| --- | --- | --- |
| Ana y Bruno | Dos clientes y operador; sesiones independientes | Compras, archivos y mensajes aislados |
| Inventario | Productos disponible, agotado, sin dato y ambiguos | No confundir desconocido con cero |
| Cotización | Dos líneas conocidas, descuento cero y recogida gratuita | Suma reproducible sin cargos ocultos |
| Soporte 054 | Escenario histórico con reloj controlado; código FER-0001 × 1 y FER-0222 × 1, precios verificados | Total 148000; fecha documental 2026-09-11; sin inventar referencias |
| Pedido 054 | Reloj de pruebas el 11 de septiembre de 2026 después de las 12:14 locales, orden creada antes de esa hora; sin modificar fecha de la imagen | Coherencia temporal identificada como escenario de pruebas |
| Envío | Un pedido confirmado, eventos de operador y fechas ficticias | Estado consultable sin transportadora externa |
| Posventa | Compra entregada con dos unidades y cobro aceptado; ventanas dentro y fuera de regla | Devolución parcial y escalamiento correctos |
| Reembolso | Una unidad recibida y dos solicitudes que compiten por el mismo saldo | Aprobaciones no exceden importe elegible |

Para el soporte 054, los precios de referencia son 121300 y 26700. Si el catálogo de tu copia difiere, informa la diferencia; no cambies un precio para hacerlo coincidir. La revisión comercial ficticia de un fixture no se presenta como aprobación humana real. Las pruebas con mocks tampoco se presentan como lectura real de imagen.

## Registro de ajustes

Antes de construir, registra en tu copia si mantienes estas reglas o el mentor decide cambios. Para cada cambio anota nota y versión, regla anterior/nueva y casos afectados. Mantén separados los documentos emitidos bajo cada versión. Evita promesas comerciales que no tengan una regla comprobable.
