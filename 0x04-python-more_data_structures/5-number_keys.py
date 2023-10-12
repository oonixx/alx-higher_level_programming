#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    list_keys = list(a_dictionary.keys())

    for index in list_keys:
        num += 1

    return (num)
