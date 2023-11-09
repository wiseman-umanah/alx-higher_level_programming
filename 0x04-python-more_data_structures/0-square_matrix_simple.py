#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    temp = []
    square = lambda j: j ** 2
    for i in matrix:
        for j in i:
            temp.append(square(j))
        new_matrix.append(temp)
        temp = []
    return new_matrix
