#!/usr/bin/python3


def common_elements(set_1, set_2):
    if set_1 is None:
        return []
    if set_2 is None:
        return []
    return [v for v in set_1 if v in set_2]
