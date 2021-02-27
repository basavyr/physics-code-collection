#! /Users/robertpoenaru/.pyenv/shims/python

import numpy as np
from numpy import linalg as LA

import matplotlib.pyplot as plt


def makeMatrix(param):
    M = np.array(([0, 1, 0], [1, 0, 1], [0, 1, 0]))
    return M * param


# study the evolution in magnitude of the i-th eigenvalue of the matrix M(a)
# for a given interval of a [a_left,a_right]
def LambdaEvolution(lambda_id, a_left, a_right):
    STEP = 0.1
    params = np.arange(a_left, a_right + STEP, STEP)
    values = []
    for p in params:
        m_p = makeMatrix(p)
        eig_vals = np.sort(LA.eig(m_p)[0])
        val_0 = eig_vals[lambda_id]
        if(np.isnan(val_0)):
            pass
        else:
            values.append(val_0)

    if(len(values) == len(params)):
        return [params, values, np.abs(values)]
    return [[6969], [6969], [6969]]


def PlotLambdaEvolution(ID, plotname):
    params, vminus, vplus = LambdaEvolution(ID, 0.69, 2.69)

    plt.plot(params, vminus, 'o-r', label=r'$\lambda$_')
    plt.plot(params, vplus, 'o-b', label=r'$\lambda_+$')
    plt.legend(loc='best')
    plt.xlabel(f'a')

    plt.ylabel(r'$\lambda$' + f'{ID}')
    plt.savefig(f'{plotname}.png', dpi=1200, bbox_inches='tight')
    plt.close()


PlotLambdaEvolution(0, 'lambda_0')
PlotLambdaEvolution(1, 'lambda_1')
PlotLambdaEvolution(2, 'lambda_2')


# M = makeMatrix(2)

# VALUES, VECTORS = LA.eig(M)

# vecs = [[np.round(comp, 2) for comp in vec] for vec in VECTORS]
# vals = [np.round(value, 2) for value in VALUES]
# print(vals)
# print(vecs)
