#!/usr/bin/python3
""" Square """


class Square:
    """ Square """

    def __init__(self, size=0):
        self.size(size)

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self._Square__size = size

    def area(self):
        return self._Square__size ** 2
