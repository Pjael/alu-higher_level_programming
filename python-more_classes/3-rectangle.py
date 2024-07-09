#!/usr/bin/python3
"""defines class Rectangle with private instance attributes width/height
and public instance methods to return the rectangle area and primeter
and can print the rectangle using '#' with print() or str()"""


class Rectangle:

    """defines private instance attribute width + height"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """property, retrieves private instance attribute width"""
    @property
    def width(self):
        return(self.__width)

    """sets private instance attribute width"""
    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
           raise TypeError('width must be an integer')
        if value < 0:
           raise ValueError('width must be >= 0')

    """retrieves private instance attribute height"""
    @property
    def height(self):
        return(self.__height)

    """sets private instance attribute height"""
    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
           raise TypeError('heightmust be an integer')
        if value < 0:
           raise ValueError('height must be >= 0')

    """ public instance method, returns rectangle area"""
    def area(self):
        return(self.__height * self.__width)

    """public instance method, returns rectangle perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
           return(0)
        else:
           return((self.__height + self.__width) * 2)

    """returns string representation of rectangle"""
    def __str__(self):
        rec_string = ''
        if self.__height == 0 or self.__width == 0:
            return(rec_string)
        for row in range(self.__height):
            for column in range(self.__width):
                rec_string += '#'
            rec_string += '\n'
        rec_string = rec_string[:-1]
        return(rec_string)



