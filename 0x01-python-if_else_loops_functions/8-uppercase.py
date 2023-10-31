#!/usr/bin/python3

def uppercase(str):
    stringformat = ""
    for i in str:
        if ord(i) in range(97, 123):
            i = ord(i) - 32
            stringformat += chr(i)
        else:
            stringformat += i
    print(stringformat)
