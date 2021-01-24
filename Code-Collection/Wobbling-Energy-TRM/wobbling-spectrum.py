#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt


def Omega_Rot(spin, I1):
    return float(spin / I1)


def Omega_Wob(spin, I1, I2, I3):
    w_rot = Omega_Rot(spin, I1)
    delta = float((I1 - I2) * (I1 - I3))
    I23 = I2 * I3
    w_wob = w_rot * np.sqrt(delta / I23)
    return w_wob


def E_rot(spin, MOIS, n_wob):
    I = spin
    I1 = MOIS[0]
    w_wob = Omega_Wob(I, MOIS[0], MOIS[1], MOIS[2])
    E = I * (I + 1) * 1.0 / (2 * I1) + w_wob * (n_wob + 0.5)
    return E


MOIS = [25, 5, 2]

spins = np.arange(10, 22, 2)
energies = lambda k: [E_rot(x, MOIS, k) for x in spins]

# print(energies(1))
# print(energies(2))
# print(energies(3))
# print(energies(4))
# print(energies(5))

e0 = energies(0)
e1 = energies(1)
e2 = energies(2)
e3 = energies(3)
e4 = energies(4)

plt.plot(spins, e0, '-sr', label=r'$n_w=0$')
plt.plot(spins, e1, '-^k', label=r'$n_w=1$')
plt.plot(spins, e2, '-vb', label=r'$n_w=2$')
plt.plot(spins, e3, '-oc', label=r'$n_w=3$')
plt.plot(spins, e4, '-*m', label=r'$n_w=4$')
plt.xlabel(f'Spin $[\hbar]$')
plt.ylabel(f'Energy $[MeV]$')
plt.legend(loc='best')
plt.savefig('simple_wobbling_spectrum.pdf', dpi=600, bbox_inches='tight')
plt.close()
