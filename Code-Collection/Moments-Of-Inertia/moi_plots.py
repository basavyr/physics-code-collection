#! /Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd

import mois

rad = lambda deg: deg * np.pi / 180.0


MOIS = mois.MOI(50)


beta = 0.33

# gammas = np.arange(-60.0, 121.0, 1.0)
gammas = np.arange(0.0, 61.0, 1.0)
rigids_1 = [MOIS.Rigid(beta, rad(gamma))[0] for gamma in gammas]
rigids_2 = [MOIS.Rigid(beta, rad(gamma))[1] for gamma in gammas]
rigids_3 = [MOIS.Rigid(beta, rad(gamma))[2] for gamma in gammas]
hydros_1 = [MOIS.Hydro(rad(gamma))[0] for gamma in gammas]
hydros_2 = [MOIS.Hydro(rad(gamma))[1] for gamma in gammas]
hydros_3 = [MOIS.Hydro(rad(gamma))[2] for gamma in gammas]


rigid_plots = 'rigid_mois.png'
plt.plot(gammas, rigids_1, '-r', label=r'$\mathcal{I}_1$')
plt.plot(gammas, rigids_2, '-k', label=r'$\mathcal{I}_2$')
plt.plot(gammas, rigids_3, '-b', label=r'$\mathcal{I}_3$')
plt.legend(loc='best')
plt.title(f'The rigid-body moments of inertia')
plt.xlabel(r'$\gamma$' + f' [deg]')
plt.ylabel(r'$\mathcal{I}_{rigid}\ [\hbar^2/MeV]$')
plt.savefig(rigid_plots, dpi=1200, bbox_inches='tight')
plt.close()


hydro_plots = 'hydro_mois.png'
plt.plot(gammas, hydros_1, '-r', label=r'$\mathcal{I}_1$')
plt.plot(gammas, hydros_2, '-k', label=r'$\mathcal{I}_2$')
plt.plot(gammas, hydros_3, '-b', label=r'$\mathcal{I}_3$')
plt.legend(loc='best')
plt.title(f'The hydrodynamic moments of inertia')
plt.xlabel(r'$\gamma$' + f' [deg]')
plt.ylabel(r'$\mathcal{I}_{hydro}\ [\hbar^2/MeV]$')
plt.savefig(hydro_plots, dpi=1200, bbox_inches='tight')
plt.close()
