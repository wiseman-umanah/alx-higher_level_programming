#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    sort_set = (set_1 | set_2) - (set_1 & set_2)
    return sort_set
