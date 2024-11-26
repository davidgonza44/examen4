from src.modelos.modelo_enfriamiento import ModeloEnfriamiento

def test_temperatura_decrece():
    """Prueba que la temperatura siempre decrece"""
    modelo = ModeloEnfriamiento()
    tiempo, temp = modelo.calcular_enfriamiento()
    for i in range(len(temp)-1):
        assert temp[i] >= temp[i+1]
