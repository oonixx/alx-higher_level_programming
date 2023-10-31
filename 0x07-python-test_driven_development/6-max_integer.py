#!/usr/bin/python3
"""Module to find max integer in the list
"""


def max_integer(list=[]):
    """Function finds and returns the max integer in the list of integers
        If the list empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    index = 1
    while index < len(list):
        if list[index] > result:
            result = list[i]
        index += 1
    return result
