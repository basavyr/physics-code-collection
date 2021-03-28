#!/Users/robertpoenaru/.pyenv/shims/python

import gordan as CGC
import numpy as np

j1 = 1.0 / 2.0
j2 = 1.0 / 2.0


def makeM(j):
    return np.arange(-j, j + 1.0, 1.0)


coeffs = 'coeffs.dat'


# compute the Clebsch-Gordan coefficient for a system with j1=j2=1/2 coupled to a total angular momentum of j=1
def cg_half(m1, m2):
    return CGC.N(CGC.CG(j1, m1, j2, m2, j1 + j2, m1 + m2).doit())


def reducedSeries(j1, j2):
    m1Values = makeM(j1)
    m2Values = makeM(j2)
    with open(coeffs, 'w+') as filer:
        for m1P in m1Values:
            # filer.write('new m1`\n')
            for m2P in m2Values:
                # filer.write('new m2`\n')
                for m1 in m1Values:
                    for m2 in m2Values:
                        c1 = f'm1`={m1P} m1={m1}'
                        c2 = f'm2`={m2P} m2={m2}'
                        CG1 = cg_half(m1P, m2P)
                        CG2 = cg_half(m1, m2)
                        if(CG1 * CG2 != 0):
                            c3 = c1 + " " + str(CG1)
                            c4 = c2 + " " + str(CG2)
                            filer.write(str(c3) + '\n' + str(c4) + '\n')


reducedSeries(j1, j2)
