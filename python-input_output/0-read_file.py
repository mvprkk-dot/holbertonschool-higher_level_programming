#!/usr/bin/python3
"""
Read in file and print out its content
"""


def read_file(filename=""):
    """ Read the file and print out the content """

    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
