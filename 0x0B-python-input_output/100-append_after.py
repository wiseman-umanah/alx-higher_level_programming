#!/usr/bin/python3

"""
Module that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """Function to insert a line of text to a file
    after each line containing a specific string

    Args:
        search_string: the string to search for
        new_string: string to insert after the line
    """
    temp = ""
    with open(filename, "r") as fp:
        for i in fp.readlines():
            temp += i
            if search_string in i:
                temp += new_string
    with open(filename, "w") as fp:
        fp.write(temp)
