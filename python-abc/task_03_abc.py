#!/usr/bin/python3
"""Module extends over iter method"""


class CountedIterator:
    """Class extends the iter method"""

    def __init__(self, data):
        """ initializes instance of Counted iterator

        Args:
            data (int): data is an iterable
        """

        self.iterator = iter(data)
        self.counter = 0

    def __next__(self):
        """
        Next function increments a counter for each fetch.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """returns the count"""
        return self.counter
