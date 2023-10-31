#!/usr/bin/python3
"""Defines the name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print the name.

    Args:
        first_name (str): Print the first name.
        last_name (str): Print the last name.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
