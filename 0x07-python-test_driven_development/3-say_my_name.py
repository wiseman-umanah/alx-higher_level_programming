#!/usr/bin/python3

"""
define a function that print the information of the user
>>>say_my_name("Wiseman", "Umanah")
My name is Wiseman Umanah
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first and last name of user
    Parameters: first_name, last_name
    Raise TypeError if parameter is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
