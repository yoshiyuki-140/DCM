#coding:utf-8


import doctest
from copy import deepcopy


class CalculationUtil:
    def __init__(self) -> None:
        pass

    def whenDimensionIsTwo(self, dimension: int, matrix: list):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    def whenDimensionIsMoreThanThree(self, dimension: int, matrix: list):
        dimension = deepcopy(dimension)
        matrix = deepcopy(matrix)
        for x in range(len(dimension)):
            pass

    def findCofactor(self, dimension: int, matrix: list, k: int):
        """
        # k >= 1
        >>> CalculationUtil().findCofactor(3,[[1,2,3],[1,2,3],[1,3,4]],1)
        [1, [2, 3], [3, 4]]
        >>> CalculationUtil().findCofactor(3,[[1,2,3],[1,2,3],[1,3,4]],2)
        [-2, [1, 3], [1, 4]]
        """

        # v高速化のために
        result = [pow(-1, k+1)*matrix[0][k-1]]
        k = k-1
        for i, y in enumerate(matrix):
            if i == 0:
                continue
            else:
                result.append([])
            for j, x in enumerate(y):
                if j == k:
                    continue
                result[i].append(x)
        return result

    def findDeterminant(self, dimension: int, matrix: list):
        if dimension == 1:
            result = matrix
        elif dimension == 2:
            result = self.whenDimensionIsTwo(dimension, matrix)
        else:
            pass


if __name__ == '__main__':
    doctest.testmod()