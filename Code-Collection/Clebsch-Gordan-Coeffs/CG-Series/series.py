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
    CGC_products = []
    Wd_products = []
    OK_Status = 1
    with open(coeffs, 'w+') as filer:
        for m1P in m1Values:
            for m2P in m2Values:
                for m1 in m1Values:
                    for m2 in m2Values:
                        m_index = f'm1`={m1P} m1={m1} ' + f'm2`={m2P} m2={m2}'

                        # compute the two Wigner-d functions within the redcued formula
                        wd1 = WD.Wigner_d(j1, beta, m1P, m1, 0)
                        wd2 = WD.Wigner_d(j2, beta, m2P, m2, 0)
                        Wd_12 = wd1 * wd2
                        if(np.isnan(Wd_12)):
                            filer.writelines(m_index + '\n')
                            filer.writelines('Non-Physical solutions' + '\n')
                            OK_Status = 0
                            return -1

                        # compute the CGC coefficients within the reduced formula
                        CG01 = cg_half(m1, m2)
                        CG02 = cg_half(m1P, m2P)
                        CG_12 = float(CG01 * CG02)
                        if(np.isnan(CG_12)):
                            filer.writelines(m_index + '\n')
                            filer.writelines('Non-Physical solutions' + '\n')
                            OK_Status = 0
                            return -1

                        # results = [m1P, m1, m2P, m2, CG_12 * Wd_12]
                        CGC_products.append(CG_12)
                        Wd_products.append(Wd_12)
    if(OK_Status):
        print('Reduced series computation finished successfully!')
    else:
        print('Computation of the Clebsch-Gordan series failed!')
    return [CGC_products, Wd_products]


CG_Series = reducedSeries(j1, j2)


reduced_sum = 0
for tuple_item in zip(CG_Series[0], CG_Series[1]):
    reduced_sum += tuple_item[0] * tuple_item[1]
print(reduced_sum)