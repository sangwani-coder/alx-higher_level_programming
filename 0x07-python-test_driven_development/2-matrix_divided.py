"""
    This module defines a function that divides all
    elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
     param: matrix( list of lists)
     param: div(int) can be an integer or a float
     return: a new matrix with each element divided by div
    """
    if (not isinstance(div, int)) and (not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if isinstance(matrix, list):
        if len(matrix) != 2:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if isinstance(matrix[0], list):
            len_list1 = len(matrix[0])
        else:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if isinstance(matrix[1], list):
            len_list2 = len(matrix[1])
        else:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len_list1 != len_list2:
            raise TypeError("Each row of the matrix must have the same size")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    import copy
    res = copy.deepcopy(matrix)
    for row in range(len(res)):
        for cols in range(len(res[row])):
            if(not isinstance(matrix[row][cols], int)) and (not isinstance(matrix[row][cols], float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            res[row][cols] = round((res[row][cols] / div), 2)
    return res
