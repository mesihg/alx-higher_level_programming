#!/usr/bin/python3
"""A function that divides all elements of a matrix module """


def matrix_divided(matrix, div):
    """Return a new matrix with each elements of the matrix divided by div.

    Args:
       matrix (list): first input of type list
       div (int): second input of type integer or float

    Returns:
        A new matrix with each elements of the matrix divided by div.

    Raises:
       TypeError: if div is not integer or not float
       TypeError: if the matrix consists of non-integer values
       TypeError: if the matrix consists of different row size
       ZeroDivisionError : if div is 0
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(col, list) for col in matrix) or
            not all((isinstance(val, int) or isinstance(val, float))
                    for val in [num for row in matrix for num in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(col) == len(matrix[0]) for col in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(row/div, 2) for row in col] for col in matrix]
