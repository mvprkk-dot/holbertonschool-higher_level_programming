#!/usr/bin/python3
"""
append to file and print out its length
"""


def append_write(filename="", text=""):
    """ append to the file and print out its length """

    with open(filename, 'a', encoding='utf-8') as file:
        length = file.write(text)
        return length
