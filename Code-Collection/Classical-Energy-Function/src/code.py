###################################################################################################
###################################################################################################
# evaluate the canonical factors that arise in the expression of the classical energy function (CEF)
###################################################################################################
###################################################################################################

import numpy as np
import matplotlib.pyplot as plt

plot_location = './results'


class Canonical:
    """
    - collection of methods that correspond to each of the four canonical terms within the CEF
    """

    @staticmethod
    def A_varphi(inertia_factors, varphi):
        return 1

    @staticmethod
    def A_psi(inertia_factors, psi):
        return 1

    # define the mixed canonical factor which contains both the varphi and phi coordinates
    @staticmethod
    def A_mixed(inertia_factors, varphi, psi):
        return 1

    @staticmethod
    def A_gamma(gamma, j, f, psi):
        return 1


print(Canonical.A_varphi(1, 1))
