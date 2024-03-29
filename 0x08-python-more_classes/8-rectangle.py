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
        """ Create a string object from the given objects """
        new_str = ""
        if self.__width > 0 and self.__height > 0:
            for s in range(self.__height):
                for t in range(self.__width):
                    new_str += str(self.print_symbol)
                new_str += '\n'
            return new_str

    def __repr__(self):
        """ Create the string representation of the object """
        return 'Rectangle({}, {})'.format(self.__height, self.__width)

    def __del__(self):
        """ Print message when obj is deleted """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """ Compare the area of two instances of the Rectangle class """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
