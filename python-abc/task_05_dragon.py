#!/usr/bin/python3

class SwimMixin:
    """Mixin to add swimming functionality."""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin to add flying functionality."""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class inheriting from both SwimMixin and FlyMixin."""
    def roar(self):
        print("The dragon roars!")
