#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """Adds 2 integers.

    Args:
        a: first number (int or float)
        b: second number (int or float), defaults to 98

    Returns:
        The addition of a and b (int)

    Raises:
        TypeError: If a or b are not integers or floats, or are NaN/Inf.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN və Infinity yoxlaması - int() çevrilməsindən əvvəl mütləq olmalıdır
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

