#!/usr/bin/python3
"""Module that contains function to append contents to file"""


def append_write(filename="", text=""):
    """Function that appends text to a file

    Args:
        filename: the filename

    Returns:
        The number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
