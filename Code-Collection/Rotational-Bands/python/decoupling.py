#! /Users/robertpoenaru/.pyenv/versions/3.8.6/envs/numerical/bin/python

import numpy as np
import matplotlib.pyplot as plt


# definition of the Kronecker-Delta δ symbol
def Kronecker_Delta(a, b):
    x = 1 if a == b else 0
    return x


# The angular momentum component along the x-axis (rotational axis)
# I_x is the total angular momentum projected ono the x-axis
# the argument of the function must be the total angular momentum I
# !!! evaluation of the aligned a.m. is done for the "mean-angular momentum" I_m=I-1
def I_x(I):
    I_m = I - 1
    K_values = np.arange(-I + 1, I, 1)
    I_x_components = []
    for K in K_values:
        I_m_squared = np.power(I_m + 1. / 2., 2)
        IK_diff = I_m_squared - np.power(K, 2)
        current_I_m = np.sqrt(IK_diff)
        I_x_components.append([K, current_I_m])
    return I_x_components


# Approximation of the aligned angular momentum for pure K=1/2 bands and the large I limit (I>>K)
def I_x_Large_I(I):
    return I - 1.0 / 2.0


# the reference value of the Aligned Angular Momentum I_ref as a function of rotational frequency ω
# the reference value is parametrized in terms of the Harris parameters J0,J1
def I_ref(omega, J0, J1):
    omega_squared = np.power(omega, 2)
    I_ref_value = (J0 + J1 * omega_squared) * omega
    return I_ref_value


# the energy spectrum for a spin state I, with given projection K
# the spectrum is parametrized in terms of the intrinsic energy of the band-head "EK_0", the decoupling parameter "a", and the inertial parameter "A"
# the decoupling parameter depends on the j-components which contribute to the particle state ψ_{1/2}.
def E_I(EK_0, I, A, a, K):
    return '1'

# print(I_x(4))
# print(I_ref(0.2, 8, 40))
