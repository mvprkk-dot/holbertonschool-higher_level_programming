#!/usr/bin/env python3
"""Module for converting CSV format to JSON"""

import json
import csv


def convert_csv_to_json(filename):
    """
    Convert a CSV file to a JSON file.
    
    Parameters:
    filename (str): The name of the CSV file to read.
    add to line 20 #print(list(reader))testing reader content    
    """
    data = []  # Initialize an empty list to store rows
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        # Convert the list of rows to JSON and print it
        json_output = json.dumps(data, indent=4)
        # Write the JSON output to a file
        with open("data.json", 'w') as file:
            file.write(json_output)
        return True
    except Exception as e:
        print(f"Error during serialization: {e}")
        return False    

if __name__ == "__main__":
    convert_csv_to_json("data.csv")
