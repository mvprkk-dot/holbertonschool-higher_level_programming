#!/usr/bin/python3
"""
write to file as JSON
"""


import json


def save_to_json_file(my_obj, filename):
    """ write to file as JSON """

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
