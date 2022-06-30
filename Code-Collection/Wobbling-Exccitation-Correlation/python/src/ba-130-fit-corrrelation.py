from matplotlib import pyplot as plt
from sre_compile import MAXCODE
import numpy as np
from scipy.optimize import curve_fit


MAX_VAL = 6969696969


def chi_plotter(exp_data, th_data):
    # unpacking
    spins, experimental_energy = exp_data
    _, theoretical_energy = th_data
    plt.plot(spins, exp_data, 'ok', label='Exp.')
    plt.plot(spins, th_data, '--*b', label='Th.')
    plt.legend(loc='best')
    plt.savefig('chi_plot.pdf', dpi=300)
    plt.close()


def Wobbling_Frequency(spin, A1, A2, A3):
    # skip the non-physical solutions
    if(A1 == A3):
        return MAX_VAL
    if(A2 == A3):
        return MAX_VAL
    if(A1 == A2):
        return MAX_VAL
    if(A1 < A3 and A3 < A2):
        return MAX_VAL
    if(A3 < A1 and A2 < A3):
        return MAX_VAL

    I = spin
    t1 = I*(A2+A1-2.0*A3)
    t2 = I*(A2-A1)
    if(t1 < t2):
        return MAX_VAL

    omega = np.sqrt(np.power(t1, 2)-np.power(t2, 2))
    return omega


def Ak(moi):
    return 1.0/(2.0*moi)


ak_values = [Ak(x) for x in np.arange(0.5, 125, 5)]
moi_values = [1.0/(2.0*x) for x in ak_values]


def do_procedure():
    print(ak_values)
    print("*********************")
    print(moi_values)
    plt.plot(ak_values, '-or', label=r'$\mathcal{A}_k$')
    plt.plot(moi_values, '-ob', label=r'$\mathcal{J}_k$')
    plt.legend(loc='best')
    plt.savefig('plotter.pdf', dpi=300)
    plt.close()


if __name__ == '__main__':
    do_procedure()
