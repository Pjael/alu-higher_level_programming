#!/usr/bin/python3
"""class,defines a square with private instance attirbute size"""


class Square:

    """defines class, instantiates private inst. attribut+public instance method"""
    def __init__(self, size=0):
        self.__size = size

    """property, retieve private instance attirbute size"""
    @property
    def size(self):
        return(self.__size)

    """setter, sets private instance attribute size"""
    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    """public instance method, calculates +returns current square area"""
    def area(self):
        return(self.__size * self.__size)

    """public instance method,  prints in stdout, square in #"""
    def my_print(self):
        if self.__size > 0:
            for column in range(self.__size):
                for row in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
