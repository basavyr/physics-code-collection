#!/Users/robertpoenaru/.pyenv/shims/python


from sympy.physics.quantum.cg import CG
from sympy import S
from sympy import *

clebsch = CG

j1 = 0.5
j2 = 0.5
m = 1
m2 = 1.0 / 2.0
m1 = m - m2
j = j1 + j2


def CG(j1, m1, j2, m2, j, m):
    if(m1 + m2 != m):
        return -1
    else:
        cg = clebsch(j1, m1, j2, m2, j, m)
        return N(cg.doit())
    return -1


print(f'j1={j1} | m1={m1}')
print(f'j2={j2} | m2={m2}')
print(f'j={j} | m={m}')
print(f'C_{m1},{m2},{m}^{j1},{j2},{j}')
print(CG(j1, m1, j2, m2, j, m))
