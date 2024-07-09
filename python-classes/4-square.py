#!/usr/bin/python3
"""a class that defines a square with a private instance attribute size"""


class Square:

    """method that defines the class and instantiates size"""
    def __init__(self, size=0):
        self.__size = size

    """property to retrieve private instance attibute size"""
    @property
    def size(self):
        return(self.__size)

    """property setter to set private instance attribute size"""
    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    """method that calculates the current square area"""
    def area(self):
        return(self.__size * self.__size)
