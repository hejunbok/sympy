#!/usr/bin/env python
from sympy import *

A = Symbol('A',(3,3),commutative=False)
x = Symbol('x',(3,1),commutative=False)

print factor(A*x + A*x)
print factor(A*x + x*A)
print diff(A*x,x)
