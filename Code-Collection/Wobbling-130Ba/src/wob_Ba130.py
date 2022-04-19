import numpy as np
from scipy.optimize import curve_fit
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
PHONON_BAND1 = [0 for _ in range(len(SPINS_BAND1))]
PHONON_BAND2 = [1 for _ in range(len(SPINS_BAND2))]


# define the general energy formula
# the Energy depends on two parameters: 3rd MOI and the wobbling frequency
def Energy(n, spin, moi3, omega):
    # calculate the energy term coming from the rotational motion around the 3-axis
    T_rotor = 1.0/(2.0*moi3)*spin*(spin+1.0)

    # calculate the energy coming from the contribution of axes (1,2) as small amplitude oscillations
    T_wobbling = (n+0.5)*omega

    T = T_rotor+T_wobbling

    return T


def modelFunction(data, p1, p2):
    wobbling_phonons, spins = data

    model_energies = Energy(wobbling_phonons, spins, p1, p2)

    return model_energies


data_1 = (np.asarray(PHONON_BAND1), np.asarray(SPINS_BAND1))
data_2 = (np.asarray(PHONON_BAND2), np.asarray(SPINS_BAND2))

# x_1 = modelFunction(data_1, 1, 1)
# x_2 = modelFunction(data_2, 1, 1)

# print(x_1)
# print(x_2)

# initial set of params to be adopted within the fitting procedure
initial_params = [10, 20]
popt, pcov = curve_fit(modelFunction, data_1, ENERGIES_BAND1, initial_params)

print(popt)