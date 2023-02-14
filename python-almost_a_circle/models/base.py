#!/usr/bin/python3
""" base """
import json


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

    def save_to_file(cls, list_objs):
        """ save to file """
        with open('%s.json' % (cls.__name__), 'w') as file:
            file.write(Base.to_json_string(list_objs))
