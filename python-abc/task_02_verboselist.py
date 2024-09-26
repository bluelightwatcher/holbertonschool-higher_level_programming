#!/usr/bin/python3
"""module extends a class"""

class VerboseList(list):
    """ is a subclass of list"""

    def __init__(self, args=None):
        """creates an instance of VerboseList
        """
        if args is None:
            super().__init__()
        else:
            super().__init__(args)

    def append(self, item):
        """
        calls the original append method
        then prints a message

        Args:
            item (int): is the item to append
        """

        super().append(item)
        print(f"Added [{item}] to the list")


    def extend(self, args):
        """
        calls the original extend method
        then prints a message

        Args:
            args (tuple): is the list of item to extend
        """

        super().extend(args)
        nbr_item = len(args)
        print(f"Extended the list with [{nbr_item}] items")

        
    def remove(self, args):
        """
        calls the original remove method
        then prints a message

        Args:
            args (tuple): is the list of item to remove
        """
        rem_item = args
        print(f"Removed [{args}] from the list")
        super().remove(rem_item)


    def pop(self, index=-1):
        """
        calls the original pop method
        then prints a message

        Args:
            index: is the index of item to pop
        """

        item = self[index]

        print(f"Removed [{item}] from the list")
        super().pop(index)
