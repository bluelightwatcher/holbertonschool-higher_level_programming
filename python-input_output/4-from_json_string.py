#!/usr/bin/python3
"""Module serialize from json to python."""
import json


def from_json_string(my_str):
    """Return a python object.

    Args:
        json: my_str
    Return:
        str: my_strJSON
    """
    my_strJSON = json.load(my_str)
    return (my_strJSON)
