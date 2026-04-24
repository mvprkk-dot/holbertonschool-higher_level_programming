#!/usr/bin/python3
"""
Fayla yazan və simvol sayını qaytaran funksiya
"""


def write_file(filename="", text=""):
    """Faylı açır və mətni içinə yazır"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
