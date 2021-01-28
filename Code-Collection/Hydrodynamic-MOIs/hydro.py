#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt


def Hydrodynamic_MOI(I0, gamma):
    hydro = lambda k: 4.0 / 3.0 * I0 * \
        np.power(np.sin(gamma + ((2.0 * np.pi) / 3.0 * k)), 2.0)
    I1 = hydro(1)
    I2 = hydro(2)
    I3 = hydro(3)
    MOIS = [I1, I2, I3]
    return MOIS


gammas_deg = np.arange(0.0, 61.0, 1.0)

gammas = gammas_deg * np.pi / 180.0

I0 = 25

hydro_mois1 = [Hydrodynamic_MOI(I0, X)[0] for X in gammas]
hydro_mois2 = [Hydrodynamic_MOI(I0, X)[1] for X in gammas]
hydro_mois3 = [Hydrodynamic_MOI(I0, X)[2] for X in gammas]

plt.rcParams.update({'font.size': 15})

plt.plot(gammas_deg, hydro_mois1, '-r', label=r'$\mathcal{I}_1$')
plt.plot(gammas_deg, hydro_mois2, '-b', label=r'$\mathcal{I}_2$')
plt.plot(gammas_deg, hydro_mois3, '-k', label=r'$\mathcal{I}_3$')
plt.xlabel(r'$\gamma\ [deg]$')
plt.ylabel(r'$\mathcal{I}\ [\hbar^2/MeV]$')
plt.legend(loc='center left',bbox_to_anchor=(0.07, 0.3))

plt.savefig('hydro_mois.pdf',dpi=600,bbox_inches='tight')
plt.close()