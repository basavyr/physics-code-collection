#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


def A_Factor(MOI):
    return float(1.0 / (2.0 * MOI))


def B_Term(I, J, I1, I2, I3, V, GAMMA):
    A1 = A_Factor(I1)
    A2 = A_Factor(I2)
    A3 = A_Factor(I3)
    SING = np.sin(GAMMA)
    COSG = np.cos(GAMMA)
    JJ1 = (2.0 * J - 1.0) / (J * (J + 1.0))
    CGAMMA1 = np.sqrt(3.0) * (np.sqrt(3.0 * COSG + SING))
    CGAMMA2 = 2.0 * np.sqrt(3.0) * SING
    T1 = (2.0 * I - 1.0) * (A3 - A1) + 2.0 * J * A1
    T2 = (2.0 * I - 1.0) * (A2 - A1) + 2.0 * J * A1
    T3 = (2.0 * J - 1.0) * (A3 - A1) * 2.0 * I * A1 + V * JJ1 * CGAMMA1
    T4 = (2.0 * J - 1.0) * (A2 - A1) + 2.0 * I * A1 + V * JJ1 * CGAMMA2
    B_Sides = -1.0 * (T1 * T2 + 8.0 * A2 * A3 * I * J + T3 * T4)
    return B_Sides


def C_Term(I, J, I1, I2, I3, V, GAMMA):
    A1 = A_Factor(I1)
    A2 = A_Factor(I2)
    A3 = A_Factor(I3)
    SING = np.sin(GAMMA)
    COSG = np.cos(GAMMA)
    JJ1 = (2.0 * J - 1.0) / (J * (J + 1.0))
    CGAMMA1 = np.sqrt(3.0) * (np.sqrt(3.0 * COSG + SING))
    CGAMMA2 = 2.0 * np.sqrt(3.0) * SING
    T1 = (2.0 * I - 1.0) * (A3 - A1) + 2.0 * J * A1
    T2 = (2.0 * J - 1.0) * (A3 - A1) + 2.0 * I * A1 + V * JJ1 * CGAMMA1
    T3 = (2.0 * I - 1.0) * (A2 - A1) + 2.0 * J * A1
    T4 = (2.0 * J - 1.0) * (A2 - A1) + 2.0 * I * A1 + V * JJ1 * CGAMMA2
    T01 = T1 * T2 - 4.0 * I * J * A3 * A3
    T02 = T3 * T4 - 4.0 * I * J * A3 * A2
    C_Sides = T01 * T02
    return C_Sides


def Omega(I, J, I1, I2, I3, V, GAMMA):
    b = B_Term(I, J, I1, I2, I3, V, GAMMA)
    c = C_Term(I, J, I1, I2, I3, V, GAMMA)
    x1 = np.sqrt(0.5 * (-b - np.sqrt(b * b - 4.0 * c)))
    x2 = np.sqrt(0.5 * (-b + np.sqrt(b * b - 4.0 * c)))
    wobbling_freq = [x1, x2]
    return wobbling_freq


I1 = 72
I2 = 15
I3 = 7
GAMMA = 22 * np.pi / 180.0
V = 2.1
J = 6.5

spins = np.arange(6.5, 52.5, 2.0)

omega1 = [Omega(X, J, I1, I2, I3, V, GAMMA)[0] for X in spins]
omega2 = [Omega(X, J, I1, I2, I3, V, GAMMA)[1] for X in spins]

plt.rcParams.update({'font.size': 15})
# plt.rcParams["font.family"] = "Times New Roman"

rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=True)

plt.plot(spins, omega1, '-^r', label=r'$\Omega_1^I$')
plt.plot(spins, omega2, '-sb', label=r'$\Omega_2^I$')
plt.xlabel(r'$I\ [\hbar]$')
plt.ylabel(r'$\Omega^I\ [MeV]$')
plt.legend(loc='best')
# plt.legend(loc='center left', bbox_to_anchor=(0.07, 0.3))

plt.savefig('wobbling-frequencies.pdf', dpi=600, bbox_inches='tight')
plt.close()
