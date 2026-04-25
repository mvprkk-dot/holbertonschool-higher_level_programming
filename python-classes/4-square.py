#!/usr/bin/python3
"""Kvadratı təyin edən modul."""


class Square:
    """Kvadratı təmsil edən klas."""

    def __init__(self, size=0):
        """
        Yeni bir Square yaradır.

        Args:
            size (int): Kvadratın ölçüsü.
        """
        self.size = size

    @property
    def size(self):
        """Kvadratın ölçüsünü götürmək (Getter)."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Kvadratın ölçüsünü təyin etmək (Setter).

        Args:
            value (int): Yeni ölçü dəyəri.

        Raises:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Kvadratın sahəsini hesablayır.

        Returns:
            Sahə dəyəri.
        """
        return self.__size * self.__size
