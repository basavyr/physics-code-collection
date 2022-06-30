from matplotlib import pyplot as plt
from sre_compile import MAXCODE
import numpy as np
from scipy.optimize import curve_fit


MAX_VAL = 6969696969


def Ak(moi):
    return 1.0/(2.0*moi)


def Ik(inertia_factor):
    return 1.0/(2.0*inertia_factor)


def Physical_Conditions(A1, A2, A3):
    # skip the non-physical solutions
    if(A1 < A3 or A2 < A3):
        return 0
    if(A1 == A3):
        return 0
    if(A2 == A3):
        return 0
    if(A1 == A2):
        return 0
    if(A1 == 0 or A2 == 0 or A3 == 0):
        return 0
    if(A1 < A3 and A3 < A2):
        return 0
    if(A3 < A1 and A2 < A3):
        return 0

    t1 = np.power((A2+A1-2.0*A3), 2)
    t2 = np.power((A2-A1), 2)
    if(t1 < t2):
        return 0

    # return true if the proper conditions for the inertia factors are net
    return 1


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


ak_values = [Ak(x) for x in np.arange(0.5, 125, 1)]


def do_procedure():
    good_I1 = []
    good_I2 = []
    good_I3 = []

    for A1 in ak_values:
        for A2 in ak_values:
            for A3 in ak_values:
                if(Physical_Conditions(A1, A2, A3)):
                    good_I1.append(Ik(A1))
                    good_I2.append(Ik(A2))
                    good_I3.append(Ik(A3))

    plt.plot(good_I1, '-b', label=r'good $\mathcal{J}_1$')
    plt.plot(good_I2, '-r', label=r'good $\mathcal{J}_2$')
    plt.plot(good_I3, '-k', label=r'good $\mathcal{J}_3$')
    plt.legend(loc='best')
    plt.savefig('physical_mois.pdf', dpi=300)
    plt.close()


if __name__ == '__main__':
    do_procedure()
