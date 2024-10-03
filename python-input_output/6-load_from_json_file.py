#!/usr/bin/python3
"""Module creates an object from a json file."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.
    
    Args:
        filename: The name of the file to retrieve data from.
    """
    with open(filename, 'r', encoding='utf8') as file:
        return json.load(file)
