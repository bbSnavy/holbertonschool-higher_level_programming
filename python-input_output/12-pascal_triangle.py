#!/usr/bin/python3
""" pascal triangle """


def f(n):
    """ f """
    return {
        i: v
        for i, v in
        enumerate(pascal(n - 1))
    }


def pascal(n):
    """ pascal """
    if n < 0:
        return []
    if n == 0:
        return [1]
    r = (lambda d: [d.get(x - 1, 0) + d.get(x, 0) for x in range(n + 1)])(f(n))
    return r


def pascal_triangle(n):
    """ pascal triangle """
    return [pascal(x) for x in range(n)]
