#!/usr/bin/python3
def replace_in_list(my_list, index, element):
    if index < 0 or index > len(my_list) - 1:
        return my_list
    else:
        my_list[index] = element
        return my_list
