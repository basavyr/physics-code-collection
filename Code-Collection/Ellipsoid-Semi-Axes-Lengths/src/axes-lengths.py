# evaluating the semi-axes lengths for a triaxial ellipsoid
# the required parameters are $\gamma$, $\beta_2$
# each semi-axis has a specific index k

import numpy as np
from matplotlib import pyplot as plt


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


def main():
    r0 = 1.2
    beta = 0.35
    gamma = 20
    print(R_k(1, r0, beta, gamma))
    print(R_k(2, r0, beta, gamma))
    print(R_k(3, r0, beta, gamma))


if __name__ == '__main__':
    main()
