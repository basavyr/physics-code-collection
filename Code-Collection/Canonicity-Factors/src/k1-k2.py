import numpy as np
import matplotlib.pyplot as plt


# local import
from common_factors import Factors as F


# define k1 according to Eq. 6.46
def k1(Spin, OddSpin, A1, A2, A3):
    I = Spin
    j = OddSpin

    Delta_21 = F.Delta_I(I, j, A1, A2)
    Delta_31 = F.Delta_I(I, j, A1, A3)

    Term_I = (Delta_21/Delta_31)*np.power(I, 2)
    k_factor = np.power(Term_I, 0.25)

    return k_factor


# define k2 according to Eq. 6.46
def k2(Spin, OddSpin, A1, A2, A3, V, gamma):
    I = Spin
    j = OddSpin
    gm = gamma

    Sigma_21 = F.Sigma_j(I, j, A1, A2)
    Sigma_31 = F.Sigma_j(I, j, A1, A3)

    T0_1 = Sigma_21+V*F.G_1(j, gm)
    T0_2 = Sigma_31+V*F.G_2(j, gm)

    Term_j = (T0_1/T0_2)*np.power(j, 2)
    k_factor = np.power(Term_j, 0.25)

    return k_factor


# define the constants
A1 = 0.2
I0 = 35.0/2.0
j0 = 13.0/2.0
V0 = 3.0
gm0 = 25.0*np.pi/180.0

spins = np.arange(0.5, 45.4, 2)


k1_data_1 = k1(spins, j0, A1, 2.0*A1, 5.0*A1)
k1_data_2 = k1(spins, j0, A1, 5.0*A1, 2.0*A1)
print(k1_data_1)
print(k1_data_2)

k2_data_1 = k2(spins, j0, A1, 2.0*A1, 5.0*A1, V0, gm0)
k2_data_2 = k2(spins, j0, A1, 5.0*A1, 2.0*A1, V0, gm0)
print(k2_data_1)
print(k2_data_2)
