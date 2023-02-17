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

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        l = []
        if list_objs:
            [l.append(v.to_dictionary()) for v in list_objs]

        with open('%s.json' % (cls.__name__), 'w') as file:
            file.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """ from json string """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create """

        if 'rectangle' in cls.__name__.lower():
            obj = cls(7, 7)
        else:
            obj = cls(7)

        obj.update(dictionary)
        return obj
