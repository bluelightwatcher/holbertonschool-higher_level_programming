#!/usr/bin/python3
"""Module returns the json repr of an obj."""
import json


def to_json_string(my_obj):
    """Return type of a json object.

    Args:
        my_obj
    Return:
        str: type of obj
    """
    return json.dumps(my_obj) 
