#!/usr/bin/pyhton3
def square_matrix_simple(matrix=[]):
    a_matrix = [[1]] * len(matrix)
    an_index = 0
    for row in matrix:
        a_matrix[an_index] = [x**2 for x in row]
        an_index += 1
    return(a_matrix)
