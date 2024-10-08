import pytest
from src.calcular_medidas import CalcularArea
from src.medidas import Medida

@pytest.fixture
def resultado():
    medida = Medida(2, 3)
    resultado = CalcularArea('Área', medida)
    return resultado

def test_passar_valor_raio_devolver_valor_area(resultado):
    # raio = Medida(2, 3)
    # calcularArea = CalcularArea('Área', raio)
    # assert calcularArea.calcular_area() == 12.56
    assert resultado.calcular_area() == 12.56

def test_passar_valor_raio_devolver_valor_volume(resultado):
    # raio = Medida(2, 3)
    # calcularArea = CalcularArea('Volume', raio)
    # assert calcularArea.calcular_volume() == 37.68
    assert resultado.calcular_volume() == 37.68