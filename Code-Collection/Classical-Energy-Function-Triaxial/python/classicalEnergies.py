import numpy as np

import matplotlib.pyplot as plt


def I_Components(spin, theta, phi):
    """
    For a given spin and polar coordinates, calculate the total angular momentum components for all three quantization cases
    """
    I = spin

    One_Axis_Components = [
        I * np.cos(theta), I * np.sin(theta) * np.cos(phi), I * np.sin(theta) * np.sin(phi)]
    Two_Axis_Components = [
        I * np.sin(theta) * np.sin(phi), I * np.cos(theta), I * np.sin(theta) * np.cos(phi)]
    Three_Axis_Components = [I * np.sin(theta) * np.cos(phi), I * np.sin(theta) * np.sin(phi),
                             I * np.cos(theta)]

    return [One_Axis_Components, Two_Axis_Components, Three_Axis_Components]


def j_Components(oddspin, theta, phi):
    """
    For a given odd-spin and polar coordinates, calculate the odd spin components for all three quantization cases
    """
    j = oddspin

    One_Axis_Components = [
        j * np.cos(theta), j * np.sin(theta) * np.cos(phi), j * np.sin(theta) * np.sin(phi)]
    Two_Axis_Components = [
        j * np.sin(theta) * np.sin(phi), j * np.cos(theta), j * np.sin(theta) * np.cos(phi)]
    Three_Axis_Components = [j * np.sin(theta) * np.cos(phi), j * np.sin(theta) * np.sin(phi),
                             j * np.cos(theta)]

    return [One_Axis_Components, Two_Axis_Components, Three_Axis_Components]


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
THETA = np.pi / 4.0
PHI = np.pi / 4.0

j_Values_1axis = j_Components(ODD_SPIN, THETA, PHI)[0]
j_Values_2axis = j_Components(ODD_SPIN, THETA, PHI)[1]
j_Values_3axis = j_Components(ODD_SPIN, THETA, PHI)[2]

I_values_1axis = lambda theta, phi: I_Components(SPIN, theta, phi)[0]
I_values_2axis = lambda theta, phi: I_Components(SPIN, theta, phi)[1]
I_values_3axis = lambda theta, phi: I_Components(SPIN, theta, phi)[2]


# numerical test
def NumericalTest(thetas, phis):
    for theta in thetas:
        for phi in phis:
            print(theta, phi, Pure_Energy(COEFFS, I_values_1axis(theta, phi), j_Values_1axis), Pure_Energy(
                COEFFS, I_values_2axis(theta, phi), j_Values_2axis), Pure_Energy(COEFFS, I_values_3axis(theta, phi), j_Values_3axis))


PHIS = [-3.14159, -2.14159, -1.14159, -0.141593, 0.858407, 1.85841, 2.85841, -3.14159, -2.14159, -1.14159, -0.141593, 0.858407, 1.85841,
        2.85841, -3.14159, -2.14159, -1.14159, -0.141593, 0.858407, 1.85841, 2.85841, -3.14159, -2.14159, -1.14159, -0.141593, 0.858407, 1.85841, 2.85841]

NumericalTest([0, 1, 2, 3], [-3.14159, -2.14159, -1.14159, -
                             0.141593, 0.858407, 1.85841, 2.85841])
