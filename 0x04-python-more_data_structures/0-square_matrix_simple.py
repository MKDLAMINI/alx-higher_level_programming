#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    the_squared_value = []
    for line in matrix:
        the_squared_value.append([c**2 for c in line])
    return the_squared_value
