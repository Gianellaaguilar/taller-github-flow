IMPUESTOS_POR_PAIS = {
    "CO": 0.19,
    "MX": 0.16,
    "CL": 0.19
}


def obtener_descuento(es_vip: bool, monto: float) -> float:
    if es_vip and monto > 1000:
        return 0.20
    if es_vip:
        return 0.10
    return 0.0


def procesar_pago_usuario(usuario: dict, tarjeta: dict, monto: float, pais: str, es_vip: bool) -> bool:
    # Guard Clauses (Validadiones tempranas)
    if not usuario or not usuario.get('activo', False):
        return False
    if tarjeta.get('saldo', 0) < monto:
        return False

    # Descuento
    porcentaje_descuento = obtener_descuento(es_vip, monto)
    monto_final = monto * (1 - porcentaje_descuento)

    # Impuesto
    tasa_impuesto = IMPUESTOS_POR_PAIS.get(pais, 0.0)
    monto_final += monto_final * tasa_impuesto

    tarjeta['saldo'] -= monto_final
    return True