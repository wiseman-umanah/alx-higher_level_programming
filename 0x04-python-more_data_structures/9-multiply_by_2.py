#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for i, v in a_dictionary.items():
        v *= 2
        new_dict[i] = v
    return new_dict
