import pytest
from src.modelos.modelo_pendulo import ModeloPendulo

def test_validacion_parametros():
    """Prueba la validación de parámetros"""
    with pytest.raises(ValueError):
        ModeloPendulo(longitud=-1)
    with pytest.raises(ValueError):
        ModeloPendulo(gravedad=0)
