import numpy as np
from scipy.optimize import curve_fit

import data130
import correlations as model


def model_energy(x_data, A1, A2, A3):
    """
    The model energy is capable of dealing with numpy arrays within the x_data tuple
    """
    spins, phonons = x_data
    local_energy = model.Wobbling_Energy(spins, phonons, A1, A2, A3)

    return local_energy


def fitting_procedure(guess):
    # x_data = (np.concatenate((data130.Spins.band1[1:], data130.Spins.band2)), np.concatenate(
    #     (data130.Phonon_Number.band1[1:], data130.Phonon_Number.band2)))
    x_data = (data130.Spins.band2, data130.Phonon_Number.band2)
    y_data = data130.Exp_Wobbling_Energy.band1
    bounds = ([1.0/(2.0*120), 1.0/(2.0*120), 1.0/(2.0*120)],
              [1.0/(2.0*0.5), 1.0/(2.0*0.5), 1.0/(2.0*0.5)])

    ########
    ##actual fitting procedure##
    ########
    fit_parameters, _ = curve_fit(
        model_energy, x_data, y_data, p0=guess, bounds=bounds)
    ########
    ########

    ret_val = (fit_parameters[0], fit_parameters[1], fit_parameters[2])

    print(model.Ik(fit_parameters[0]))
    print(model.Ik(fit_parameters[1]))
    print(model.Ik(fit_parameters[2]))

    return ret_val


def main():
    fitting_procedure()


if __name__ == '__main__':
    main()
