#!/Users/robertpoenaru/.pyenv/shims/python


import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd


class Quadrupole:
    def __init__(self, rms):
        self.rms = rms

    # the effective charges of the nucleons factored in terms of the electric charge e
    e = 1.0
    e_eff_proton = 1.6 * e
    e_eff_neutron = 0.95 * e

    # the radius R_O for a spherical nucleus
    R0 = 1.2

    # the constant that enters in the expression of the intrinsic Q, as a factor which is multiplied to beta-deformation parameter ß
    C_BETA = 0.36

    R = lambda A: Quadrupole.R0 * np.power(A, 1.0 / 3.0)

    def Nucleus(self):
        return f'The root mean square of the charge distribution is: {self.rms}'

    @staticmethod
    def Q_SingleParticle(j_shell, rms, I3):
        j = j_shell
        if(I3 == -0.5):
            return 0
        else:
            e_j = Quadrupole.e_eff_proton
            c_j = (2.0 * j - 1) / (2.0 * j + 2)
            Q_SP = -e_j * c_j * rms
            return Q_SP
        return -1

    @staticmethod
    def Q_deformed(A, Z, diffusion, beta):
        return 2

    @staticmethod
    def Q_0(A, Z, beta):
        # the intrinsic quadrupole moment induced by a non-spherical charge distribution of the protons inside the nucleus
        # the Q_0 intrinsic quadrupole moment depends on the quadrupole deformation parameter ß
        c = 3.0 / (np.sqrt(5.0 * np.pi))
        r = Quadrupole.R(A)
        r2 = np.power(r)
        f_beta = beta * (1.0 + Quadrupole.C_BETA * beta)

        # finally calculates the expression of the (intrinsic) quadrupole moment
        q_0 = c * Z * r2 * f_beta
        return q_0

    @staticmethod
    def Q_S(A, Z, beta, I, K):
        # the spectroscopic (measured) quadrupole moment of a deformed nucleus parametrized by the quadrupole deformation paramater beta ß

        Projection = lambda X: (3 * np.power(X, 2) - I * (I + 1.0)) / \
            ((I + 1.0) * (2.0 * I + 3.0))

        # firstly evaluated the intrinsic quadrupole moment Q_0
        Q_O = Quadrupole.Q_0(A, Z, beta)

        C = Projection(K)

        # evaluates the spectroscopic quadrupole moment
        q_s = C * Q_O
        return q_s


# # the quadrupole moment for a single nucleon in an orbit j=J
# # the quadrupole term contains the rms distribution as a constant function of R
# def Q_j_constR(A, Z, j, particle):
#     e = CHARGE_E
#     e_eff_proton = 1.5 * e
#     e_eff_neutron = 0.95 * e
#     C_j = (2.0 * j - 1) / (2.0 * j + 2.0)
#     rms = RMS_ConstantR(A)
#     if(particle == 'p'):
#         Q_eff = e_eff_proton / e
#     else:
#         Q_eff = e_eff_neutron / e
#     ret_Q_j = -1.0 * C_j * Q_eff * rms
#     return ret_Q_j


# Z = 72
# A = 163

# QUADRUPOLE_CONST = 'quadrupole_j.png'

# js = np.arange(0.5, 10.5, 1)
# Q_js = [Q_j_constR(A, Z, j, 'p') for j in js]
# plt.plot(js, Q_js, '-r', label=r'$Q_j$')
# plt.legend(loc='best')
# plt.savefig(QUADRUPOLE_CONST, dpi=600, bbox_inches='tight')
# plt.close()


# CHARGE_DENSITY = 'charge_density.png'

# rs = np.arange(0, 10, 0.05)
# rhos = [Fermi_Distribution(A, Z, r) for r in rs]
# plt.plot(rs, rhos, '-k', label=r'$\rho_{ch}(r)$')
# plt.legend(loc='best')
# plt.savefig(CHARGE_DENSITY, dpi=600, bbox_inches='tight')
# plt.close()
