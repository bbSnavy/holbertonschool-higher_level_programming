#!/usr/bin/python3
""" class to json """


def class_to_json(obj):
    """ class to json """
    r = {}
    for k, v in obj.__dict__.items():
        if not isinstance(v, (list, dict, str, int, bool)):
            raise TypeError("Attribute {} is not serializable".format(attr))
        r[k] = v
    return r
