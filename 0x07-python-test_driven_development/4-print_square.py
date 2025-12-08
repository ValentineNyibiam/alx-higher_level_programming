#!/usr/bin/python3
"""
Defines a print_square function
"""

def print_square(size):
    """
    prints a square of size
    """
    # validate size
    if not isinstance(size, (int, float)) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()