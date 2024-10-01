#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """Creates an object from a JSON file
    
    Args:
        filename: The name of the file to retrieve data from
    """
    with open(filename, 'r') as file:
        file = json.load(file)
