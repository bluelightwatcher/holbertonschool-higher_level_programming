#!/usr/bin/python3
import json
"""module returns the json repr of a string"""


def to_json_string(my_obj):
    """function returns type of a json object

    Args:
        my_obj
    Return:
        my_obj: type of obj
    """
    return json.dumps(my_obj) 
