#!/usr/bin/python3
"""class defines rectangle with private instance attribute width"""


class Rectangle:

    """defines class, instantiates private instance attribute width + height"""
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
                raise TypeError(width must be an integer)
            if value < 0:
                raise ValueError(width must be >= 0)

        """retrieves private instance attribute height"""
        @property
        def height(self):
            return(self.__height)

        """sets private instance attribute height"""
        @height.setter
        def height(self, value):
            self.__height = value
            if type(value) is not int:
                raise TypeError(heightmust be an integer)
            if value < 0:
                raise ValueError(height must be >= 0)
