#!/usr/bin/python3
""" print square """


def print_square(size):
    """ print square """
    if size is None:
        raise TypeError(
            "print_square() missing 1 required positional argument: 'size'")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end="")

        print()
