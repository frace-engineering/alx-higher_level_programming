#!/usr/bin/python3
"""
Create class Square with private instance
"""


class Square:
    """ class quare defined here """
    def __init__(self, size=0):
        """ Initialize variables """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

        """ Define public instance method area """
    def area(self):
        """ Return the area of the square """
        return (self.__size ** 2)
