#!/usr/bin/python3
""" this module overwrites content on a file"""


def write_file(filename="", text=""):
    """ function opens a file in write mode

    Args:
        filename: is the name of the file
        text: is the text to write
    """

    with open(filename, 'w', encoding="utf8") as f:
        content = f.write(text)
        return (content)
