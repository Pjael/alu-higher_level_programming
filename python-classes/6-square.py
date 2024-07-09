#!/usr/bin/python3
"""class that defines square with  private instance attirbute size"""


class Square:

    """defines class, instantiates private instance attirbute size + position"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """property to retrieve private instance attribute size"""
    @property
    def size(self):
        return(self.__size)

    """setter to set private instance attribute size"""
    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    """property, retrieves private instance attribute position"""
    @property
    def position(self):
        return(self.__position)

    """setter, sets private instance attribute position"""
    @position.setter
    def position(self, value):
        check = 0
        while 1:
             if type(value) is not tuple or len(value) is not 2:
                 check += 1
                 break
             if type(value[0]) is not int or type(value[1])is not int:
                 check += 1
                 break
             if value[0] < 0 or value[1] < 0:
                 check += 1
             break
        if check is 0:
             self.__position = value

        else: 
             raise TypeError('position must be a tuple of 2 positive integers')

    """public instance method, calculates +returns current square area"""
    def area(self):
        return(self.__size * self.__size)

    """public instance method, prints in stdout sqaure in #"""
    def my_print(self):
        if self.__size > 0:
            for y in range(self.__position[0]):
                print()
            for column in range(self.__size):
                for x in range(self.__position[0]):
                    print('', end='')
                for row in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
