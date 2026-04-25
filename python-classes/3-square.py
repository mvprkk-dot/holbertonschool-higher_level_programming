#!/usr/bin/python3
"""Kvadratı təyin edən modul."""


class Square:
    """Kvadratı təmsil edən klas."""

    def __init__(self, size=0):
        """
        Yeni bir Square yaradır.

        Args:
            size (int): Kvadratın ölçüsü.

        Raises:
            TypeError: Əgər size integer deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Kvadratın cari sahəsini hesablayır.

        Returns:
            Kvadratın sahəsi (size * size).
        """
        return self.__size * self.__size
