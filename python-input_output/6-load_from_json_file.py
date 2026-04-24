#!/usr/bin/python3
"""
load from JSON file as python object
"""


import json


def load_from_json_file(filename):
    """ load from JSON file as python object """

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
