#!/usr/bin/python3
def delete_at(my_list=[], index=0):
    if index < 0 or index > len(my_list) - 1:
        return my_list
    else:
        del my_list[index]
    return my_list
