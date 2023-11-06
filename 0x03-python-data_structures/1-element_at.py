#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return
    i = 0
    if idx > (len(my_list) - 1):
        return
    while i < idx:
        i += 1
    return my_list[i]
