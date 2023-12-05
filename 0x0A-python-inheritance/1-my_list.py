#!/usr/bin/python3

"""
class MyList that inherits from list
"""


class MyList(list):
    """
    This class inherits from list

    Args:
        list (list): the list that is being inherited from
    Attributes:
        print_sorted: Prints sorted list to STDOUT
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
