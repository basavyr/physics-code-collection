import numpy as np

import matplotlib.pyplot as plt

# set of constants (specific to the current implementation)
COEFFS = [120, 40, 60]
SPIN = 35.0 / 2.0
ODD_SPIN = 13.0 / 2.0
THETA = np.pi / 4.0
PHI = np.pi / 4.0


def I_Components(spin, theta, phi):
    """
    For a given spin and polar coordinates, calculate the total angular momentum components for all three quantization cases
    """
    I = spin

    # the list below represents a tuple of the form I=[I1,I2,I3], evaluated for a given spin and polar coordinates using the 1-axis quantization
    One_Axis_Components = [
        I * np.cos(theta), I * np.sin(theta) * np.cos(phi), I * np.sin(theta) * np.sin(phi)]
    # the list below represents a tuple of the form I=[I1,I2,I3], evaluated for a given spin and polar coordinates using the 2-axis quantization
    Two_Axis_Components = [
        I * np.sin(theta) * np.sin(phi), I * np.cos(theta), I * np.sin(theta) * np.cos(phi)]
    # the list below represents a tuple of the form I=[I1,I2,I3], evaluated for a given spin and polar coordinates using the 3-axis quantization
    Three_Axis_Components = [I * np.sin(theta) * np.cos(phi), I * np.sin(theta) * np.sin(phi),
                             I * np.cos(theta)]

    return [One_Axis_Components, Two_Axis_Components, Three_Axis_Components]


def j_Components(oddspin, theta, phi):
    """
    For a given odd-spin and polar coordinates, calculate the odd spin components for all three quantization cases
    """
    j = oddspin

    # the list below represents a tuple of the form j=[j1,j2,j3], evaluated for a given spin and polar coordinates using the 1-axis quantization
    One_Axis_Components = [
        j * np.cos(theta), j * np.sin(theta) * np.cos(phi), j * np.sin(theta) * np.sin(phi)]
    # the list below represents a tuple of the form j=[j1,j2,j3], evaluated for a given spin and polar coordinates using the 2-axis quantization
    Two_Axis_Components = [
        j * np.sin(theta) * np.sin(phi), j * np.cos(theta), j * np.sin(theta) * np.cos(phi)]
    # the list below represents a tuple of the form j=[j1,j2,j3], evaluated for a given spin and polar coordinates using the 3-axis quantization
    Three_Axis_Components = [j * np.sin(theta) * np.cos(phi), j * np.sin(theta) * np.sin(phi),
                             j * np.cos(theta)]

    return [One_Axis_Components, Two_Axis_Components, Three_Axis_Components]


# helper functions that extract the spin components that correspond to a particular axis quantization
I_values_1axis = lambda theta, phi: I_Components(SPIN, theta, phi)[0]
I_values_2axis = lambda theta, phi: I_Components(SPIN, theta, phi)[1]
I_values_3axis = lambda theta, phi: I_Components(SPIN, theta, phi)[2]


# the components of the odd particle angular momentum as function of the CONSTANT set of polar coordinates
j1_const = j_Components(ODD_SPIN, THETA, PHI)[0]
j2_const = j_Components(ODD_SPIN, THETA, PHI)[1]
j3_const = j_Components(ODD_SPIN, THETA, PHI)[2]


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


def Classical_Energy(quantization_axis, theta, phi):
    """
    Mainstream function to evaluate the classical energy in terms of the polar coordinates and the quantization axis
    """
    j_values = j_Components(ODD_SPIN, THETA, PHI)[quantization_axis - 1]
    j1, j3, j3 = j_values
    # <---------- change THETA and PHI if the component does not use the constant parameters defined at the start

    I_values = I_Components(SPIN, theta, phi)[quantization_axis - 1]
    I1, I3, I3 = I_values
    # <---------- change theta and phi if the component does not use the constant parameters defined at the start

    print(j_values)
    print(I_values)


# numerical test
def NumericalTest(thetas, phis):
    for theta in thetas:
        for phi in phis:
            print(theta, phi, Pure_Energy(COEFFS, I_values_1axis(theta, phi), j1_const), Pure_Energy(
                COEFFS, I_values_2axis(theta, phi), j2_const), Pure_Energy(COEFFS, I_values_3axis(theta, phi), j3_const))


PHIS = [-3.14159, -2.14159, -1.14159, -0.141593, 0.858407, 1.85841, 2.85841, -3.14159, -2.14159, -1.14159, -0.141593, 0.858407, 1.85841,
        2.85841, -3.14159, -2.14159, -1.14159, -0.141593, 0.858407, 1.85841, 2.85841, -3.14159, -2.14159, -1.14159, -0.141593, 0.858407, 1.85841, 2.85841]

if __name__ == "__main__":
    # NumericalTest([0, 1, 2, 3], [-3.14159, -2.14159, -1.14159, -0.141593, 0.858407, 1.85841, 2.85841])
    Classical_Energy(1, 1.21, 0.53)
