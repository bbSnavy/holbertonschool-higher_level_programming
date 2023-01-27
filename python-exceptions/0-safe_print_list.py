#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    r = 0

    if my_list is None:
        return r

    for i in range(x):
        try:
            if my_list[i] is None:
                continue

            print("{:d}".format(my_list[i]), end='')
            r += 1

        except IndexError:
            pass

    print()
    return r
