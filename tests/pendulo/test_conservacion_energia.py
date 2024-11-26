import numpy as np
from src.modelos.modelo_pendulo import ModeloPendulo

def test_conservacion_energia():
    """Prueba la conservación de la energía"""
    modelo = ModeloPendulo()
    tiempo, angulo, velocidad = modelo.calcular_movimiento()

    def energia_total(ang, vel):
        return 0.5 * vel**2 + (modelo.gravedad/modelo.longitud) * (1 - np.cos(ang))

    E_inicial = energia_total(angulo[0], velocidad[0])
    E_final = energia_total(angulo[-1], velocidad[-1])
    assert abs(E_final - E_inicial) < 0.1
