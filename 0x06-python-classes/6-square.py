#!/usr/bin/python3
"""Module that defines the square class
    calculats the area of the square
    and prints out the square using (#)
"""


class Square:
    """Class that defines the square """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size and position attributes """
        self.__size = size
        self.__position = position

        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Method that calculates the area of the square """
        return self.__size * self.__size

    @property
    def size(self):
        """Method that returns the size """
        return self.__size

    @size.setter
    def size(self, value):
        """Method that sets the size of the square """
        if type(value) == int:
            self.__size = value
        else:
            raise TypeError("size must be integer")

    @property
    def position(self):
        """Method that returns the values of position """
        return self.__position

    @position.setter
    def position(self, value):
        """Method that sets the position of the square """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Method that prints the square """
        if self.__size != 0:
            for p in range(self.position[1]):
                print()
            for i in range(0, self.__size):
                for j in range(self.position[0]):
                    print(" ", end='')
                for k in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()
