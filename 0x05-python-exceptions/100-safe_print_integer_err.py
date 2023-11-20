#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        int(value)
        print(value)
        return True
    except ValueError:
        sys.stderr.write("Exception: Unknown format code")
        sys.stderr.write("'d' for object of type 'str'")
        print("")
        return False
