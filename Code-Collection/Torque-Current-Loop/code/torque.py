#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np

N_COILS = 3  # INTEGER NUMBER
RADIUS = 3  # CENTIMETERS
CURRENT = 5  # AMPERES
B_FIELD = 2.5  # TESLA

# ANGLE BETWEEN THE MAGNETIC MOMENT OF THE LOOP AND THE MAGNETIC FIELD B
THETA = 30.0  # RADIANS


def Rad(angle):
    return float(angle * np.pi / 180.0)


def Area(radius):
    return float(np.power(radius, 2) * np.pi)

# Compute the magnetic moment (magnetic dipole) of the current carrying loop


def MU(PARAMS):
    # magnetic moment is directly proportional to the product between the current running through the loop and the enclosing area
    r = PARAMS[1] * 0.01
    I = PARAMS[2]
    N = PARAMS[0]

    # the magnetic moment of a single loop
    mu_0 = Area(r) * I

    # the magnetic moment of the entire coil
    mu = N * mu_0

    print(f'The magnetic moment is: µ= {mu}')
    return mu


# Calculate the torque that is exerted by the magnetic field on the magnetic moment of the loop.
# Torque will start to align the magnetic moment of the loop with the field itself
def T(PARAMS):
    B = float(PARAMS[3])
    theta = float(Rad(PARAMS[4]))
    T = MU(PARAMS) * B * np.sin(theta)
    print(f'The torque applied on the current carrying loop is T= {T}')
    return T


# Compute the radius of the trajectory of a charged particle moving inside a magnetic field with constant magnitude
def R(MASS, CHARGE, SPEED, B_FIELD):
    R = (MASS * SPEED) / (CHARGE * B_FIELD)
    print(f'The radius of the particle trajectory is R= {R}')
    return R


PARAM_SET = [N_COILS, RADIUS, CURRENT, B_FIELD, THETA]

print(MU(PARAM_SET))
print(T(PARAM_SET))
print(R(1, 1, 1, 1))
