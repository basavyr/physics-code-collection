from ast import BitAnd
import numpy as np
from scipy.optimize import curve_fit
import plotter


MAXVAL = 696969696969


def MeV(energy):
    return np.round(energy/1000.0, 3)


SPINS_BAND1 = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
SPINS_BAND2 = [11, 13, 15, 17, 19, 21, 23, 25]
ENERGIES1 = [3790.3, 4256.3, 4884.2, 5678.3,
             6563.3, 7524.3, 8574.3, 9690.3, 10821.3, 11984.3]
ENERGIES2 = [4456.2, 4986.2, 5647.2,
             6442.2, 7319.3, 8265.3, 9283.3, 10436.3]
ENERGIES_BAND1 = list(map(MeV, ENERGIES1))
ENERGIES_BAND2 = list(map(MeV, ENERGIES2))
PHONON_BAND1 = [0 for _ in range(len(SPINS_BAND1))]
PHONON_BAND2 = [1 for _ in range(len(SPINS_BAND2))]


# define the general energy formula
# the Energy depends on two parameters: 3rd MOI and the wobbling frequency
def Energy(n, spin, I1, I2, I3):
    I1 = np.round(I1, 3)
    I2 = np.round(I2, 3)
    I3 = np.round(I3, 3)
    if(I1 == I2 or I1 == I3 or I3 == I2):
        return MAXVAL
    if(I1 <= 0.0 or I2 <= 0.0 or I3 <= 0.0):
        return MAXVAL
    if(I3 < I1 and I3 > I2):
        return MAXVAL
    if(I3 > I1 and I3 < I2):
        return MAXVAL

    # calculate the energy term coming from the rotational motion around the 3-axis
    T_rotor = 1/(2.0*I3)*spin*(spin+1.0)

    # calculate the energy coming from the contribution of axes (1,2) as small amplitude oscillations
    T_wobbling = 2*spin*np.sqrt((1/(2.0*I1)-1/(2.0*I3))
                                * (1/(2.0*I2)-1/(2.0*I3)))*(n+0.5)

    T = T_rotor+T_wobbling

    return T


# define the general energy formula using generalized MOI I_i=theta_I(1+cI)
# the Energy depends on two parameters: 3rd MOI and the wobbling frequency
def Energy(n, spin, c, theta1, theta2, theta3):
    I1 = theta1*(1+c*spin)
    I2 = theta2*(1+c*spin)
    I3 = theta3*(1+c*spin)
    I1 = np.round(I1, 4)
    I2 = np.round(I2, 4)
    I3 = np.round(I3, 4)
    # if(I1 == I2 or I1 == I3 or I3 == I2):
    #     return MAXVAL
    # if(I1 <= 0.0 or I2 <= 0.0 or I3 <= 0.0):
    #     return MAXVAL
    # if(I3 < I1 and I3 > I2):
    #     return MAXVAL
    # if(I3 > I1 and I3 < I2):
    #     return MAXVAL

    # calculate the energy term coming from the rotational motion around the 3-axis
    T_rotor = 1/(2.0*I3)*spin*(spin+1.0)

    # calculate the energy coming from the contribution of axes (1,2) as small amplitude oscillations
    T_wobbling = 2*spin*np.sqrt((1/(2.0*I1)-1/(2.0*I3))
                                * (1/(2.0*I2)-1/(2.0*I3)))*(n+0.5)

    T = T_rotor+T_wobbling

    return T


# update the model to include 4 parameters: c, theta_{1,2,3}
def modelFunction(data, p0, p1, p2, p3):
    wobbling_phonons, spins = data

    model_energies = Energy(wobbling_phonons, spins, p0, p1, p2, p3)

    return model_energies


# create a fitting procedure only for the first wobbling band
def fit_band_1():
    data_1 = (np.asarray(PHONON_BAND1), np.asarray(SPINS_BAND1))

    # initial set of params to be adopted within the fitting procedure
    initial_params = [0.5, 1, 5, 20]

    popt, pcov = curve_fit(modelFunction, data_1,
                           ENERGIES_BAND1, initial_params)
    print(popt)


# create a fitting procedure only for the second wobbling band
def fit_band_2():
    data_2 = (np.asarray(PHONON_BAND2), np.asarray(SPINS_BAND2))

    # initial set of params to be adopted within the fitting procedure
    initial_params = [10, 20]

    popt, pcov = curve_fit(modelFunction, data_2,
                           ENERGIES_BAND1, initial_params)
    print(popt)


def fit_full_bands():
    # create joint data sets
    spins = np.asarray(SPINS_BAND1+SPINS_BAND2)
    phonons = np.asarray(PHONON_BAND1+PHONON_BAND2)

    # keep the energies in the same form
    energies = ENERGIES_BAND1+ENERGIES_BAND2

    normalize = False
    # use normalized data
    if normalize == True:
        band_head = energies[0]
        energies = [e-band_head for e in energies]
        energies = energies[1:]
        spins = spins[1:]
        phonons = phonons[1:]

    initial_params = [0.5, 1, 5, 12]
    popt, pcov = curve_fit(
        modelFunction, (spins, phonons), energies, initial_params)

    return popt


FIT = fit_band_1()
print(FIT)
