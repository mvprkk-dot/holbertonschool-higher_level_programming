#!/usr/bin/python3
"""Düzbucaqlını təyin edən modul."""


class Rectangle:
    """Düzbucaqlını təmsil edən klas."""

    def __init__(self, width=0, height=0):
        """Yeni bir düzbucaqlı yaradır."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Eni götürmək üçün getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Eni təyin etmək üçün setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hündürlüyü götürmək üçün getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Hündürlüyü təyin etmək üçün setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Düzbucaqlının sahəsini qaytarır."""
        return self.__width * self.__height

    def perimeter(self):
        """Düzbucaqlının perimetrini qaytarır."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
