#!/usr/bin/python3

"""
Function to div elements of a matrix with a number
>>>matrix_divdied([2, 4, 6], 2)
[0.1, 0.2, 0.3]
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix of divided value with div
    Parameters: matrix-list, div-the number to div through
    Error Handles: TypeError, ZeroDivisionError
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    erro_len = "Each row of the matrix must have the same size"
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(error)
    length = len(matrix[0])
    new_matrix = []
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(error)
        if len(i) > length or len(i) < length:
            raise TypeError(erro_len)
        temp = []
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(error)
            temp.append(round((j / div), 2))
        new_matrix.append(temp)
    return new_matrix
