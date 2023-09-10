#!/usr/bin/python3
"""
Create a class rectangle
"""


class Rectangle:
    """ initializing the Rectangle class private fields """
    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Return width """
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
        """ Return height """
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
        """ Return a string rpresentation of the triangle """
        if (self.__width == 0) and (self.__height == 0):
            return ""
        new_str = ([str(self.print_symbol * self.__width)
                    for s in range(self.__height)])
        return '\n'.join(new_str)

    def __repr__(self):
        """ Return the string representation of the triangle """
        return 'Rectangle({}, {})'.format(self._width, self.height)

    def __del__(self):
        """ Print a message when an obj is deleted """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
