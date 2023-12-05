#!/usr/bin/python3


def read_file(filename=""):
    """Function to open and reads a file's content"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
