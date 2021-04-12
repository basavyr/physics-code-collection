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


def MinusOneTo(exp):
    return np.power(-1, exp)


# the energy spectrum for a spin state I, with given projection K
# the spectrum is parametrized in terms of the intrinsic energy of the band-head "EK_0", the decoupling parameter "a", and the inertial parameter "A"
# the inertial parameter "A" is obtained from the moment of inertia J
# the decoupling parameter depends on the j-components which contribute to the particle state ψ_{1/2}.
def E_I(EK_0, I, J, a, K):
    if(Kronecker_Delta(K, 1.0 / 2.0) == 0):
        return -1
    if(J == 0):
        return -1
    A = 1.0 / (2.0 * J)
    rotor_term = I * (I + 1.0)
    I_half = I + 0.5
    decoupling_term = a * MinusOneTo(I_half) * \
        I_half * Kronecker_Delta(K, 1.0 / 2.0)
    E = A * (rotor_term + decoupling_term)
    EK_I = E + EK_0
    return EK_I


energy = lambda I, J, a: E_I(0, I, J, a, 1.0 / 2.0)
spectrum = lambda spins, moi, a: [energy(spin, moi, a) for spin in spins]


print(I_x(4))
print(I_ref(0.2, 8, 40))


band_head_spin = 0.5
MOI = 65
spins = np.arange(band_head_spin, band_head_spin + 20, 2)
energies = spectrum(spins, MOI, 0.2)
