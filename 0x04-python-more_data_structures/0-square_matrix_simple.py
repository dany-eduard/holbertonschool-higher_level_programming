#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda row: list(map(lambda i: i ** 2, row)), matrix))
    """ Add one list inside another to build the matrix """
