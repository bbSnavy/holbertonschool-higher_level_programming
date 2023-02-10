#!/usr/bin/python3
""" student """


class Student():
    """ student """

    def __init__(self, first_name='', last_name='', age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        r = {}
        for k, v in self.__dict__.items():
            if not isinstance(v, (list, dict, str, int, bool)):
                raise TypeError(
                    "Attribute {} is not serializable".format(attr))
            r[k] = v
        return r
