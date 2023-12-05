#!/usr/bin/python3


def append_write(filename="", text=""):
    """Function that appends text to a file"""
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
