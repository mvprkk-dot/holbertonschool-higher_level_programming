#!/usr/bin/python3

"""
This module provides a function that divides all elements of a matrix.
"""


def say_my_name(first_name, last_name=""):
    """
    Print full name.

    Parameters:
        irst_name: string of first name
        last_name: string of last name

    Returns:
        full name: first name and last name combine

    Raises:
        TypeError: if the type is not string

    """
    if first_name =="" and last_name == "":
             raise TypeError("say_my_name() missing 1 required"
                             "positional argument: 'first_name'")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
