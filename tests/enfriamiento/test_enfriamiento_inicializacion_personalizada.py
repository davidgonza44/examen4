from src.modelos.modelo_enfriamiento import ModeloEnfriamiento

def test_inicializacion_personalizada():
    """Prueba la inicialización con valores personalizados"""
    modelo = ModeloEnfriamiento(temp_inicial=100, temp_ambiente=20, k=0.2)
    assert modelo.temp_inicial == 100
    assert modelo.temp_ambiente == 20
    assert modelo.k == 0.2
