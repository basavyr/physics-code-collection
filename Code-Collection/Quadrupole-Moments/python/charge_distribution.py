#!/Users/robertpoenaru/.pyenv/shims/python


import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd


CHARGE_E = 1

# return the radius of a nuclei with respect to the total number of nucleus (assuming a constant density)


def R(A):
    return 1.25 * np.power(A, 1.0 / 3.0)


# the constant nuclear charge density
def rho_0(Z, A):
    C_0 = 0.17
    e = CHARGE_E
    C_1 = float(Z / A)
    return e * C_0 * C_1


def R_half(A):
    C_0 = 1.128
    C_1 = 0.89
    r_half = C_0 * np.power(A, 1.0 / 3.0) - C_1 * np.power(A, -1.0 / 3.0)
    return r_half


# create the Fermi-function which describes the nuclear charge distribution within the nucleus
def Fermi_Distribution(A, Z, r):
    # rho0=0.08
    RHO0 = rho_0(Z, A)
    R_HALF = R_half(A)
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