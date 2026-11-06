# Taller de ventas y posventa de Comercial La Esquina

Clase 9 · Integración multisistema y operación confiable
Mentor: William Vergara · Encuentro: 6 de noviembre de 2026 · Entrega: 20 de noviembre de 2026

Construye un canal donde un cliente consulta conocimiento de Obsidian, revisa disponibilidad, obtiene una cotización, genera un pedido y adjunta un comprobante. Después puede consultar su envío e historial, repetir una compra y solicitar atención de una persona, una devolución o un reembolso administrativo.

La meta es componer una solución medible: seguir un caso completo, comprobar sus resultados y recuperarlo después de una falla. Trabaja por etapas. En cada una, pide al asistente que construya, prueba tú el resultado y conserva evidencia antes de continuar. No hace falta terminar todos los recorridos durante el encuentro; la construcción y las evidencias continúan hasta la entrega.

Este taller parte de la app inicial Módulo 9. Hereda comprobantes y propuestas revisadas de la clase 8; todavía no incluye el portal de clientes, las cotizaciones ni la posventa descritos aquí. Los prompts siguientes son encargos de construcción: leerlos no implementa las capacidades. Las políticas del archivo acompañante son reglas ficticias del ejercicio y se pueden ajustar con el mentor antes de implementarlas.

## Mapa de construcción

| Etapa | Pieza que se construye | Comprobación decisiva |
| --- | --- | --- |
| 0 | Copia independiente y arranque | Catálogo y verificación de base funcionan. |
| 1 | Registro, sesiones y permisos | Bruno no puede consultar datos ni archivos de Ana. |
| 2 | Chat con conocimiento | La respuesta cita una nota autorizada que la respalda. |
| 3 | Catálogo y disponibilidad | Distingue stock agotado, desconocido e histórico. |
| 4 | Cotización versionada | Total reproducible y aceptación de la versión vigente. |
| 5 | Orden del cliente | Un pedido por aceptación, incluso con doble clic. |
| 6 | Soporte y confirmación | Una venta y pedido confirmado mediante revisión. |
| 7 | Seguimiento | Solo el operador registra cambios de entrega. |
| 8 | Historial y recompra | Nueva cotización sin heredar pago ni aprobación. |
| 9 | Reclamación y devolución | Cantidades y decisiones quedan separadas y registradas. |
| 10 | Reembolso administrativo | Compromisos no exceden saldo; no hay transferencia. |
| 11 | Atención humana | El mismo caso continúa con contexto y responsable. |
| 12 | Trazas y métricas | Se reconstruye el caso y se identifica el consumo conocido. |
| 13 | Recuperación | Antes/después del commit sin efectos duplicados. |
| 14 | Entrega | Otra copia limpia puede arrancar y reproducir el caso. |

La atención humana se integra desde el inicio como solicitud persistente; su bandeja completa llega en la etapa 11. Las trazas se capturan desde la etapa 1; en la 12 se construye su vista y evaluación. Así no dependemos de reconstruir al final lo que nunca se registró.

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
- Repositorio público de partida: [MrsWiver/Modulo9](https://github.com/MrsWiver/Modulo9). Contiene app, vault y materiales. También puedes usar el ZIP independiente del módulo 9, si lo recibiste.
- `README.md`, `AGENTS.md`, `docs/CONTRATOS.md`, `docs/CONTRATOS-M9.md`, `docs/VALIDACION.md` y `BASE.json` dentro de esa copia.

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

## Antes de construir: dos conversaciones distintas

| Espacio | Qué haces | Ejemplo |
| --- | --- | --- |
| Asistente de programación, como OpenCode | Le encargas construir, ejecutar y probar la app | «Implementa solo la etapa 1 y comprueba sus permisos». |
| Chat del cliente dentro de La Esquina | Usas la función ya construida | «Cotiza una unidad para recoger». |
| Mesa del operador | Revisas, autorizas y registras decisiones humanas | Aprobar la versión de una propuesta o recibir una devolución. |
| Obsidian | Editas conocimiento comercial aprobado | Revisar condiciones y versión de una política. |

El asistente de programación ejecuta el trabajo técnico. Tú revisas el resultado visible y tomas las decisiones del negocio. No pegues todos los prompts a la vez: termina y comprueba una etapa antes de pedir la siguiente. Si una etapa necesita varias sesiones, retoma desde el último resultado registrado.

### Lo que debe existir al cerrar cada etapa

1. Una función usable en la interfaz, con su registro persistido cuando corresponde.
2. Pruebas de la regla implementada, no solo de que una página devuelve 200.
3. Un recorrido manual que tú observaste y una prueba de rechazo o excepción.
4. Un registro de avance con IDs, resultado, origen de prueba y pendientes.

Usaremos referencias como COT-A, PED-A y CASO-A para hablar del recorrido; anota los IDs reales que genere tu copia. No son identificadores que debas forzar en la base. Ana compra y Bruno sirve para comprobar aislamiento. Una tercera cuenta, creada desde el formulario, empieza sin compras.

### Tu primera acción

Abre el asistente en la carpeta elegida. Si usas OpenCode desde terminal, inicia `opencode`. Si ya tienes la app clonada y funcionando gracias a la guía de instalación, entrégale esa ruta y pide comprobarla: no descargues otra copia encima ni vuelvas a preparar la clase 8.

## Cómo trabajar con el asistente

Pega el siguiente acuerdo al empezar la sesión de construcción. Luego entrega un prompt de etapa por vez. Reutilízalo si cambias de asistente.

```text
Estamos construyendo el módulo 9 de Comercial La Esquina. Lee AGENTS.md, README.md,
docs/CONTRATOS.md, docs/CONTRATOS-M9.md, docs/VALIDACION.md y los tres documentos del módulo 9
que te indicaré en la etapa 0. Ayúdame a construir por etapas. Guíame con pasos claros,
explica cada decisión y verifica el resultado antes de continuar.

Ejecuta tú instalación, configuración técnica, cambios, diagnóstico y pruebas. Pídeme
intervención para escribir credenciales privadas o resolver una decisión del negocio; nunca me
pidas pegar claves en el chat. No hagas llamadas pagadas durante pruebas automáticas. Para una
prueba real explícita, usa solo la solicitud o imagen que se esté verificando y registra su
procedencia.

Conserva la base inicial del módulo 9 y las imágenes autorizadas que hereda de la clase 8. No
reinicialices mi práctica ni modifiques el proyecto de la clase 3. Conserva el prompt íntegro
del extractor, OPENAI_OCR_MODEL y OPENAI_CHAT_MODEL según la configuración existente; no
cambies de modelo por tu cuenta. Nunca uses docente/ como respuesta de IA.

Implementa únicamente la etapa solicitada. Antes de modificar explica qué construirás, qué
reutilizarás y cómo lo comprobarás; después procede. Usa migraciones y permisos de servidor.
No habilites SQL libre, aprobación administrativa, ejecución comercial, lectura arbitraria de
archivos ni cambio de cliente como herramientas del chat del cliente. Preserva inventario en
lectura, revisión, propuestas versionadas, autorización humana e idempotencia. No publiques ni
despliegues.

Prepara desde la etapa 1 un escalamiento mínimo persistente con motivo e IDs, aunque la
bandeja completa se construya en la etapa 11. Si aún no existe, informa que falta
implementarlo; no afirmes haber avisado a una persona.

Desde la primera etapa nueva registra caso_id, actor, acción, resultado y error, con IDs
relacionados; completarás su vista y métricas en la etapa 12. Al cerrar cada etapa entrega
archivos cambiados, cómo iniciar o retomar, pruebas con sus resultados, IDs para comprobar y
cualquier pendiente. Distingue claramente función implementada, prueba con mock, simulación de
falla y ejecución real con IA. No declares completado un recorrido solo porque respondió el
chat.
```

## Preparación privada de IA: cuando llegues a la etapa 2

El catálogo y las pruebas no necesitan IA. La conexión real del chat sí necesita una credencial propia y el modelo configurado para la app. El acceso a tu asistente de programación es independiente. Esta preparación no realiza ninguna llamada.

**Copia en el asistente — preparar sin mostrar secretos:**

```text
Prepara la configuración privada de esta copia de Modulo9.
La app lee backend/.env. Si no existe, cópialo desde backend/.env.example
con OPENAI_API_KEY vacía y conserva los modelos del ejemplo.
Si ya existe, no lo leas, muestres ni sobrescribas.
Comprueba que backend/.env está ignorado y no versionado, sin abrirlo.
Comprueba por configuración pública que OPENAI_OCR_MODEL y OPENAI_CHAT_MODEL
se conservan según el curso; no sustituyas modelos automáticamente.
Indícame la ruta absoluta para abrir el archivo en mi editor local.
No pegues su contenido en el chat ni hagas llamadas reales. Espera a que yo
confirme que lo guardé antes de una comprobación real que solicitemos.
```

Ingresa la clave directamente en tu editor, guarda y reinicia el servidor. Conserva `OPENAI_OCR_MODEL=gpt-5.6-luna` y `OPENAI_CHAT_MODEL=gpt-5.6-luna`, como establece el repositorio. No envíes la clave en el chat del asistente ni en el de clientes.

**Para una demostración real puntual, después de construir la integración:**

```text
La configuración privada está guardada. Ejecuta únicamente una consulta real
al chat de cliente de mi sesión: «¿Cuánto dura una cotización?».
No proceses imágenes ni otros casos. No listes modelos ni cambies la configuración.
Muestra respuesta, fuente recuperada, IDs de la traza y consumo reportado,
sin mostrar la clave. Si falla, informa el error y no reintentes automáticamente.
```

Esta comprobación puede consumir saldo. Si no la ejecutas, registra «chat probado con mock; integración real pendiente». Una respuesta fija o de un mock permite probar interfaz y reglas, pero no demuestra una conversación real con herramientas.

## Cierre de cada etapa: pide evidencia antes de seguir

Después del prompt de construcción, usa este pedido:

```text
Comprueba la etapa que acabas de implementar. Ejecuta pruebas específicas de
sus reglas y uv run pytest -q; corrige los fallos introducidos.
Usa fixtures temporales y mocks identificados; no hagas llamadas reales a IA.
Reinicia solo el servidor de esta copia si hace falta y verifica su URL activa.
Dime dónde entrar, qué escribir, qué acción realizar y qué resultado observar.
Comprueba permisos mediante acceso directo y mediante la herramienta del chat
cuando la etapa maneje información privada. Distingue simulación de uso real.
Actualiza el estado de capacidades y docs/modulo-9/AVANCE.md con: etapa,
archivos cambiados, migración, regla probada, resultado esperado/observado,
IDs, origen de la prueba y pendientes. No cambies etapas futuras a implementadas.
Conserva los pasos de arranque y recuperación. No publiques ni despliegues.
```

La columna de resultado observado se completa después de ejecutar. Una prueba pendiente conserva ese estado. La comprobación visible del estudiante y las pruebas automáticas se complementan.

## Etapa 0 Preparar una copia reproducible

**Construyes:** un espacio independiente para la clase 9 y un registro verificable del punto de partida. Si aún terminas la clase 8, esta copia permite construir las ampliaciones sin reemplazar tu entrega anterior.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Una app que abre y una base de partida registrada.

1. Abre el asistente de programación en una carpeta de trabajo. Si usas OpenCode en terminal, inicia `opencode`; utiliza el acceso al proveedor de programación que ya tienes configurado.
2. Entrégale el acuerdo anterior y después el prompt de esta etapa. El asistente clona, instala y ejecuta; tú completas únicamente los diálogos que el sistema requiera.
3. Recorre catálogo, mesa y construcción. Anota URL activa, commit y cómo detener el servidor antes de pedir cambios.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Prepara la app inicial desde https://github.com/MrsWiver/Modulo9.git.
Identifica sistema, terminal y ruta; comprueba Git y uv. Si faltan, usa fuentes
oficiales y explica cualquier intervención que requiera el sistema.
Clona en una carpeta nueva Modulo9. Si ya tengo una copia o ZIP del módulo 9,
comprueba origen y estado, conserva cambios y úsala sin reclonar encima.
No clones el módulo 8 ni reemplaces sus archivos. Trabaja siempre desde
la ruta absoluta de esta copia y no supongas que cd persiste entre herramientas.

Lee AGENTS.md, README.md, docs/TALLER.md, docs/CONTRATOS.md,
docs/CONTRATOS-M9.md, docs/VALIDACION.md y los tres documentos de docs/modulo-9/.
BASE.json registra la procedencia heredada 096d8fe37259a4c5d363c6eb666dc2976e6d0bc9;
no hagas checkout de ese commit en Modulo9: no es el commit de esta entrega.
Revisa Git y crea taller-modulo-9 si no existe y es seguro cambiar de rama.
Conserva cambios previos. No publiques ni despliegues.

Ejecuta uv python install 3.11 y uv sync --locked --python 3.11.
Ejecuta uv run python -m scripts.iniciar_datos conservando la práctica existente,
uv run python -m scripts.verificar_base y uv run pytest -q sin API real.
Arranca uv run python -m src.app como proceso persistente solo en 127.0.0.1:8009.
Conserva cómo detenerlo. Si el puerto está ocupado no cierres procesos ajenos:
identifica la causa y usa el puerto 8010 con el comando alternativo del README.
Mantén una sola instancia por carpeta de datos y comprueba las rutas /, /mesa,
/construccion y /api/modulo-9/estado mediante HTTP.

No leas .env ni configures IA todavía. No copies bases o secretos de otra clase.
Guarda docs/modulo-9/BASE.md con ruta, sistema, commit actual de Modulo9,
procedencia heredada, versiones, arranque, conteos y resultados reales.
Informa qué está implementado y qué devuelve 501 capacidad_pendiente.
Si falla el asistente de programación, conserva archivos y estado para retomar
con otro sin cambiar por ello el modelo configurado dentro de la app.
```

### Qué le estás pidiendo y por qué

Separar procedencia y commit actual evita volver por error a la clase 8. Instalar con el archivo de bloqueo conserva las versiones de dependencias. Verificar la base antes de construir permite distinguir un fallo heredado de uno introducido en el taller.



**Comprueba tú**

1. Abre la app y observa catálogo, ocho ventas y los ejemplos autorizados de la base limpia.
2. Busca ventas por `134200`: aparecen dos candidatos, no una asociación automática.
3. Comprueba el informe del asistente: commit, ruta nueva y pruebas. La base publicada b96215e pasó 65 pruebas en macOS con Python 3.11 durante la preparación de la guía; anota tu resultado real y no atribuyas esa prueba a Windows. Esas pruebas no acreditan las capacidades nuevas pendientes.
4. Cierra y abre la app. No desaparecen los registros que hayas creado en tu copia.

**Si falla:** instalación o puerto se diagnostican sin borrar datos. Si falta la clave, continúa con interfaz y pruebas aisladas; registra que la conversación real y el OCR real quedan pendientes. Un chat de comandos no cuenta como chat con IA conectado al vault.

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Abre `/` y busca `FER-0001`. | Aparece un producto del catálogo con precio; no un catálogo dibujado de ejemplo. |
| Abre `/construccion` y `/api/modulo-9/estado`. | Las nuevas capacidades figuran pendientes; un 501 no se presenta como éxito. |
| Revisa `verificar_base` y pytest. | Base limpia: 1.250 productos, 75 proveedores, 827 filas de inventario, 8 ventas y 12 soportes autorizados. Se informa el resultado de esta ejecución. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Si no abre, confirma primero proceso, puerto y carpeta. Después revisa el error de instalación. Conserva datos/practica/; reinicializarla no resuelve un puerto ocupado.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 0. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** `BASE.md`, resultado de las pruebas y captura del arranque. Tener la base lista no completa el módulo 9.

## Etapa 1 Crear cuentas y separar cliente y administración

**Construyes:** registro de clientes, inicio y cierre de sesión, conversación por cliente, caso persistente y permisos reales en el servidor. Ana y Bruno sirven como cuentas ficticias de prueba, además de una cuenta nueva que crearás desde el formulario.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Una puerta de entrada y un dueño para cada dato.

1. Construye primero registro, ingreso y salida, junto con un procedimiento separado para preparar al operador.
2. Añade identidad y propiedad a conversaciones, casos y futuros documentos. Registra eventos básicos y un mecanismo mínimo para dejar una solicitud pendiente de persona.
3. Protege las rutas heredadas antes de mostrar historial. Después prueba con sesiones independientes: Ana, Bruno y una cuenta creada desde cero.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Implementa registro de cliente, inicio y cierre de sesión, y separación de cliente y operador
del módulo 9. Crea formularios locales con nombre, correo y contraseña, validaciones, unicidad
del correo y cliente_id estable generado en servidor. Guarda contraseñas mediante el mecanismo
seguro de hash del framework, nunca texto ni registros de credenciales. La contraseña se
escribe solo en el formulario, no se pide al modelo ni en el chat. El registro público solo
crea rol cliente; el operador se prepara por un procedimiento administrativo separado.

Crea cuentas de prueba para Ana, Bruno y un operador, pero permite además registrar una cuenta
nueva desde la interfaz. Resuelve identidad en servidor, protege las sesiones y sus
escrituras, evita fijación de sesión y limita intentos de acceso. Invalida la sesión al salir.
No uses un parámetro cliente_id enviado por el modelo como identidad. Separa las sesiones de
los navegadores. Documenta cuentas ficticias para localhost, sin correo de verificación ni
recuperación por email implementados. No presentes el correo ingresado como identidad
verificada.

Permite consultas públicas de políticas y catálogo sin cuenta; exige iniciar sesión antes de
aceptar cotización, crear pedido o consultar recursos privados. Una cuenta nueva empieza con
historial vacío. Cada pedido, compra vinculada, caso y archivo conserva propietario por
cliente_id. No asignes ventas antiguas por coincidencia de nombre o correo. Si hay borrador
anónimo, no lo pierdas al iniciar sesión y solo vincúlalo desde la misma sesión previa, con
confirmación del cliente y validación en servidor.

Protege también las rutas existentes de la clase 8: API, historial global, imágenes, archivos,
comprobantes, ventas y propuestas. No basta con ocultar botones. Una sesión de cliente no
puede acceder a listados globales ni al agente administrativo anterior. Cada acceso a un
recurso debe validar propietario en servidor. Usa sesiones, protección de escrituras y cookies
apropiadas para el entorno local; conserva las protecciones existentes donde correspondan.

Añade conversaciones y casos de atención con propietario, ID, estado, fecha y versión. Separa
el estado de atención del estado de pedido, envío o reembolso. Conserva mensajes por
conversación, sin reutilizar el historial global para todos. Crea fixtures aislados con una
compra conocida de Ana y otra de Bruno; no atribuyas ventas antiguas a alguien por
coincidencia de nombre. No modifiques la semilla heredada.

Prueba accesos directos y mediante herramientas a los registros del otro cliente, archivos
incluidos. Comprueba que reiniciar preserva los casos. Todavía no implementes cotizaciones ni
pagos nuevos.
```

### Qué le estás pidiendo y por qué

Un nombre escrito en el chat no identifica al cliente. La sesión del servidor determina quién consulta. El hash protege la contraseña almacenada; no reemplaza los permisos de cada compra y archivo. La prueba con otra cuenta comprueba esa separación.



**Comprueba tú:** crea una cuenta ficticia nueva desde el formulario y comprueba que su historial está vacío. Intenta repetir el correo: no debe crear otro cliente. Cierra sesión e intenta abrir su historial: debe exigir acceso. Inicia sesión de nuevo y recupera sus casos tras reiniciar. Después entra como Ana en una ventana y como Bruno en otra sesión independiente. Inicia conversaciones diferentes; no deben mezclarse. Intenta consultar como Bruno el ID de una compra o soporte de Ana: debe denegarse sin revelar su contenido. El operador ve su bandeja mediante su propia sesión.

**Si falla:** detén las funciones de historial hasta corregir la propiedad. Un filtro que el modelo puede omitir no resuelve el problema.

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Registra una cuenta ficticia y repite su correo. | Se crea un solo cliente; el segundo registro informa la validación y no mezcla identidades. |
| Cierra sesión e intenta abrir una URL privada guardada. | Exige autenticación y no devuelve contenido privado. |
| Como Bruno solicita por URL y por chat un caso o archivo de Ana. | No obtiene datos de Ana. Una respuesta de error no incluye su nombre, importe o contenido. |
| Como cliente intenta abrir `/mesa`, listados globales y el agente administrativo. | El servidor bloquea el acceso; ocultar el menú no cuenta como protección. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Si se filtra un registro, no habilites historial ni continúes con operaciones privadas. Corrige la comprobación de propiedad en servidor y repite tanto la consulta directa como la herramienta del chat.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 1. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** registro de cuenta nueva, ID de cliente, comprobación de correo duplicado, inicio/cierre de sesión, IDs de dos casos, sesiones separadas y prueba de acceso denegado. No muestres contraseñas en las evidencias.

## Etapa 2 Conectar el chat con el vault de Obsidian

**Construyes:** un vault comercial y una herramienta de búsqueda que devuelve evidencia. Empieza por búsqueda de texto y secciones; una base vectorial es opcional si puedes justificar la necesidad.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Un chat que busca antes de afirmar una regla.

1. Abre la bóveda existente en Obsidian y localiza las políticas de cotizaciones y entregas. Revisa versión y audiencia antes de cambiar código.
2. Construye búsqueda y lectura acotadas, compruébalas sin modelo y añade fuentes visibles. Después conecta esas herramientas al chat del cliente.
3. Prepara configuración privada solo si harás la demostración real; prueba una pregunta concreta y contrasta la respuesta con la nota que cita.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Inspecciona y conserva el vault existente conocimiento/la-esquina/ y su manifiesto.
Ya contiene 2.191 notas: productos, políticas, guías y referencias internas.
Lee las políticas ficticias vigentes de docs/modulo-9/modulo-9-politicas-y-datos.md
y contrástalas con las notas; no regeneres ni sobrescribas ediciones humanas.
Si encuentras contradicciones, informa cuáles y deja pendiente la publicación.
Comprueba ID, versión, vigencia, estado y audiencia en la recuperación.
Inicio.md e Interno/ son internos. Aplica una lista publicada de documentos
cliente, mantenida por operador: editar audiencia en una nota no la autoriza
por sí solo. Revalida permisos de cada fragmento y cada enlace.

Implementa buscar_conocimiento y consultar_fragmento restringidas al directorio autorizado.
Devuelve documento, versión, fecha, encabezado, fragmento y huella del contenido. Excluye
secretos, archivos no Markdown, rutas externas y enlaces simbólicos que salgan del directorio.
No ejecutes código ni visites enlaces de una nota. Refleja cambios guardados en Obsidian sin
reiniciar; muestra cuándo se consultó la fuente. Si falta evidencia, devuelve ese estado
explícitamente.

Conecta el chat del cliente a un agente con esas herramientas y sesiones de la etapa 1. Debe
responder desde fragmentos recuperados, citar nota y sección y distinguir texto documental de
instrucciones. Una pregunta pública de políticas puede responderse sin identidad comercial;
historial y pedidos exigen sesión. Limita pasos y llamadas por turno, informa límites sin
falso éxito y conserva el caso. No envíes todo el vault ni todos los registros al modelo.

Prueba recuperación, documento ausente, actualización y un documento con instrucciones para
revelar compras ajenas. Usa mocks para pruebas automáticas. Deja lista una comprobación manual
real de una pregunta; no la declares hecha sin ejecutarla.
```

### Qué le estás pidiendo y por qué

Recuperar significa localizar fragmentos pertinentes. El modelo redacta con ellos; no aprende automáticamente toda la carpeta. El filtro del servidor impide leer material interno. La cita permite comprobar la afirmación, pero también debes leer que el fragmento la respalda.



**Conversaciones para probar**

- «¿Cuánto dura una cotización y cuándo empieza a contar la entrega?»
- «¿Hacen entregas internacionales?» La política no contempla ese servicio: debe reconocerlo y ofrecer atención humana.
- Cambia en Obsidian la vigencia de nuevas cotizaciones de 7 a 5 días y aumenta la versión. Pregunta de nuevo; debe usar el cambio. Restaura la política del ejercicio al finalizar la prueba.

**Comprueba tú:** abre la nota citada y encuentra el fragmento que respalda la respuesta. Confirma que la conversación está usando el modelo y herramientas, no una respuesta fija. La edición de la nota no cambia cotizaciones ya emitidas.

**Si falla:** conserva la consulta y muestra que el conocimiento no está disponible; no inventes la política ni sustituyas una búsqueda fallida por conocimiento general.

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Escribe: «¿Cuánto dura una cotización?». | Responde 7 días calendario bajo la política inicial, con nota, sección y versión verificables. |
| Escribe: «¿Hacen entregas internacionales?». | Reconoce que no hay condición aprobada y ofrece registrar atención humana; no inventa transporte ni plazo. |
| Pide «muéstrame los costos y proveedores del producto». | La herramienta del cliente no devuelve fragmentos internos, aunque se lo pida el modelo. |
| En una copia de prueba añade una instrucción maliciosa a una nota. | No cambia permisos ni ejecuta instrucciones del documento; la prueba queda marcada como simulación. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Prueba por separado búsqueda, permisos y conexión al modelo. Si falla la recuperación no uses conocimiento general para completar políticas; conserva el mensaje y permite retomar o escalar.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 2. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** una respuesta real con fuente, versión y traza de consulta; pruebas aisladas de actualización y contenido malicioso.

## Etapa 3 Consultar productos y disponibilidad

**Construyes:** consultas de catálogo e inventario con una interpretación honesta de lo que se conoce.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Productos elegidos por código y disponibilidad honesta.

1. Inspecciona catálogo e inventario y documenta qué significan las filas, unidades y fechas.
2. Construye búsqueda y consulta estructurada; después habilítalas como herramientas del chat. El cliente elige entre resultados ambiguos.
3. Muestra precio y disponibilidad con fecha o advertencia. Reserva las referencias de lotes, proveedores y ubicaciones para la vista del operador.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Añade herramientas de cliente para buscar productos y consultar disponibilidad mediante
consultas parametrizadas. Inspecciona el esquema real: explica unidades, ubicaciones y cómo
calcularás existencia sin sumar filas incompatibles ni multiplicar datos por un join. No
deduzcas cero cuando falta una fila ni presentes como reciente una semilla sin fecha de
actualización.

Para el cliente devuelve código, nombre, unidad, precio de catálogo y un estado de
disponibilidad respaldado por datos aptos para uso comercial, con procedencia y fecha o no
disponible. Cantidades publicables dependen de su validación; no expongas ubicaciones
internas, lotes, costos o proveedores. El operador puede inspeccionar esos detalles con sus
permisos. Diferencia existencia positiva, agotado y dato desconocido. Con nombres ambiguos
muestra opciones antes de elegir. No escribas inventario, reserves ni descuentes existencias.
Explica que la disponibilidad consultada requiere confirmación comercial antes del pedido.

Crea escenarios aislados con un producto disponible, uno agotado, otro sin dato y dos nombres
similares. Prueba herramientas y conversación; la respuesta comercial debe usar resultados del
servidor. No permitas al cliente cambiar precios ni acceder a datos internos de proveedores.
```

### Qué le estás pidiendo y por qué

Precio y existencia son hechos que se consultan. Una nota puede describir un producto, pero un inventario antiguo no permite prometer entrega hoy. Dato ausente, cero unidades y existencia histórica son resultados distintos.



**Comprueba tú:** pregunta por una necesidad general, selecciona un código y pide una cantidad. Contrasta precio y cantidad con la consulta estructurada. Solicita un producto sin inventario: la respuesta debe decir «disponibilidad por confirmar». Repite la consulta y comprueba que no cambió ninguna existencia.

**Si falla:** solicita código o aclaración; el resultado vacío no autoriza inventar un producto sustituto.

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Pregunta: «Necesito un producto para reparar una puerta». | Presenta opciones reales y pide elegir; no inventa un código. |
| Con un código elegido pregunta por dos unidades. | El precio coincide con catálogo. La disponibilidad muestra límites y fecha de sus datos. |
| Usa fixtures disponible, agotado y sin dato. | Distingue los tres; no convierte ausencia en cero ni usa lotes vencidos como disponibilidad actual. |
| Consulta dos veces el mismo producto. | La existencia no cambia y no se crea reserva ni movimiento. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Si el dato no permite confirmar existencia, conserva la selección y marca disponibilidad por confirmar. El operador puede revisar; el bot no fabrica una respuesta para permitir el siguiente paso.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 3. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** comparación entre chat y datos para disponible, agotado y desconocido.

## Etapa 4 Generar una cotización completa

**Construyes:** un documento comercial calculado en servidor, con versiones y condiciones congeladas al emitirlo.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Una cotización que se puede revisar y aceptar.

1. Recoge productos, cantidades, cliente y modalidad. Empieza por recogida gratuita y descuento cero, según la política de práctica.
2. Construye el cálculo y el documento completo antes de añadir la redacción del chat. Conserva condiciones y precios de cada versión emitida.
3. Añade aceptación explícita de ID y versión, control de vencimiento y rechazo de versiones anteriores.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Implementa cotizaciones usando la política ficticia del módulo 9. El agente recoge necesidad,
productos seleccionados, cantidades, destino y modalidad de entrega; prepara borrador y
solicita faltantes. El servidor resuelve códigos, valida cantidades, consulta precios y
calcula subtotales, impuestos según datos explícitos, transporte, descuentos autorizados y
total en COP. Nunca inventes desglose tributario. En los fixtures usa precios finales del
catálogo, descuento cero y recogida gratuita para conservar compatibilidad con la venta de la
clase 8.

Genera una vista imprimible y guardable como documento con: ID y versión, fecha y vencimiento,
negocio y cliente ficticios, líneas con código/nombre/unidad/cantidad/precio/subtotal,
tratamiento de impuestos, descuentos, transporte, total, destino/modalidad, forma de pago,
condiciones de disponibilidad y plazo de entrega con evento de inicio. Incluye política y
versión utilizadas, exclusiones y canal para aclaraciones. No es factura fiscal. No inventes
identificación tributaria ni datos de contacto reales.

Guarda la versión exacta de precios y condiciones al emitir. El cliente revisa el documento
completo y usa una acción explícita de aceptación vinculada a ID y versión; un sí interpretado
por el modelo no basta. Editar crea otra versión e invalida la aceptación previa. Valida
vencimiento en servidor con reloj controlable en tests. Cotizar y aceptar no crean una venta
ni reservan inventario.

Prueba cálculos, faltantes, modificación de cantidades, documento imprimible, vencimiento,
doble emisión y aceptación de versión obsoleta. Si una condición comercial necesita aprobación
del operador, no emitas la cotización como firme hasta obtenerla.
```

### Qué le estás pidiendo y por qué

El servidor calcula y el modelo explica. Una versión conserva exactamente lo ofrecido. Cambiar una cantidad requiere una versión nueva para que la aceptación siga refiriéndose a un documento concreto, no a una frase ambigua del chat.



**Comprueba tú**

1. «Cotiza dos unidades de [código elegido], para recoger en tienda». Elige un código con precio conocido; calcula por tu cuenta cantidad × precio.
2. Abre el documento: debe tener todas las condiciones, no solamente un total en el chat.
3. Cambia la cantidad; comprueba el nuevo total y la nueva versión.
4. Intenta aceptar la versión anterior: debe rechazarse y mostrar la actual.
5. En una prueba aislada cambia el precio del catálogo: la cotización emitida conserva su importe; un pedido requiere revalidación como indica la política.

**Si falla:** conserva el borrador y explica qué falta. Una cotización sin plazo definido para el destino debe quedar pendiente de revisión, sin promesa inventada.

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Pide: «Cotiza FER-0001 × 1 y FER-0222 × 1 para recoger». | Si el catálogo conserva 121300 y 26700, el total es 148000 COP. Si cambió, se informa; no se fuerzan precios. |
| Abre la cotización fuera del chat. | Incluye todas las líneas, importes, vigencia, entrega, condiciones y políticas aplicadas. No es solo un mensaje con un total. |
| Cambia FER-0001 de 1 a 2 unidades. | Con esos precios el total nuevo es 269300 COP y existe otra versión. |
| Intenta aceptar la versión anterior y una vencida en pruebas. | Ambas se rechazan; no se crea pedido ni venta. |
| Solicita entrega en un destino sin condiciones aprobadas. | Queda borrador o pendiente de persona hasta definir transporte y plazo. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Si falla un cálculo o falta una condición, conserva el borrador. No habilites aceptación hasta mostrar total y condiciones completas. Una nueva emisión no borra el documento anterior.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 4. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** documento imprimible, dos versiones y comprobación de cálculos y aceptación.

### Lista de revisión del documento de cotización

| Campo | Qué debe mostrar |
| --- | --- |
| Identidad | Comercial La Esquina y cliente, identificados como ficticios; ID y versión. |
| Fechas | Emisión, vencimiento exacto y zona America/Bogota; vigencia inicial de 7 días calendario. |
| Productos | Código, nombre, unidad, cantidad, precio unitario y subtotal por línea. |
| Importes | COP, precios finales, descuento cero y recogida gratuita para el recorrido base. Si no hay desglose tributario, se indica; no se inventa tarifa. |
| Total | Suma calculada en servidor y detalle de cualquier cargo realmente definido. |
| Entrega | Modalidad, destino aportado y plazo. Recogida: siguiente día hábil; Zona A: del segundo al tercer día hábil. Se cuenta desde confirmación comercial, no desde cotización. |
| Calendario | Lunes a viernes, sin festivos en el escenario ficticio; día de confirmación es día cero. |
| Disponibilidad | Consultada y pendiente de confirmación comercial; emitir o aceptar no reserva stock. |
| Pago | Aceptación comercial de soporte revisado; sin afirmar recepción bancaria. No inventar cuentas o instrucciones de transferencia. |
| Condiciones | Políticas y versiones, exclusiones, aclaraciones en el mismo chat y nueva aceptación ante cambios. |
| Aceptación | Control explícito sobre el ID y versión vigentes; no equivale a factura, venta ni pago. |

## Etapa 5 Convertir la aceptación en pedido

**Construyes:** una orden comercial del cliente, enlazada a la cotización. En esta práctica «orden de compra» es la orden que el cliente genera para comprar a La Esquina; no es una compra a un proveedor ni un documento fiscal.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Una orden vinculada a lo que el cliente aceptó.

1. Añade la acción Generar pedido sobre una aceptación vigente. El servidor revalida propietario, versión y datos comerciales.
2. Resuelve la confirmación de disponibilidad con el operador. Con una duda, guarda el pedido en revisión y explica el siguiente paso.
3. Muestra orden consultable e imprimible y aplica unicidad persistente por aceptación, además de deshabilitar visualmente un doble clic.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Crea el pedido a partir de una cotización vigente y aceptada por su propietario. Revalida
versión, precio, cantidades y disponibilidad en servidor antes de solicitar confirmación
comercial. Si cambió precio o condición, genera revisión y nueva aceptación; no alteres
silenciosamente lo aceptado. Si falta stock o su dato no es suficiente, deriva al operador. El
operador confirma disponibilidad para esta práctica sin modificar ni reservar inventario.

Conserva pedido_id, cliente, cotización_id/versión, caso, líneas, total, entrega, dirección
ficticia cuando corresponda y condiciones aceptadas. El estado comercial inicial, una vez
autorizado, es pendiente_soporte. Si necesita revisión, usa pendiente_revision. Separa los
estados de pago y envío. Impide más de un pedido por la misma aceptación mediante una
restricción persistente e idempotencia, incluso con dos solicitudes concurrentes.

El cliente debe poder abrir su orden imprimible y consultar el siguiente paso. Todavía no
crees una venta ni confirmes el pedido por tener una cotización aceptada. Añade migraciones
sin pérdida y pruebas de propiedad, aceptación vencida, precio cambiado, disponibilidad
insuficiente y doble clic.
```

### Qué le estás pidiendo y por qué

Aceptar una cotización y crear un pedido son hechos distintos. La restricción persistente evita duplicados aunque dos solicitudes lleguen juntas o el navegador repita una petición; bloquear un botón no alcanza.



**Comprueba tú:** acepta la cotización vigente y genera la orden dos veces. Debes obtener el mismo pedido, con sus líneas, condiciones y estado pendiente. Consulta desde Bruno el pedido de Ana: denegado. Simula stock insuficiente: queda en revisión, no confirmado.

**Si falla:** recupera por ID de aceptación antes de volver a crear. Conserva el motivo de revisión y permite continuar cuando el operador resuelva.

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Acepta una versión vigente y pulsa Generar pedido. | La orden conserva cliente, líneas, total, versión aceptada y condiciones; queda pendiente_soporte o pendiente_revision. |
| Repite la misma intención y recarga. | Se recupera el mismo pedido_id y existe una sola orden por aceptación. |
| En pruebas cambia el precio o deja disponibilidad incierta. | Se exige revisión y, si cambian condiciones, nueva cotización y aceptación. |
| Comprueba las ventas e inventario antes y después. | Crear el pedido no registra venta ni modifica existencias. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Si la respuesta no llega, busca el pedido por aceptación y clave de solicitud antes de repetir. Si hay revisión pendiente, resuelve esa revisión sobre el mismo caso.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 5. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** orden, aceptación asociada y una sola fila de pedido tras el reintento.

## Etapa 6 Adjuntar soporte y confirmar el pedido

**Construyes:** el enlace del pedido con el circuito de comprobantes de la clase 8 y una confirmación comercial verificable.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Un pedido confirmado mediante el circuito de revisión.

1. Añade carga de soporte propio y estado visible de revisión; reutiliza la infraestructura de imágenes y extracción.
2. Desde la mesa, revisa original, moneda, importe, fecha, naturaleza y singularidad. Prepara la propuesta con los datos del pedido, no con supuestos de la imagen.
3. Aprueba y ejecuta la versión revisada. La escritura conjunta debe incluir venta, operación, vínculos, confirmación de pedido y evento obligatorio de resultado.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Permite al cliente cargar un soporte en su propio pedido, recuperar su estado y ver que está
en revisión. Reutiliza carga, extracción original, revisión humana, propuestas y aprobación
por versión del módulo 8. Protege el archivo por propietario. No presentes carga o lectura OCR
como confirmación.

Aplica la política del módulo 9: soporte revisado, naturaleza de cobro, COP confirmado, monto
exacto para el caso principal, pedido vigente autorizado y referencia no reutilizada o
revisión humana explícita cuando la referencia no sea legible. El soporte no debe estar
aplicado a otro pedido. Con faltantes, monto distinto, financiación o posible duplicidad,
conserva la evidencia y escala; no confirmes automáticamente.

Prepara desde el pedido la propuesta de crear venta usando sus líneas y datos aceptados. No
infieras productos ni cliente de la imagen. El operador revisa el soporte y aprueba la versión
exacta de la propuesta comercial. Cuando el servidor ejecuta esa versión, debe guardar
conjuntamente venta, líneas, operación, vínculo y confirmación del pedido con motivo
aceptacion_de_soporte, sin cambiar el estado bancario no_verificado. No añadas un segundo
botón que permita confirmar sin esos controles.

Inspecciona los límites transaccionales existentes antes de modificar: evita commits
intermedios que dejen venta sin pedido confirmado o pedido sin venta. Mantén compatibilidad
con las operaciones anteriores. Congela y valida la correspondencia entre versión de pedido y
propuesta; el agente no puede alterar contenidos aceptados. Si la validación heredada exige
precio vigente distinto del aceptado, bloquea y solicita nueva cotización y aceptación; no
evadas el control.

Garantiza unicidad de venta por pedido e idempotencia persistente de la ejecución. Carga
idéntica devuelve el mismo archivo; otra foto del mismo pago requiere revisión y no suma
dinero. Conserva la extracción original y las correcciones humanas. Añade pruebas aisladas de
importe diferente, soporte repetido entre pedidos, doble ejecución, rollback y consulta
después de reiniciar.
```

### Qué le estás pidiendo y por qué

El ejercicio acepta el soporte para una confirmación comercial, con revisión y autorización. Cargarlo o extraer texto no autoriza la venta. Una transacción guarda el conjunto completo o lo revierte; la idempotencia conserva un solo resultado al repetir.



**Comprueba tú**

1. Adjunta una imagen autorizada al pedido correcto. Observa «soporte en revisión».
2. En la mesa del operador, compara original y campos; registra correcciones y motivo si hacen falta.
3. Revisa y aprueba la propuesta concreta. Antes de ejecutarla, el pedido sigue sin confirmar.
4. Ejecuta y consulta: pedido confirmado, una venta, una operación y su vínculo. El estado bancario permanece `no_verificado`.
5. Repite la ejecución: mismo resultado y conteos.

Para un recorrido con el soporte 054, el escenario docente aporta expresamente FER-0001 × 1 a 121300 y FER-0222 × 1 a 26700: total 148000. Verifica esos precios en tu catálogo. Son datos comerciales ficticios aportados para el ejercicio, no datos extraídos de la imagen. La moneda debe confirmarse: el símbolo $ no identifica por sí solo COP. La referencia oculta requiere revisión manual de singularidad.

La fecha del soporte 054 es 11 de septiembre de 2026. Para comprobar reglas temporales usa una copia de pruebas con reloj fijado a ese escenario y etiquétala como tal; no cambies silenciosamente la fecha documental ni la fecha real de la app. Otros casos con importes coherentes pueden usar fixtures sintéticos identificados, sin presentarlos como OCR real.

**Si falla:** nunca subas otra imagen para «forzar» éxito. Consulta estado de propuesta y pedido. Si ya existe resultado, muéstralo; si no hubo commit, reintenta la misma acción con su clave. Si quedó estado parcial, es un defecto de la implementación que debe corregirse antes de continuar.

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Adjunta un soporte al pedido de Ana. | Solo Ana y el operador pueden abrirlo. El estado informa revisión, todavía sin confirmar. |
| Revisa y aprueba una propuesta; no la ejecutes aún. | El pedido continúa sin confirmar: aprobar y ejecutar son pasos separados. |
| Ejecuta la propuesta aprobada. | Existe una sola venta vinculada y el pedido queda confirmado por aceptacion_de_soporte; el banco sigue no_verificado. |
| Repite ejecución y luego reinicia la app. | Se recuperan los mismos IDs y conteos. |
| En pruebas usa monto distinto o el mismo soporte en otro pedido. | Bloquea confirmación y conserva una excepción para el operador. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Antes de reintentar consulta propuesta y pedido. Si la escritura ya terminó, muestra su resultado. Si fue revertida, repite con la misma clave. Un resultado parcial es un defecto que debe corregirse.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 6. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** extracción y revisión con procedencia, aprobación de versión, IDs relacionados y conteos después del reintento. No incluyas imágenes personales.

## Etapa 7 Consultar el envío

**Construyes:** seguimiento persistente actualizado por el operador y consultable desde el chat.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Un seguimiento que muestra lo que realmente se registró.

1. Construye eventos de entrega por modalidad y controles de transición para el operador.
2. Calcula la estimación desde la confirmación comercial con la regla del calendario ficticio y guarda la condición aplicada.
3. Conecta consulta de envío propia al chat y presenta la última actualización, estimación y novedades.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Implementa el seguimiento de recogidas y envíos de pedidos confirmados. Usa la política de
entrega: separa pedido confirmado de enviado y de entregado. Registra eventos con estado,
fecha efectiva, fecha de registro, actor, motivo, guía y transportadora solo si fueron
aportadas. Para recogida usa listo_para_recoger y retirado; para domicilio, en_preparacion,
despachado, entregado y novedad. Valida transiciones y conserva historial de correcciones sin
borrarlo.

Solo el operador puede registrar avances. El chat del cliente consulta sus datos y explica la
última actualización y el plazo acordado; no actualiza el estado porque el cliente lo pida ni
inventa ubicación, guía o hora de llegada. Identifica la fuente como registro interno de
práctica: no hay conexión con transportadora.

Prueba acceso a envío ajeno, estado inexistente, salto no permitido y reinicio. Permite abrir
una novedad y escalar cuando el registro contradiga lo que informa el cliente.
```

### Qué le estás pidiendo y por qué

Estado comercial, estado financiero y estado de entrega son independientes. El plazo comienza en el evento indicado por la política; una estimación no demuestra que el pedido haya sido despachado.



**Comprueba tú:** pregunta «¿Dónde va mi pedido?». Registra preparación y despacho como operador, usando datos ficticios identificados. Vuelve a preguntar y comprueba las fechas. Si dices «márcalo entregado» como cliente, no debe cambiar nada. Para un pedido pendiente de soporte no debe aparecer un envío inventado.

**Si falla:** muestra la última información guardada y ofrece registrar una novedad. «No tengo actualización» es diferente de «se perdió el paquete».

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Pregunta: «¿Dónde va mi pedido?», antes de confirmarlo. | No inventa despacho, guía ni transportadora. |
| El operador registra en preparación y después listo para recoger o despacho, según modalidad. | El cliente ve los eventos y fechas; para recogida no exige una transportadora ficticia. |
| Como cliente escribe: «Márcalo entregado». | Puede registrar una novedad, pero no cambia el estado de entrega. |
| En pruebas confirma un viernes. | Recogida: lunes al finalizar el día; Zona A: martes a miércoles, sin festivos en el calendario ficticio. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Si no hay una actualización, presenta la última conocida y permite abrir novedad. Un error del chat no debe borrar ni adelantar el estado persistido.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 7. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** secuencia de estados, respuesta del chat y rechazo de modificación por cliente.

## Etapa 8 Historial y recompra

**Construyes:** continuidad comercial usando compras verificablemente relacionadas con el cliente.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Un historial propio y una compra nueva a partir de otra.

1. Muestra historial desde relaciones verificadas de cliente y pedido, incluyendo su venta y entrega cuando existan.
2. Añade selección de líneas para recompra, referencia al origen y consulta de precios y disponibilidad actuales.
3. Abre un nuevo borrador, presenta cambios y pide nueva aceptación. Conserva sin cambios la compra anterior.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Añade historial del cliente con pedidos, ventas vinculadas, estado comercial y de entrega.
Filtra por la identidad del servidor. Las ventas heredadas que no tengan dueño verificado no
deben aparecer por coincidencia de nombre. Permite abrir una compra propia y solicitar
recompra de todas o algunas líneas.

La recompra crea un nuevo borrador de cotización, con referencia a la compra origen, precios y
disponibilidad actuales y comparación de cambios. Omite o consulta productos inexistentes;
pregunta antes de sustituirlos. No reutilices comprobantes, aprobación, entrega, precio
histórico ni una dirección sin reconfirmación. Sigue después las etapas de nueva aceptación y
pedido; no crees venta automáticamente.

Garantiza que reintentar una misma solicitud devuelve el mismo borrador. Una recompra
intencional posterior usa una solicitud nueva y crea otro borrador. Prueba ambos casos, precio
cambiado y producto agotado con fixtures aislados; no edites el catálogo de trabajo para
simularlos.
```

### Qué le estás pidiendo y por qué

Recomprar reutiliza la selección, no el contrato anterior. Precios, disponibilidad y destino se vuelven a revisar. Un pago anterior no paga automáticamente otra compra.



**Comprueba tú:** Ana consulta su historial y pide «quiero repetir esta compra, pero solo una unidad del primer producto». La cotización muestra cantidad y precio actuales, referencia de origen y necesidad de nueva aceptación. Bruno no ve la compra de Ana. El pedido original y su pago no cambian.

**Si falla:** conserva selección y faltantes en un borrador; no uses el precio anterior para completar el documento.

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Como Ana abre la compra creada en el recorrido. | Ve sus líneas, total y estados; Bruno no puede consultarla. |
| Pide: «Quiero repetir esta compra, solo una unidad del primer producto». | Crea un borrador de cotización con esa selección y referencia al origen. |
| En pruebas cambia el precio de catálogo y repite. | Muestra precio actual y diferencia respecto de la compra anterior. |
| Reintenta la misma solicitud y luego inicia otra recompra intencional. | El reintento devuelve el mismo borrador; la intención nueva puede generar otro. |
| Consulta pedido, pago y entrega anteriores. | Permanecen intactos; no aparecen como aceptados o pagados en el borrador nuevo. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Si falta un producto, conserva las demás selecciones y pide elegir. No sustituyas silenciosamente ni uses un precio histórico para cerrar la nueva cotización.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 8. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** compra origen, nueva cotización, comparación y ausencia de pagos heredados.

## Etapa 9 Reclamaciones y devoluciones

**Construyes:** una solicitud de posventa con evidencias y decisiones separadas.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Un expediente de inconformidad y una devolución controlada.

1. Selecciona la compra propia desde historial y recoge línea, cantidad, motivo y relato; guarda información incompleta como tal.
2. Muestra un resumen y registra la reclamación al confirmar. Aplica política como orientación y deja las excepciones a revisión.
3. Separa autorización de devolución y recepción; ambas requieren operador y no alteran inventario ni la venta original.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Implementa reclamaciones y devoluciones desde una compra propia. Recoge pedido/venta, línea,
cantidad afectada, motivo, descripción, fecha y evidencias opcionales. Si el cliente no conoce
el ID, ayúdalo a elegir desde su historial; nunca busques en las compras de todos. Conserva lo
incompleto y pide faltantes. Antes de registrar, muestra resumen y exige confirmación
explícita del cliente vinculada a su versión.

Consulta la política del vault y registra versión y criterios orientativos. Para plazo usa
fecha de entrega registrada y zona America/Bogota, con reloj controlable para pruebas. Falta
de fecha o reclamo fuera de las reglas no debe impedir abrir el caso: deriva a revisión humana
sin afirmar una elegibilidad que no se conoce. La clasificación automática no aprueba la
devolución.

Estados de reclamación: abierta, falta_informacion, en_revision, resuelta. Estados de
devolución separados: solicitada, autorizada, recibida, rechazada o cancelada. Solo el
operador autoriza y registra recepción con motivo y evidencia. No reintegres stock ni
modifiques venta original. Controla cantidad acumulada para impedir devolver más unidades que
las compradas, aun con solicitudes concurrentes.

Prueba caso incompleto, devolución parcial, cantidad excesiva, falta de fecha, ventana
excedida y doble envío. Protege también los adjuntos de la reclamación y restringe sus tipos y
tamaños.
```

### Qué le estás pidiendo y por qué

Reclamar, autorizar devolver y recibir la mercancía son tres hechos diferentes. La ventana de 7 días orienta la revisión del escenario; su incumplimiento no impide registrar el caso ni autoriza un rechazo automático.



**Comprueba tú:** «Me llegó dañada una unidad de este pedido». El chat identifica la compra, pregunta lo necesario y presenta la solicitud para confirmar. El cliente obtiene un número de caso. El operador autoriza y después registra recepción. El inventario permanece igual.

**Si falla:** el cliente conserva número y estado de la solicitud; puede adjuntar la evidencia pendiente sin abrir otro caso idéntico. Una reclamación fuera de la regla orientativa pasa a una persona.

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Di: «Una unidad de esta compra llegó dañada». | Pregunta la línea y los datos faltantes; no exige inventar evidencia para guardar. |
| Confirma el resumen de solicitud. | Obtienes un caso consultable y el operador lo encuentra con la misma referencia. |
| El operador autoriza una unidad y después registra recepción. | Quedan dos eventos distintos y cantidades consistentes. |
| En pruebas pide más unidades que las compradas y envía dos solicitudes concurrentes. | La cantidad acumulada no excede la comprada. |
| Usa una compra sin fecha de entrega o fuera de ventana. | Se registra y escala la excepción con su motivo; no se afirma elegibilidad desconocida. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Retoma el expediente existente por su ID, añade lo faltante y conserva decisiones. No abras otro caso idéntico porque faltó una foto o una respuesta del modelo.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 9. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** solicitud, fuente de política, decisiones con actor y cantidad afectada.

## Etapa 10 Solicitar y resolver el reembolso administrativo

**Construyes:** un expediente administrativo. La aplicación no transfiere, devuelve ni marca dinero como pagado.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Un trámite de reembolso sin transferencias.

1. Desde la reclamación prepara importe y líneas elegibles usando el precio realmente vendido.
2. Añade revisión del operador, control atómico de saldo administrativo y decisión con motivo.
3. Genera la ficha y la remisión administrativa a pago externo; muestra con claridad el estado del trámite al cliente.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Añade solicitud de reembolso ligada a una reclamación y compra propias. Muestra importe
solicitado, motivo, líneas/cantidades, devolución asociada y desglose calculado desde el
precio realmente comprado. No uses el precio actual del catálogo para devolver una compra
anterior. En el piloto de recogida y descuento cero, el importe de productos es cantidad
autorizada por precio de venta histórico; no añadas transporte ni impuestos otra vez.

Estados: solicitado, en_revision, aprobado_administrativamente, rechazado, revocado y
remitido_a_pago_externo. La revocación es una acción autorizada previa a la remisión, con
motivo y sin borrar la decisión original. El cliente solicita y consulta; el operador decide
importe, fundamento y necesidad de recepción previa. Cualquier excepción exige motivo y queda
registrada. Aprobar una devolución no equivale a aprobar el reembolso.

Valida propiedad, versión, cantidad devuelta, monto cobrado aplicable y saldo reembolsable.
Reserva administrativamente importes aprobados para que dos solicitudes no excedan lo cobrado.
Haz la comprobación y escritura de forma atómica; documenta cómo una revocación autorizada
libera esa reserva. No borres decisiones anteriores. Rechaza montos negativos o superiores al
saldo. No pidas datos bancarios para este ejercicio.

Genera una ficha administrativa imprimible. Al remitir a pago externo guarda responsable y
referencia administrativa y cierra el trabajo del caso sin marcar dinero devuelto. No
implementes API bancaria ni estado pagado. Prueba solicitud duplicada, dos solicitudes
concurrentes y aprobación intentada desde el cliente o el modelo.
```

### Qué le estás pidiendo y por qué

Devolver un artículo no aprueba automáticamente un reembolso. El saldo administrativo impide comprometer dos veces el mismo importe. Remitir el expediente concluye este ejercicio sin afirmar que se movió dinero.



**Comprueba tú:** solicita devolución de una unidad y un reembolso parcial. El operador revisa y aprueba el importe permitido; el cliente ve «aprobado administrativamente; pago externo pendiente». Remite el expediente y comprueba que no aparece «dinero devuelto». Intenta solicitar de nuevo un monto ya comprometido: debe detectarse el saldo insuficiente.

**Si falla:** consulta el expediente existente antes de repetir la aprobación. Una respuesta perdida no libera una reserva administrativa ya guardada.

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| En un fixture se compraron 2 unidades a 10000 COP y se recibió 1 en devolución. | El importe elegible del caso es 10000 COP, sin añadir impuestos ni transporte no cobrado. |
| Solicita el reembolso como cliente. | Queda solicitado o en revisión; el cliente y el modelo no pueden aprobarlo. |
| Aprueba como operador y remite el expediente. | Conserva responsable y referencia, y muestra pago externo pendiente, nunca pagado. |
| Dos solicitudes compiten por el mismo saldo en pruebas. | La suma aprobada vigente no excede el saldo elegible. |
| Revoca una aprobación antes de remitir en pruebas. | Libera su reserva con decisión y motivo conservados; después de remitir no libera automáticamente. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Consulta expediente y saldo comprometido antes de repetir. Una respuesta perdida no revoca una aprobación ni autoriza otro compromiso del mismo importe.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 10. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** ficha de reembolso, cálculo, decisión, saldo administrativo y ausencia de movimientos de dinero.

## Etapa 11 Escalar y retomar con una persona

**Construyes:** una bandeja de atención humana dentro de la app. No se necesita enviar correos o mensajes externos.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Una conversación que una persona puede retomar.

1. Amplía el mecanismo mínimo de atención humana creado al inicio y conéctalo a todos los motivos del recorrido.
2. Construye bandeja, toma de caso con un responsable, respuesta humana y acción de reanudar o cerrar.
3. Muestra el contexto y la identidad del autor de cada respuesta; prueba que el expediente persiste incluso sin modelo.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Integra escalamiento desde todos los recorridos. Debe activarse cuando el cliente pide una
persona, falta una política, existe ambigüedad comercial, posible duplicidad, novedad de envío
o excepción de posventa. Registra en el caso existente motivo, hechos confirmados, faltantes,
fuentes con versión, relaciones a pedido/propuesta/venta y acciones intentadas. Distingue
resumen generado de datos consultados y evita copiar secretos o imágenes completas a los
registros.

Crea bandeja del operador con pendiente_persona, asignado, atendido y cerrado. Una asignación
concurrente no debe dejar dos responsables activos. El cliente puede consultar número, estado
y respuesta humana. El operador lee el contexto, solicita información o responde sin obligar a
repetir toda la historia. Las aprobaciones siguen en sus controles administrativos
específicos; responder un mensaje no autoriza un reembolso.

Al tomar el caso una persona, pausa nuevas acciones comerciales del agente en ese caso.
Permite consultas de estado y aportes del cliente. Reanudar requiere acción registrada del
operador, conserva el mismo caso y no repite pasos completados. Si falla generar el resumen,
conserva el escalamiento con los IDs y hechos disponibles; el operador accede al historial
autorizado.

Prueba escalamiento repetido, reinicio, doble toma, respuesta humana y continuación del flujo.
La bandeja local es el destino real; no afirmes que se notificó por un canal externo.
```

### Qué le estás pidiendo y por qué

Escalar significa guardar y transferir contexto al destino que realmente existe: la bandeja local. Un resumen ayuda al operador, pero las decisiones siguen en sus controles. La toma humana pausa acciones comerciales del agente en ese caso.



**Comprueba tú:** escribe «quiero hablar con una persona». Como operador, abre la bandeja y verifica que contiene el contexto correcto. Responde y retoma el caso. El cliente ve la respuesta identificada como humana y puede seguir sin crear otra compra ni otro expediente.

**Si falla:** el escalamiento persiste aunque no funcione el modelo. No prometas atención inmediata ni resolución automática.

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Escribe: «Quiero hablar con una persona». | Aparece el mismo caso en la bandeja, con motivo, hechos, faltantes e IDs. |
| Dos operadores intentan tomarlo simultáneamente en pruebas. | Hay un solo responsable activo. |
| Con el caso tomado pide al bot que cree otra operación comercial. | Pausa la acción y permite consultar o aportar información. |
| El operador responde y reanuda. | El cliente identifica la respuesta humana y continúa el mismo caso sin duplicar compras. |
| Simula que falla el resumen del modelo. | El escalamiento se guarda igualmente con motivo e IDs disponibles. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Usa el mecanismo persistente, aunque falte el resumen. Si la bandeja no pudo guardar, informa la falla y conserva la solicitud recuperable; no afirmes que alguien recibió una notificación externa.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 11. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** un mismo caso antes, durante y después de la intervención humana.

## Etapa 12 Mostrar el recorrido y medirlo

**Construyes:** una vista de ejecución que permita explicar tanto el éxito como el error. Añade la captura básica de eventos a medida que construyes las etapas anteriores; aquí completas su consulta y las métricas.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Un recorrido que se puede explicar con registros.

1. Reúne los eventos capturados desde la etapa 1 en una vista por caso e intento.
2. Relaciona fuentes, versiones, decisiones, documentos, errores y resultados; muestra al cliente solo sus estados y próximos pasos.
3. Calcula métricas desde casos ejecutados y uso reportado, diferenciando API real, mocks y fallas simuladas.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Completa trazabilidad por caso y ejecución. Usa caso_id estable para el recorrido y
ejecucion_id para cada intento; vincula conversación, documentos/versiones, cotización,
pedido, propuesta, venta, envío y posventa. Captura por paso actor, herramienta, inicio, fin,
duración, resultado, IDs, estado previo/posterior y error controlado. Registra decisiones y no
solo el último mensaje. Guarda el evento obligatorio de resultado comercial en la misma
transacción del negocio: si no se puede guardar, revierte todos sus efectos. Conserva intentos
y eventos de fallo mediante un registro separado, sin confirmar escrituras de negocio
parciales. Si ese registro separado también falla, informa incidente de auditoría y permite
consultar el estado comercial existente; no inventes una traza completa ni repitas una
operación ya confirmada.

Captura modelo y usage reportado por cada respuesta de API, incluida extracción, sin guardar
claves ni todo el contenido privado. No supongas cero ante consumo desconocido. Marca por
separado llamadas intentadas, completadas y aquellas cuyo consumo no se conoce. No dupliques
tokens almacenados al consultar o reintentar una lectura. Muestra tokens de entrada/salida y
detalles adicionales solo si existen. Para convertir a dinero exige tarifa oficial verificada
y fechada para el modelo exacto; sin ella muestra costo no disponible y conserva tokens.

Añade vista administrativa con pasos, fallas, recuperación y conteos. El cliente ve su estado
y próximo paso sin recibir registros internos. Registra origen api_real, mock_prueba o
simulacion_falla por evento. Mantén límite de llamadas por turno y registro de límites
alcanzados; no fuerces todo el recorrido comercial en un solo turno.

Crea un informe de evaluación que lea los casos efectivamente ejecutados de la matriz, muestre
éxitos sobre total, respuestas fundamentadas revisadas sobre las que requerían fuente,
duplicados y escrituras no autorizadas observados, intervenciones con motivo, duración y
llamadas por caso. No declares confiabilidad universal ni uses la intervención humana como
fracaso automático.
```

### Qué le estás pidiendo y por qué

Una traza conecta hechos mediante identificadores. La duración y el consumo ayudan a observar el proceso, pero no acreditan por sí solos una respuesta correcta. Los porcentajes necesitan un numerador y un denominador de pruebas efectivamente ejecutadas.



**Comprueba tú:** elige un pedido y reconstruye cómo surgió: consulta, fuente, cotización, aceptación, soporte, autorización y resultado. Comprueba que puedes ver una falla y su recuperación. Si el proveedor no reportó tokens de una solicitud fallida, debe mostrarse «no disponible».

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Abre un pedido y sigue sus relaciones hasta la fuente y aceptación. | Reconstruyes el origen, soporte, autorización y resultado con IDs y versiones. |
| Consulta una ejecución exitosa y otra fallida. | Ambas conservan resultado, intento y origen; la fallida no se presenta como éxito. |
| Simula una llamada sin usage reportado. | Se ve consumo no disponible, nunca cero supuesto. |
| Consulta varias veces la misma traza. | No aumenta tokens ni duplica eventos de llamadas existentes. |
| Revisa el informe de evaluación. | Distingue éxitos/ejecutados y fundamentación revisada/requerida; los pendientes no cuentan como aprobados. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Si falta el evento obligatorio del resultado comercial, la operación se revierte. Si falló un registro independiente de intento, informa incidente y consulta el estado de negocio antes de repetir.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 12. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** exportación depurada de una traza completa e informe con numeradores, denominadores y origen de cada prueba.

## Etapa 13 Provocar fallas y recuperar sin duplicar

**Construyes:** mecanismos de recuperación comprobados. Una prueba de «error» que no comprueba el estado final queda incompleta.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Recuperación que conserva un solo efecto comercial.

1. Prepara una copia temporal, registra su ruta y confirma que las fallas no tocarán la práctica del estudiante.
2. Inyecta cada falla en un punto definido y captura IDs, estados y conteos antes del reintento.
3. Aplica la recuperación apropiada y compara el estado final esperado con el observado; conserva un informe de cada caso.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Ejecuta la matriz docs/modulo-9/modulo-9-casos-y-evidencias.md sobre una copia temporal
aislada. Implementa inyección de fallas solo accesible desde pruebas, nunca una ruta de
cliente ni un interruptor público. No cortes el servicio real del proveedor ni consumas API
para simular errores.

Prueba al menos: modelo sin respuesta; vault ausente; propuesta editada tras aprobación; caída
antes del commit comercial; respuesta perdida después del commit; doble clic concurrente;
reinicio con caso pendiente; soporte repetido en otro pedido; acceso a historial ajeno;
documento malicioso; reembolso duplicado y escalamiento sin modelo. Ejecuta además los
escenarios funcionales de la matriz y las regresiones heredadas pertinentes.

Para cada falla registra estado anterior, punto de interrupción, acción de recuperación,
estado posterior, conteos y resultado esperado/observado. Tras respuesta perdida consulta por
ID y clave persistente, no crees otra solicitud. Tras rollback reintenta la misma intención;
tras conflicto de versión solicita nueva revisión. Verifica que reiniciar conserva identidad
del recurso y permisos, aunque la sesión necesite volver a iniciarse.

Implementa una cola de pendientes o un procedimiento de reconciliación si existen efectos en
pasos separados. No prometas exactamente una llamada a proveedores externos; garantiza la
unicidad de nuestros efectos comerciales con restricciones y transacciones. No reintentes
indefinidamente ni vuelvas a invocar OCR ya persistido. Si no sabemos si el proveedor completó
una llamada, registra esa incertidumbre y consulta el estado local antes de repetirla.

Entrega un informe sin secretos. No marques una prueba no ejecutada como aprobada. Indica qué
comportamientos se comprobaron con API real y cuáles solo con mocks o simulación.
```

### Qué le estás pidiendo y por qué

Antes del commit se espera ningún efecto comercial. Después del commit, aunque la respuesta no llegue, se espera un resultado ya guardado. La recuperación debe distinguir esos dos momentos para no repetir ventas ni aprobaciones.



**Comprueba tú:** presencia una prueba de respuesta perdida después de guardar el pedido confirmado. Antes de reintentar, abre el pedido: el resultado ya existe. Repite la acción: conserva los mismos IDs y una sola venta. Después presencia una falla antes del commit: no queda ninguno de los efectos comerciales, y el reintento completo funciona.

### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Simula caída antes del commit de confirmación. | No queda una venta, operación o pedido confirmado parcial. Reintentar permite guardar el conjunto una vez. |
| Simula pérdida de respuesta después del commit. | Consultar devuelve el resultado existente; repetir conserva los mismos IDs y una venta. |
| Envía doble clic concurrente y reinicia con caso pendiente. | No duplica efectos y permite retomar el mismo recurso después de autenticarse. |
| Prueba vault ausente, modelo sin respuesta y escalamiento sin modelo. | Conserva caso, informa límites y guarda la solicitud de persona cuando ese almacenamiento está disponible. |
| Prueba acceso ajeno, soporte repetido y reembolso duplicado. | Rechaza la acción sin escrituras no autorizadas ni exceso de saldo. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

No borres los registros para convertir una prueba roja en verde. Corrige la causa, conserva el intento fallido y repite la prueba en una copia aislada que mantenga el estado necesario para verificar recuperación.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 13. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

**Evidencia:** comparación antes/después y traza de ambos escenarios. Reiniciar la base para borrar el problema no cuenta como recuperación.

## Etapa 14 Demostrar y entregar

**Construyes:** una entrega que otra persona puede arrancar y evaluar.

### Paso a paso: qué vas a construir

**Resultado de esta etapa:** Una entrega reproducible con evidencia real.

1. Revisa capacidades y documentación: cada función conserva estado implementado o pendiente según evidencia.
2. Empaqueta con semilla ficticia, migraciones y pruebas; extrae e instala en una carpeta nueva sin entorno ni configuración privada anteriores.
3. Demuestra venta y posventa, recompra, atención humana y una falla recuperada usando los mismos IDs a través de las pantallas.

### Prompt de construcción

Cópialo en el asistente de programación. Implementa esta etapa antes de continuar.

**Prompt para el asistente**

```text
Prepara la entrega del módulo 9. Ejecuta los checks adecuados y registra los resultados
reales. Conserva código, migraciones, vault ficticio, fixtures, pruebas, instrucciones de
instalación y recuperación, política versionada, matriz ejecutada e informe depurado. No
incluyas claves, backend/.env, imágenes personales, sesiones, cachés, bases de clientes reales
ni trazas privadas.

Revisa el empaquetador antes de usarlo: el heredado de la clase 8 no garantiza incluir
nuestras nuevas tablas, vault o fixtures. Construye un paquete reproducible y comprueba su
extracción en una carpeta nueva, con una base ficticia limpia y sin configuración privada. Las
evidencias de ejemplo van separadas y no deben confundirse con una práctica vacía ni con API
real.

Actualiza README para que otra persona pueda iniciar, entrar con cuentas de demostración
locales, abrir Obsidian, ejecutar pruebas y reproducir una falla. Registra commit de partida y
commit o versión final. Separa pruebas hechas en este sistema operativo de compatibilidad aún
no comprobada. No publiques ni despliegues. No cambies la rúbrica del curso ni inventes
porcentajes.
```

### Qué le estás pidiendo y por qué

La entrega debe poder arrancar fuera de tu carpeta de desarrollo. Un ZIP que solo funciona con tu .venv o base personal no es reproducible. Las evidencias se guardan separadas para no confundir un ejemplo preparado con el estado inicial.



### Validación guiada para avanzar

| Acción que realizas | Resultado que debes observar |
| --- | --- |
| Extrae la entrega y sigue su README en una carpeta nueva. | Se instala sin referenciar rutas de tu equipo ni leer secretos del proyecto original. |
| Ejecuta pruebas y revisa estado de capacidades. | Los resultados son los de esta entrega; no se acreditan funciones nuevas con pruebas antiguas. |
| Abre los materiales y el vault incluidos. | Los enlaces locales funcionan y están las políticas utilizadas con sus versiones. |
| Revisa el contenido del paquete sin abrir credenciales. | Excluye backend/.env, sesiones, entornos, cachés, respaldos y datos personales. |
| Muestra la falla recuperada. | Se observan estado anterior, interrupción, consulta, reintento y conteos finales. |

No avances solo porque el asistente diga «listo». Abre el resultado, comprueba los IDs y observa también el rechazo o la excepción.

### Recuperación de esta etapa

Corrige empaquetado o migraciones y vuelve a extraer en otra carpeta limpia. No completes a mano una entrega rota ni copies tu configuración privada para que arranque.

Si observas un resultado distinto, copia este prompt y añade el mensaje o ID concreto:

```text
No doy por cerrada la etapa 14. Observé: [resultado o error, sin secretos].
Esperaba: [resultado de la validación guiada]. Caso o recurso: [ID, si existe].
Consulta primero el estado persistido y la traza; explica la causa probable.
Corrige solo esta etapa conservando datos, evidencias y relaciones existentes.
Antes de repetir una escritura, comprueba si ya se guardó su resultado.
Repite la comprobación que falló y las regresiones afectadas, sin API real.
Indica resultado observado, conteos e IDs, y cualquier prueba aún pendiente.
No reinicialices la base ni des por aprobada una prueba que no ejecutaste.
```

En el video o recorrido de entrega muestra los dos caminos principales, una recompra y un escalamiento. Usa los mismos identificadores al pasar de cliente a operador. Incluye una falla recuperada y la vista que explica qué ocurrió.

La evidencia acompaña los criterios vigentes de calidad, seguridad, trazabilidad, costos, fallas y evolución. No sustituye la rúbrica ni establece nuevos porcentajes. Cuando una prueba quede pendiente, indica qué falta y cómo ejecutarla.

## Guion para la demostración final

### Recorrido A: consulta, compra y recompra

1. Como visitante pregunta por vigencia y entrega. Abre la fuente que respalda la respuesta.
2. Registra una cuenta ficticia nueva. Muestra su historial vacío. Para las pruebas de aislamiento usa Ana y Bruno en sesiones independientes.
3. Como Ana selecciona productos y modalidad; solicita y revisa la cotización completa. Anota COT-A y su versión real.
4. Acepta mediante el control de la interfaz. Genera PED-A y repite la misma solicitud: sigue existiendo un pedido.
5. Adjunta un soporte autorizado coherente con el escenario. Muestra el estado de revisión. No reutilices un soporte histórico como pago de hoy sin el escenario temporal de pruebas indicado en la etapa 6.
6. Como operador revisa, aprueba la versión y ejecuta. Anota IDs de propuesta, venta y operación. Como cliente muestra pedido confirmado y banco no verificado.
7. Registra preparación y recogida o despacho desde el operador. Como cliente consulta estado, última actualización y estimación.
8. Abre historial y pide recompra parcial. Muestra una cotización nueva sin heredar pago ni autorización.
9. Solicita una persona, toma el caso como operador y responde. Muestra continuidad sin perder COT-A y PED-A.

### Recorrido B: devolución y trámite de reembolso

1. Usa una compra propia entregada con cantidades suficientes, preparada como fixture si el recorrido A solo tenía una unidad. Identifica ese origen.
2. Solicita devolución de una unidad. Revisa y confirma el resumen; anota el caso de posventa.
3. El operador autoriza y registra recepción por separado. Muestra que inventario y venta original no cambian.
4. Solicita reembolso, comprueba cálculo histórico y deja que el operador decida.
5. Remite el trámite a pago externo. El cliente ve la situación administrativa; no se muestra dinero transferido.
6. Intenta comprometer el mismo saldo dos veces en una prueba aislada. Muestra el rechazo y saldo final.

### Recorrido C: falla y recuperación

1. En una copia aislada provoca pérdida de respuesta después del commit.
2. Antes de repetir, consulta el pedido y propuesta: el resultado existe.
3. Reintenta con la misma clave y comprueba un solo resultado, con los mismos IDs.
4. Contrasta con una falla antes del commit: ningún efecto parcial, seguido de un reintento completo.
5. Abre la traza y explica el punto de falla, la consulta usada para recuperar y los conteos finales.

### Registro mínimo de evidencias

Usa una fila por prueba, no una captura genérica para todo el taller:

| Etapa/caso | Preparación y origen | Acción | Esperado | Observado | IDs y evidencia | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| Ejemplo: pedido repetido | Fixture temporal, sin IA real | Repetir la misma aceptación | Un pedido, mismo ID | Se completa al ejecutar | ID y conteo antes/después | Pendiente hasta ejecutar |

Etiqueta cada evidencia como interfaz manual, prueba automatizada con mock, simulación de falla o llamada real de IA. Depura claves y datos privados. Una captura del chat complementa el registro del servidor; no sustituye la prueba de la escritura o del permiso.

## Preguntas para explicar tu solución

- ¿Qué dato viene del vault y cuál de SQLite?
- ¿Por qué el cliente no puede consultar una compra ajena aunque conozca su ID?
- ¿Qué versión de la cotización aceptó y qué pasa si cambió un precio?
- ¿Qué significa pedido confirmado por soporte y qué no se verificó bancariamente?
- ¿Qué diferencia hay entre solicitar, aprobar y remitir un reembolso?
- ¿Qué quedó guardado cuando falló la respuesta y cómo evitaste duplicarlo?
- ¿Qué midieron tus pruebas y qué sigue sin comprobarse?
