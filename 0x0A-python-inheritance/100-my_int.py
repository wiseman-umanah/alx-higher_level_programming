#!/usr/bin/python3

"""Class inheritance"""


class MyInt(int):
    """class MyInt that inherits from int"""
    def __init__(self, number):
        """Initializes a new class

        Args:
            number (int): the number to initialize with
        """
        self.number = number
