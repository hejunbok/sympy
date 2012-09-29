#!/usr/bin/env python
from sympy import *

A = MatrixSymbol('A',3,3)
C = MatrixSymbol('C',3,3)
D = MatrixSymbol('D',3,3)
x = MatrixSymbol('x',3,1)
b = MatrixSymbol('b',3,1)
e = MatrixSymbol('e',3,1)

pprint(diff(x.T*A*x,x).fix(x))
a = (A*x+b).T*C*(D*x+e)
print diff(a,x).fix(x)
