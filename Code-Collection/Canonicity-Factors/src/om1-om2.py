from re import I
import numpy as np
import matplotlib.pyplot as plt


# local import
from common_factors import Factors as F


def omega1(Spin, OddSpin, A1, A2, A3):
    I = Spin
    j = OddSpin
    Delta_31 = F.Delta_I(I, j, A1, A3)
    Delta_21 = F.Delta_I(I, j, A1, A2)

    omega = np.sqrt(Delta_31*Delta_21)

    return omega


def omega2(Spin, OddSpin, A1, A2, A3, V, gamma):
    I = Spin
    j = OddSpin
    gm = gamma

    Sigma_21 = F.Sigma_j(I, j, A1, A2)
    Sigma_31 = F.Sigma_j(I, j, A1, A3)

    G_1 = F.G_1(j, gm)
    G_2 = F.G_2(j, gm)

    T0_1 = Sigma_21+V*F.G_2(j, gm)
    T0_2 = Sigma_31+V*F.G_1(j, gm)

    omega = np.sqrt(T0_1)*np.sqrt(T0_2)

    return omega


# define the constants
A1 = 0.2
I0 = 35.0/2.0
j0 = 13.0/2.0
V0 = 3.0
gm0 = 25.0*np.pi/180.0

spins = np.arange(0.5, 45.4, 2)
