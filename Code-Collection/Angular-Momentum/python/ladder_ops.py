#!/Users/robertpoenaru/.pyenv/shims/python
import numpy as np

# generate the matrices for the Ladder operators J_, J+, and also the set of commuting operators J^2, J_z

HBAR = 1


# generate the matrix element of $J^2$
def J2_MatEl(j, m1, m2):
    if(m1 != m2):
        return 0
    return np.power(HBAR, 2) * j * (j + 1)


# generate the matrix element of $J_z$
def Jz_MatEl(j, m1, m2):
    if(m1 != m2):
        return 0
    return HBAR * m1


# generate the matrix element of $J_+$
def JPlus_MatEl(j, m1, m2):
    if(m2 != m1 + 1):
        return 0
    c_plus = np.sqrt((j - m1) * (j + m1 + 1)) * HBAR
    return c_plus


# generate the matrix element of $J_-$
def JMinus_MatEl(j, m1, m2):
    if(m2 != m1 - 1):
        return 0
    c_minus = np.sqrt((j + m1) * (j - m1 + 1)) * HBAR
    return c_minus


# for a given angular momentum j, generate the matrix associated with the possible states that this |jm> representation can have
def JM_Matrix(j, angular_operator):
    matrix = []
    for m2 in reversed(np.arange(-j, j + 1, 1)):
        line = []
        for m1 in reversed(np.arange(-j, j + 1, 1)):
            # line.append(f'<{j},{m2}|{j},{m1}>')
            # line.append([m2, m1, angular_operator(j, m1, m2)])
            # only add the value of the operator's matrix element itself
            line.append(angular_operator(j, m1, m2))

        matrix.append(line)
    for line in matrix:
        print(line)


JM_Matrix(1, J2_MatEl)
JM_Matrix(1, Jz_MatEl)
JM_Matrix(1, JPlus_MatEl)
JM_Matrix(1, JMinus_MatEl)
