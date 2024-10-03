#!/usr/bin/python3
""" this module prints content of a file"""


def read_file(filename=""):
    """ function opens a file
    Args:
        filename: is the name of the file
    """

    with open(filename, 'r', encoding="utf8") as f:
        content = f.read()
        print(content, end="")
