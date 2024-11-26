import numpy as np
from src.modelos.modelo_pendulo import ModeloPendulo

def test_periodo_pequenas_oscilaciones():
    """Prueba el período para pequeñas oscilaciones"""
    modelo = ModeloPendulo(longitud=1.0)
    periodo_teorico = 2 * np.pi * np.sqrt(1.0/9.8)
    tiempo, angulo, velocidad = modelo.calcular_movimiento()

    # Encuentra el primer cruce por cero
    for i in range(1, len(angulo)):
        if angulo[i-1] * angulo[i] <= 0:
            periodo_calculado = tiempo[i] * 4
            assert abs(periodo_calculado - periodo_teorico) < 0.1
            break
