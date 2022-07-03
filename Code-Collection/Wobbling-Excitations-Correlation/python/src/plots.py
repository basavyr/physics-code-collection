import matplotlib.pyplot as plt

import fitting
import data130
import correlations


def chi_plotter(exp_data, th_data):
    # unpacking
    spins, experimental_energy = exp_data
    # no need to unpack the spins twice
    _, theoretical_energy = th_data
    plt.plot(spins, experimental_energy, 'ok', label='Exp.')
    plt.plot(spins, theoretical_energy, '--*b', label='Th.')
    plt.legend(loc='best')
    plt.savefig('chi_plot.pdf', dpi=300)
    plt.close()


def main(guess):
    print('Fitting the experimental wobbling energies')
    parameters = fitting.fitting_procedure(guess)
    exp_data = (data130.Spins.band2, data130.Exp_Wobbling_Energy.band1)

    th_data = (data130.Spins.band2,
               correlations.Wobbling_Energy_Theoretical(parameters))

    print(exp_data)
    print('**************')
    print(th_data)
    chi_plotter(exp_data, th_data)


if __name__ == '__main__':
    guess = [0.3, 0.2, 0.1]
    main(guess)
