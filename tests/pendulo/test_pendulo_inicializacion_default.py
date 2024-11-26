from src.modelos.modelo_pendulo import ModeloPendulo

def test_inicializacion_default():
    """Prueba la inicialización con valores por defecto"""
    modelo = ModeloPendulo()
    assert modelo.longitud == 2.0
    assert modelo.gravedad == 9.8
    assert modelo.angulo_inicial == 0.2
