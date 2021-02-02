#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
from numpy import random as rd
import matplotlib.pyplot as plt
from matplotlib import rc 
# units are in keV
SD_BAND2 = [8577.7, 7781.2, 7016.0, 6283.3, 5583.4, 4917.2, 4285.1,
            3687.9, 3126.3, 2601.1, 2113.0, 1662.7, 1250.9, 878.2, 545.1, 252.4, 0]
SD_BAND3 = [8793.2, 7992.6, 7221.3, 6481.3, 5772.8, 5096.7, 4454.0,
            3844.5, 3269.5, 2729.8, 2225.9, 1758.8, 1329.1, 937.6, 585.1, 272.0, 0]

# sort and transform to MeV
SD_BAND2 = [x / 1 for x in SD_BAND2]
SD_BAND2 = sorted(SD_BAND2)
SD_BAND3 = [x / 1 for x in SD_BAND3]
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


# gives the difference in energy between the I-state and (I-2)-state
def E_gamma(band, spin):
    S, E = zip(*band)
    # print(S)
    try:
        I = S.index(spin)
        IM2 = S.index(spin - 2)
    except ValueError:
        # print(F'Cannot perform calculation due to: {err}')
        return 6969
    else:
        print(f'searching for the transition {S[I]} -> {S[IM2]}')
        E_gamma = round(E[I] - E[IM2], 3)
        return E_gamma


S, E = zip(*BAND2)

x_2 = []
x_3 = []
y_2 = []
y_3 = []

# update the first band
for spin in S:
    if(E_gamma(BAND2, spin) == 6969):
        pass
    else:
        E = E_gamma(BAND2, spin) - 9.6 * (2.0 * spin - 1)
        y_2.append(E)
        x_2.append(spin)

S, E = zip(*BAND3)

# update the second band
for spin in S:
    if(E_gamma(BAND3, spin) == 6969):
        pass
    else:
        E = E_gamma(BAND3, spin) - 9.6 * (2.0 * spin - 1)
        y_3.append(E)
        x_3.append(spin)


plt.rcParams.update({'font.size': 15})

fig, ax = plt.subplots()


plt.plot(x_2, y_2, 'o-r', label='band2')
plt.plot(x_3, y_3, 'o-k', label='band3')
ax.legend(loc='best')
ax.set_xlabel(r'$I\ [\hbar]$')
ax.set_ylabel(r'$E_\gamma(relative)$')
plt.text(0.5, 0.5, r'$^{191}Hg$', horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes)
plt.savefig('staggering.pdf', dpi=600, bbox_inches='tight')

plt.close()


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


# x = []
# y = []
# for spin in SPINS_BAND2:
#     s = Stagger(BAND2, BAND3, spin)
#     if(s != 6969):
#         x.append(spin)
#         y.append(s)
#         print(spin, s)

# plt.plot(x, y, '-r', label='stagger parameter')
# plt.savefig('staggering.pdf', dpi=600, bbox_inches='tight')
# plt.close()
