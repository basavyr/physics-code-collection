import numpy as np
from scipy.optimize import curve_fit

import Energies

# paths at which fitting data will be saved
BAND_1_PATH = "/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/ba_130_B1_band.dat"
BAND_2_PATH = "/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/ba_130_B2_band.dat"
FITTING_PARAMS_PATH = "/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/fit_params.dat"


# create joint data-sets
spins = np.asarray(Energies.SPINS_BAND1+Energies.SPINS_BAND2)
phonons = np.asarray(Energies.PHONON_BAND1+Energies.PHONON_BAND2)
experimental_energies = Energies.BAND1_EXP+Energies.BAND2_EXP
x_data = (phonons, spins)


# create a function which evaluates the excitation energy for a triaxial rotor
def model_energy(x_data, I1, I2, I3):
    """
    The model energy is capable of dealing with numpy arrays within the x_data tuple
    """
    phonons, spins = x_data
    local_energy = Energies.Excitation_Energy(phonons, spins, I1, I2, I3)

    return local_energy


############################################################
############################################################
################### FITTING PROCEDURE ######################
############################################################
############################################################
# initial guess for the parameter set
p0 = [10, 1, 3]
bounds = ([0.5, 0.5, 0.5], [120, 120, 120])
fit_parameters, _ = curve_fit(model_energy, x_data, experimental_energies,
                              p0, bounds=bounds)
############################################################
############################################################
################### FITTING PROCEDURE ######################
############################################################
############################################################


##############################################################################
# generate the theoretical values for the energies from the fitting parameters
##############################################################################
Band1_Th = [Energies.Excitation_Energy(
    0, Energies.SPINS_BAND1[idx], fit_parameters[0], fit_parameters[1], fit_parameters[2]) for idx in range(len(Energies.SPINS_BAND1))]
Band2_Th = [Energies.Excitation_Energy(
    1, Energies.SPINS_BAND2[idx], fit_parameters[0], fit_parameters[1], fit_parameters[2]) for idx in range(len(Energies.SPINS_BAND2))]
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


# save the energies for band 1 to a file
with open(BAND_1_PATH, 'w+') as writer:
    for idx in range(len(Energies.SPINS_BAND1)):
        data_line = f'{Energies.SPINS_BAND1[idx]} {Energies.BAND1_EXP[idx]} {Band1_Th[idx]}'
        writer.write(data_line)
        writer.write("\n")


# save the energies for band 2 to a file
with open(BAND_2_PATH, 'w+') as writer:
    for idx in range(len(Energies.SPINS_BAND2)):
        data_line = f'{Energies.SPINS_BAND2[idx]} {Energies.BAND2_EXP[idx]} {Band2_Th[idx]}'
        writer.write(data_line)
        writer.write("\n")


def generate_latex_table(params):
    """
    Generate a latex table from the parameter set
    """

    table1 = """
                \\begin{table}
                \\centering
                \\resizebox{0.5\\textwidth}{!}{%
                \\begin{tabular}{|c|c|c|l|}
                \hline
                $\mathcal{I}_1$ & $\mathcal{I}_3$ & $\mathcal{I}_2$ & Unit \\\\ \hline
            """
    table0 = f'{int(params[0])} &{int(params[1])} &{int(params[2])} &' + "$\hbar ^ 2\\text{MeV} ^ {-1}$ \\\\ \hline"
    table2 = """
                \end{tabular}%
                }
                \caption{Table.}
                    \label{table-params-ba130}
                \end{table}
            """
    latex = table1+'\n'+table0+'\n'+table2
    print(table0)


write_params(fit_parameters)
# print_params(fit_parameters)
generate_latex_table(fit_parameters)
