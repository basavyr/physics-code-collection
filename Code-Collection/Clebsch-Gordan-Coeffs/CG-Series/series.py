#!/Users/robertpoenaru/.pyenv/shims/python

import gordan as CGC
import numpy as np
import wignerD as WD


j1 = 1.0 / 2.0
j2 = 1.0 / 2.0


def makeM(j):
    return np.arange(j, -(j + 1.0), -1.0)


coeffs = 'coeffs.dat'


# compute the Clebsch-Gordan coefficient for a system with j1=j2=1/2 coupled to a total angular momentum of j=1
def cg_half(m1, m2):
    return CGC.N(CGC.CG(j1, m1, j2, m2, j1 + j2, m1 + m2).doit())


def reducedSeries(j1, j2):
    m1Values = makeM(j1)
    m2Values = makeM(j2)
    beta = 25 * np.pi / 180.0
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
                        wd1 = WD.Wigner_d(j1, beta, m1P, m1)
                        wd2 = WD.Wigner_d(j2, beta, m2P, m2)
                        WD_12 = wd1 * wd2
                        coeff_list = str(CG01) + ' ' + str(CG02) + \
                            ' ' + str(CG) + ' ' + str(WD_12)
                        if(np.isnan(WD_12)):
                            filer.writelines(m_index + '\n')
                            filer.writelines('Non-Physical solutions' + '\n')
                            return -1
                        results = [m1P, m2P, m1, m2, CG01, CG02, wd1, wd2]
                        if(CG != 0):
                            filer.writelines(m_index + '\n')
                            filer.writelines(str(results) + '\n')


reducedSeries(j1, j2)
