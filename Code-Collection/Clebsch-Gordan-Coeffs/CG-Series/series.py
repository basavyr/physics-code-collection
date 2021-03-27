#!/Users/robertpoenaru/.pyenv/shims/python

import gordan as CGC
import numpy as np

j1 = 1 / 2
j2 = 1 / 2


def makeM(j):
    return np.arange(-j, j + 1, 1)


coeffs = 'coeffs.dat'


def cg_half(m1, m2, m):
    return CGC.N(CGC.CG(j1, m1, j2, m2, 1, m).doit())


def reducedSeries(j1, j2):
    m1Values = makeM(j1)
    m2Values = makeM(j2)
    with open(coeffs, 'w+') as filer:
        for m1P in m1Values:
            for m2P in m2Values:
                for m1 in m1Values:
                    for m2 in m2Values:
                        c1 = f'm1`={m1P} m1={m1}'
                        c2 = f'm2`={m2P} m2={m2}'
                        c3 = c1 + " " + str(cg_half(m1P, m2P, 1))
                        c4 = c2 + " " + str(cg_half(m1, m2, 1))
                        filer.write(str(c3) + '\n' + str(c4) + '\n')


reducedSeries(j1, j2)
