#!/usr/bin/python3
"""Defines the text-indentation function."""


def text_indentation(text):
    """Print the text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to be printed.
    Raises:
        TypeError: If the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("the text must be a string")

    rca = 0
    while rca < len(text) and text[rca] == ' ':
        rca += 1

    while rca < len(text):
        print(text[rca], end="")
        if text[rca] == "\n" or text[rca] in ".?:":
            if text[rca] in ".?:":
                print("\n")
            rca += 1
            while rca < len(text) and text[rca] == ' ':
                rca += 1
            continue
        rca += 1
