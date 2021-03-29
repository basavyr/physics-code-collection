#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np

# import matplotlib.pyplot as plt
from numpy.linalg import matrix_power
import gordan as CGC

# define the imaginary unit
I = 1j


# define a function for raising a matrix to a power
def Matrix_Power(mat, n):
    mat_n = matrix_power(mat, n)
    return mat_n


# define the Pauli matrix for a rotation around the Y-axis
Sigma_Y = [[0, -I], [I, 0]]

# for id in range(5):
#     print(f'n={id+1}')
#     sy_2n = Matrix_Power(Sigma_Y, 2 * id + 1)
#     print(np.array(sy_2n))


def cPlus(j, m):
    t1 = j - m
    t2 = j + m + 1
    t = t1 * t2
    if(t < 0):
        print('Non-physical solution -> ', t1, t2)
        return -1
    elif (t == 0):
        return 0
    else:
        return np.sqrt(t)


def cMinus(j, m):
    t1 = j + m
    t2 = j - m + 1
    t = t1 * t2
    if(t < 0):
        print('Non-physical solution -> ', t1, t2)
        return -1
    elif (t == 0):
        return 0
    else:
        return np.sqrt(t)


def Delta(a, b):
    if(a == b):
        return 1
    return 0


def Wigner_d(j, beta, m1, m2):
    t0 = np.cos(beta / 2.0) * Delta(m1, m2)
    print(f't0 ---> {t0}')
    t1 = cPlus(j, m2) * Delta(m1, m2 + 1)
    print(f't1 ---> {t1}')
    t2 = cMinus(j, m2) * Delta(m1, m2 - 1)
    print(f't2 ---> {t2}')
    t3 = np.sin(beta / 2.0) * (t1 - t2)
    print(f't3 ---> {t3}')
    t = t0 - t3
    print(f't ---> {t}')
    return t


wd = lambda m1, m2: Wigner_d(0.5, 25.0 * np.pi / 180.0, m1, m2)

# wd(0.5, 0.5)
wd(0.5, -0.5)
# wd(-0.5, 0.5)
# wd(-0.5, -0.5)

# print(wd(0.5, 0.5))
# print(wd(0.5, -0.5))
# print(wd(-0.5, 0.5))
# print(wd(-0.5, -0.5))
