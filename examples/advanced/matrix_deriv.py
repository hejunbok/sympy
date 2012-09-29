#!/usr/bin/env python
from sympy import *
from sympy.abc import m,n

A = MatrixSymbol('A',n,n)
C = MatrixSymbol('C',n,n)
D = MatrixSymbol('D',n,n)
x = MatrixSymbol('x',n,1)
b = MatrixSymbol('b',n,1)
e = MatrixSymbol('e',n,1)
a = MatrixSymbol('a',n,1)

exps = [x.T*A*x,
        (A*x+b).T*C*(D*x+e),
        #a.T*x*x.T*b
       ]
for exp in exps:
    print
    print 'exp'
    pprint(exp)
    print 'diff'
    pprint(diff(exp,x))
    print 'diff fix'
    pprint(diff(exp,x).fix(x))
