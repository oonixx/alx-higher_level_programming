#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        max = my_list[0]
        for index in range(len(my_list)):
            if my_list[index] > max:
                max = my_list[i]
        return max
