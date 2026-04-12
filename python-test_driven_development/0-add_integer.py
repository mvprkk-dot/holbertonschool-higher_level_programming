#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):
    """Adds 2 integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a != a or abs(a) > 1e308: # NaN və Infinity yoxlaması
        raise TypeError("a must be an integer")
    if b != b or abs(b) > 1e308:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
