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

    def to_json(self, attrs=None):
        """Return a dictionnary representation of Student class.

        if a list of attributes is given func returns list of attributes
        if none is given func return all the attributes of the student class
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        else:
            return self.__dict__
