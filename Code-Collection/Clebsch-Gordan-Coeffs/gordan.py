#!/Users/robertpoenaru/.pyenv/shims/python

from sympy.physics.quantum.cg import CG
from sympy import S
from sympy import *


# calculates the Clebsch-Gordan coefficient for a given set of parameters j1,j2,m1,m2,j,m=m1+m2
from sympy.physics.quantum.cg import CG
from sympy import S
cg =CG(S(3) / 2, S(3) / 2, S(1) / 2, -S(1) / 2, 1, 1)

RESULT=N(cg.doit())
