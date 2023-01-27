#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    return {0: max(a_dictionary.values())}.get(0, 0)
