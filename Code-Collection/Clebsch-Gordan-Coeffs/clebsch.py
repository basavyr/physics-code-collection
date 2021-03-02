#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
from sympy.physics.quantum.cg import CG
from sympy import S
from sympy import *


# Checks wether a spin-quantum-number is half-integer or not
def HalfInteger(x):
    half = 1 / 2
    x_half = x + half
    if(x_half.is_integer()):
        return 1
    return 0


# shows all the angular momentum states |J,M> which result from coupling the two angular momenta j1 and j2
def ShowJM_States(j1, j2):
    j_vals = np.arange(abs(j1 - j2), j1 + j2 + 1, 1)
    JM = []
    for j in j_vals:
        m_vals = np.arange(-j, j + 1, 1)
        for m in m_vals:
            JM.append((j, m))
    return JM


print(ShowJM_States(1, 1 / 2))

# shows all the states that form the basis {s=|j1,j2;m1,m2>=s1+s2}
# where s1,s2 are the two subspaces which correspond to each of the two angular momenta
# i.e., s1=|j1,m1> and s2=|j2,m2>


def ShowJ1J2M1M2_States(j1, j2):
    return 0


def GenerateQuantumNumbers(j1, j2):
    if(j1 < 0 or j2 < 0):
        return -1
    if(HalfInteger(j1)):
        J1 = f'{int(2*j1)}/2'
    else:
        J1 = j1
    if(HalfInteger(j2)):
        J2 = f'{int(2*j2)}/2'
    else:
        J2 = j2
    m1 = np.arange(-j1, j1 + 1, 1)
    m2 = np.arange(-j2, j2 + 1, 1)
    j12 = np.arange(abs(j1 - j2), j1 + j2 + 1, 1)
    count_j = 1
    JM = []
    J1J2_M1M1 = []
    for m11 in m1:
        if(HalfInteger(m11)):
            M1 = f'{int(2*m11)}/2'
        else:
            M1 = m11
        for m21 in m2:
            if(HalfInteger(m21)):
                M2 = f'{int(m21*2)}/2'
            else:
                M2 = m21
            print(f'|j1,j2;m1,m2> = |{J1},{J2},{M1},{M2}>')
    for j in j12:
        m12 = np.arange(-j, j + 1, 1)
        # print(f'j_{count_j}={j}')
        if(HalfInteger(j)):
            J = f'{int(j*2)}/2'
        else:
            J = j
        for m in m12:
            if(HalfInteger(m)):
                M = f'{int(2*m)}/2'
            else:
                M = m
            # print(f'|j,m> = |{J},{M}>')
            JM.append((j, m))
        count_j = count_j + 1
    print(f'The |J,M> states')
    print(JM)


qn = GenerateQuantumNumbers

j1 = 1
j2 = 1 / 2

# qn(j1, j2)

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
