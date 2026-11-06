"""Crea conocimiento comercial desde la semilla, sin copiar datos de clientes.

La semilla permanece intacta. Las notas manuales existentes se conservan.
Una nota generada editada por una persona bloquea su reemplazo automático.
"""
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORTE = '2026-11-06'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dinero(value):
    return f'{value:,}'.replace(',', '.')+' COP'


def celda(value):
    return str(value if value is not None else 'No informado').replace('|', '\\|').replace('\n', ' ')


def tabla(headers, rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(celda(x) for x in row)+' |\n' for row in rows)


def meta(ident, audiencia, tipo, origen='escenario_ficticio', **extra):
    values=dict(id=ident, version='1.0', actualizado_en=CORTE, estado='aprobado',
                audiencia=audiencia, tipo=tipo, origen=origen,
                responsable='Operador de práctica', **extra)
    return '---\n'+''.join(f'{k}: {json.dumps(v,ensure_ascii=False)}\n' for k,v in values.items())+'---\n\n'


def generar(destino=None):
    vault=Path(destino) if destino else ROOT/'conocimiento/la-esquina'
    vault.mkdir(parents=True,exist_ok=True)
    semilla=ROOT/'datos/semilla/catalogo.json'
    data=json.loads(semilla.read_text())
    productos=sorted(data['productos'],key=lambda p:p['codigo'])
    lotes=defaultdict(list)
    por_categoria=defaultdict(list)
    por_proveedor=defaultdict(list)
    for row in data['inventario']:lotes[row['producto_codigo']].append(row)
    for p in productos:
        por_categoria[p['categoria']].append(p)
        por_proveedor[p['proveedor_id']].append(p)
    notas={}

    def nota(path,title,body,ident,audiencia='cliente',tipo='guia',origen='escenario_ficticio',**extra):
        notas[path]=meta(ident,audiencia,tipo,origen,**extra)+f'# {title}\n\n'+body.strip()+'\n'

    nota('Negocio/Perfil.md','Perfil de Comercial La Esquina','''
Comercial La Esquina es el negocio ficticio del taller Cognitus. Trabaja con cinco categorías: abarrotes, ferretería, miscelánea, panadería y papelería. El catálogo contiene 1.250 referencias, con códigos y precios procedentes de la semilla de la aplicación.

## Oferta y canal

El recorrido de práctica permite consultar productos y políticas, preparar cotizaciones, generar pedidos y reportar pagos mediante soportes revisados. Continúa con seguimiento, historial, recompra y atención de posventa. Se construye sobre una aplicación local; las capacidades no terminadas no se presentan como disponibles.

## Datos de identificación

Moneda comercial: COP. Zona horaria: America/Bogota. El operador coordina recogida o domicilio del piloto. No hay NIT, dirección de tienda, teléfono, correo comercial, cuenta bancaria ni horario de apertura reales suministrados. El bot debe pedir coordinación por el canal interno, sin inventarlos. Los documentos se identifican como comerciales de práctica y no como factura fiscal.

## Responsable

El operador de práctica confirma condiciones y resuelve excepciones. Los clientes ficticios Ana y Bruno sirven para diseñar pruebas; sus nombres no prueban propiedad sobre ventas. Consulta [[cuentas]], [[Catalogo/Indice]] y [[Negocio/Servicios y alcance]].
''','NEG-PERFIL')

    nota('Negocio/Servicios y alcance.md','Servicios y alcance','''
## Procesos del escenario

- Consulta de catálogo y condiciones comerciales.
- Cotización con documento, vigencia y aceptación de versión.
- Pedido del cliente y confirmación por soporte aceptado tras revisión.
- Seguimiento interno de preparación, despacho, recogida y novedades.
- Historial propio y recompra con condiciones actuales.
- Reclamación, devolución y reembolso administrativo.
- Escalamiento a una persona con contexto persistido.

## Límites comerciales

Cotizar no reserva inventario. La práctica no descuenta ni reintegra stock, registra compras a proveedores, emite factura fiscal ni verifica movimientos bancarios. El reembolso se tramita administrativamente, sin transferir dinero. El seguimiento proviene del operador y no consulta una transportadora.

## Condiciones fuera del piloto

Destinos fuera de Zona A, condiciones especiales, descuentos o productos no identificados requieren revisión. Hasta acordar los datos no se promete un precio final, una fecha o un servicio. Consulta [[entregas]], [[cotizaciones]] y [[escalamiento]].
''','NEG-ALCANCE')

    nota('Negocio/Datos por confirmar.md','Datos por confirmar','''
Los siguientes datos no fueron suministrados para el escenario: dirección física, horario de atención, teléfono y correo comercial, identificación tributaria, medios o números de recaudo, límites geográficos reales de Zona A, servicio de transportadora y sus tarifas, fichas técnicas del fabricante y garantías por referencia.

Una pregunta sobre esos datos se conserva y escala al operador. No se llenan con datos de otra empresa ni con una sugerencia del modelo. El operador puede crear una versión nueva de la política y registrar la fuente cuando los defina.

El plazo de respuesta de una persona y la fecha de pago de un reembolso externo tampoco están definidos. El cliente puede consultar el estado de su solicitud, sin promesa automática de atención o pago inmediato. Consulta [[Negocio/Perfil]] y [[escalamiento]].
''','NEG-FALTANTES')

    nota('Catalogo/Indice.md','Catálogo de productos', '\n'.join([
        'El catálogo contiene **1.250 productos en cinco categorías**. Cada ficha conserva código, nombre, unidad y precio de referencia de la semilla. No añade especificaciones que no están en los datos.',
        '', '## Categorías', '',
        *[f'- [[Catalogo/Categorias/{cat}|{cat}]]: {len(rows)} referencias.' for cat,rows in sorted(por_categoria.items())],
        '', '## Uso de los valores', '',
        'Los precios son una fotografía de referencia del material de práctica. Su fecha de vigencia comercial no fue informada. Para una cotización o pedido, el servidor consulta y revalida el precio operacional en SQLite. No se extrae un precio de una nota antigua para reemplazar esa consulta.',
        '', 'La ficha pública no incluye costos de compra, ubicaciones de almacén ni evaluación de proveedores. La disponibilidad se confirma por la herramienta operacional, no por el número de fichas ni por una fotografía de inventario. Consulta [[Catalogo/Disponibilidad y vigencia]] y [[cotizaciones]].'
    ]),'CAT-INDICE',tipo='indice',origen='semilla_catalogo')

    nota('Catalogo/Disponibilidad y vigencia.md','Disponibilidad y vigencia','''
## Tres respuestas posibles

Existencia positiva en el registro no equivale a reserva ni entrega garantizada. Existencia cero significa agotado en ese registro. Ausencia de un dato significa disponibilidad por confirmar; no debe convertirse en cero.

## Fechas y calidad

La semilla tiene registros de inventario actualizados entre junio y septiembre de 2026. Son anteriores al corte de este vault del 6 de noviembre de 2026. Algunos estados históricos contradicen lo que indica su fecha de vencimiento al corte. No se presentan como disponibilidad comercial actual.

El operador valida existencia utilizable y cantidad antes de autorizar pedido. Un registro marcado VENCIDO o con fecha de vencimiento anterior al corte no justifica ofrecer un producto. Si no hay dato suficiente, se solicita confirmación. No se afirma que toda la referencia esté agotada porque uno de sus registros requiera revisión.

## Cantidades y unidades

La cantidad de venta se expresa con la unidad del catálogo. Un nombre como Mini, Familiar o Premium no proporciona gramaje, tamaño, composición ni compatibilidad. Pregunta al operador o pide una ficha del fabricante cuando esos datos sean necesarios.

Las fichas públicas son referencia documental. Costos, lotes, ubicaciones y notas de inventario se conservan con audiencia interna. Consulta [[Catalogo/Indice]], [[cotizaciones]] y [[escalamiento]].
''','CAT-DISPONIBILIDAD')

    for cat, rows in sorted(por_categoria.items()):
        prefijo=rows[0]['codigo'].split('-')[0]
        nota(f'Catalogo/Categorias/{cat}.md',cat,
             f'Categoría del catálogo de práctica con {len(rows)} referencias. Consulta por código para evitar elegir variantes similares. Los nombres provienen de la semilla y no equivalen a una ficha técnica.\n\n'+
             tabla(['Código','Producto','Unidad','Precio de referencia'],[
                 (f'[[Catalogo/Productos/{p["codigo"]}|{p["codigo"]}]]',p['nombre'],p['unidad'],dinero(p['precio_venta'])) for p in rows])+ 
             '\nAntes de cotizar, confirma precio y disponibilidad operacional. [[Catalogo/Disponibilidad y vigencia|Cómo interpretar los datos]].',
             'CAT-'+prefijo,tipo='categoria',origen='semilla_catalogo')
    for p in productos:
        codigo=p['codigo']
        nota(f'Catalogo/Productos/{codigo}.md',f'{codigo} {p["nombre"]}',f'''
## Identificación

- Código: {codigo}.
- Nombre exacto: {p['nombre']}.
- Categoría: [[Catalogo/Categorias/{p['categoria']}|{p['categoria']}]].
- Unidad comercial: {p['unidad'] or 'No informada'}.

## Precio de referencia

{dinero(p['precio_venta'])}, tomado de datos/semilla/catalogo.json. Fecha de vigencia comercial del precio: no informada. Este valor documenta la semilla y no sustituye la consulta actual del catálogo al emitir o ejecutar una operación.

## Disponibilidad y condiciones

Consulta la herramienta operacional y confirma la cantidad con el operador antes del pedido. Esta ficha no reserva existencias ni garantiza entrega. La ausencia de inventario no debe interpretarse como cero.

## Información del producto

No se proporcionaron gramaje, dimensiones, material, composición, compatibilidad, instrucciones de uso ni garantía específica del fabricante. No deducirlos del nombre comercial. Solicita una aclaración o documentación antes de recomendar una propiedad que no consta.

Condiciones: [[cotizaciones]], [[entregas]] y [[reclamaciones-y-devoluciones]]. Consulta [[Catalogo/Disponibilidad y vigencia]].
''','PROD-'+codigo,tipo='producto',origen='semilla_catalogo',codigo=codigo,
             fuente_operacional='SQLite.productos',requiere_consulta_operacional=True)

    for codigo, rows in sorted(lotes.items()):
        p=next(p for p in productos if p['codigo']==codigo)
        estado='; '.join(sorted({r['estado'] for r in rows}))
        nota(f'Interno/Inventario/{codigo}.md',f'Referencia de inventario {codigo}',f'''
Producto: [[Catalogo/Productos/{codigo}|{p['nombre']}]]. Unidad: {p['unidad'] or 'No informada'}. Esta nota es de consulta interna y no se entrega al chat del cliente.

## Fotografía de la semilla

Las fechas de actualización son históricas. Los estados originales se conservan sin corregirlos silenciosamente. Al corte {CORTE}, revisa fechas, estado, cantidad y procedencia antes de afirmar disponibilidad utilizable.

'''+tabla(['ID','Ubicación','Lote','Stock registrado','Mínimo','Vencimiento','Estado original','Actualización','Observación','Fila origen'],[
                (r['id'],r['ubicacion'],r['lote'],r['stock'],r['stock_minimo'],r['fecha_vencimiento'],r['estado'],r['ultima_actualizacion'],r['observaciones'],r['fila_origen']) for r in rows])+f'''
## Revisión al corte

{sum(1 for r in rows if r['fecha_vencimiento'] and r['fecha_vencimiento'] < CORTE)} registro(s) con fecha de vencimiento anterior al corte. Estados registrados: {estado}. Este conteo es una alerta documental, no una decisión de venta ni un ajuste de stock. La fecha de vencimiento igual al día de corte también requiere revisión; no se presume utilizable sin criterio definido.

No descuentes, reserves ni reintegres inventario desde una respuesta. La fuente operacional conserva el estado real y cualquier decisión requiere validación. Consulta [[Interno/Control de inventario]].
''','INV-'+codigo,audiencia='interno',tipo='referencia_inventario',origen='semilla_inventario')

    for prv in sorted(data['proveedores'],key=lambda x:x['id']):
        rows=por_proveedor[prv['id']]
        nota(f'Interno/Proveedores/{prv["id"]}.md',f'{prv["id"]} {prv["razon_social"]}',f'''
## Referencia interna

ID: {prv['id']}. Razón social de la semilla: {prv['razon_social']}. Categoría: {prv['categoria']}. Esta ficha es interna; no publica información de costos al cliente.

No hay contacto, teléfono, correo, NIT, cuenta de pago, plazo de compra ni evaluación de proveedor en los datos. No inventarlos. La práctica no registra pedidos de compra a proveedores.

## Productos asociados

'''+tabla(['Código','Producto','Costo de referencia','Precio de venta de referencia'],[
                (f'[[Catalogo/Productos/{p["codigo"]}|{p["codigo"]}]]',p['nombre'],dinero(p['precio_costo']),dinero(p['precio_venta'])) for p in rows])+
             '\nLos importes provienen de la semilla. Su vigencia no está informada y no autorizan descuentos o promesas de reposición. [[Interno/Indice|Volver al manual interno]].',
             prv['id'],audiencia='interno',tipo='proveedor',origen='semilla_proveedores')

    nota('Atencion/Estilo de atencion.md','Estilo de atención','''
Atiende en español claro y respetuoso. Usa el nombre declarado por la persona solo como trato, no como autenticación. Responde primero a su necesidad, muestra lo que se conoce y pregunta por el faltante que cambia el siguiente paso.

## Consulta comercial

Pide producto o necesidad, cantidad y fecha deseada cuando sean relevantes. Si hay varias referencias parecidas, ofrece opciones por código y nombre. No elijas por la semejanza del nombre. Para cotizar, recoge también destino o recogida. Para compras existentes, pide acceso a la cuenta y permite escoger una compra propia.

## Respuestas con evidencia

Explica la condición y cita documento, sección y versión. Diferencia política general y estado del caso. Si falta respaldo, di qué no está definido y ofrece revisión. Una intervención humana no es un fallo cuando la regla la requiere.

## Confirmaciones

Antes de registrar una solicitud, muestra su resumen. La aceptación de cotizaciones, revisión de pagos y decisiones administrativas utilizan controles de versión en la aplicación. No recojas contraseñas ni credenciales en la conversación.

Relacionadas: [[escalamiento]], [[cuentas]], [[Catalogo/Indice]] y [[Atencion/Datos necesarios por solicitud]].
''','ATN-ESTILO')

    nota('Atencion/Datos necesarios por solicitud.md','Datos necesarios por solicitud','''
## Consulta de producto

Código o nombre y cantidad. Si se pregunta por una propiedad técnica, se necesita ficha o confirmación del operador. No deducir especificaciones del nombre.

## Cotización

Productos seleccionados, cantidades, cliente identificado al aceptar, modalidad y destino si corresponde. El servidor obtiene precios y calcula; la política aporta vigencia y condiciones.

## Pedido y soporte

Cotización vigente y versión aceptada, disponibilidad confirmada, datos de entrega y pedido propio. El archivo original se adjunta al pedido. El operador revisa naturaleza, monto, moneda, fecha y duplicidad.

## Seguimiento

Pedido propio, modalidad, último evento y fechas registradas. Una guía solo se muestra si existe. El relato del cliente puede abrir una novedad; no reemplaza un evento administrativo.

## Reclamación y devolución

Compra propia, línea, cantidad afectada, motivo, fecha y evidencias disponibles. Una solicitud incompleta se guarda para continuar. La autorización y recepción de devolución son decisiones separadas.

## Reembolso y persona

Reclamación, compra, cantidades, decisión de devolución y recepción o excepción. El expediente requiere monto elegible y saldo. Para escalar, conserva caso, motivo, hechos y faltantes sin pedir repetir la historia. Consulta [[reembolsos]] y [[escalamiento]].
''','ATN-DATOS')

    preguntas = {
      'Preguntas de venta':[
        ('¿Cómo encuentro un producto?','Indica nombre o código. Si aparecen variantes, elige por código y nombre antes de cotizar. [[Catalogo/Indice]].'),
        ('¿El precio de esta nota sigue vigente?','Es una referencia de semilla. Para una oferta, consulta el precio operacional y su validación. [[Catalogo/Disponibilidad y vigencia]].'),
        ('¿Hay disponibilidad?','Consulta el inventario operacional; si falta fecha, dato o confirmación, informa disponibilidad por confirmar. Cotizar no reserva. [[Catalogo/Disponibilidad y vigencia]].'),
        ('¿Cuánto dura una cotización?','En el escenario, siete días calendario desde emisión; revisa el vencimiento exacto del documento. [[cotizaciones]].'),
        ('¿Puedo cambiar una cantidad?','Antes de confirmar, el cambio requiere nueva versión y aceptación. Un pedido confirmado pasa a corrección administrativa, sin borrar el historial. [[cotizaciones]] y [[pedidos-y-pagos]].'),
        ('¿Hay descuento por cantidad?','El piloto usa descuento cero. Una condición especial requiere revisión y un contrato comercial que la soporte; no se promete automáticamente. [[cotizaciones]].'),
        ('¿El total incluye transporte e impuestos?','La cotización debe indicarlo. El piloto usa precios finales y recogida gratuita; no se inventa desglose tributario. Otros destinos requieren definición. [[cotizaciones]] y [[entregas]].'),
        ('¿La cotización o la orden es una factura?','Son documentos comerciales de práctica, no factura fiscal. [[cotizaciones]].'),
      ],
      'Preguntas de pago y entrega':[
        ('¿Adjuntar el comprobante confirma mi pedido?','Primero entra a revisión. El servidor confirma después de ejecutar la propuesta revisada y aprobada que cumple la política. [[pedidos-y-pagos]].'),
        ('¿Eso confirma que el banco recibió el dinero?','La aceptación comercial del soporte conserva el estado bancario no verificado. [[pedidos-y-pagos]].'),
        ('¿Puedo abonar solo una parte?','El recorrido principal exige importe exacto. Un pago parcial o diferente pasa a revisión, sin confirmar automáticamente el pedido. [[pedidos-y-pagos]].'),
        ('¿Puedo volver a enviar el mismo soporte?','Se consulta el registro existente. Otra foto del mismo pago requiere revisión y no suma dinero otra vez. [[pedidos-y-pagos]].'),
        ('¿Cuándo puedo recoger?','Al finalizar el siguiente día hábil de práctica desde confirmación comercial, según el documento aceptado. [[entregas]].'),
        ('¿Cuándo llega a Zona A?','El piloto estima del segundo al tercer día hábil de práctica desde confirmación. Zona A es ficticia y el operador confirma destino. [[entregas]].'),
        ('¿Dónde está mi pedido?','Consulta el último evento de tu pedido en la base. Sin actualización no se inventa despacho, guía o ubicación. [[Guias/Seguimiento y novedades]].'),
        ('¿Hacen entregas fuera de Zona A?','Requiere revisión de transporte y plazo antes de una oferta firme. No hay política de entrega internacional definida. [[entregas]] y [[escalamiento]].'),
      ],
      'Preguntas de posventa':[
        ('¿Cómo informo un producto dañado?','Elige tu compra y señala línea, cantidad, motivo y evidencias disponibles. Se registra una reclamación. [[reclamaciones-y-devoluciones]].'),
        ('¿Qué pasa si no tengo foto o fecha de entrega?','Se conserva la solicitud y se pide el faltante o revisión humana. No se inventa elegibilidad. [[reclamaciones-y-devoluciones]].'),
        ('¿Cuál es la ventana orientativa del ejercicio?','Daño o producto equivocado dentro de siete días calendario desde entrega pasa a evaluación ordinaria. Las excepciones se registran y escalan. [[reclamaciones-y-devoluciones]].'),
        ('¿Una devolución autoriza el reembolso?','Son decisiones distintas. El operador evalúa cantidad, recepción o excepción, monto y saldo. [[reembolsos]].'),
        ('¿Cómo calculan el reembolso?','Desde cantidad elegible y precio histórico vendido, limitado al cobro administrativo disponible. No se usa el precio actual de recompra. [[reembolsos]].'),
        ('¿La aplicación ya me devuelve dinero?','No mueve dinero. Registra aprobación y remisión administrativa, informando pago externo pendiente. [[reembolsos]].'),
        ('¿Cuándo se paga el reembolso externo?','No hay plazo de pago externo definido en este escenario. El operador informa el estado administrativo y coordina lo pendiente. [[Negocio/Datos por confirmar]].'),
        ('¿Puedo hablar con una persona?','Sí, solicita escalamiento en el mismo caso. La bandeja interna conserva el contexto para continuar. [[escalamiento]].'),
      ],
      'Preguntas de cuenta e historial':[
        ('¿Puedo mirar el catálogo sin cuenta?','Las políticas y el catálogo son públicos en el escenario. Aceptar cotizaciones, crear pedidos e historial requieren cuenta. [[cuentas]].'),
        ('¿Cómo creo mi cuenta?','Usa el formulario de registro con nombre, correo y contraseña. La cuenta inicia con rol cliente e historial vacío. [[cuentas]].'),
        ('¿Debo dar la contraseña al bot?','No. Se escribe solo en el formulario de acceso. No debe quedar en conversaciones o documentos. [[cuentas]].'),
        ('¿Puedo reclamar una venta antigua con mi correo?','Un nombre o correo coincidente no prueba propiedad. La asociación histórica requiere revisión explícita. [[cuentas]].'),
        ('¿Cómo repito una compra?','Elige una compra propia y sus líneas. Se prepara una nueva cotización con condiciones y disponibilidad actuales. [[historial-y-recompra]].'),
        ('¿La recompra reutiliza mi comprobante?','El soporte y la aprobación siguen ligados a la compra original. La nueva orden necesita su propio circuito. [[historial-y-recompra]].'),
        ('¿Cerrar sesión borra mi historial?','El cierre termina el acceso de esa sesión. Al iniciar de nuevo, el servidor recupera recursos por tu ID de cliente. [[cuentas]].'),
        ('¿El piloto tiene recuperación por correo?','No incorpora verificación de email ni recuperación por email implementadas. Pide atención del operador sin entregar contraseñas. [[cuentas]].'),
      ],
    }
    for i,(title,items) in enumerate(preguntas.items(),1):
        nota(f'Atencion/{title}.md',title,
             '\n\n'.join(f'## {q}\n\n{a}' for q,a in items),f'FAQ-{i:02d}',tipo='preguntas_frecuentes')

    guias = [
      ('Preparar una compra','GUIA-COMPRA','''
## Recorrido

Identifica productos y cantidades. Consulta precio y disponibilidad por herramientas. Define recogida o destino y completa los datos faltantes. El servidor calcula una cotización con ID, versión y condiciones. El cliente revisa el documento y acepta una versión vigente.

Antes de generar pedido se revalidan condiciones. El operador confirma disponibilidad sin reserva de inventario. Una diferencia de precio exige nueva oferta y aceptación. El pedido autorizado queda pendiente de soporte. No hay venta confirmada por el solo hecho de aceptar una cotización.

## Resultado consultable

El cliente obtiene una cotización y orden propias. Un reintento de la misma aceptación devuelve la misma orden; una nueva compra intencional recibe otra solicitud. Consulta [[cotizaciones]], [[pedidos-y-pagos]] y [[Atencion/Datos necesarios por solicitud]].
'''),
      ('Seguimiento y novedades','GUIA-SEGUIMIENTO','''
## Consulta de estado

Inicia sesión y elige un pedido propio. La respuesta utiliza modalidad, último evento, fecha de actualización y plazo acordado. La guía y transportadora se incluyen solo si existen en el registro. Esta práctica usa registro interno.

## Recogida y domicilio

Recogida sigue preparación, listo para recoger y retirado. Domicilio sigue preparación, despachado y entregado. Una estimación no acredita un evento. El cliente puede informar contradicción o demora; el operador registra y resuelve la novedad.

## Cambio de condiciones

No se cambia destino o fecha aceptada por texto del modelo. Si hay diferencia, conserva la solicitud y pide revisión antes de prometer. Consulta [[entregas]], [[escalamiento]] y [[Negocio/Datos por confirmar]].
'''),
      ('Correcciones y cancelaciones','GUIA-CORRECCIONES','''
## Antes de confirmar

Un cambio de líneas, modalidad o condiciones requiere nueva versión de cotización y aceptación. Conserva la versión anterior y sus relaciones. No aceptes una versión vencida ni reutilices su aprobación sobre otro contenido.

## Después de confirmar

La base del ejercicio no define una cancelación automática ni un plazo general de cancelación. Registra la solicitud como caso administrativo y escala. No borres la venta, su pago o sus soportes. La decisión del operador debe describir qué corrige y cómo conserva trazabilidad.

## Efectos de dinero y stock

Una corrección o cancelación solicitada no mueve dinero, libera saldos o reintegra inventario por sí sola. El reembolso exige su expediente y controles independientes. Consulta [[pedidos-y-pagos]], [[reembolsos]] y [[escalamiento]].
'''),
      ('Recompra paso a paso','GUIA-RECOMPRA','''
Elige una compra propia del historial y confirma qué líneas y cantidades quieres repetir. El sistema vuelve a consultar códigos, precios y disponibilidad, y pregunta por destino o recogida. Explica diferencias respecto de la compra anterior.

Un producto que ya no existe o está agotado requiere elección. No se sustituye automáticamente. Se genera un nuevo borrador y una aceptación posterior. Precio histórico, fecha de entrega, pago y autorizaciones no se heredan.

Si la misma solicitud se interrumpe, se recupera su borrador. Una nueva intención de compra puede crear otro, con su propia clave. Consulta [[historial-y-recompra]] y [[cotizaciones]].
'''),
      ('Garantias y dudas de producto','GUIA-GARANTIAS','''
## Información disponible

La semilla contiene nombre, código, categoría, unidad y precios. No incluye fichas técnicas ni términos de garantía por producto o fabricante. No se promete duración, compatibilidad, composición o resultado de uso a partir del nombre.

## Solicitud del cliente

Recoge código y pregunta concreta. Si ya compró, identifica su compra propia y el motivo de la inconformidad. Guarda el caso y solicita documentación o revisión del operador. Una falta de ficha técnica no impide registrar una reclamación.

## Alcance de la práctica

Las reglas de devolución y reembolso son ficticias para evaluar el sistema. No se afirma que agoten garantías o derechos legales. Las decisiones comerciales excepcionales pasan a una persona. Consulta [[reclamaciones-y-devoluciones]] y [[Negocio/Datos por confirmar]].
'''),
      ('Cuenta y privacidad','GUIA-PRIVACIDAD','''
Usa datos ficticios en el taller. El cliente solo consulta sus pedidos, compras, casos y archivos. El servidor determina la sesión y valida propietario aunque conozca un ID ajeno. No se entrega un listado global de ventas o conversaciones al cliente.

Las contraseñas se ingresan en formularios de acceso. No se solicitan claves de API, datos bancarios completos o contraseñas en el chat ni para tramitar un reembolso administrativo. El operador mantiene sus funciones separadas del registro público.

La práctica no define un procedimiento de supresión de datos ni una política jurídica completa de retención. Una solicitud relacionada se registra y escala sin prometer que se eliminó información. Consulta [[cuentas]], [[escalamiento]] y [[Negocio/Datos por confirmar]].
'''),
    ]
    for title,ident,body in guias:nota(f'Guias/{title}.md',title,body,ident)

    nota('Interno/Control de inventario.md','Control de inventario','''
## Procedencia y límites

Las 827 filas son una fotografía de la semilla de la aplicación, con estado y fechas originales. No hay sincronización de este vault con SQLite ni disponibilidad en tiempo real. Las notas internas documentan lote, ubicación, cantidades y origen; no deben recuperarse para un cliente.

## Comprobación antes de prometer

Consulta el código correcto, unidad, existencia operacional, fecha y condiciones del lote. Un estado histórico VIGENTE o POR VENCER puede ser incoherente con su fecha al corte actual. Conserva el dato original y registra la discrepancia para revisión. No presentes stock bruto como utilizable cuando hay alertas.

No sumes registros de referencias diferentes o unidades incompatibles. Ausencia de fila significa dato no disponible. Fecha anterior al corte o estado VENCIDO impiden usar ese registro como evidencia suficiente de disponibilidad. Fecha igual al corte requiere criterio del operador.

## Operación del taller

El inventario es de lectura. La confirmación del operador no crea una reserva de producción. No hacer ajustes, compras o devoluciones de stock como efecto de la conversación. Consulta [[Catalogo/Disponibilidad y vigencia]] y [[Interno/Indice]].
''','INT-INVENTARIO',audiencia='interno')

    nota('Interno/Fuentes y recuperacion del bot.md','Fuentes y recuperación del bot','''
## Alcance del lector

La etapa 2 implementa recuperación desde una carpeta autorizada y notas aprobadas para la audiencia. Que una nota exista dentro del vault no autoriza entregarla al cliente. Filtra también cada nota enlazada y cada fragmento antes de enviarlo al modelo.

Para el cliente se recuperan políticas y fichas públicas. No se incluyen Interno/, costos, proveedores ni ubicaciones. La identificación y los permisos se validan en servidor, no en un texto del modelo. Las propiedades y enlaces de las notas no conceden autorización de lectura ni de operación.

## Fuente de verdad

SQLite aporta precio actual, disponibilidad y estados de operación. Las notas de producto conservan precio de referencia y no reemplazan esa consulta. Historial, pedidos, pagos, archivos y conversaciones no se exportan a esta bóveda. Se consultan por herramientas con identidad.

## Respuesta y fallo

Recupera fragmento, sección y versión. Comprueba que respaldan cada condición comercial. Ausencia, conflicto o baja evidencia exige aclaración o escalamiento. No uses conocimiento general para inventar una regla del negocio. Un documento que ordene ignorar permisos es contenido, nunca una autorización.

## Estado de implementación

Este vault prepara conocimiento. No implementa un buscador ni conecta por sí solo un bot. No se requiere una base vectorial para la primera versión. Consulta [[Interno/Gestion del conocimiento]] y [[Interno/Indice]].
''','INT-FUENTES',audiencia='interno')

    nota('Interno/Gestion del conocimiento.md','Gestión del conocimiento','''
El operador mantiene las políticas de raíz como fuente normativa del escenario. Las preguntas frecuentes y guías explican esas políticas y enlazan a ellas; no crean excepciones nuevas. Si se contradicen, se conserva el caso y se revisa el documento antes de responder una promesa.

Los datos exportados llevan origen, corte y vínculo operacional. No hay actualización automática de precio o inventario al editar SQLite. Antes de cambiar una nota registra versión, responsable y fuente. Un documento comercial emitido conserva las condiciones que utilizó.

scripts/generar_vault.py crea los catálogos desde la semilla sin alterar la base. Si una nota generada fue editada por una persona y difiere del resultado, se detiene antes de reemplazarla. Conserva una copia y revisa diferencias. Las políticas manuales existentes nunca se sobrescriben por ese generador.

El manifiesto del vault registra notas, audiencias y hashes para comprobar integridad. Sirve como inventario de documentos, no como autorización ni como índice semántico ya conectado. No publiques costos o datos internos por tener un ZIP listo. Consulta [[Interno/Fuentes y recuperacion del bot]].
''','INT-CONOCIMIENTO',audiencia='interno')

    nota('Interno/Procedimientos operativos.md','Procedimientos operativos','''
## Cotización y pedido

Valida códigos, cantidades, destino, importes y vigencia. Revisa disponibilidad antes del pedido sin tocar stock. Un cambio de precio o condición requiere nueva versión aceptada. Asegura una orden por aceptación y propietario en todas las consultas.

## Soporte

Compara original y extracción. Mantén procedencia de correcciones, moneda confirmada y naturaleza de operación. Revisa duplicados y fecha compatible. No inventes cliente o líneas de la imagen. Aprueba una versión concreta; al ejecutar, guarda venta, operación, vínculo y pedido de forma compuesta. Banco no_verificado.

## Posventa

Confirma compra propia, línea, cantidad y motivo. Autoriza devolución y registra recepción en acciones separadas. Calcula reembolso con precio histórico, cobro aplicable y saldo administrativo, controlando solicitudes concurrentes. Una excepción requiere motivo y responsable.

## Atención y cierre

Al tomar un caso conserva un responsable activo y pausa nuevas acciones comerciales del agente. La respuesta humana no sustituye controles de aprobación. Cierra con estado real y siguiente paso; remitir a pago externo no significa dinero devuelto. Consulta [[Interno/Recuperacion y evidencias]].
''','INT-PROCEDIMIENTOS',audiencia='interno')

    nota('Interno/Recuperacion y evidencias.md','Recuperación y evidencias','''
## Resultado incierto

Antes de repetir consulta caso, pedido y propuesta por ID. Si la ejecución ya persistió, recupera su resultado con la misma clave. Si no hubo commit, verifica que no hay efectos parciales antes de reintentar. Si cambió una versión, pide revisión nuevamente.

## Reinicio

La persistencia conserva IDs, versiones, propietarios y relaciones. Un reinicio puede exigir otra sesión; no debe recrear el negocio a partir del chat. Recupera base y archivos juntos desde respaldo privado, con la app detenida. No borres la práctica para ocultar un error.

## Evidencia y medición

Conserva actor, paso, fuente y versión, herramienta, resultado, error, duración y consumo disponible. Separa API real, mocks y fallas inyectadas. Un consumo desconocido no es cero. La tarifa monetaria necesita verificación y fecha. No registres secretos ni imágenes privadas enteras en las trazas.

Este documento describe el procedimiento a construir y comprobar. La bóveda no ejecuta recuperaciones, pruebas ni escrituras. Consulta [[Interno/Procedimientos operativos]] y [[escalamiento]].
''','INT-RECUPERACION',audiencia='interno')

    # Índices internos y vínculos sin exponerlos en documentos de cliente.
    nota('Interno/Indice.md','Manual interno de La Esquina','''
Esta sección es exclusiva del operador y del asistente de construcción autorizado. No se entrega al chat del cliente. Los precios de costo, proveedores, ubicaciones y lotes son información interna del escenario.

## Procedimientos

- [[Interno/Procedimientos operativos]]
- [[Interno/Control de inventario]]
- [[Interno/Fuentes y recuperacion del bot]]
- [[Interno/Gestion del conocimiento]]
- [[Interno/Recuperacion y evidencias]]
- [[Interno/Indice de proveedores]]
- [[Interno/Indice de inventario]]

## Datos que permanecen en la aplicación

Ventas, compradores, historiales, pedidos, soportes y conversaciones se consultan mediante herramientas con permisos. No se exportan aquí desde la base de trabajo. Los ocho ejemplos de venta de la app no prueban identidad ni propiedad del cliente por su nombre.
''','INT-INDICE',audiencia='interno',tipo='indice')

    nota('Interno/Indice de proveedores.md','Índice de proveedores',
         'Las 75 fichas proceden de la semilla sin contactos. No se infieren plazos de reposición ni se generan compras.\n\n'+tabla(['ID','Razón social','Categoría'],[
             (f'[[Interno/Proveedores/{p["id"]}|{p["id"]}]]',p['razon_social'],p['categoria']) for p in sorted(data['proveedores'],key=lambda p:p['id'])]),
         'INT-PROVEEDORES',audiencia='interno',tipo='indice',origen='semilla_proveedores')
    nota('Interno/Indice de inventario.md','Índice de inventario',
         '827 registros históricos y 827 productos con fila. Los otros 423 códigos no tienen dato de inventario en la semilla; no significa stock cero. Consulta [[Interno/Control de inventario]].\n\n'+
         tabla(['Código','Producto','Última actualización de referencia'],[
             (f'[[Interno/Inventario/{p["codigo"]}|{p["codigo"]}]]',p['nombre'],max(r['ultima_actualizacion'] or '' for r in lotes[p['codigo']])) for p in productos if p['codigo'] in lotes]),
         'INT-INDICE-INVENTARIO',audiencia='interno',tipo='indice',origen='semilla_inventario')

    # Mantener políticas existentes como autoridad del escenario.
    politicas=['cotizaciones','cuentas','entregas','escalamiento','historial-y-recompra','pedidos-y-pagos','reclamaciones-y-devoluciones','reembolsos']
    for name in politicas:
        if not (vault/(name+'.md')).exists():
            raise RuntimeError(f'Falta la política manual {name}.md; no se reemplaza con contenido inventado.')

    inicio=meta('VAULT-INICIO','interno','indice')+'''# Conocimiento de Comercial La Esquina

Base de conocimiento del negocio ficticio del módulo 9. Contiene catálogo documental, políticas, guías de atención y referencias internas de inventario y proveedores. Abre esta carpeta como bóveda en Obsidian.

## Consulta comercial

- [[Negocio/Perfil]] y [[Negocio/Servicios y alcance]].
- [[Catalogo/Indice]] y [[Catalogo/Disponibilidad y vigencia]].
- [[cotizaciones]], [[pedidos-y-pagos]] y [[entregas]].
- [[cuentas]] y [[historial-y-recompra]].
- [[reclamaciones-y-devoluciones]], [[reembolsos]] y [[escalamiento]].
- [[Atencion/Estilo de atencion]] y [[Atencion/Datos necesarios por solicitud]].
- [[Atencion/Preguntas de venta]], [[Atencion/Preguntas de pago y entrega]], [[Atencion/Preguntas de posventa]] y [[Atencion/Preguntas de cuenta e historial]].
- [[Guias/Preparar una compra]], [[Guias/Seguimiento y novedades]], [[Guias/Recompra paso a paso]], [[Guias/Correcciones y cancelaciones]], [[Guias/Garantias y dudas de producto]] y [[Guias/Cuenta y privacidad]].

## Operación interna

[[Interno/Indice]] reúne procedimientos, proveedores y registros de inventario. Esta portada también es interna porque enlaza esos materiales. Los lectores de cliente deben empezar por fuentes públicas filtradas por audiencia, sin recorrer todo el vault sin control.

## Fuentes y límites

El catálogo y el inventario documental son fotografías de la semilla. Precios vigentes, disponibilidad y estados reales se consultan en la base operacional con permisos. Las políticas son ficticias y no se presentan como obligaciones legales. [[Negocio/Datos por confirmar]] identifica lo que no fue suministrado.

La conexión del bot se construye durante el taller. Este conjunto no activa RAG, no sincroniza SQLite y no concede permisos por sí solo. Nunca se copian aquí claves, contraseñas ni historiales privados de la práctica.
'''

    # Validar todos los reemplazos antes de escribir. Las notas manuales no se regeneran.
    anterior=vault/'manifest.json'
    if anterior.exists() and (vault/'Inicio.md').exists():
        previo=json.loads(anterior.read_text())
        portada=next((d for d in previo.get('documentos',[]) if d['ruta']=='Inicio.md'),None)
        if portada and sha(vault/'Inicio.md')!=portada['sha256']:
            raise RuntimeError('La nota Inicio.md cambió. Conserva la edición antes de regenerar.')
    for path,content in notas.items():
        p=vault/path
        if p.exists() and p.read_text()!=content:
            raise RuntimeError(f'La nota {path} cambió. Revisa y conserva la edición antes de regenerar.')
    for path,content in notas.items():
        p=vault/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content)
    if (vault/'Inicio.md').exists() and (vault/'Inicio.md').read_text()!=inicio:
        backup=ROOT/'datos/respaldos/vault-inicio-2026-11-06.md'
        backup.parent.mkdir(parents=True,exist_ok=True)
        if not backup.exists():backup.write_text((vault/'Inicio.md').read_text())
    (vault/'Inicio.md').write_text(inicio)
    docs=[]
    for p in sorted(vault.rglob('*.md')):
        text=p.read_text()
        match=re.search(r'^audiencia:\s*(.+)$',text,re.M)
        audiencia=match.group(1).strip().strip('"\'') if match else 'sin_clasificar'
        docs.append(dict(ruta=p.relative_to(vault).as_posix(),audiencia=audiencia,sha256=sha(p)))
    manifest=dict(nombre='Conocimiento de Comercial La Esquina',corte=CORTE,
                  origen='semilla_y_politicas_ficticias',fuente_catalogo_sha256=sha(semilla),
                  productos=1250,categorias=5,proveedores=75,filas_inventario=827,
                  notas=len(docs),preguntas_frecuentes=sum(map(len,preguntas.values())),
                  distribucion_audiencia=dict(Counter(d['audiencia'] for d in docs)),
                  sincronizacion_operacional=False,documentos=docs)
    (vault/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in manifest.items() if k!='documentos'},ensure_ascii=False,indent=2))
    return manifest


if __name__=='__main__':
    generar()
