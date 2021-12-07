#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    def area(self):
        return self.__size * self.__size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) == int:
            self.__size = value
        else:
            raise TypeError("size must be integer")
