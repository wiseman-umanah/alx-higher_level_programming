#!/usr/bin/python3

"""
Function that strips a string based on some punctation mark
>>>text_indentation("hello? boy")
hello
boy
"""


def text_indentation(text):
    """
    Prints the formatted string
    Parameters: the text to strip
    Raise TypeError if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    puncs = [".", ",", "?", ":"]
    for i in text:
        if i in puncs:
            print("\n")
            continue
        print(i, end="")
    print("")
