#!/Users/robertpoenaru/.pyenv/shims/python


import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd


CHARGE_E = 1

# return the radius of a nuclei with respect to the total number of nucleus (assuming a constant density)


class Charge_Distribution:
    def __init__(self, A, Z, diffuseness, beta):
        self.A = A
        self.Z = Z
        self.a = diffuseness
        self.beta = beta

    R0 = 1.25

    # the constant nuclear charge density
    rho_0 = lambda A, Z, e: 0.17 * Z * e / A

    R = lambda A: Charge_Distribution.R0 * np.power(A, 1.0 / 3.0)

    R_half = lambda A: 1.128 * \
        np.power(A, 1.0 / 3.0) - 0.89**np.power(A, 1.0 / 3.0)

    # create the Fermi-function which describes the nuclear charge distribution within the nucleus
    @staticmethod
    def Fermi_Distribution(x0, x, a):
        T = 1.0 + np.exp(x / a)
        return x0 / T

    @staticmethod
    def rho_charge(A, Z, e, a):
        # rho0=0.08
        RHO0 = Charge_Distribution.rho_0(A, Z, e)
        R_HALF = Charge_Distribution.R_half(A)
        # declare the diffuseness parameter a
        # a_diffuse = 0.524
        a_diffuse = 1.69
        exp_f = 1.0 + np.exp((r - R_HALF) / a_diffuse)
        rho = RHO0 / exp_f
        return rho


# evaluate the function under the integrand for the RMS radius of the charge distribution
def RMS_Radius(A, Z, r):
    C = 4.0 * np.pi
    r2 = np.power(r, 2)
    r2 = np.power(r, 2)
    rho_ch = Fermi_Distribution(A, Z, r)
    rms = r2 * rho_ch * C * r2
    return rms


# evaluate the rms function with the constant term proportional to the square of nuclear radius
# radius is given as a function of nuclear mass number A
def RMS_ConstantR(A):
    r_const = R(A)
    rms = 3.0 / 5.0 * np.power(r_const, 2)
    return rms
