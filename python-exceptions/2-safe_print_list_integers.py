#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    r = 0

    if my_list is None:
        return 0

    for i in range(x):
        try:
            v = my_list[i]
        except IndexError as exception:
            raise exception

        if v is None:
            continue

        if type(v) != int:
            continue

        print("{:d}".format(v), end="")
        r += 1

    print()
    return r
