#!/usr/bin/python3
"""Module Creates a class and retrives its data as dict."""


class Student:
    """Public class Student."""

    def __init__(self, first_name, last_name, age):
        """Instantiate a student class.

        Args:
        str: first_name
        str: last_name
        int: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionnary representation of Student class."""
        return self.__dict__
