#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    it = 0
    for i in matrix:
        it = len(i)
        for j in i:
            print("{} ".format(j) if j != (len(i)) else "{}".format(j), end="")
        print("")
