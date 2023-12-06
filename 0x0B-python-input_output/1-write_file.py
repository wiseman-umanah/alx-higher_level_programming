#!/usr/bin/python3
"""Module that contains a function that write to file"""


def write_file(filename="", text=""):
    """Function that writes to a file

    Args:
        filename: the filename
        text: contents to be written

    Return:
        The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
