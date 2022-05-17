###################################################################################################
###################################################################################################
# evaluate the canonical factors that arise in the expression of the classical energy function (CEF)
###################################################################################################
###################################################################################################

import numpy as np


class Canonical:
    """
    - collection of methods that correspond to each of the four canonical terms within the CEF
    """

    @staticmethod
    def rad(angle):
        return angle*np.pi/180.0

    @staticmethod
    def A_varphi(inertia_factors, varphi):
        A1 = inertia_factors[0]
        A2 = inertia_factors[1]
        A3 = inertia_factors[2]

        A = A1*np.power(np.cos(Canonical.rad(varphi)), 2)+A2 * \
            np.power(np.sin(Canonical.rad(varphi)), 2)-A3

        return A

    @staticmethod
    def A_psi(inertia_factors, psi):
        A1 = inertia_factors[0]
        A2 = inertia_factors[1]
        A3 = inertia_factors[2]

        A = A1*np.power(np.cos(Canonical.rad(psi)), 2)+A2 * \
            np.power(np.sin(Canonical.rad(psi)), 2)-A3

        return A

    # define the mixed canonical factor which contains both the varphi and phi coordinates
    @staticmethod
    def A_mixed(inertia_factors, varphi, psi):
        A1 = inertia_factors[0]
        A2 = inertia_factors[1]

        A = A1*np.cos(Canonical.rad(varphi))*np.cos(Canonical.rad(psi)) + \
            A2*np.sin(Canonical.rad(varphi))*np.sin(Canonical.rad(psi))

        return A

    @staticmethod
    def A_gamma(gamma, j, f, psi):
        rad3 = np.sqrt(3.0)

        A = np.cos(Canonical.rad(gamma))-(f*(2.0*j-f))/(2.0*j*j)*rad3*(rad3*np.cos(
            Canonical.rad(gamma))+np.sin(Canonical.rad(gamma))*np.cos(2*Canonical.rad(psi)))

        return A
