#!/usr/bin/python3
""" square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ square """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        r = ''
        r += '[Square] '
        r += '(%s) ' % (self.id)
        r += '%s/%s' % (self.x, self.y)
        r += ' - '
        r += '%s' % (self.size)
        return r

    @property
    def size(self):
        return self.__size

    @size.setter(self, value):
        if type(value) not in [int]:
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value
