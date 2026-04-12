#!/usr/bin/python3
"""Modul matrisin bölünməsi funksiyasını ehtiva edir."""


def matrix_divided(matrix, div):
    """Matrisin bütün elementlərini div-ə bölür.

    Args:
        matrix: Tam ədəd və ya float siyahılarının siyahısı.
        div: Bölən (rəqəm olmalıdır).

    Returns:
        Bölünmüş elementlərdən ibarət yeni matris.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]

