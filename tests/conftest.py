import pytest
from src.modelos.modelo_enfriamiento import ModeloEnfriamiento
from src.modelos.modelo_pendulo import ModeloPendulo

@pytest.fixture
def modelo_enfriamiento_default():
    return ModeloEnfriamiento()

@pytest.fixture
def modelo_pendulo_default():
    return ModeloPendulo()
