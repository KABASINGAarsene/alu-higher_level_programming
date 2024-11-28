#!/usr/bin/python3
"""
matrix_divided: Divides all elements of a matrix.
Each element is divided by 'div' and rounded to 2 decimal places.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    
    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The divisor.
    
    Returns:
        list: A new matrix with divided values, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   or if rows in the matrix are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Validate matrix is not empty
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division
    return [[round(el / div, 2) for el in row] for row in matrix]
