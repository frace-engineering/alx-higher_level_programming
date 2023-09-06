#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix

