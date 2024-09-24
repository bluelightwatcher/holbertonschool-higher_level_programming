#!/usr/bin/python3
"""This module compares object"""


def inherits_from(obj, a_class):
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
    if isinstance(obj, a_class):
        return True
    else:
        return False
