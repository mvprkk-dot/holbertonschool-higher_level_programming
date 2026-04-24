#!/usr/bin/env python3
"""Module for converting XML format to JSON"""

import json
import xml.etree.ElementTree as ET
import os

def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.
    
    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the XML file to write.
    """
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename)
        return True
    except Exception as e:
        print(f"Error during serialization: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Convert an XML file to a JSON file.
    
    Parameters:
    filename (str): The name of the XML file to read.
    """
    if not os.path.exists(filename):
        return None

    with open(filename, 'r') as file:
        xml_content = file.read().strip()

        if not xml_content:
            return {}
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {}
        for child in root:
            key = child.tag
            value = child.text

            data[key] = value

        return data
    except ET.ParseError:
        print("Error: The XML file is not well-formed.")
        return None
