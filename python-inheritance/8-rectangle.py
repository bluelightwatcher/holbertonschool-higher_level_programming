#!/usr/bin/python3
"""This module is in progress"""


class BaseGeometry():
    """
    the class is not yet initialized
    """

    def __init__(self):
        """
        method not implemented yet
        """
        pass

    def area(self):
        """
        method not implemented yet
        only raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method validates input

        Args:
            name: is the name of this instance
            value: is the value of this instance
        """

        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than zero")


class Rectangle(BaseGeometry):
    """Sub-class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        if self.integer_validator("width", width):
            self._width = width
        if self.integer_validator("height", height):
            self._height = height