#!/usr/bin/python3
"""this is class that defines a square with a private instance attribut size"""


class Square:

    """method that defines the class and instantiates size"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
    def area(self):
        """calculate
        self.area = square_area
    def __mul__(self, other):
        return data(self.area * other.area)
