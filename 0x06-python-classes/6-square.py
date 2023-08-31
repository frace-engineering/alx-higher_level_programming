#!/usr/bin/python3
"""
Creat a class Square
"""


class Square:
    """ Define and initalise the square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize attributes """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Get the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position with safe assignment """
        if (len(tuple(value)) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")

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
            print("\n")
