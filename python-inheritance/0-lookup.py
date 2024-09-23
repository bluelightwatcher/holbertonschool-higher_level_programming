# /usr/bin/python3
"""This module prints all attributes of a class in a list"""


def lookup(obj):
    """
    Function uses dir to print class attibutes

    Args:
        obj: is an instance of a class
    """

    print(dir(obj))
