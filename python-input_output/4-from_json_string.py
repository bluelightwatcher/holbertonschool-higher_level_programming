#!/usr/bin/python3
import json
"""module convert from json to python"""


def from_json_string(my_str):
    """function returns a python object

    Args:
        my_str
    Return:
        my_strJSON
    """
    my_strJSON = json.loads(my_str)
    return (my_strJSON)
