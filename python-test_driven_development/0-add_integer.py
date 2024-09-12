#!/usr/bin/python3
"""
Module for add_integer function.
This module provides a function that adds two integers, with
type checking and conversion from float to integer.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns an integer.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (defaults to 98).

    Returns:
        The sum of a and b, as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
        always look on the bright side of life
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast both to integers if they are floats
    a = int(a)
    b = int(b)
    
    return a + b

