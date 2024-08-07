#!/usr/bin/python3
"""class defines a Rectangle"""


class Rectangle:

    """defines private instance attribute width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        """property, retrieves private instance attribute width"""
        @property
        def width(self):
            return(self.__width)

        """sets private instance attribute width"""
        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError('width must be an integer')
            elif value < 0:
                raise ValueError('width must be >= 0')
            else:
                self.__width = value

        """retrieves private instance attribute height"""
        @property
        def height(self):
            return(self.__height)

        """sets private instance attribute height"""
        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError('height must be an integer')
            elif value < 0:
                raise ValueError('height must be >= 0')
            else:
                self.__height = value
