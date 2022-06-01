# evaluating the semi-axes lengths for a triaxial ellipsoid
# the required parameters are $\gamma$, $\beta_2$
# each semi-axis has a specific index k

from operator import indexOf
import numpy as np
from matplotlib import pyplot as plt

r0 = 1.2


def R_k(k, R_0, beta, gamma):
    # constants
    rad = np.sqrt(5.0/(4.0*np.pi))
    gm = gamma*np.pi/180.0
    pi_23 = 2.0*np.pi/3.0

    # the cosine term defined in terms of the k-index
    cos_term = np.cos(gm-pi_23*k)

    # define the term that depends on the quadrupole deformation
    beta_term = rad*beta*cos_term

    RK = R_0*(1+beta_term)

    return RK


def Show_Axes(beta, gamma):
    R1 = R_k(1, r0, beta, gamma)
    R2 = R_k(2, r0, beta, gamma)
    R3 = R_k(3, r0, beta, gamma)

    axes = {"1": R1,
            "2": R2,
            "3": R3,
            }
    max_axes = max([ax for _, ax in axes.items()])
    index_of_max_axes = indexOf(
        [ax for _, ax in axes.items()], max_axes)+1
    print(max_axes)
    print(index_of_max_axes)


def main():
    beta = 0.35
    gamma = 20
    Show_Axes(beta, gamma)


if __name__ == '__main__':
    main()
