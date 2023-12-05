#!/usr/bin/python3


def write_file(filename="", text=""):
    """Function that opens and write to a file"""
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
