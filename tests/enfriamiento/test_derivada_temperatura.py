import numpy as np
from src.modelos.modelo_enfriamiento import ModeloEnfriamiento

def test_derivada_temperatura():
    """Prueba el cálculo de la derivada de temperatura"""
    modelo = ModeloEnfriamiento(temp_inicial=90, temp_ambiente=25, k=0.1)
    derivada = modelo.derivada_temp(90)
    assert np.isclose(derivada, -0.1 * (90 - 25))
