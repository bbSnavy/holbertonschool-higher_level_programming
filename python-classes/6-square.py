#!/usr/bin/python3
""" Square """


class Square:
    """ Square """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        e = TypeError("position must be a tuple of 2 positive integers")

        if type(position) is not tuple:
            raise e

        if len(position) != 2:
            raise e

        if type(position[0]) is not int:
            raise e

        if type(position[1]) is not int:
            raise e

        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        r = ''
        s = self.__size
        p = self.__position
        for x in range(s):
            r += ' ' * p[0]
            for y in range(s):
                r += '#'
            if (x + 1) < s:
                r += '\n'
        print(r)
