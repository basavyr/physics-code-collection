#!/Users/robertpoenaru/.pyenv/shims/python


import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd

import quadrupole as Q
import charge_distribution as ch


A = 163
Z = 72
beta = 0.38
a = 0.54
j = 6.5
I3_proton = 0.5
I3_neutron = -0.5
I = 25.0 / 2.0

rms = ch.Charge_Distribution.RMS_Deformed(A, beta)

nucleus = Q.Quadrupole(rms, A, Z, I, beta, a, I3_proton)

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
