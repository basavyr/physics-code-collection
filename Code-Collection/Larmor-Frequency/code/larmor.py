#! /Users/robertpoenaru/.pyenv/shims/python

# Sources 

# Larmor Frequency
# http://hyperphysics.phy-astr.gsu.edu/hbase/Nuclear/larmor.html

# Larmor Precession
# http://hyperphysics.phy-astr.gsu.edu/hbase/magnetic/larmor.html#c1

# Nuclear Magnetic Resonance
# http://hyperphysics.phy-astr.gsu.edu/hbase/Nuclear/nmr.html#c1

# Nuclear Spin Polarization
# http://hyperphysics.phy-astr.gsu.edu/hbase/Nuclear/spinpol.html#c1

# Energy Calculation for Rigid Rotor Molecules
# http://hyperphysics.phy-astr.gsu.edu/hbase/molecule/rotqm.html#c1


import numpy as np

# The gyromagnetic ratio
g = 2.0

M_PROTON = 1.0
M_ELECTRON = float((1 / 1836) * M_PROTON)

B_FIELD = 2.5  # TESLA

MU_PROTON = 12
MU_ELECTRON = 24


def Larmor(b_field, mass, gyromagnetic):
    CHARGE = 1.6
    W_1 = CHARGE * gyromagnetic
    W_2 = 2.0 * mass
    omega_L = (W_1 / W_2) * b_field
    print(
        f'The frequency of precession of the given spin state around the magnetic field is f_L= {omega_L}')
    return omega_L


Larmor(B_FIELD, M_PROTON, g)
