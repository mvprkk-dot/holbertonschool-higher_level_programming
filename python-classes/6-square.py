#!/usr/bin/python3
"""Kvadratı təyin edən modul."""


class Square:
    """Kvadratı təmsil edən klas."""

    def __init__(self, size=0, position=(0, 0)):
        """Yeni bir Square yaradır."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size üçün getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Size üçün setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position üçün getter."""
        return self.__position

    @position.setter
    def position(self, value):
        """Position üçün setter."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Sahəni hesablayır."""
        return self.__size * self.__size

    def my_print(self):
        """Kvadratı position-a uyğun '#' ilə çap edir."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
