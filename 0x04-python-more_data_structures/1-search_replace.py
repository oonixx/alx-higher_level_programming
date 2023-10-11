#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
        A function that traverse through a list for an element that matches
        search and modify it with replace then returns a new list.
        @elm: Elements
    '''
    if len(my_list) == 0:
        return my_list

    new_lst = [elm if elem != search else replace for elm in my_list]
    return new_lst
