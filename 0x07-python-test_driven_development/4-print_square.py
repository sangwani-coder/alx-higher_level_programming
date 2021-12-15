#!/usr/bin/python3
# Author: Sangwani P. Zyambo

"""
    Defines a function that prints a square
"""


def print_square(size):
    """
        Prints a square with the character "#".

        param: size(int) - the length of the square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()
