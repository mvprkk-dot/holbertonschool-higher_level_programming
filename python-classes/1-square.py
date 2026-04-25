#!/usr/bin/python3
"""Kvadrat klasını təyin edən modul."""


class Square:
    """Kvadrat klası."""

    def __init__(self, size):
        """
        Kvadratı yaradır.

        Args:
            size: Kvadratın ölçüsü (private atribut).
        """
        self.__size = size
