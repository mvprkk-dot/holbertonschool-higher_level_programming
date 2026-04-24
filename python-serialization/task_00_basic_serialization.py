#!/usr/bin/python3
"""
    This module will load python dictionary and serialise it into json as file
    then it will reload the saved jason file and deserialise it back into
    python object.
"""


import json


def serialize_and_save_to_file(data, filename):

    """
    Turning python dictionary into json and save to file
    """    

    with open(filename, 'w') as file:
        json.dump(data,file)

def load_and_deserialize(filename):

    """
    Reversing json file into python dictionary
    """    

    with open(filename, 'r') as file:
        return json.load(file)
