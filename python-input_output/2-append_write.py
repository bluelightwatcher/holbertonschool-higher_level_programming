#!/usr/bin/python3
""" this module overwrites content on a file"""


def append_write(filename="", text=""):
    """ function opens a file in append mode

    Args:
        filename: is the name of the file
        text: is the text to write
    """

    with open(filename, 'a', encoding="utf8") as f:
        content = f.write(text)
        return (content)
