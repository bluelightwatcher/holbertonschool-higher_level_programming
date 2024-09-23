#!/usr/bin/python3
""" This modules sorts a list"""

class Mylist(list):
    """ This class is a child of the list class

    Attributes: 
        none
    """

    def __init__(self):
        """ Function sorts a list

        args:
            none
        Returns:
            sorted list
        """
        super().__init__(self)
        self.sort()

        print(self)   
