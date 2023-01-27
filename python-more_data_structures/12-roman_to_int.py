#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None:
        return None
    if type(roman_string) is not str:
        return None
    r = 0
    for c in roman_string:
        r += {
            'i': 1,
            'v': 5,
            'x': 10,
            'l': 50,
            'c': 100,
            'd': 500,
            'm': 1000,
        }.get(c.lower(), 0)
    return r
