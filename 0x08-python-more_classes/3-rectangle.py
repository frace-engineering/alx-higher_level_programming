#!/usr/bin/python3
"""
Create a class rectangle
"""


class Rectangle:
    """ initializing the Rectangle class private fields """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ raise TypeError if width is not an integer """
        if type(value) is not int:
            raise TypeError("width must be an integer")
            """ raise ValueError if width < 0 """
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            """ raise TypeError if height is not an integer """
            raise TypeError("height must be an integer")
        if value < 0:
            """ raise ValueError if height < 0 """
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return the area of the triangle """
        return self.__width * self.__height

    def perimeter(self):
        """ return the perimeter of the triangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Create a string object from the given objects """
        new_str = ""
        if self.__width > 0 and self.__height > 0:
            for s in range(self.__height):
                for t in range(self.__width):
                    new_str += '#'
                new_str += '\n'
            return new_str
