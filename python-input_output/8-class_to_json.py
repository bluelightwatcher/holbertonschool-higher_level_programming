#!/usr/bin/python3
"""Module return dictionnary from a class."""


def class_to_json(obj):
    """Return the dictionnary representation of an object."""
    return obj.__dict__
