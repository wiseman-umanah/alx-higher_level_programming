#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0:
        return my_list
    i = 0
    if idx > (len(my_list) - 1):
        return my_list
    while i < len(my_list):
        if i == idx:
            new_list.append(element)
        else:
            new_list.append(my_list[i])
        i += 1
    return new_list
