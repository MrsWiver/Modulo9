# Taller de ventas y posventa de Comercial La Esquina

Clase 9 · Integración multisistema y operación confiable  
Mentor: William Vergara · Encuentro: 6 de noviembre de 2026 · Entrega: 20 de noviembre de 2026

Construye un canal donde un cliente consulta conocimiento de Obsidian, revisa disponibilidad, obtiene una cotización, genera un pedido y adjunta un comprobante. Después puede consultar su envío e historial, repetir una compra y solicitar atención de una persona, una devolución o un reembolso administrativo.

La meta es componer una solución medible: seguir un caso completo, comprobar sus resultados y recuperarlo después de una falla. Trabaja por etapas. En cada una, pide al asistente que construya, prueba tú el resultado y conserva evidencia antes de continuar. No hace falta terminar todos los recorridos durante el encuentro; la construcción y las evidencias continúan hasta la entrega.

Este taller define funcionalidades por construir. La base de la clase 8 ya resuelve comprobantes y propuestas revisadas; todavía no incluye el portal de clientes, las cotizaciones ni la posventa descritos aquí. Las políticas del archivo acompañante son reglas ficticias del ejercicio y se pueden ajustar con el mentor antes de implementarlas.

## Qué entregarás

Una aplicación local con dos espacios: chat del cliente y mesa administrativa. Debe integrar documentos Markdown, SQLite y un modelo con herramientas limitadas. El cliente puede iniciar solicitudes desde la conversación y confirmar acciones en controles que muestran sus detalles. Las decisiones administrativas se toman desde la mesa del operador.

Conserva dos recorridos de demostración:

1. Consulta → disponibilidad → cotización → aceptación → pedido → soporte de pago → confirmación comercial → seguimiento → historial → recompra.
2. Compra identificada → reclamación → devolución → solicitud de reembolso → evaluación humana → cierre administrativo.

En ambos recorridos debe existir escalamiento a una persona y continuidad después de reiniciar. Las pruebas de fallas usarán copias aisladas y resultados identificados como simulados cuando corresponda.

## Material de trabajo

- Este taller.
- [Políticas y datos de la práctica](modulo-9-politicas-y-datos.md).
- [Matriz de comprobación y recuperación](modulo-9-casos-y-evidencias.md).
- Base inicial distribuida: carpeta `modulo-9/` del paquete `modulo-9-inicial.zip`, con README y `BASE.json`. Su origen es el [repositorio de la clase 8](https://github.com/MrsWiver/comercial-la-esquina-modulo-8), commit `096d8fe37259a4c5d363c6eb666dc2976e6d0bc9`.

La app inicial del módulo 9 añade portada, catálogo y puntos de extensión sobre esa referencia, contrastada con `main` el 6 de noviembre. Usa el paquete del módulo 9 como punto de partida; no vuelvas a clonar la clase 8 encima. Comprueba procedencia en `BASE.json`. No uses como instrucción vigente las secciones históricas del taller 8 que dicen que OCR y propuestas siguen sin implementar. Lee el README actual, los contratos y las entradas más recientes de validación.

## Acuerdos para construir

El vault contiene reglas; la base contiene los hechos comerciales; el chat es el canal. El modelo interpreta y propone; el servidor calcula, autoriza y guarda. El chat del cliente no tiene las herramientas generales de búsqueda y escritura del agente administrativo de la clase 8.

| Dato o decisión | Fuente o responsable |
| --- | --- |
| Políticas, requisitos y explicación de plazos | Markdown del vault, con versión y fecha |
| Precio, existencia y fecha del dato | Catálogo e inventario en SQLite |
| Historial, cotización, pedido, envío y reclamación | Registros identificados en SQLite |
| Cálculos, propiedad de registros y transiciones | Servidor con reglas comprobables |
| Revisión del soporte y autorización comercial heredada | Operador, mediante aprobación de una versión |
| Respuesta, aclaraciones y preparación de solicitudes | Agente con herramientas permitidas |
| Excepciones, devoluciones y reembolso administrativo | Persona responsable, con motivo registrado |

La política de la práctica acepta un soporte revisado y válido para confirmar comercialmente el pedido. Esa confirmación no depende de consultar un banco. Se conserva `no_verificado` como estado bancario y el motivo `aceptacion_de_soporte` como fundamento comercial. No se retiran los controles de revisión y autorización de la clase 8.

Usa datos ficticios y sesiones de cliente de prueba. La aplicación permanece en localhost; una práctica con dos vistas no acredita que exista un servicio público seguro.

## Cómo trabajar con el asistente

Pega el siguiente acuerdo al empezar la sesión de construcción. Luego entrega un prompt de etapa por vez. Reutilízalo si cambias de asistente.

```text
Estamos construyendo el módulo 9 de Comercial La Esquina. Lee AGENTS.md, README.md, docs/CONTRATOS.md, docs/VALIDACION.md y los tres documentos del módulo 9 que te indicaré en la etapa 0. Ayúdame a construir por etapas. Guíame con pasos claros, explica cada decisión y verifica el resultado antes de continuar.

Ejecuta tú instalación, configuración técnica, cambios, diagnóstico y pruebas. Pídeme intervención para escribir credenciales privadas o resolver una decisión del negocio; nunca me pidas pegar claves en el chat. No hagas llamadas pagadas durante pruebas automáticas. Para una prueba real explícita, usa solo la solicitud o imagen que se esté verificando y registra su procedencia.

Conserva la base y las imágenes de la clase 8. No reinicialices mi práctica ni modifiques el proyecto de la clase 3. Conserva el prompt íntegro del extractor, OPENAI_OCR_MODEL y OPENAI_CHAT_MODEL según la configuración existente; no cambies de modelo por tu cuenta. Nunca uses docente/ como respuesta de IA.

Implementa únicamente la etapa solicitada. Antes de modificar explica qué construirás, qué reutilizarás y cómo lo comprobarás; después procede. Usa migraciones y permisos de servidor. No habilites SQL libre, aprobación administrativa, ejecución comercial, lectura arbitraria de archivos ni cambio de cliente como herramientas del chat del cliente. Preserva inventario en lectura, revisión, propuestas versionadas, autorización humana e idempotencia. No publiques ni despliegues.

Desde la primera etapa nueva registra caso_id, actor, acción, resultado y error, con IDs relacionados; completarás su vista y métricas en la etapa 12. Al cerrar cada etapa entrega archivos cambiados, cómo iniciar o retomar, pruebas con sus resultados, IDs para comprobar y cualquier pendiente. Distingue claramente función implementada, prueba con mock, simulación de falla y ejecución real con IA. No declares completado un recorrido solo porque respondió el chat.
```

## Etapa 0 Preparar una copia reproducible

**Construyes:** un espacio independiente para la clase 9 y un registro verificable del punto de partida. Si aún terminas la clase 8, esta copia permite construir las ampliaciones sin reemplazar tu entrega anterior.

**Prompt para el asistente**

```text
Usa la carpeta modulo-9 distribuida en modulo-9-inicial.zip. Si ya está abierta, conserva esa copia; si aún está comprimida, extráela a una carpeta independiente sin reemplazar archivos. Lee BASE.json y verifica el origen 096d8fe37259a4c5d363c6eb666dc2976e6d0bc9. No reclones la clase 8 ni pierdas las ampliaciones de esta base. Si ya existe Git crea una rama de trabajo; si no, puedes iniciar un repositorio local para conservar avances. No hagas reset ni limpies una copia existente.

Los materiales de referencia ya están en docs/modulo-9/: modulo-9-taller.md, modulo-9-politicas-y-datos.md y modulo-9-casos-y-evidencias.md. Lee las instrucciones del proyecto y esos documentos antes de modificar. Comprueba la portada, la mesa en /mesa y la ruta /construccion. El vault conocimiento/la-esquina/ contiene políticas de trabajo; todavía no está conectado al cliente.

Instala con uv sync --locked. Inicializa solo una práctica nueva con el procedimiento del README, ejecuta scripts.verificar_base y arranca en el puerto 8009 o uno libre de localhost. Ejecuta uv run pytest -q sin API real. No copies bases personales ni secretos desde otro proyecto. Guíame para configurar backend/.env con mi editor local. Comprueba presencia de configuración sin mostrar valores privados ni exigir listar modelos.

Guarda docs/modulo-9/BASE.md con sistema operativo, commit, versiones, procedimiento de arranque y resultado real de las pruebas. Si un asistente o proveedor no está disponible, diagnostica y permite retomar con otro asistente sobre los mismos archivos. No cambies el proveedor de la app por esa falla.
```

**Comprueba tú**

1. Abre la app y observa catálogo, ocho ventas y los ejemplos autorizados de la base limpia.
2. Busca ventas por `134200`: aparecen dos candidatos, no una asociación automática.
3. Comprueba el informe del asistente: commit, ruta nueva y pruebas. La app inicial del módulo 9 tenía 62 pruebas aprobadas al prepararse; anota tu resultado real. Esas pruebas no acreditan las capacidades nuevas pendientes.
4. Cierra y abre la app. No desaparecen los registros que hayas creado en tu copia.

**Si falla:** instalación o puerto se diagnostican sin borrar datos. Si falta la clave, continúa con interfaz y pruebas aisladas; registra que la conversación real y el OCR real quedan pendientes. Un chat de comandos no cuenta como chat con IA conectado al vault.

**Evidencia:** `BASE.md`, resultado de las pruebas y captura del arranque. Tener la base lista no completa el módulo 9.

## Etapa 1 Crear cuentas y separar cliente y administración

**Construyes:** registro de clientes, inicio y cierre de sesión, conversación por cliente, caso persistente y permisos reales en el servidor. Ana y Bruno sirven como cuentas ficticias de prueba, además de una cuenta nueva que crearás desde el formulario.

**Prompt para el asistente**

```text
Implementa registro de cliente, inicio y cierre de sesión, y separación de cliente y operador del módulo 9. Crea formularios locales con nombre, correo y contraseña, validaciones, unicidad del correo y cliente_id estable generado en servidor. Guarda contraseñas mediante el mecanismo seguro de hash del framework, nunca texto ni registros de credenciales. La contraseña se escribe solo en el formulario, no se pide al modelo ni en el chat. El registro público solo crea rol cliente; el operador se prepara por un procedimiento administrativo separado.

Crea cuentas de prueba para Ana, Bruno y un operador, pero permite además registrar una cuenta nueva desde la interfaz. Resuelve identidad en servidor, protege las sesiones y sus escrituras, evita fijación de sesión y limita intentos de acceso. Invalida la sesión al salir. No uses un parámetro cliente_id enviado por el modelo como identidad. Separa las sesiones de los navegadores. Documenta cuentas ficticias para localhost, sin correo de verificación ni recuperación por email implementados. No presentes el correo ingresado como identidad verificada.

Permite consultas públicas de políticas y catálogo sin cuenta; exige iniciar sesión antes de aceptar cotización, crear pedido o consultar recursos privados. Una cuenta nueva empieza con historial vacío. Cada pedido, compra vinculada, caso y archivo conserva propietario por cliente_id. No asignes ventas antiguas por coincidencia de nombre o correo. Si hay borrador anónimo, no lo pierdas al iniciar sesión y solo vincúlalo desde la misma sesión previa, con confirmación del cliente y validación en servidor.

Protege también las rutas existentes de la clase 8: API, historial global, imágenes, archivos, comprobantes, ventas y propuestas. No basta con ocultar botones. Una sesión de cliente no puede acceder a listados globales ni al agente administrativo anterior. Cada acceso a un recurso debe validar propietario en servidor. Usa sesiones, protección de escrituras y cookies apropiadas para el entorno local; conserva las protecciones existentes donde correspondan.

Añade conversaciones y casos de atención con propietario, ID, estado, fecha y versión. Separa el estado de atención del estado de pedido, envío o reembolso. Conserva mensajes por conversación, sin reutilizar el historial global para todos. Crea fixtures aislados con una compra conocida de Ana y otra de Bruno; no atribuyas ventas antiguas a alguien por coincidencia de nombre. No modifiques la semilla heredada.

Prueba accesos directos y mediante herramientas a los registros del otro cliente, archivos incluidos. Comprueba que reiniciar preserva los casos. Todavía no implementes cotizaciones ni pagos nuevos.
```

**Comprueba tú:** crea una cuenta ficticia nueva desde el formulario y comprueba que su historial está vacío. Intenta repetir el correo: no debe crear otro cliente. Cierra sesión e intenta abrir su historial: debe exigir acceso. Inicia sesión de nuevo y recupera sus casos tras reiniciar. Después entra como Ana en una ventana y como Bruno en otra sesión independiente. Inicia conversaciones diferentes; no deben mezclarse. Intenta consultar como Bruno el ID de una compra o soporte de Ana: debe denegarse sin revelar su contenido. El operador ve su bandeja mediante su propia sesión.

**Si falla:** detén las funciones de historial hasta corregir la propiedad. Un filtro que el modelo puede omitir no resuelve el problema.

**Evidencia:** registro de cuenta nueva, ID de cliente, comprobación de correo duplicado, inicio/cierre de sesión, IDs de dos casos, sesiones separadas y prueba de acceso denegado. No muestres contraseñas en las evidencias.

## Etapa 2 Conectar el chat con el vault de Obsidian

**Construyes:** un vault comercial y una herramienta de búsqueda que devuelve evidencia. Empieza por búsqueda de texto y secciones; una base vectorial es opcional si puedes justificar la necesidad.

**Prompt para el asistente**

```text
Crea conocimiento/la-esquina/ como vault de Obsidian dentro de este proyecto. Toma las reglas ficticias de docs/modulo-9/modulo-9-politicas-y-datos.md y sepáralas en notas de cotizaciones, pedidos y pagos, entregas, posventa y escalamiento. Cada nota debe incluir identificador, versión, fecha de vigencia, responsable y origen ficticio. No uses el vault de Cognitus como política comercial de La Esquina.

Implementa buscar_conocimiento y consultar_fragmento restringidas al directorio autorizado. Devuelve documento, versión, fecha, encabezado, fragmento y huella del contenido. Excluye secretos, archivos no Markdown, rutas externas y enlaces simbólicos que salgan del directorio. No ejecutes código ni visites enlaces de una nota. Refleja cambios guardados en Obsidian sin reiniciar; muestra cuándo se consultó la fuente. Si falta evidencia, devuelve ese estado explícitamente.

Conecta el chat del cliente a un agente con esas herramientas y sesiones de la etapa 1. Debe responder desde fragmentos recuperados, citar nota y sección y distinguir texto documental de instrucciones. Una pregunta pública de políticas puede responderse sin identidad comercial; historial y pedidos exigen sesión. Limita pasos y llamadas por turno, informa límites sin falso éxito y conserva el caso. No envíes todo el vault ni todos los registros al modelo.

Prueba recuperación, documento ausente, actualización y un documento con instrucciones para revelar compras ajenas. Usa mocks para pruebas automáticas. Deja lista una comprobación manual real de una pregunta; no la declares hecha sin ejecutarla.
```

**Conversaciones para probar**

- «¿Cuánto dura una cotización y cuándo empieza a contar la entrega?»
- «¿Hacen entregas internacionales?» La política no contempla ese servicio: debe reconocerlo y ofrecer atención humana.
- Cambia en Obsidian la vigencia de nuevas cotizaciones de 7 a 5 días y aumenta la versión. Pregunta de nuevo; debe usar el cambio. Restaura la política del ejercicio al finalizar la prueba.

**Comprueba tú:** abre la nota citada y encuentra el fragmento que respalda la respuesta. Confirma que la conversación está usando el modelo y herramientas, no una respuesta fija. La edición de la nota no cambia cotizaciones ya emitidas.

**Si falla:** conserva la consulta y muestra que el conocimiento no está disponible; no inventes la política ni sustituyas una búsqueda fallida por conocimiento general.

**Evidencia:** una respuesta real con fuente, versión y traza de consulta; pruebas aisladas de actualización y contenido malicioso.

## Etapa 3 Consultar productos y disponibilidad

**Construyes:** consultas de catálogo e inventario con una interpretación honesta de lo que se conoce.

**Prompt para el asistente**

```text
Añade herramientas de cliente para buscar productos y consultar disponibilidad mediante consultas parametrizadas. Inspecciona el esquema real: explica unidades, ubicaciones y cómo calcularás existencia sin sumar filas incompatibles ni multiplicar datos por un join. No deduzcas cero cuando falta una fila ni presentes como reciente una semilla sin fecha de actualización.

Devuelve código, nombre, unidad, precio de catálogo, cantidad conocida, ubicación si existe, procedencia y fecha del inventario o no disponible. Diferencia existencia positiva, agotado y dato desconocido. Con nombres ambiguos muestra opciones antes de elegir. No escribas inventario, reserves ni descuentes existencias. Explica que la disponibilidad consultada requiere confirmación comercial antes del pedido.

Crea escenarios aislados con un producto disponible, uno agotado, otro sin dato y dos nombres similares. Prueba herramientas y conversación; la respuesta comercial debe usar resultados del servidor. No permitas al cliente cambiar precios ni acceder a datos internos de proveedores.
```

**Comprueba tú:** pregunta por una necesidad general, selecciona un código y pide una cantidad. Contrasta precio y cantidad con la consulta estructurada. Solicita un producto sin inventario: la respuesta debe decir «disponibilidad por confirmar». Repite la consulta y comprueba que no cambió ninguna existencia.

**Si falla:** solicita código o aclaración; el resultado vacío no autoriza inventar un producto sustituto.

**Evidencia:** comparación entre chat y datos para disponible, agotado y desconocido.

## Etapa 4 Generar una cotización completa

**Construyes:** un documento comercial calculado en servidor, con versiones y condiciones congeladas al emitirlo.

**Prompt para el asistente**

```text
Implementa cotizaciones usando la política ficticia del módulo 9. El agente recoge necesidad, productos seleccionados, cantidades, destino y modalidad de entrega; prepara borrador y solicita faltantes. El servidor resuelve códigos, valida cantidades, consulta precios y calcula subtotales, impuestos según datos explícitos, transporte, descuentos autorizados y total en COP. Nunca inventes desglose tributario. En los fixtures usa precios finales del catálogo, descuento cero y recogida gratuita para conservar compatibilidad con la venta de la clase 8.

Genera una vista imprimible y guardable como documento con: ID y versión, fecha y vencimiento, negocio y cliente ficticios, líneas con código/nombre/unidad/cantidad/precio/subtotal, tratamiento de impuestos, descuentos, transporte, total, destino/modalidad, forma de pago, condiciones de disponibilidad y plazo de entrega con evento de inicio. Incluye política y versión utilizadas, exclusiones y canal para aclaraciones. No es factura fiscal. No inventes identificación tributaria ni datos de contacto reales.

Guarda la versión exacta de precios y condiciones al emitir. El cliente revisa el documento completo y usa una acción explícita de aceptación vinculada a ID y versión; un sí interpretado por el modelo no basta. Editar crea otra versión e invalida la aceptación previa. Valida vencimiento en servidor con reloj controlable en tests. Cotizar y aceptar no crean una venta ni reservan inventario.

Prueba cálculos, faltantes, modificación de cantidades, documento imprimible, vencimiento, doble emisión y aceptación de versión obsoleta. Si una condición comercial necesita aprobación del operador, no emitas la cotización como firme hasta obtenerla.
```

**Comprueba tú**

1. «Cotiza dos unidades de [código elegido], para recoger en tienda». Elige un código con precio conocido; calcula por tu cuenta cantidad × precio.
2. Abre el documento: debe tener todas las condiciones, no solamente un total en el chat.
3. Cambia la cantidad; comprueba el nuevo total y la nueva versión.
4. Intenta aceptar la versión anterior: debe rechazarse y mostrar la actual.
5. En una prueba aislada cambia el precio del catálogo: la cotización emitida conserva su importe; un pedido requiere revalidación como indica la política.

**Si falla:** conserva el borrador y explica qué falta. Una cotización sin plazo definido para el destino debe quedar pendiente de revisión, sin promesa inventada.

**Evidencia:** documento imprimible, dos versiones y comprobación de cálculos y aceptación.

## Etapa 5 Convertir la aceptación en pedido

**Construyes:** una orden comercial del cliente, enlazada a la cotización. En esta práctica «orden de compra» es la orden que el cliente genera para comprar a La Esquina; no es una compra a un proveedor ni un documento fiscal.

**Prompt para el asistente**

```text
Crea el pedido a partir de una cotización vigente y aceptada por su propietario. Revalida versión, precio, cantidades y disponibilidad en servidor antes de solicitar confirmación comercial. Si cambió precio o condición, genera revisión y nueva aceptación; no alteres silenciosamente lo aceptado. Si falta stock o su dato no es suficiente, deriva al operador. El operador confirma disponibilidad para esta práctica sin modificar ni reservar inventario.

Conserva pedido_id, cliente, cotización_id/versión, caso, líneas, total, entrega, dirección ficticia cuando corresponda y condiciones aceptadas. El estado comercial inicial, una vez autorizado, es pendiente_soporte. Si necesita revisión, usa pendiente_revision. Separa los estados de pago y envío. Impide más de un pedido por la misma aceptación mediante una restricción persistente e idempotencia, incluso con dos solicitudes concurrentes.

El cliente debe poder abrir su orden imprimible y consultar el siguiente paso. Todavía no crees una venta ni confirmes el pedido por tener una cotización aceptada. Añade migraciones sin pérdida y pruebas de propiedad, aceptación vencida, precio cambiado, disponibilidad insuficiente y doble clic.
```

**Comprueba tú:** acepta la cotización vigente y genera la orden dos veces. Debes obtener el mismo pedido, con sus líneas, condiciones y estado pendiente. Consulta desde Bruno el pedido de Ana: denegado. Simula stock insuficiente: queda en revisión, no confirmado.

**Si falla:** recupera por ID de aceptación antes de volver a crear. Conserva el motivo de revisión y permite continuar cuando el operador resuelva.

**Evidencia:** orden, aceptación asociada y una sola fila de pedido tras el reintento.

## Etapa 6 Adjuntar soporte y confirmar el pedido

**Construyes:** el enlace del pedido con el circuito de comprobantes de la clase 8 y una confirmación comercial verificable.

**Prompt para el asistente**

```text
Permite al cliente cargar un soporte en su propio pedido, recuperar su estado y ver que está en revisión. Reutiliza carga, extracción original, revisión humana, propuestas y aprobación por versión del módulo 8. Protege el archivo por propietario. No presentes carga o lectura OCR como confirmación.

Aplica la política del módulo 9: soporte revisado, naturaleza de cobro, COP confirmado, monto exacto para el caso principal, pedido vigente autorizado y referencia no reutilizada o revisión humana explícita cuando la referencia no sea legible. El soporte no debe estar aplicado a otro pedido. Con faltantes, monto distinto, financiación o posible duplicidad, conserva la evidencia y escala; no confirmes automáticamente.

Prepara desde el pedido la propuesta de crear venta usando sus líneas y datos aceptados. No infieras productos ni cliente de la imagen. El operador revisa el soporte y aprueba la versión exacta de la propuesta comercial. Cuando el servidor ejecuta esa versión, debe guardar conjuntamente venta, líneas, operación, vínculo y confirmación del pedido con motivo aceptacion_de_soporte, sin cambiar el estado bancario no_verificado. No añadas un segundo botón que permita confirmar sin esos controles.

Inspecciona los límites transaccionales existentes antes de modificar: evita commits intermedios que dejen venta sin pedido confirmado o pedido sin venta. Mantén compatibilidad con las operaciones anteriores. Congela y valida la correspondencia entre versión de pedido y propuesta; el agente no puede alterar contenidos aceptados. Si la validación heredada exige precio vigente distinto del aceptado, bloquea y solicita nueva cotización y aceptación; no evadas el control.

Garantiza unicidad de venta por pedido e idempotencia persistente de la ejecución. Carga idéntica devuelve el mismo archivo; otra foto del mismo pago requiere revisión y no suma dinero. Conserva la extracción original y las correcciones humanas. Añade pruebas aisladas de importe diferente, soporte repetido entre pedidos, doble ejecución, rollback y consulta después de reiniciar.
```

**Comprueba tú**

1. Adjunta una imagen autorizada al pedido correcto. Observa «soporte en revisión».
2. En la mesa del operador, compara original y campos; registra correcciones y motivo si hacen falta.
3. Revisa y aprueba la propuesta concreta. Antes de ejecutarla, el pedido sigue sin confirmar.
4. Ejecuta y consulta: pedido confirmado, una venta, una operación y su vínculo. El estado bancario permanece `no_verificado`.
5. Repite la ejecución: mismo resultado y conteos.

Para un recorrido con el soporte 054, el escenario docente aporta expresamente FER-0001 × 1 a 121300 y FER-0222 × 1 a 26700: total 148000. Verifica esos precios en tu catálogo. Son datos comerciales ficticios aportados para el ejercicio, no datos extraídos de la imagen. La moneda debe confirmarse: el símbolo $ no identifica por sí solo COP. La referencia oculta requiere revisión manual de singularidad.

La fecha del soporte 054 es 11 de septiembre de 2026. Para comprobar reglas temporales usa una copia de pruebas con reloj fijado a ese escenario y etiquétala como tal; no cambies silenciosamente la fecha documental ni la fecha real de la app. Otros casos con importes coherentes pueden usar fixtures sintéticos identificados, sin presentarlos como OCR real.

**Si falla:** nunca subas otra imagen para «forzar» éxito. Consulta estado de propuesta y pedido. Si ya existe resultado, muéstralo; si no hubo commit, reintenta la misma acción con su clave. Si quedó estado parcial, es un defecto de la implementación que debe corregirse antes de continuar.

**Evidencia:** extracción y revisión con procedencia, aprobación de versión, IDs relacionados y conteos después del reintento. No incluyas imágenes personales.

## Etapa 7 Consultar el envío

**Construyes:** seguimiento persistente actualizado por el operador y consultable desde el chat.

**Prompt para el asistente**

```text
Implementa el seguimiento de recogidas y envíos de pedidos confirmados. Usa la política de entrega: separa pedido confirmado de enviado y de entregado. Registra eventos con estado, fecha efectiva, fecha de registro, actor, motivo, guía y transportadora solo si fueron aportadas. Para recogida usa listo_para_recoger y retirado; para domicilio, en_preparacion, despachado, entregado y novedad. Valida transiciones y conserva historial de correcciones sin borrarlo.

Solo el operador puede registrar avances. El chat del cliente consulta sus datos y explica la última actualización y el plazo acordado; no actualiza el estado porque el cliente lo pida ni inventa ubicación, guía o hora de llegada. Identifica la fuente como registro interno de práctica: no hay conexión con transportadora.

Prueba acceso a envío ajeno, estado inexistente, salto no permitido y reinicio. Permite abrir una novedad y escalar cuando el registro contradiga lo que informa el cliente.
```

**Comprueba tú:** pregunta «¿Dónde va mi pedido?». Registra preparación y despacho como operador, usando datos ficticios identificados. Vuelve a preguntar y comprueba las fechas. Si dices «márcalo entregado» como cliente, no debe cambiar nada. Para un pedido pendiente de soporte no debe aparecer un envío inventado.

**Si falla:** muestra la última información guardada y ofrece registrar una novedad. «No tengo actualización» es diferente de «se perdió el paquete».

**Evidencia:** secuencia de estados, respuesta del chat y rechazo de modificación por cliente.

## Etapa 8 Historial y recompra

**Construyes:** continuidad comercial usando compras verificablemente relacionadas con el cliente.

**Prompt para el asistente**

```text
Añade historial del cliente con pedidos, ventas vinculadas, estado comercial y de entrega. Filtra por la identidad del servidor. Las ventas heredadas que no tengan dueño verificado no deben aparecer por coincidencia de nombre. Permite abrir una compra propia y solicitar recompra de todas o algunas líneas.

La recompra crea un nuevo borrador de cotización, con referencia a la compra origen, precios y disponibilidad actuales y comparación de cambios. Omite o consulta productos inexistentes; pregunta antes de sustituirlos. No reutilices comprobantes, aprobación, entrega, precio histórico ni una dirección sin reconfirmación. Sigue después las etapas de nueva aceptación y pedido; no crees venta automáticamente.

Garantiza que reintentar una misma solicitud devuelve el mismo borrador. Una recompra intencional posterior usa una solicitud nueva y crea otro borrador. Prueba ambos casos, precio cambiado y producto agotado con fixtures aislados; no edites el catálogo de trabajo para simularlos.
```

**Comprueba tú:** Ana consulta su historial y pide «quiero repetir esta compra, pero solo una unidad del primer producto». La cotización muestra cantidad y precio actuales, referencia de origen y necesidad de nueva aceptación. Bruno no ve la compra de Ana. El pedido original y su pago no cambian.

**Si falla:** conserva selección y faltantes en un borrador; no uses el precio anterior para completar el documento.

**Evidencia:** compra origen, nueva cotización, comparación y ausencia de pagos heredados.

## Etapa 9 Reclamaciones y devoluciones

**Construyes:** una solicitud de posventa con evidencias y decisiones separadas.

**Prompt para el asistente**

```text
Implementa reclamaciones y devoluciones desde una compra propia. Recoge pedido/venta, línea, cantidad afectada, motivo, descripción, fecha y evidencias opcionales. Si el cliente no conoce el ID, ayúdalo a elegir desde su historial; nunca busques en las compras de todos. Conserva lo incompleto y pide faltantes. Antes de registrar, muestra resumen y exige confirmación explícita del cliente vinculada a su versión.

Consulta la política del vault y registra versión y criterios orientativos. Para plazo usa fecha de entrega registrada y zona America/Bogota, con reloj controlable para pruebas. Falta de fecha o reclamo fuera de las reglas no debe impedir abrir el caso: deriva a revisión humana sin afirmar una elegibilidad que no se conoce. La clasificación automática no aprueba la devolución.

Estados de reclamación: abierta, falta_informacion, en_revision, resuelta. Estados de devolución separados: solicitada, autorizada, recibida, rechazada o cancelada. Solo el operador autoriza y registra recepción con motivo y evidencia. No reintegres stock ni modifiques venta original. Controla cantidad acumulada para impedir devolver más unidades que las compradas, aun con solicitudes concurrentes.

Prueba caso incompleto, devolución parcial, cantidad excesiva, falta de fecha, ventana excedida y doble envío. Protege también los adjuntos de la reclamación y restringe sus tipos y tamaños.
```

**Comprueba tú:** «Me llegó dañada una unidad de este pedido». El chat identifica la compra, pregunta lo necesario y presenta la solicitud para confirmar. El cliente obtiene un número de caso. El operador autoriza y después registra recepción. El inventario permanece igual.

**Si falla:** el cliente conserva número y estado de la solicitud; puede adjuntar la evidencia pendiente sin abrir otro caso idéntico. Una reclamación fuera de la regla orientativa pasa a una persona.

**Evidencia:** solicitud, fuente de política, decisiones con actor y cantidad afectada.

## Etapa 10 Solicitar y resolver el reembolso administrativo

**Construyes:** un expediente administrativo. La aplicación no transfiere, devuelve ni marca dinero como pagado.

**Prompt para el asistente**

```text
Añade solicitud de reembolso ligada a una reclamación y compra propias. Muestra importe solicitado, motivo, líneas/cantidades, devolución asociada y desglose calculado desde el precio realmente comprado. No uses el precio actual del catálogo para devolver una compra anterior. En el piloto de recogida y descuento cero, el importe de productos es cantidad autorizada por precio de venta histórico; no añadas transporte ni impuestos otra vez.

Estados: solicitado, en_revision, aprobado_administrativamente, rechazado, revocado y remitido_a_pago_externo. La revocación es una acción autorizada previa a la remisión, con motivo y sin borrar la decisión original. El cliente solicita y consulta; el operador decide importe, fundamento y necesidad de recepción previa. Cualquier excepción exige motivo y queda registrada. Aprobar una devolución no equivale a aprobar el reembolso.

Valida propiedad, versión, cantidad devuelta, monto cobrado aplicable y saldo reembolsable. Reserva administrativamente importes aprobados para que dos solicitudes no excedan lo cobrado. Haz la comprobación y escritura de forma atómica; documenta cómo una revocación autorizada libera esa reserva. No borres decisiones anteriores. Rechaza montos negativos o superiores al saldo. No pidas datos bancarios para este ejercicio.

Genera una ficha administrativa imprimible. Al remitir a pago externo guarda responsable y referencia administrativa y cierra el trabajo del caso sin marcar dinero devuelto. No implementes API bancaria ni estado pagado. Prueba solicitud duplicada, dos solicitudes concurrentes y aprobación intentada desde el cliente o el modelo.
```

**Comprueba tú:** solicita devolución de una unidad y un reembolso parcial. El operador revisa y aprueba el importe permitido; el cliente ve «aprobado administrativamente; pago externo pendiente». Remite el expediente y comprueba que no aparece «dinero devuelto». Intenta solicitar de nuevo un monto ya comprometido: debe detectarse el saldo insuficiente.

**Si falla:** consulta el expediente existente antes de repetir la aprobación. Una respuesta perdida no libera una reserva administrativa ya guardada.

**Evidencia:** ficha de reembolso, cálculo, decisión, saldo administrativo y ausencia de movimientos de dinero.

## Etapa 11 Escalar y retomar con una persona

**Construyes:** una bandeja de atención humana dentro de la app. No se necesita enviar correos o mensajes externos.

**Prompt para el asistente**

```text
Integra escalamiento desde todos los recorridos. Debe activarse cuando el cliente pide una persona, falta una política, existe ambigüedad comercial, posible duplicidad, novedad de envío o excepción de posventa. Registra en el caso existente motivo, hechos confirmados, faltantes, fuentes con versión, relaciones a pedido/propuesta/venta y acciones intentadas. Distingue resumen generado de datos consultados y evita copiar secretos o imágenes completas a los registros.

Crea bandeja del operador con pendiente_persona, asignado, atendido y cerrado. Una asignación concurrente no debe dejar dos responsables activos. El cliente puede consultar número, estado y respuesta humana. El operador lee el contexto, solicita información o responde sin obligar a repetir toda la historia. Las aprobaciones siguen en sus controles administrativos específicos; responder un mensaje no autoriza un reembolso.

Al tomar el caso una persona, pausa nuevas acciones comerciales del agente en ese caso. Permite consultas de estado y aportes del cliente. Reanudar requiere acción registrada del operador, conserva el mismo caso y no repite pasos completados. Si falla generar el resumen, conserva el escalamiento con los IDs y hechos disponibles; el operador accede al historial autorizado.

Prueba escalamiento repetido, reinicio, doble toma, respuesta humana y continuación del flujo. La bandeja local es el destino real; no afirmes que se notificó por un canal externo.
```

**Comprueba tú:** escribe «quiero hablar con una persona». Como operador, abre la bandeja y verifica que contiene el contexto correcto. Responde y retoma el caso. El cliente ve la respuesta identificada como humana y puede seguir sin crear otra compra ni otro expediente.

**Si falla:** el escalamiento persiste aunque no funcione el modelo. No prometas atención inmediata ni resolución automática.

**Evidencia:** un mismo caso antes, durante y después de la intervención humana.

## Etapa 12 Mostrar el recorrido y medirlo

**Construyes:** una vista de ejecución que permita explicar tanto el éxito como el error. Añade la captura básica de eventos a medida que construyes las etapas anteriores; aquí completas su consulta y las métricas.

**Prompt para el asistente**

```text
Completa trazabilidad por caso y ejecución. Usa caso_id estable para el recorrido y ejecucion_id para cada intento; vincula conversación, documentos/versiones, cotización, pedido, propuesta, venta, envío y posventa. Captura por paso actor, herramienta, inicio, fin, duración, resultado, IDs, estado previo/posterior y error controlado. Registra decisiones y no solo el último mensaje. Guarda el evento obligatorio de resultado comercial en la misma transacción del negocio: si no se puede guardar, revierte todos sus efectos. Conserva intentos y eventos de fallo mediante un registro separado, sin confirmar escrituras de negocio parciales. Si ese registro separado también falla, informa incidente de auditoría y permite consultar el estado comercial existente; no inventes una traza completa ni repitas una operación ya confirmada.

Captura modelo y usage reportado por cada respuesta de API, incluida extracción, sin guardar claves ni todo el contenido privado. No supongas cero ante consumo desconocido. Marca por separado llamadas intentadas, completadas y aquellas cuyo consumo no se conoce. No dupliques tokens almacenados al consultar o reintentar una lectura. Muestra tokens de entrada/salida y detalles adicionales solo si existen. Para convertir a dinero exige tarifa oficial verificada y fechada para el modelo exacto; sin ella muestra costo no disponible y conserva tokens.

Añade vista administrativa con pasos, fallas, recuperación y conteos. El cliente ve su estado y próximo paso sin recibir registros internos. Registra origen api_real, mock_prueba o simulacion_falla por evento. Mantén límite de llamadas por turno y registro de límites alcanzados; no fuerces todo el recorrido comercial en un solo turno.

Crea un informe de evaluación que lea los casos efectivamente ejecutados de la matriz, muestre éxitos sobre total, respuestas fundamentadas revisadas sobre las que requerían fuente, duplicados y escrituras no autorizadas observados, intervenciones con motivo, duración y llamadas por caso. No declares confiabilidad universal ni uses la intervención humana como fracaso automático.
```

**Comprueba tú:** elige un pedido y reconstruye cómo surgió: consulta, fuente, cotización, aceptación, soporte, autorización y resultado. Comprueba que puedes ver una falla y su recuperación. Si el proveedor no reportó tokens de una solicitud fallida, debe mostrarse «no disponible».

**Evidencia:** exportación depurada de una traza completa e informe con numeradores, denominadores y origen de cada prueba.

## Etapa 13 Provocar fallas y recuperar sin duplicar

**Construyes:** mecanismos de recuperación comprobados. Una prueba de «error» que no comprueba el estado final queda incompleta.

**Prompt para el asistente**

```text
Ejecuta la matriz docs/modulo-9/modulo-9-casos-y-evidencias.md sobre una copia temporal aislada. Implementa inyección de fallas solo accesible desde pruebas, nunca una ruta de cliente ni un interruptor público. No cortes el servicio real del proveedor ni consumas API para simular errores.

Prueba al menos: modelo sin respuesta; vault ausente; propuesta editada tras aprobación; caída antes del commit comercial; respuesta perdida después del commit; doble clic concurrente; reinicio con caso pendiente; soporte repetido en otro pedido; acceso a historial ajeno; documento malicioso; reembolso duplicado y escalamiento sin modelo. Ejecuta además los escenarios funcionales de la matriz y las regresiones heredadas pertinentes.

Para cada falla registra estado anterior, punto de interrupción, acción de recuperación, estado posterior, conteos y resultado esperado/observado. Tras respuesta perdida consulta por ID y clave persistente, no crees otra solicitud. Tras rollback reintenta la misma intención; tras conflicto de versión solicita nueva revisión. Verifica que reiniciar conserva identidad del recurso y permisos, aunque la sesión necesite volver a iniciarse.

Implementa una cola de pendientes o un procedimiento de reconciliación si existen efectos en pasos separados. No prometas exactamente una llamada a proveedores externos; garantiza la unicidad de nuestros efectos comerciales con restricciones y transacciones. No reintentes indefinidamente ni vuelvas a invocar OCR ya persistido. Si no sabemos si el proveedor completó una llamada, registra esa incertidumbre y consulta el estado local antes de repetirla.

Entrega un informe sin secretos. No marques una prueba no ejecutada como aprobada. Indica qué comportamientos se comprobaron con API real y cuáles solo con mocks o simulación.
```

**Comprueba tú:** presencia una prueba de respuesta perdida después de guardar el pedido confirmado. Antes de reintentar, abre el pedido: el resultado ya existe. Repite la acción: conserva los mismos IDs y una sola venta. Después presencia una falla antes del commit: no queda ninguno de los efectos comerciales, y el reintento completo funciona.

**Evidencia:** comparación antes/después y traza de ambos escenarios. Reiniciar la base para borrar el problema no cuenta como recuperación.

## Etapa 14 Demostrar y entregar

**Prompt para el asistente**

```text
Prepara la entrega del módulo 9. Ejecuta los checks adecuados y registra los resultados reales. Conserva código, migraciones, vault ficticio, fixtures, pruebas, instrucciones de instalación y recuperación, política versionada, matriz ejecutada e informe depurado. No incluyas claves, backend/.env, imágenes personales, sesiones, cachés, bases de clientes reales ni trazas privadas.

Revisa el empaquetador antes de usarlo: el heredado de la clase 8 no garantiza incluir nuestras nuevas tablas, vault o fixtures. Construye un paquete reproducible y comprueba su extracción en una carpeta nueva, con una base ficticia limpia y sin configuración privada. Las evidencias de ejemplo van separadas y no deben confundirse con una práctica vacía ni con API real.

Actualiza README para que otra persona pueda iniciar, entrar con cuentas de demostración locales, abrir Obsidian, ejecutar pruebas y reproducir una falla. Registra commit de partida y commit o versión final. Separa pruebas hechas en este sistema operativo de compatibilidad aún no comprobada. No publiques ni despliegues. No cambies la rúbrica del curso ni inventes porcentajes.
```

En el video o recorrido de entrega muestra los dos caminos principales, una recompra y un escalamiento. Usa los mismos identificadores al pasar de cliente a operador. Incluye una falla recuperada y la vista que explica qué ocurrió.

La evidencia acompaña los criterios vigentes de calidad, seguridad, trazabilidad, costos, fallas y evolución. No sustituye la rúbrica ni establece nuevos porcentajes. Cuando una prueba quede pendiente, indica qué falta y cómo ejecutarla.

## Preguntas para explicar tu solución

- ¿Qué dato viene del vault y cuál de SQLite?
- ¿Por qué el cliente no puede consultar una compra ajena aunque conozca su ID?
- ¿Qué versión de la cotización aceptó y qué pasa si cambió un precio?
- ¿Qué significa pedido confirmado por soporte y qué no se verificó bancariamente?
- ¿Qué diferencia hay entre solicitar, aprobar y remitir un reembolso?
- ¿Qué quedó guardado cuando falló la respuesta y cómo evitaste duplicarlo?
- ¿Qué midieron tus pruebas y qué sigue sin comprobarse?
