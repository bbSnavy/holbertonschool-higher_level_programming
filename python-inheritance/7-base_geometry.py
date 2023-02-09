#!/usr/bin/python3
""" base geometry """


class BaseGeometry:
    """ base geometry """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) not in [int]:
            raise TypeError("<{}> must be an integer".format(value))

        if value <= 0:
            raise ValueError("<{}> must be greater than 0".format(name))
