#!/usr/bin/python3
""" rectangle """


def integer_validator(self, name, value):
    """ integer validator """
    if type(value) not in [int]:
        raise TypeError("{} must be an integer".format(name))

    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))

    return value


class Rectangle():
    """ rectangle """

    def __init__(self, width, height):
        self._Rectangle__width = self.integer_validator("width",  width)
        self._Rectangle__height = self.integer_validator("height", height)
