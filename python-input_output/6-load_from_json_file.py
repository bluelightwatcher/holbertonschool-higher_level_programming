#!/usr/bin/python3
import json
"""Module creates an object from a json file."""


def load_from_json_file(filename):
    """Creates an object from a JSON file
    
    Args:
        filename: The name of the file to retrieve data from
    """
    with open(filename, 'r') as file:
        return json.load(file)
