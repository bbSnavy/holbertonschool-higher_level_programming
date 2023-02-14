#!/usr/bin/python3
""" base """


class Base:
    """ base """
    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects += 1

        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json string """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
