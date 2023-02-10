#!/usr/bin/python3
""" student """


class Student():
    """ student """

    def __init__(self, first_name='', last_name='', age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        r = {}
        for k, v in self.__dict__.items():
            f = True
            if attrs is not None:
                f = False
            if type(attrs) is list:
                for attr in attrs:
                    if k == attr:
                        f = True
            else:
                f = True

            if not f:
                continue

            if not isinstance(v, (list, dict, str, int, bool)):
                raise TypeError(
                    "Attribute {} is not serializable".format(attr))
            r[k] = v
        return r

    def reload_from_json(self, json):
        for k, v in json.items():
            self.__dict__[k] = v
