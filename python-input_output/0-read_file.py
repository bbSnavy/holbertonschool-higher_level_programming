#!/usr/bin/python3
def read_file(filename=""):
    """ read file """
    with open(filename, 'r', encoding='utf-8') as file:
        s = file.read()
    return s