#!/usr/bin/python3
"""
This module will define a square class.
"""


class Square:
    """
    This is a square class.
    """
    def __init__(self, size=0):
        """
         Creating instances of a square with one parameter.

         Args:
            size: will be the size of the square

         Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
         """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size


    def area(self):
        """
        Determines the area of a square.

        Returns:
            int: The size of a square depending on the size
        """
        return self.__size * self.__size
