#!/usr/bin/python3
""" write file """


def write_file(filename="", text=""):
    """ write file """
    with open(filename, 'w', encoding='utf-8') as file:
        r = file.write(text)
    return r
