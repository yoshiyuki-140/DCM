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
        >>> CalculationUtil().findCofactor(3,[[1,2,3],[1,2,3],[1,3,4]],2)
        {'head': -2, 'matrix': [[1, 3], [1, 4]]}
        >>> CalculationUtil().findCofactor(3,[[1,2,3],[1,2,3],[1,3,4]],1)
        {'head': 1, 'matrix': [[2, 3], [3, 4]]}
        """

        result = {'head':pow(-1, k+1)*matrix[0][k-1],'matrix':[[] for _ in range(dimension-1)]}
        tmpMatrix = matrix
        # 1行目を削除
        del tmpMatrix[0]
        # k列目を削除
        for i in range(dimension-1):
            del tmpMatrix[i][k-1]
        result['matrix'] = tmpMatrix

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
