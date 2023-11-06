#!/usr/bin/python3
def extract_tupA(tuple_a=()):
    a1 = b1 = 0
    if len(tuple_a) == 0:
        a1, b1 = 0, 0
    elif len(tuple_a) < 2 and len(tuple_a) != 0:
        a1, *c1 = tuple_a
    elif len(tuple_a) > 2:
        a1, b1, *c1 = tuple_a
    else:
        a1, b1 = tuple_a
    tuple_ap = (a1, b1)
    return tuple_ap


def add_tuple(tuple_a=(), tuple_b=()):
    a1, b1 = extract_tupA(tuple_a)
    a2, b2 = extract_tupA(tuple_b)
    tuple_c = (a1 + a2, b1 + b2)
    return tuple_c
