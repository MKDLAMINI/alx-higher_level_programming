#!/usr/bin/python3
"""Create module of a new square"""


class Square:
    """Define a square"""

    def __init__(self, size):
        """Class builder
        Args:
            size: length of side of the square
        """
        self.__size = size
