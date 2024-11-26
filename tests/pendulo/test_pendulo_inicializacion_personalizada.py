from src.modelos.modelo_pendulo import ModeloPendulo

def test_inicializacion_personalizada():
    """Prueba la inicialización con valores personalizados"""
    modelo = ModeloPendulo(longitud=1.0, angulo_inicial=0.1)
    assert modelo.longitud == 1.0
    assert modelo.angulo_inicial == 0.1
