#!/usr/bin/env python
from sympy import *

A = MatrixSymbol('A',3,3)
x = MatrixSymbol('x',3,1)

pprint(diff(x.T*A*x,x).fix(x))
