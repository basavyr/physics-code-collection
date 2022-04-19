import numpy as np

import plotter


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
PHONON_BAND1 = 0
PHONON_BAND2 = 1

# define the general energy formula
# the Energy depends on two parameters: 3rd MOI and the wobbling frequency


def Energy(n, spin, moi3, omega):
    # calculate the energy term coming from the rotational motion around the 3-axis
    T_rotor = 1.0/(2.0*moi3)*spin*(spin+1.0)

    # calculate the energy coming from the contribution of axes (1,2) as small amplitude oscillations
    T_wobbling = (n+0.5)*omega

    T = T_rotor+T_wobbling

    return T


def E_band1(spin, moi3, omega):
    return Energy(PHONON_BAND1, spin, moi3, omega)


def E_band2(spin, moi3, omega):
    return Energy(PHONON_BAND2, spin, moi3, omega)


def comboModel(comboData, moi3, omega):
    partial_data1 = [E_band1(spin, moi3, omega) for spin in spin_set1]
    partial_data2 = [E_band2(spin, moi3, omega) for spin in spin_set2]

    return np.append(partial_data1, partial_data2)


# return a joint array containing the spins for the two bands
def comboSpins(spin_set1, spin_set2):
    return np.append(spin_set1, spin_set2)


# return a joint array containing the energies for the two bands
def comboEnergies(energy_set1, energy_set2):
    return np.append(energy_set1, energy_set2)


print(comboModel(SPINS_BAND1, SPINS_BAND2, 30, 20))

#183-187Au_Wobbling-Bands/au_187_workflow.py at main · basavyr/183-187Au_Wobbling-Bands
#https://github.com/basavyr/183-187Au_Wobbling-Bands/blob/main/src/python/excitation_energies_fit/au_187_workflow.py
#
#Simultaneously curve fitting for 2 models with shared parameters in R - Cross Validated
#https://stats.stackexchange.com/questions/348765/simultaneously-curve-fitting-for-2-models-with-shared-parameters-in-r
#
#optimization - Fitting two sets of data with two different model functions simultaneously giving a unique optimal parameter - Stack Overflow
#https://stackoverflow.com/questions/51906152/fitting-two-sets-of-data-with-two-different-model-functions-simultaneously-givin
#
#scipy.optimize.curve_fit — SciPy v1.8.0 Manual
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
#
#scipy - Python curve_fit with multiple independent variables - Stack Overflow
#https://stackoverflow.com/questions/28372597/python-curve-fit-with-multiple-independent-variables/28373422