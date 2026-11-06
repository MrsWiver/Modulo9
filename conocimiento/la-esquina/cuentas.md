---
id: POL-CUENTAS
version: "1.0"
vigente_desde: 2026-11-06
estado: aprobado
audiencia: cliente
responsable: Operador de práctica
origen: escenario_ficticio
---

# Registro y acceso de clientes

El cliente puede consultar políticas y catálogo sin registrarse. Para aceptar cotizaciones, generar pedidos y acceder a historial, soportes o expedientes necesita una cuenta y sesión propias. El registro solicita nombre, correo y contraseña y crea un cliente_id estable con rol cliente. No concede rol operador ni asigna compras antiguas por coincidencias de texto.

El correo debe ser único bajo una normalización documentada. La contraseña se ingresa en el formulario de acceso y no pasa por el chat, las trazas o los documentos. Se conserva un hash seguro, nunca su texto. Cerrar sesión invalida el acceso privado hasta volver a autenticarse. Las cuentas de Ana y Bruno sirven para pruebas, sin sustituir el registro de una cuenta nueva.

La práctica es local con datos ficticios: no incorpora verificación de correo ni recuperación por email. Una dirección ingresada no acredita identidad sobre compras anteriores. Las asociaciones históricas requieren revisión administrativa explícita. Si se crea una cotización anónima, su posible vinculación al registrarse exige pertenecer a la misma sesión previa y confirmación, sin buscar borradores de otras personas.
