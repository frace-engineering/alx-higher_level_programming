#!/usr/bin/python3
"""Division of multidimentional matrix"""


def matrix_divided(matrix, div):
    """Check if matrix is None"""
    if matrix is None:
        return None
    """Check if the divisor is a number, else throw TypeError"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    """If div is zero, throw ZeroDivisionError"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    """Check if elements of the matrix are all numbers, else throw TypeError"""
    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
    """Generate new matrix by dividing the elements of"
    " the original matrix and returning it in 2 decimal places"""
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
