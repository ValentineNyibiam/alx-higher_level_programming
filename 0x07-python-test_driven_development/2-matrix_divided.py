#!/usr/bin/python3
"""
This is a module that defines a matrix divide function
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix (list of lists): A list of lists of integers/floats.
        div (int or float): The number to divide the matrix elements by.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   if each row is not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists: A new matrix with elements divided by div.
    """
    # validate div
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # validate matrix type
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # validate sub matrix length and all elements type
    list_len = len(matrix[0])
    for row in matrix:
        if len(row) != list_len:
            raise TypeError("Each row of the matrix must have the same size")
        for column in row:
            if not isinstance(column, (int, float)) or isinstance(column, bool):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    return [[round(element / div, 2) for element in row] for row in matrix]
