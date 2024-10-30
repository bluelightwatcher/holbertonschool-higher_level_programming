#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        """Initializes Student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only this list is retrieved.
        Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces attributes of Student instance with values of json dict.
        Assumes json file is always valid .
        """
        for key, value in json.items():
            setattr(self, key, value)
