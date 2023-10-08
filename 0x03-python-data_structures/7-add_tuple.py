#!/usr/bin/python3
def add_tuple(tuple_1=(), tuple_2=()):
    new_tuple = ()
    tuple_a = tuple_1 + (0, 0)
    tuple_b = tuple_2 + (0, 0)
    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return new_tuple
