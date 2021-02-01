#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
from numpy import random as rd
import matplotlib.pyplot as plt

# units are in keV
SD_BAND2 = [8577.7, 7781.2, 7016.0, 6283.3, 5583.4, 4917.2, 4285.1,
            3687.9, 3126.3, 2601.1, 2113.0, 1662.7, 1250.9, 878.2, 545.1, 252.4, 0]
SD_BAND3 = [8793.2, 7992.6, 7221.3, 6481.3, 5772.8, 5096.7, 4454.0,
            3844.5, 3269.5, 2729.8, 2225.9, 1758.8, 1329.1, 937.6, 585.1, 272.0, 0]

# sort and transform to MeV
SD_BAND2 = [x / 1000.0 for x in SD_BAND2]
SD_BAND2 = sorted(SD_BAND2)
SD_BAND3 = [x / 1000.0 for x in SD_BAND3]
SD_BAND3 = sorted(SD_BAND3)

B2_SPIN_0 = 21.0 / 2.0
B3_SPIN_0 = 23.0 / 2.0

SPINS_BAND2 = [B2_SPIN_0 + 2 * N for N in np.arange(0, len(SD_BAND2))]
SPINS_BAND3 = [B3_SPIN_0 + 2 * N for N in np.arange(0, len(SD_BAND3))]


def Gamma_Transitions(band):
    gammas = []
    for id in range(len(band) - 1):
        gamma = band[id + 1] - band[id]
        gammas.append(gamma)
    return gammas


BAND2 = list(zip(SPINS_BAND2, SD_BAND2))
BAND3 = list(zip(SPINS_BAND3, SD_BAND3))


def E_gamma(band, spin):
    S, E = zip(*band)
    try:
        I2 = S.index(spin + 2)
        I = S.index(spin)
    except ValueError as err:
        # print(F'Cannot perform calculation due to: {err}')
        return 6969
    else:
        E_gamma = round(E[I2] - E[I], 3)
        return E_gamma


I = SPINS_BAND2[3]


def Stagger(band2, band3, spin):
    I = spin
    IM2 = I - 2
    IM1 = I - 1
    e_gamma_plus = E_gamma(band2, I)
    e_gamma_minus = E_gamma(band2, IM2)
    e_gamma_partner = E_gamma(band3, IM1)
    if(e_gamma_partner == 6969 or e_gamma_minus == 6969 or e_gamma_plus == 6969):
        return 6969
    stagger = 0.5 * (e_gamma_plus + e_gamma_minus) - e_gamma_partner
    return stagger
    # print(e_gamma_plus, e_gamma_minus,e_gamma_partner)


x = []
y = []
for spin in SPINS_BAND2:
    s = Stagger(BAND2, BAND3, spin)
    if(s != 6969):
        x.append(spin)
        y.append(s)
        print(spin, s)

plt.plot(x,y,'-r', label='stagger parameter')
plt.savefig('staggering.pdf',dpi=600,bbox_inches='tight')
plt.close()
