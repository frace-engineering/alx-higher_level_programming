#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new_matrix = []
    for x in matrix:
        new = [y**2 for y in x]
        new_matrix.append(new)
    return new_matrix
