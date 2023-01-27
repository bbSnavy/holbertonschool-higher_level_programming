#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    return [v for v in my_list if v != search else replace]
