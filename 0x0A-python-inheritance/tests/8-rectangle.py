#!/usr/bin/python3
# Auth Sangwani P Zyambo

""" This module defines a class based on 6-base_geometry.py ."""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """unimplemneted area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Derived class that inherits from BaseGeometry base class"""

    def __init__(self, width, height):
        """instantiates class object"""
        if self.integer_validator("width", width):
            self._width = width
        if self.integer_validator("height", height):
            self._height = height
