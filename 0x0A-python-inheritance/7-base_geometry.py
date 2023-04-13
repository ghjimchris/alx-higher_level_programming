#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:

    """Base Geometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Args:
            name (str): string
            value (int): integer
        """

        self.name = name
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value
