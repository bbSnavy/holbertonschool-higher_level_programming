#!/usr/bin/python3
""" div matrix """


def matrix_divided(matrix, div):
    r = []

    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all([type(v) is list for v in matrix]):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all([all([type(e) in [int, float] for e in v]) for v in matrix]):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    l = len(matrix)
    for v in matrix:
        if len(v) is not l:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0.0:
        raise ZeroDivisionError("division by zero")

    for l in matrix:
        n = []

        for v in l:
            o = round(v / div, 2)

            n.append(o)

        r.append(n)

    return r
