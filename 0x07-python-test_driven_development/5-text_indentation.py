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

    Args:
		text (str): The string to reprint

    Raises:
    	TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    s = ""
    while i != len(text):
        if text[i] in [':', '?', '.']:
            s += text[i]
            s += "\n"
            i += 1
            if text[i] == " ":
                s += "\n"
            else:
                s += text[i]
        else:
            s += text[i]
        i += 1
    print(s, end="")
