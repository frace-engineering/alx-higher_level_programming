#!/usr/bin/python3
""" Demonstration of class inheritance
MyList is a subclass of list class
"""


class MyList(list):
    """ Implement sorted list printing for the built-in list class """
    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
