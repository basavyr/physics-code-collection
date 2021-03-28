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
                        m_index = f'm1`={m1P} m1={m1} ' + f'm2`={m2P} m2={m2}'
                        CG01 = cg_half(m1P, m2P)
                        CG02 = cg_half(m1, m2)
                        CG = CG01 * CG02
                        coeff_list = str(CG01) + ' ' + \
                            str(CG02) + ' ' + str(CG)
                        if(CG != 0):
                            filer.writelines(m_index + '\n')
                            filer.writelines(coeff_list + '\n')


reducedSeries(j1, j2)
