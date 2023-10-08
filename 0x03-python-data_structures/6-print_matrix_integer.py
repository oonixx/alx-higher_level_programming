#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ow in matrix:
        for ol in ow:
            print("{:d}".format(ol), end=" " if ol != ow[-1] else "")
        print()
