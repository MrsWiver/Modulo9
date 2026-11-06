---
id: POL-REEMBOLSOS
version: "1.0"
vigente_desde: 2026-11-06
estado: aprobado
audiencia: cliente
responsable: Operador de práctica
origen: escenario_ficticio
---

# Reembolso administrativo

El cliente solicita; una persona revisa y decide. La aprobación de devolución no aprueba automáticamente un reembolso. En el escenario ordinario de devolución de producto, se exige recepción registrada antes de aprobar el reembolso. Una excepción requiere motivo explícito del operador.

El monto usa cantidades elegibles y precio realmente vendido. En el piloto sin descuentos y recogida gratuita: monto de productos = cantidad aprobada × precio unitario de la venta. No se añade de nuevo un impuesto incluido. No se reembolsa un transporte no cobrado. Otros ajustes o cargos requieren ampliar el desglose y probarlo antes de utilizarlos.

El saldo administrativo disponible es el monto de cobro aplicado a la venta, menos los reembolsos aprobados o remitidos aún vigentes. Los aprobados reservan ese saldo y la comprobación es atómica. Esta es una cuenta administrativa basada en soportes aceptados, no un saldo bancario verificado. Una revocación autorizada antes de remitir libera su reserva y conserva la decisión y motivo; después de remitir, una corrección exige expediente adicional, sin liberar automáticamente el saldo.

Estados: `solicitado`, `en_revision`, `aprobado_administrativamente`, `rechazado`, `revocado`, `remitido_a_pago_externo`. La transición a `revocado` exige autorización del operador antes de la remisión y conserva el historial. La remisión guarda responsable, fecha y referencia administrativa. El caso puede cerrarse por remisión, indicando «trámite administrativo remitido; pago externo pendiente». Nunca mostrar «dinero devuelto» ni un estado `pagado` en esta práctica. No se recogen cuentas bancarias ni se ejecutan transferencias.
