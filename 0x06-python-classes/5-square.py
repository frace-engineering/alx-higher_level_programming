#!/usr/bin/python3
"""
Creat a class Square
"""


class Square:
    """ Define and initalise the square """
    def __init__(self, size=0):
        """ Initialize attributes """
        self.size = size

    @property
    def size(self):
        """ Get the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size with safe assignment """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the area of the square """
        return (self.__size ** 2)

    def my_print(self):
        """ Print to stdout the square with the character '#' """
        if (self.size != 0):
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
