#!/usr/bin/python3
"""This module explores multiple inheritances."""


class Fish():
    """Parent class

    Method:
        swim: print a message.
        habitat: prints a message.
    """

    def swim(self):
        """ prints a basic message."""

        message = "The fish is swimming"
        print(message)

    def habitat(self):
        """ prints a basic message."""

        message = "The fish lives in water"
        print(message)


class Bird():
    """Parent class

    Method:
        fly: print a message.
        habitat: prints a message.
    """

    def fly(self):
        """ prints a basic message."""

        print("The bird is flying")

    def habitat(self):
        """ prints a basic message."""

        print("The bird lives in the sky")


class FlyingFish(Bird, Fish):
    """
    Classes override the methods inherited from the parent classes

    Attributes:
        Fish and Bird cls.
    """

    def __init__(self):
        """creating and instance of FlyingFish"""

    def fly(self):
        """overridesthe fly method"""

        print("The flyingFish is soaring!")

    def swim(self):
        """override the swim method"""

        print("The flying fish is swimming!")

    def habitat(self):
        """overrides the habitat method"""

        print("The flying fish lives both in water and the sky!")
