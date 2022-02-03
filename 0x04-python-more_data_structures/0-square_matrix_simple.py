#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in (matrix):
            new_matrix.append([x*x for x in row])
    return new_matrix
