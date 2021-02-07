#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt


class Quadrupole:
    def __init__(self, rms, A, Z, I, beta, diffuseness, isospin):
        self.a = diffuseness
        self.A = A
        self.Z = Z
        self.beta = beta
        self.I = I
        self.rms = rms
        self.I3 = isospin

    def Show_Data(self):
        print(f'Q_0= {self.Q_0(self.A, self.Z, self.beta)}')
        print(
            f'Q_0_diffused= {Quadrupole.Q_0_deformed(self.A,self.Z,self.a,self.beta,self.I3)}')

    # the effective charges of the nucleons factored in terms of the electric charge e
    e = 1.0
    e_eff_proton = 1.6 * e
    e_eff_neutron = 0.95 * e

    # the radius R_O for a spherical nucleus
    R0 = 1.2

    # the constant that enters in the expression of the intrinsic Q, as a factor which is multiplied to beta-deformation parameter ß
    C_BETA = 0.36

    R = lambda A: Quadrupole.R0 * np.power(A, 1.0 / 3.0)

    # normalize the quadrupole moments
    Q_NORM = 100.0

    def Nucleus(self, A, Z, beta, diffuseness):
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
            return Q_SP / Quadrupole.Q_NORM
        return -1

    @staticmethod
    def Q_0_deformed(A, Z, diffuseness, beta, I3):
        # the quadrupole moment as a function of the quadrupole deformation parameter ß and also parametrized by a correction due to the surface thickness
        # the thickness parameter is called diffuseness constant (denoted by a)

        if(I3 == -0.5):
            e_eff = Quadrupole.e_eff_neutron
        else:
            e_eff = Quadrupole.e_eff_proton

        a = diffuseness
        r = Quadrupole.R(A)
        r2 = np.power(r, 2)
        C = 3.0 / np.sqrt(5.0 * np.pi) * e_eff * Z

        T1 = np.power(np.pi, 2) * np.power(a / r, 2)
        T2 = (2.0 / 7.0) * np.sqrt(5 / np.pi) * beta
        g_beta = beta * (1.0 + T1 + T2)

        # finally calculates the expression of the (intrinsic) quadrupole moment
        Q_0 = C * r2 * g_beta
        return Q_0 / Quadrupole.Q_NORM

    @staticmethod
    def Q_0(A, Z, beta):
        # the intrinsic quadrupole moment induced by a non-spherical charge distribution of the protons inside the nucleus
        # the Q_0 intrinsic quadrupole moment depends on the quadrupole deformation parameter ß
        c = 3.0 / (np.sqrt(5.0 * np.pi)) * Z
        r = Quadrupole.R(A)
        r2 = np.power(r, 2)

        f_beta = beta * (1.0 + Quadrupole.C_BETA * beta)

        # finally calculates the expression of the (intrinsic) quadrupole moment
        q_0 = c * r2 * f_beta
        return q_0 / Quadrupole.Q_NORM

    @staticmethod
    def Q_S(A, Z, beta, I, K):
        # the spectroscopic (measured) quadrupole moment of a deformed nucleus parametrized by the quadrupole deformation paramater beta ß
        # The nucleus' angular momentum is assumed to have a projection onto the symmetry axis that is maximal (namely, K=K_max=I)
        Projection = lambda X, Y: (3 * np.power(X, 2) - Y * (Y + 1.0)) / \
            ((Y + 1.0) * (2.0 * Y + 3.0))

        # firstly evaluated the intrinsic quadrupole moment Q_0
        Q_O = Quadrupole.Q_0(A, Z, beta)

        C = Projection(K, I)

        # evaluates the spectroscopic quadrupole moment
        q_s = C * Q_O
        return q_s


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
