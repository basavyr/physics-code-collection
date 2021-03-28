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
    re turn mat_n


# define the Pauli matrix for a rotation around the Y-axis
Sigma_Y = [[0, -I], [I, 0]]

for id in range(5):
    print(f'n={id+1}')
    sy_2n = Matrix_Power(Sigma_Y, 2 * id + 1)
    print(np.array(sy_2n))


def cPlus(j, m):
    t1 = j - m
    t2 = j + m + 1
    try:
        t = np.sqrt(t1 * t2)
    except:
        print('Non-physical solutions')
