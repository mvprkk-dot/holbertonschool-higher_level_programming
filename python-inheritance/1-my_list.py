#!/usr/bin/python3
"""
Module for MyList class.
"""


class MyList(list):
    """
    A class that inherits from list and adds a sorted printing method.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        """
        print(sorted(self))
