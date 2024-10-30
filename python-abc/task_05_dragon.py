#!/usr/bin/python3
"""module explores mixin classes"""

class SwimMixin:
    """Class to mixin

    Method:
    swim: prints a message
    """

    def swim(self):
        """method print string"""

        print("The creature swims!")

class FlyMixin:
    """Class to mixin

    Method:
    fly: prints a string
    """

    def fly(self):
        """method print string"""

        print("The creature flys!")

class Dragon(SwimMixin, FlyMixin):
    """Child class will add another method

    Method:
    roar: prints a string
    """

    def roar(self):
        print("The dragon roars!")
