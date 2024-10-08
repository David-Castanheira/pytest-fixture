import pytest
from src.medidas import Medida

def test_passar_valor_area():
    medida = Medida(2, 3)
    assert medida.get_raio() == 2

def test_passar_valor_altura():
    medida = Medida(2, 3)
    assert medida.get_altura() == 3

