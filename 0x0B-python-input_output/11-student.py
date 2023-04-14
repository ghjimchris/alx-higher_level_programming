#!/usr/bin/python3
"""Defines a student"""


class Student:
    """Student class

    Attributes:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student
    """

    first_name = ""
    last_name = ""
    age = 0

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

    def reload_from_json(self, json):
        """Replaces all attributes of Student instance"""

        for k, v in json.items():
            setattr(self, k, v)
