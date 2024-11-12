#!/usr/bin/python3
"""
wnsdvuybadsb ashdufybvasdvad
sasdfbuwasbvwaea suvhweauisdwasf
asfvnyuasfuywasb eadsgjhwas fweasfbweasgv
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row

    for i in range(1, n):
        """
        Create the next row by adding adjacent
        elements from the previous row.
        """
        prev_row = triangle[-1]
        next_row = [1]  # First element is always 1
        for j in range(1, len(prev_row)):
            next_row.append(prev_row[j - 1] + prev_row[j])
        next_row.append(1)  # Last element is always 1
        triangle.append(next_row)

    return triangle
