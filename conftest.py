import pytest 
from src.calcular_medidas import CalcularArea
from src.medidas import Medida

# Funções fixtures para reutilização para medida e resultado
@pytest.fixture
def medida():
    return Medida(2, 3)

# Calcula e exibe o resultado
@pytest.fixture
def resultado():
    medida = Medida(2, 3)
    resultado = CalcularArea('Área', raio)
    return resultado