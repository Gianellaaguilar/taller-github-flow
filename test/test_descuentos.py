import pytest
from descuentos import calcular_precio_final

def test_cliente_vip_con_cupon():
    # Cobertura de es_vip=True y cupon="DESCUENTO10"
    resultado = calcular_precio_final(100.0, es_vip=True, cupon="DESCUENTO10")
    assert resultado == 70.0

def test_cupon_superpromo():
    # Cobertura de cupon="SUPERPROMO" (Línea 10)
    resultado = calcular_precio_final(100.0, es_vip=False, cupon="SUPERPROMO")
    assert resultado == 50.0

def test_cupon_oro():
    # Cobertura de cupon="ORO" (Línea 13)
    resultado = calcular_precio_final(100.0, es_vip=False, cupon="ORO")
    assert resultado == 70.0

def test_sin_descuentos():
    # Cobertura para cliente no VIP y sin cupón
    resultado = calcular_precio_final(100.0, es_vip=False)
    assert resultado == 100.0

def test_precio_invalido_lanza_excepcion():
    # Cobertura de la excepción ValueError
    with pytest.raises(ValueError):
        calcular_precio_final(-10, es_vip=False)