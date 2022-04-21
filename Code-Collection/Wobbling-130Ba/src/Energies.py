import numpy as np
import math

# escape value to be used in case of math failure
MAXVAL = 6969696969


# transform the energy from keV to MeV
def MeV(energy):
    return np.round(energy/1000.0, 3)


def Wobbling_Frequency(I, I1, I2, I3):
    """
    Define the wobbling frequency for the rotor Hamiltonian
    """
    # implement fragmented stopping conditions
    if(I1 < 0.0):
        return MAXVAL
    if(I2 < 0.0):
        return MAXVAL
    if(I3 < 0.0):
        return MAXVAL
    if(I1 == 0):
        return MAXVAL
    if(I2 == 0):
        return MAXVAL
    if(I3 == 0):
        return MAXVAL
    if(I1 == I2):
        return MAXVAL
    if(I1 == I3):
        return MAXVAL
    if(I2 == I3):
        return MAXVAL
    if(I3 >= I2 and I3 <= I1):
        return MAXVAL
    if(I3 <= I2 and I3 >= I1):
        return MAXVAL

    # compute the pure product within the square root of the wobbling frequency
    t_pure = (1.0/(2.0*I1)-1.0/(2.0*I3))*(1.0/(2.0*I2)-1.0/(2.0*I3))
    try:
        t_sqrt = math.sqrt(t_pure)
    except ValueError as err:
        print(I1, I2, I3, err)
        return MAXVAL
    else:
        # return the wobbling frequency if the term under the square root is positive
        omega = 2.0*I*t_sqrt
        return omega


def Absolute_Energy(n, I, I1, I2, I3):
    """
    Absolute energy formula
    """

    omega = Wobbling_Frequency(I, I1, I2, I3)
    energy = 1.0/(2.0*I3)*I*(I+1.0)+(n+0.5)*omega

    return energy
