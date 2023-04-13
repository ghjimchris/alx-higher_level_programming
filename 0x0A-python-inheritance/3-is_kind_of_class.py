#!/usr/bin/python3
"""Defines a class and inherited checking function"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
    or if the object is an instance of a class inherited from
    the specific class, otherwise False"""

    return isinstance(obj, a_class)
