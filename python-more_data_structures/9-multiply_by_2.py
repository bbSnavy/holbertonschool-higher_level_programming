#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    return {k: v * 2 for k, v in a_dictionary.items()}
