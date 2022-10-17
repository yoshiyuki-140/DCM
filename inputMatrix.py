#coding:utf-8


def ask_dimension():
    dimension = int(input("How many dimensions? : "))
    if dimension < 1:
        raise ValueError("The dimension must be more than 1")
    return dimension

def ask_matix(dimension:int):
    matrix = [[int(x) for x in input(f"Please input {i+1} row of the matrix >> ").split()]
                   for i in range(dimension)]
    return matrix

