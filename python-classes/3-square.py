#!/usr/bin/python3
"""this is class that defines a square with a private instance attribut size"""


class Square:

    """method that defines the class and instantiates size"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """calculates the current square area"""
        return(self.size * self.__size)
