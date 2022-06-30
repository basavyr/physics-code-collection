from matplotlib import pyplot as plt
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

    # return true if the proper conditions for the inertia factors are net
    return 1


def chi_plotter(exp_data, th_data):
    # unpacking
    spins, experimental_energy = exp_data
    # no need to unpack the spins twice
    _, theoretical_energy = th_data
    plt.plot(spins, exp_data, 'ok', label='Exp.')
    plt.plot(spins, th_data, '--*b', label='Th.')
    plt.legend(loc='best')
    plt.savefig('chi_plot.pdf', dpi=300)
    plt.close()


def Wobbling_Frequency(I, A1, A2, A3):

    # skip the non-physical solutions
    if(Physical_Conditions(A1, A2, A3)):
        t1 = np.power((A2+A1-2.0*A3), 2)
        t2 = np.power((A2-A1), 2)
        if(t1 < t2):
            return 0

        omega = 2.0*I*np.sqrt(np.power(t1, 2)-np.power(t2, 2))
        return omega

    # if the MOI give un-physical solutions return MAX_VAL
    return MAX_VAL


def Energy(I, n, A1, A2, A3):
    """
    - computes the pure rotational energy within the Harmonic Approximation
    - uses the maximal MOI (smallest inertia factor) the one for the **3**-axis
    """
    if(Physical_Conditions(A1, A2, A3)):
        rotational_term = A3*I*(I+1)
        harmonic_term = Wobbling_Frequency(I, A1, A2, A3)*(n+0.5)
        energy = rotational_term+harmonic_term
        return energy

    return MAX_VAL


def Excitation_Energy(I, I0, A1, A2, A3):
    E0 = Energy(I0, 0, A1, A2, A3)

    E = Energy(I, n, A1, A2, A3)

    return E-E0


def Wobbling_Energy(I, n, A1, A2, A3):
    if(I % 2 != 0):
        wobbling = Energy(I, n, A1, A2, A3)-0.5*(
            Energy(I-1, 0, A1, A2, A3)+Energy(I+1, 0, A1, A2, A3))
    else:
        wobbling = Energy(I, n, A1, A2, A3)-Energy(I, 0, A1, A2, A3)

    return wobbling


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
