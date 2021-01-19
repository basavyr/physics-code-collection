#! /Users/robertpoenaru/.pyenv/shims/python

import numpy as np
from numpy import random as rd
import matplotlib.pyplot as plt

M_P = 1.0  # proton mass
M_N = 1.0  # neutron mass
G_FACTOR_P = 2.79  # proton gyromagnetic factor
G_FACTOR_N = -3.8260837  # neutron gyromagnetic factor
SPIN = 1.0 / 2.0  # spin of the nucleon

CHARGE_P = +1.0  # electric charge of the proton
CHARGE_N = +0.0  # electric charge of the neutron

BOHR_N = 3.15245  # Bohr Magneton for the proton µ_N = (e\hbar) / (2mp)

PLANCK_H = 6.582

# the parameters to be used within the calculations (PROTON: GYROMAGNETIC-FACTOR,MASS,CHARGE,SPIN)
P_PARAMS = [G_FACTOR_P, M_P, CHARGE_P, SPIN, BOHR_N, PLANCK_H]
N_PARAMS = [G_FACTOR_N, M_N, CHARGE_N, SPIN, BOHR_N, PLANCK_H]


def Magnetic_Dipole_Moment(PARAMS):
    g_factor = PARAMS[0]  # the g-factor of the nucleon
    mu_n = PARAMS[4]  # the Bohr magneton
    mu = g_factor * mu_n
    return mu


def Larmor(PARAMS, B_Field):
    hbar = PARAMS[5]
    mu = Magnetic_Dipole_Moment(PARAMS)
    omega = (2.0 * mu * B_Field) / hbar
    return omega


def Larmor_Frequency(PARAMS, B_Field):
    return Larmor(PARAMS, B_Field) / (2.0 * np.pi)


B_Fields = np.arange(0.5, 6.5, 0.5)

Larmors = [Larmor(P_PARAMS, B) for B in B_Fields]
Larmor_Freqs = [Larmor_Frequency(P_PARAMS, B) for B in B_Fields]

# plt.plot(B_Fields, Larmors, '-r', label=r'$\omega_L$')
# plt.plot(B_Fields, Larmor_Freqs, 'ok', label=r'$\nu_{Larmor}$')
# plt.legend(loc='best')
# plt.savefig('larmors.pdf', dpi=500, bbox_inches='tight')
# plt.close()


# generate random spin-states

m_z = [-SPIN, SPIN]


spins = [rd.choice(m_z, 1)[0] for _ in range(100)]


def Excite(state, energy):
    return state + energy


def Relax(state, energy):
    return state - energy


def S_state(spin):
    if(spin == -0.5):
        return 'down'
    return 'up'


def Transition(spin, state, energy):
    if(S_state(spin) == 'up'):
        return Relax(state, energy)
    return Excite(state, energy)


states = [S_state(spin) for spin in spins]

MU_P = Magnetic_Dipole_Moment(P_PARAMS)
B_Field = 1

E_states = [MU_P * B_Field * (2 * spin) for spin in spins]

E_states_diff = [round(2 * E, 2) for E in E_states]

Delta_E = max(E_states) - min(E_states)

deltas = [Delta_E * rd.choice([0, 1, 0.5, 0.25]) for _ in range(len(E_states))]

status = ['-' for state in states]

mixed = zip(spins, E_states, deltas, status)

for mix in mixed:
    if(mix[2] == Delta_E):
        print(mix)
        e = Transition(mix[0], mix[1], mix[2])
        flip = 'flipped'
        print(mix[0], e, flip)
# print(E_states)
# print(E_states_diff)


# plt.plot(spins, '-ob')
# plt.savefig('spins.pdf', dpi=500, bbox_inches='tight')
# plt.close()
