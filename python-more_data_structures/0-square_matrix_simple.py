#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    r = []
    for v in matrix:
        r.append([x * x for x in v])
    return r
