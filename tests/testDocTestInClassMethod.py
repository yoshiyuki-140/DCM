#coding:utf-8

import doctest

class Tests:
    def tests1(self,n:int):
        """
        >>> Tests().tests1(5)
        5
        """
        print(n)


if __name__ == '__main__':
    doctest.testmod()