import pytest
from src.modelos.modelo_enfriamiento import ModeloEnfriamiento

def test_inicializacion_invalida():
    """Prueba que se lancen errores con valores inválidos"""
    with pytest.raises(ValueError):
        ModeloEnfriamiento(temp_inicial=-300)
    with pytest.raises(ValueError):
        ModeloEnfriamiento(k=-1)
