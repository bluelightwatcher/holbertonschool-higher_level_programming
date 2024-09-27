#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
It includes a method to print the list sorted in ascending order.
"""

class MyList(list):
    """
    MyList is a subclass of the built-in list class.

    Public methods:
        print_sorted(): Prints the list in ascending sorted order without modifying the original list.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        Does not modify the original list.
        """

        if len(self) == 0
            print([])
        else:
            print(sorted(self))
