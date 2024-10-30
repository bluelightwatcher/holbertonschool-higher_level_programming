#!/usr/bin/python3
"""
This module defines a Rectangle class.

Attributes:
    width: The width of the rectangle.
    height: The height of the rectangle.
"""


class Rectangle:
    """
    Rectangle represents a rectangle object.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle object.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """ Method to compute area of the rectangle
        Returns: area of rectangle
        """
        return (self._width * self._height)

    def perimeter(self):
        """Method computes the perimeter of the rectangle
        Returns: perimeter of the rectangle
        """
        if self._width == 0 or self._height == 0:
            return (0)

        else:
            return ((self._width + self._height) * 2)

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.
        """
        return self._width

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.
        """
        return self._height

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        else:
            shape = []
            for _ in range(self._height):
                shape.append("#" * self._width)
            return "\n".join(shape)

    def __print__(self):
        for _ in range(self._height):
            print("#" * self._width)

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        print("Bye rectangle...")
