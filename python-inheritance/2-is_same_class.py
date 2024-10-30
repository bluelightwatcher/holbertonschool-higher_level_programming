#!/usr/bin/python3
"""This module compares object"""


def is_same_class(obj, a_class):

    """
    Function uses eq magic method

        Method:
            __eq_: magic method compares two objects

        Args:
            obj: is the object to compare
            a_class: is the class to compare to

        Returns:
            boolean
    """
    return type(obj) is a_class
