#!/usr/bin/python3
"""a class that defines a square"""


class Square:
    """
    Represents a square.

    Attributes:
    size (int): the size of the square
    position (int): the position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialises an instance of Square

        Args:
            size (int, optional): the size of a square. Defaults to 0
            position (tuple, optional): the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrives itself
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Determines whether the size value for the square is appropriate

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves itself
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Puts the new position
        """
        error_message = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(error_message)
        if len(value) != 2:
            raise TypeError(error_message)
        for number in value:
            if type(number) is not int:
                raise TypeError(error_message)
            if number < 0:
                raise TypeError(error_message)
        self.__position = value

    def area(self):
        """
        Finds area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with desired size
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size, end="")
                print()
