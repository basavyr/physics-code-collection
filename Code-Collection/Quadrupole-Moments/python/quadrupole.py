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


# the quadrupole moment for a single nucleon in an orbit j=J
# the quadrupole term contains the rms distribution as a constant function of R
def Q_j_constR(A, Z, j, particle):
    e = CHARGE_E
    e_eff_proton = 1.5 * e
    e_eff_neutron = 0.95 * e
    C_j = (2.0 * j - 1) / (2.0 * j + 2.0)
    rms = RMS_ConstantR(A)
    if(particle == 'p'):
        Q_eff = e_eff_proton / e
    else:
        Q_eff = e_eff_neutron / e
    ret_Q_j = -1.0 * C_j * Q_eff * rms
    return ret_Q_j





Z = 72
A = 163

QUADRUPOLE_CONST = 'quadrupole_j.png'

js = np.arange(0.5, 10.5, 1)
Q_js = [Q_j_constR(A, Z, j, 'p') for j in js]
plt.plot(js, Q_js, '-r', label=r'$Q_j$')
plt.legend(loc='best')
plt.savefig(QUADRUPOLE_CONST, dpi=600, bbox_inches='tight')
plt.close()


CHARGE_DENSITY = 'charge_density.png'

rs = np.arange(0, 10, 0.05)
rhos = [Fermi_Distribution(A, Z, r) for r in rs]
plt.plot(rs, rhos, '-k', label=r'$\rho_{ch}(r)$')
plt.legend(loc='best')
plt.savefig(CHARGE_DENSITY, dpi=600, bbox_inches='tight')
plt.close()
