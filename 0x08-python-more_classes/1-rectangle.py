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
        if value is not int:
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
        if value is not int:
            """ raise TypeError if height is not an integer """
            raise TypeError("height must be an integer")
        if value < 0:
            """ raise ValueError if height < 0 """
            raise ValueError("height must be >= 0")
        self.__height = value
