#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt


def E_Wobb(E1i, E0ip1, E0im1):
    e = E1i - 0.5 * (E0ip1 + E0im1)
    return e


E3_Exp = [2.1237	, 2.6293	, 3.1973	, 3.8243	, 4.5094	, 5.2506	, 6.0465	,
          6.8963	, 7.7988	, 8.7546	, 9.7638	, 10.8268	, 11.9392	, 13.0861	]
E3_Th = [2.04238, 2.57396, 3.15888, 3.7974, 4.48976, 5.23613, 6.0367,
         6.89161, 7.80099, 8.76495, 9.7836, 10.857, 11.9853, 13.1685]

E2_Exp = [1.3394, 1.7467, 2.2184, 2.7527, 3.3484, 4.003, 4.7143, 5.4805,
          6.3004, 7.1733, 8.0998, 9.08, 10.1147, 11.2036, 12.3466, 13.5441, 14.7911]
E2_Th = [1.34903, 1.77368, 2.25387, 2.78958, 3.38082, 4.02758, 4.72986, 5.48767,
         6.301, 7.16986, 8.09423, 9.07413, 10.1096, 11.2005, 12.347, 13.549, 14.8065]

SPINS = [16.5, 18.5, 20.5, 22.5, 24.5, 26.5, 28.5,
         30.5, 32.5, 34.5, 36.5, 38.5, 40.5, 42.5]

# SPINS FROM BAND 2:
# 13.5,15.5,17.5,19.5,21.5,23.5,25.5,27.5,29.5,31.5,33.5,35.5,37.5,39.5,41.5,43.5,45.5

# Determine the experimental wobbling energies
EWobb_Exp = []
count = 0
for state in zip(SPINS, E3_Exp):
    spin = state[0]
    e = state[1]
    e_wobb = E_Wobb(e, E2_Exp[count + 1], E2_Exp[count + 2])
    EWobb_Exp.append(e_wobb)
    count = count + 1

# Determine the theoretical wobbling energies
EWobb_Th = []
count = 0
for state in zip(SPINS, E3_Th):
    spin = state[0]
    e = state[1]
    e_wobb = E_Wobb(e, E2_Th[count + 1], E2_Th[count + 2])
    EWobb_Th.append(e_wobb)
    count = count + 1

plt.rcParams.update({'font.size': 15})

plt.plot(SPINS,EWobb_Exp,'^r',label='Exp.')
plt.plot(SPINS,EWobb_Th,'sk',label='Th.')
plt.ylim((0,0.3))
plt.xlabel(r'$I\ [\hbar]$')
plt.ylabel(r'$E_{wobb}\ [MeV]$')
plt.legend(loc='best')
plt.savefig('wobbling_energy_ThExp.pdf',dpi=600,bbox_inches='tight')
plt.close()