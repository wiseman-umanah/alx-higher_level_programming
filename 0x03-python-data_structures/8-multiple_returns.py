#!/usr/bin/python3
def multiple_returns(sentence):
    first_character = None
    length = len(sentence)
    if length != 0:
        first_character = sentence[0]
    tuple_a = (length, first_character)
    return tuple_a
