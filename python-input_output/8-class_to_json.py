#!/usr/bin/python3
"""
load from JSON file as python object
"""


def class_to_json(obj):
    """ return dictionary description with simple data structure """
    return obj.__dict__
