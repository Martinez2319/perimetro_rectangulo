"""Pruebas de casos correctos, límites y entradas incorrectas."""

import pytest

from perimetro_rectangulo import perimetro_rectangulo


def test_caso_correcto():
    assert perimetro_rectangulo(5, 3) == 20


def test_medidas_decimales():
    assert perimetro_rectangulo(2.5, 1.2) == pytest.approx(7.4)


@pytest.mark.parametrize("largo, ancho, esperado", [(0, 0, 0), (0, 3, 6), (5, 0, 10)])
def test_caso_limite_cero(largo, ancho, esperado):
    assert perimetro_rectangulo(largo, ancho) == esperado


@pytest.mark.parametrize("largo, ancho", [(-1, 3), (5, -2)])
def test_error_medidas_negativas(largo, ancho):
    with pytest.raises(ValueError, match="negativo"):
        perimetro_rectangulo(largo, ancho)


@pytest.mark.parametrize("valor", ["5", None, True, False, [2], 2 + 1j])
@pytest.mark.parametrize("posicion", [0, 1])
def test_error_tipo_incorrecto(valor, posicion):
    medidas = [5, 3]
    medidas[posicion] = valor
    with pytest.raises(TypeError):
        perimetro_rectangulo(*medidas)


@pytest.mark.parametrize("valor", [float("inf"), float("-inf"), float("nan")])
@pytest.mark.parametrize("posicion", [0, 1])
def test_error_valor_no_finito(valor, posicion):
    medidas = [5, 3]
    medidas[posicion] = valor
    with pytest.raises(ValueError, match="finito"):
        perimetro_rectangulo(*medidas)


def test_error_desbordamiento():
    with pytest.raises(OverflowError):
        perimetro_rectangulo(1e308, 1e308)
