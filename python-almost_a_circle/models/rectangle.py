#!/usr/bin/python3
""" rectangle """


from models.base import Base


class Rectangle(Base):
    """ rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def input_check(self, value, name):
        """ input check """
        if type(value) not in [int]:
            raise TypeError(f"{name} must be an integer")

        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.input_check(value, 'width')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.input_check(value, 'height')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.input_check(value, 'x')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.input_check(value, 'y')
        self.__y = value
