#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the Rectangle.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle
        """
        self.width = width
        self.height= height

    @property
    def width(self):
        """ Get and Set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >0")
        self.__width = value

    @property
    def height(self):
        """Get and set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height mus be >=0")
        seld.__height = value

        def area(self):
            """Return the area of the rectangle"""
            return (self.__width * self.__height)

        def perimeter(self):
            """Return the perimeter of the rectangle"""
            if self.__width == 0 or self.__height == 0:
                return (0)
            return ((self.__width * 2) + (self.__height * 2))
