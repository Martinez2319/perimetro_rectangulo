"""Cálculo del perímetro de un rectángulo: actividad del alumno 8."""

import math


def perimetro_rectangulo(largo: int | float, ancho: int | float) -> int | float:
    """Devuelve el perímetro usando la fórmula 2 * (largo + ancho).

    Args:
        largo: Longitud no negativa, de tipo int o float.
        ancho: Anchura no negativa, de tipo int o float.
            Ambas medidas deben estar en la misma unidad.

    Returns:
        Perímetro en la misma unidad. Se permite cero como caso límite
        de un rectángulo degenerado.

    Raises:
        TypeError: Si una medida no es int o float, o es un booleano.
        ValueError: Si una medida es negativa, infinita o NaN.
        OverflowError: Si el resultado no puede representarse como float finito.

    Example:
        >>> perimetro_rectangulo(5, 3)
        16
    """
    for nombre, medida in (("largo", largo), ("ancho", ancho)):
        if isinstance(medida, bool) or not isinstance(medida, (int, float)):
            raise TypeError(f"{nombre} debe ser un número entero o decimal.")
        if isinstance(medida, float) and not math.isfinite(medida):
            raise ValueError(f"{nombre} debe ser un número finito.")
        if medida < 0:
            raise ValueError(f"{nombre} no puede ser negativo.")

    resultado = 2 * (largo + ancho)
    if isinstance(resultado, float) and not math.isfinite(resultado):
        raise OverflowError("El perímetro excede el rango de los números decimales.")
    return resultado
