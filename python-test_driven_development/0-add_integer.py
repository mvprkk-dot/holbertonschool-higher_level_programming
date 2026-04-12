#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: the first integer.
        b: the second integer.

    Raises:
        TypeError: if a or b are not integers or floats, or if they are NaN/Inf.

    Returns:
        The sum of the two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN və ya Infinity yoxlaması
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
