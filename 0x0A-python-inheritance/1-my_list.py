#!/usr/bin/python3
"""Defines an inherited list class"""


class MyList(list):
    """MyList class inheritance of list class"""

    def print_sorted(self):
        """Prints the list, but sorted(ascending sort)"""

        print(sorted(self))
