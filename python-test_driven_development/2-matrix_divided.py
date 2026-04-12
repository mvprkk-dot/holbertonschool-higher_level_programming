#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            if not isinstance(x, (int, float)) or x != x or abs(x) > 1e308:
                raise TypeError(msg)
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)
    return new_matrix
