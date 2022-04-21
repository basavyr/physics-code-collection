import numpy as np
import math
from scipy.optimize import curve_fit

# paths at which fitting data will be saved
BAND_1_PATH = "/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/ba_130_B1_band.dat"
BAND_2_PATH = "/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/ba_130_B2_band.dat"
FITTING_PARAMS_PATH = "/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/fit_params.dat"


# raw experimental data
SPINS_BAND1 = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
SPINS_BAND2 = [11, 13, 15, 17, 19, 21, 23, 25]
ENERGIES1 = [3790.3, 4256.3, 4884.2, 5678.3,
             6563.3, 7524.3, 8574.3, 9690.3, 10821.3, 11984.3]
ENERGIES2 = [4456.2, 4986.2, 5647.2,
             6442.2, 7319.3, 8265.3, 9283.3, 10436.3]
ENERGIES_BAND1 = list(map(MeV, ENERGIES1))
ENERGIES_BAND2 = list(map(MeV, ENERGIES2))
BAND_HEAD = ENERGIES_BAND1[0]
SPIN_HEAD = SPINS_BAND1[0]
PHONON_BAND1 = [0 for _ in range(len(SPINS_BAND1))]
PHONON_BAND2 = [1 for _ in range(len(SPINS_BAND2))]


# generate excitation energies from the absolute values
EXC_ENERGY1 = [e-BAND_HEAD for e in ENERGIES_BAND1[1:]]
EXC_ENERGY2 = [e-BAND_HEAD for e in ENERGIES_BAND2]
SPINS_BAND1 = SPINS_BAND1[1:]
PHONON_BAND1 = PHONON_BAND1[1:]


# create joint data-sets
spins = np.asarray(SPINS_BAND1+SPINS_BAND2)
phonons = np.asarray(PHONON_BAND1+PHONON_BAND2)
experimental_energies = EXC_ENERGY1+EXC_ENERGY2


# create a function which evaluates the excitation energy for a triaxial rotor
def model_energy(x_data, I1, I2, I3):
    """
    The model energy is capable of dealing with numpy arrays within the x_data tuple
    """
    phonons, spins = x_data
    local_energy = exc_energy(phonons, spins, I1, I2, I3)

    contains_bad_values = any(x == MAXVAL for x in local_energy)
    if(contains_bad_values):
        print('not good')
        return

    return local_energy


def write_energy_to_file():
    omega_file = 'omega_frequencies.dat'
    with open(omega_file, 'w+') as writer:
        writer.writelines("I1 I2 I3 E\n")
        for I1 in np.arange(0, 120, 1):
            for I2 in np.arange(0, 120, 1):
                for I3 in np.arange(0, 120, 1):
                    e = exc_energy(0, 28, I1, I2, I3)
                    if(e is not MAXVAL):
                        writer.writelines(f'{I1} {I2} {I3} {e}\n')


# create a tuple for the x-data which will be used within the model fit
x_data = (phonons, spins)
PARAMS_BOUNDS = ([0.5, 0.5, 0.5], [120, 120, 120])


############################################################
############################################################
################### FITTING PROCEDURE ######################
############################################################
############################################################
p0 = [10, 1, 3]
fit_parameters, _ = curve_fit(model_energy, x_data, experimental_energies,
                              p0, bounds=PARAMS_BOUNDS)
############################################################
############################################################
################### FITTING PROCEDURE ######################
############################################################
############################################################


##############################################################################
# generate the theoretical values for the energies from the fitting parameters
##############################################################################
theoretical_data_1 = [exc_energy(
    0, SPINS_BAND1[idx], fit_parameters[0], fit_parameters[1], fit_parameters[2]) for idx in range(len(SPINS_BAND1))]
theoretical_data_2 = [exc_energy(
    1, SPINS_BAND2[idx], fit_parameters[0], fit_parameters[1], fit_parameters[2]) for idx in range(len(SPINS_BAND2))]
##############################################################################
##############################################################################


# print the parameters to console
def print_params(params):
    print(params[0], params[1], params[2])


# write parameters to file
def write_params(params):
    with open(FITTING_PARAMS_PATH, 'w+') as writer:
        writer.write(str(params[0]))
        writer.write("\n")
        writer.write(str(params[1]))
        writer.write("\n")
        writer.write(str(params[2]))
        writer.write("\n")


with open(BAND_1_PATH, 'w+') as writer:
    for idx in range(len(SPINS_BAND1)):
        data_line = f'{SPINS_BAND1[idx]} {EXC_ENERGY1[idx]} {theoretical_data_1[idx]}'
        writer.write(data_line)
        writer.write("\n")


with open(BAND_2_PATH, 'w+') as writer:
    for idx in range(len(SPINS_BAND2)):
        data_line = f'{SPINS_BAND2[idx]} {EXC_ENERGY2[idx]} {theoretical_data_2[idx]}'
        writer.write(data_line)
        writer.write("\n")
