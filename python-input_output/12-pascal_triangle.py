#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """Pascal triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        last_row = triangle[-1]
        row = [1]
        for i in range(1, len(last_row)):
            row.append(last_row[i - 1] + last_row[i])
        row.append(1)
        triangle.append(row)
    return triangle
