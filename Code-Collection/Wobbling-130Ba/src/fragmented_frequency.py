import numpy as np
import math
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
# escape value to be used in case of math failure
MAXVAL = 6969696969


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
bandhead = ENERGIES_BAND1[0]
spinhead = SPINS_BAND1[0]
PHONON_BAND1 = [0 for _ in range(len(SPINS_BAND1))]
PHONON_BAND2 = [1 for _ in range(len(SPINS_BAND2))]


# generate excitation energies from the absolute values
EXC_ENERGY1 = [e-bandhead for e in ENERGIES_BAND1[1:]]
EXC_ENERGY2 = [e-bandhead for e in ENERGIES_BAND2]
SPINS_BAND1 = SPINS_BAND1[1:]
PHONON_BAND1 = PHONON_BAND1[1:]


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
    e0 = energy(0, spinhead, I1, I2, I3)
    # if(e0 == MAXVAL):
    #     return MAXVAL
    e = energy(n, I, I1, I2, I3)
    # if(e == MAXVAL):
    #     return MAXVAL

    return e-e0


def model_energy(xdata, I1, I2, I3):
    phonons, spins = xdata

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


# write_energy_to_file()

spins = np.asarray(SPINS_BAND1+SPINS_BAND2)
phonons = np.asarray(PHONON_BAND1+PHONON_BAND2)
energies = EXC_ENERGY1+EXC_ENERGY2
xdata = (phonons, spins)
PARAMS_BOUNDS = ([0.5, 0.5, 0.5], [120, 120, 120])


p0 = [10, 1, 3]

popt, pcov = curve_fit(model_energy, xdata, energies,
                       p0, bounds=PARAMS_BOUNDS)

print(popt[0], popt[1], popt[2])

theoretical_data_1 = [exc_energy(
    0, SPINS_BAND1[idx], popt[0], popt[1], popt[2]) for idx in range(len(SPINS_BAND1))]
theoretical_data_2 = [exc_energy(
    1, SPINS_BAND2[idx], popt[0], popt[1], popt[2]) for idx in range(len(SPINS_BAND2))]


plt.plot(SPINS_BAND1, EXC_ENERGY1, 'ok', label='band1 exp')
plt.plot(SPINS_BAND1, theoretical_data_1, '-k', label='band1 th')
plt.plot(SPINS_BAND2, EXC_ENERGY2, 'or', label='band2 exp')
plt.plot(SPINS_BAND2, theoretical_data_2, '-r', label='band2 th')
plt.legend(loc='best')
plt.xlabel('I')
plt.ylabel('E')
plt.savefig('wobbling_results.pdf', dpi=300, bbox_inches='tight')
plt.close()
