#!/usr/bin/python3
"""Defines a student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""

        new_dict = {}
        if attrs is None:
            return self.__dict__
        for el in attrs:
            if el in self.__dict__:
                new_dict[el] = self.__dict__[el]
        return new_dict
