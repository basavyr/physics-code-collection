#!/Users/robertpoenaru/.pyenv/shims/python


import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd

import quadrupole as Q
import charge_distribution as ch


A = 163
Z = 72
beta = 0.38
gamma = 21.0 * np.pi / 180.0
a = 2.20
j = 6.5

# the isospin projection t_z of the two nucleons
I3_proton = -0.5
I3_neutron = +0.5

# total angular momentum of the rotational state
I = 1.0 / 2.0

rms = ch.Charge_Distribution.RMS_Deformed(A, beta)

nucleus = Q.Quadrupole(rms, A, Z, I, beta, gamma, a, I3_proton)

nucleus.Show_Data()


projections = np.arange(-I, I + 1, 1.0)
QS = [Q.Quadrupole.Q_S(A, Z, beta, I, K)
      for K in projections]


# Plot the spectroscopic Q with respect to the projection K of the total spin on the symmetry axis
plt.plot(projections, QS, 's-r', label=r'$Q_s$')
plt.legend(loc='best')
plt.savefig('Q_spectroscopic.png', dpi=600, bbox_inches='tight')
plt.close()


# plot the intrinsic Quadrupole moment with respect to the deformation parameter beta
betas = np.arange(0.01, 1, 0.05)
Q0_betas = [Q.Quadrupole.Q_0(A, Z, b) for b in betas]
plt.plot(betas, Q0_betas, 'o--b', label=r'$Q_0$')
plt.legend(loc='best')
plt.savefig('Q_0_beta.png', dpi=600, bbox_inches='tight')
plt.close()

# plot the intrinsic Quadrupole with the thickness parameter
# the nuclear quadrupole moment is solved in the hydrodynamic model
betas = np.arange(0.01, 1, 0.05)
Q0_DIFFUSED = [[Q.Quadrupole.Q_0_deformed(
    A, Z, a_diff, b, I3_proton) for b in betas] for a_diff in np.arange(0.1, 2, 0.25)]
for qd in Q0_DIFFUSED:
    plt.plot(betas, qd, 'v-r', label=r'$Q_0(\beta_2,a)$')
plt.legend(loc='best')
plt.savefig('Q_0_diffuse.png', dpi=600, bbox_inches='tight')
plt.close()


# plot the nuclear charge distribution in the nucleus for a parameter thickness paramater
r = np.arange(0.1, 10.1, 0.1)
rhos = [[ch.Charge_Distribution.rho_charge(
    A, Z, Q.Quadrupole.e_eff_proton, a_diff, x) for x in r]for a_diff in np.arange(0.1, 2.6, 0.6)]
for ro in rhos:
    plt.plot(r, ro, '-k', label=r'$\rho_{ch}(r)$')
plt.legend(loc='best')
plt.savefig('FermiQ_dist.png', dpi=600, bbox_inches='tight')
plt.close()


# generate the two components Q2 and Q0 of the quadrupole operator, using the expressions from Yoshida's calculations [Yoshida 1972]
# vary the rms - the second radial moment
def_rms = np.arange(0, 1.55, 0.11)
q0_yoshida = [Q.Quadrupole.Q0_Y(Z, rms, beta, gamma) for rms in def_rms]
q2_yoshida = [Q.Quadrupole.Q2_Y(Z, rms, beta, gamma) for rms in def_rms]

# plot the two components Q2 and Q0 of the quadrupole operator, using the expressions from Yoshida's calculations [Yoshida 1972]
# preamble set
plt.rcParams.update({'font.size': 15})

fig, ax = plt.subplots()

ax.set_xlabel(r'$\langle r^2 \rangle$')
ax.set_ylabel(r'$Q_Y$')


plt.plot(def_rms, q0_yoshida, '^-r', label=r'$Q_0$')
plt.plot(def_rms, q2_yoshida, 'v-k', label=r'$Q_2$')
plt.text(0.2, 0.6, r'$\beta=$' + f'{beta}\n' + r'$\gamma=$' + f'{int(gamma*180/np.pi)}' + r'$^o$', horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes)
ax.legend(loc='best')
plt.savefig('yoshida_moments.png', dpi=600, bbox_inches='tight')
plt.close()
