#!/usr/bin/python3
"""
Bu modul say_my_name funksiyasını təqdim edir.
"""


def say_my_name(first_name, last_name=""):
    """
    Ad və soyadı çap edən funksiya.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
