#!/usr/bin/python3
"""Module writes a json string to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file, using a JSON representation.
    
    Args:
        my_obj: The Python object to be serialized and saved.
        filename: The name of the file to save the JSON data into.
    """
    # Use the 'with' statement correctly, without any 'if'
    with open(filename, 'w', encoding='utf-8') as file:
        file = json.dumps(my_obj)
