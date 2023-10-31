#!/usr/bin/python3
"""Defines the square-printing function."""


def print_square(size):
    """Print the square with the # character.

    Args:
        size (int): The height/width of square.
    Raises:
        TypeError: If size not an integer.
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for index in range(size):
        [print("#", end="") for ji in range(size)]
        print("")
