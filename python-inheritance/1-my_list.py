#!/usr/bin/python3
""" This modules sorts a list"""


class MyList(list):
    """ This class is a child of the list class

    Methods:
        __init__(self): Initialize the list and sorts it
    """

    def __init__(self):
        """ Function sorts a list
               
        """
        super().__init__(self)
        self.sort()
        print(self)
