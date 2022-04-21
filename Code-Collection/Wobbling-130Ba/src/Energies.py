import numpy as np
import math

# escape value to be used in case of math failure
MAXVAL = 6969696969


def MeV(energy):
    """
    Transform the energy from keV to MeV
    """
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


def Excitation_Energy(n, I, I1, I2, I3):
    """
    Define the excitation energy for the triaxial rotator.\n
    The excitation energy is defined as the difference between an energy level and the band head
    """
    # absolute value for the band head
    e0 = Absolute_Energy(0, SPINHEAD, I1, I2, I3)

    # absolute value for the current spin value
    e = Absolute_Energy(n, I, I1, I2, I3)

    return e-e0


def write_energy_to_file():
    """
    Testing function for the numerical values of the Absolute Energy
    """
    omega_file = 'omega_frequencies.dat'
    with open(omega_file, 'w+') as writer:
        writer.writelines("I1 I2 I3 E\n")
        for I1 in np.arange(0, 120, 1):
            for I2 in np.arange(0, 120, 1):
                for I3 in np.arange(0, 120, 1):
                    e = Excitation_Energy(0, 28, I1, I2, I3)
                    if(e is not MAXVAL):
                        writer.writelines(f'{I1} {I2} {I3} {e}\n')
