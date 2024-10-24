#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]] or matrix == []:
        print("")
        return
    else:
        for liste in matrix:
            for i in liste:
                if i == liste[-1]:
                    print("{:d}".format(i), end="\n")
                else:
                    print("{:d}".format(i), end=" ")
