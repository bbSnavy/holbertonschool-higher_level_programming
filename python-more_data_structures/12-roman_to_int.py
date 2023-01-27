#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if type(roman_string) is not str:
        return 0
    s = roman_string.upper()
    r = 0
    for i, _ in enumerate(roman_string):
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        if i != (len(roman_string) - 1) and d[s[i]] < d[s[i + 1]]:
            r -= d[s[i]]
        else:
            r += d[s[i]]

    return r
