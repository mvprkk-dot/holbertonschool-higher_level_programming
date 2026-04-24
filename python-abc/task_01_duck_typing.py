#!/usr/bin/python3

"""
This Python code demonstrates the concept of abstract classes and inheritance
to define an shape hierarchy with a base class `Shape` and derived classes
`Circle` and `Square`. The `Shape` class is an abstract class with an abstract
method `area()` and 'perimeter()'. The `Circle` and `Square` classes inherit
from the `Shape` class and implement the abstract methods.
"""


import math
from abc import ABC, abstractmethod
"""

"""


class Shape(ABC):
    """
    method `area()` and 'perimeter()' are abstract and must be implemented
     by the derived classes. It defines the expected behavior of making 
     method `area()` and 'perimeter()' in sub classes
    """

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return 2 * (self.height + self.width)
    
def shape_info(self):
    print(f"Area: {self.area()}")
    print(f"Perimeter: {self.perimeter()}")
