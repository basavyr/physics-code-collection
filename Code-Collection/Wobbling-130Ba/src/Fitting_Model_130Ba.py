import numpy as np
import math
from scipy.optimize import curve_fit

# paths at which fitting data will be saved
BAND_1_PATH = "/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/ba_130_B1_band.dat"
BAND_2_PATH = "/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/ba_130_B2_band.dat"
FITTING_PARAMS_PATH = "/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/fit_params.dat"


# escape value to be used in case of math failure
MAXVAL = 6969696969


# transform the energy from keV to MeV
def MeV(energy):
    return np.round(energy/1000.0, 3)


# raw experimental data
SPINS_BAND1 = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
SPINS_BAND2 = [11, 13, 15, 17, 19, 21, 23, 25]
ENERGIES1 = [3790.3, 4256.3, 4884.2, 5678.3,
             6563.3, 7524.3, 8574.3, 9690.3, 10821.3, 11984.3]
ENERGIES2 = [4456.2, 4986.2, 5647.2,
             6442.2, 7319.3, 8265.3, 9283.3, 10436.3]
ENERGIES_BAND1 = list(map(MeV, ENERGIES1))
ENERGIES_BAND2 = list(map(MeV, ENERGIES2))
BANDHEAD = ENERGIES_BAND1[0]
SPINHEAD = SPINS_BAND1[0]
PHONON_BAND1 = [0 for _ in range(len(SPINS_BAND1))]
PHONON_BAND2 = [1 for _ in range(len(SPINS_BAND2))]


# generate excitation energies from the absolute values
EXC_ENERGY1 = [e-BANDHEAD for e in ENERGIES_BAND1[1:]]
EXC_ENERGY2 = [e-BANDHEAD for e in ENERGIES_BAND2]
SPINS_BAND1 = SPINS_BAND1[1:]
PHONON_BAND1 = PHONON_BAND1[1:]


# create joint data-sets
spins = np.asarray(SPINS_BAND1+SPINS_BAND2)
phonons = np.asarray(PHONON_BAND1+PHONON_BAND2)
experimental_energies = EXC_ENERGY1+EXC_ENERGY2


# define a fragmented wobbling frequency for the rotor Hamiltonian
def omega(I, I1, I2, I3):
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
        omega_res = 2.0*I*t_sqrt
        return omega_res


# define the absolute energy formula
def energy(n, I, I1, I2, I3):
    homega = omega(I, I1, I2, I3)
    # if (homega == MAXVAL):
    #     return MAXVAL
    e = 1.0/(2.0*I3)*I*(I+1.0)+(n+0.5)*homega
    # if (e == MAXVAL):
    #     return MAXVAL

    return e


# define the excitation energy for the triaxial rotator
def exc_energy(n, I, I1, I2, I3):
    e0 = energy(0, SPINHEAD, I1, I2, I3)
    # if(e0 == MAXVAL):
    #     return MAXVAL
    e = energy(n, I, I1, I2, I3)
    # if(e == MAXVAL):
    #     return MAXVAL

    return e-e0


def model_energy(x_data, I1, I2, I3):
    phonons, spins = x_data
    local_energy = exc_energy(phonons, spins, I1, I2, I3)

    # if(local_energy == MAXVAL):
    #     return MAXVAL

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
popt, pcov = curve_fit(model_energy, x_data, experimental_energies,
                       p0, bounds=PARAMS_BOUNDS)
############################################################
############################################################
################### FITTING PROCEDURE ######################
############################################################
############################################################


# generate the theoretical values for the energies from the fitting parameters
theoretical_data_1 = [exc_energy(
    0, SPINS_BAND1[idx], popt[0], popt[1], popt[2]) for idx in range(len(SPINS_BAND1))]
theoretical_data_2 = [exc_energy(
    1, SPINS_BAND2[idx], popt[0], popt[1], popt[2]) for idx in range(len(SPINS_BAND2))]


# print the parameters to console
def prin_params(params):
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
