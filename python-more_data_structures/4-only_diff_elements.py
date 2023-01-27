#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    if set_1 is None:
        return []
    if set_2 is None:
        return []
    return [v for v in set_1 if v not in set_2]
