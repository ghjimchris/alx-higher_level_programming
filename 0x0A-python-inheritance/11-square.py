#!/usr/bin/python3
"""Defines a rectangle with a subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, inheritance of Rectangle"""

    def __init__(self, size):
        """__init__ - initialize a square class

        Args:
            size (int): size of square
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of square"""

        return self.__size * self.__size

    def __str__(self):
        """Returns the square description"""

        return f"[Square] {self.__size}/{self.__size}"
