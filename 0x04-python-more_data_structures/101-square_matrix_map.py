#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda xi: list(map(lambda yi: yi**2, xi)), matrix)))
