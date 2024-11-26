from src.modelos.modelo_enfriamiento import ModeloEnfriamiento

def test_inicializacion_default():
    """Prueba la inicialización con valores por defecto"""
    modelo = ModeloEnfriamiento()
    assert modelo.temp_inicial == 90
    assert modelo.temp_ambiente == 25
    assert modelo.k == 0.1
