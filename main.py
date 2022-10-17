#coding:utf-8
# Authoer : Yoshiyuki Kurose

from inputMatrix import *
from calculationFunc import CalculationUtil


dimension = test_ask_dimension()
matrix = test_ask_matix(dimension) 

calcUtil = CalculationUtil()
ans = calcUtil.calcDeterminant(dimension,matrix)
print(ans)


