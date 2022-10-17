#coding:utf-8
# Author : Yoshiyuki Kurose

from inputFunc import *
from calculationFunc import *


def main():
    dimension = ask_dimension()
    matrix = ask_matix(dimension)

    ans = calcDeterminant(dimension, matrix)
    print(ans)


if __name__ == "__main__":
    main()
