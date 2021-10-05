import numpy as np

import matplotlib.pyplot as plt


def Pure_Energy(coeff_list, I_values, j_values):
    """
    Uses: 1) a set of three coefficients (*weights*)
          2) the components of the Total Angular Momentum
          3) the components of the Single-Particle Angular Momentum
    """
    sizes = [len(coeff_list), len(I_values), len(j_values)]
    size_check = [l - sizes[0] for l in sizes]

    if(sum(size_check) == 0):
        # print('good')
        pass
    else:
        # print('not good')
        return

    # perform the weightted squared sum of a spin component
    xarg_diff = lambda idx: np.power((I_values[idx] - j_values[idx]), 2)

    # compute each term within the energy function (squared sub of spin components, weighted by the coefficient list)
    pure_energy_terms = [1.0 / coeff_list[idx] * xarg_diff(idx)
                         for idx in range(len(coeff_list))]

    return sum(pure_energy_terms)


COEFFS = [120, 40, 60]
SPIN = 35.0 / 2.0
ODD_SPIN = 13.0 / 2.0


I_Values = [1, 1, 1]
j_Values = [1, 1, 1]

Pure_Energy(COEFFS, I_Values, j_Values)
