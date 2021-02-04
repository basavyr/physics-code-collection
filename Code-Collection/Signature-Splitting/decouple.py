#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np

spins_f = np.arange(10.5, 34.5, 2)
spins_u = np.arange(11.5, 35.5, 2)

ALPHA_0 = 1.0 / 2.0

IsOdd = lambda n: (n % 2 != 0)
IsEven = lambda n: (n % 2 == 0)


# determine the signature quantum number for a given state with angular momentum I
def Determine_SpinSignature(spin):
    I = spin
    FAVORED = 1.0 / 2.0
    # UNFAVORED = -1.0 / 2.0
    alpha_I = 0.5 * np.power(-1, I - ALPHA_0)
    if(alpha_I == FAVORED):
        return '+1/2 signature'
    return '-1/2 signature'


def Determine_BandSignature(band):
    I = [band[0], band[1]]

    if(I[1] - I[0] != 2):
        return 'Not a signature partner !!!'

    Even = lambda x: x - ALPHA_0
    OK = [IsEven(Even(x)) for x in I]

    if(all(OK)):
        return 'favored band'

    return 'unfavored band'


def Generate_Delta1_SpinBand(I0, k):
    RET_SPINS = [I0 + N for N in range(k)]
    return RET_SPINS


# Apply a signature split for a rotational band
# split a band sequence of \Delta I=1 rotational states in their respective signature partners
# according to the scheme described in `signature_decoupling.png`
def Split(band):
    favored_band = [x for x in band if Determine_SpinSignature(
        x) == '+1/2 signature']
    unfavored_band = [
        x for x in band if Determine_SpinSignature(x) == '-1/2 signature']
    return [favored_band, unfavored_band]


def EnergySpectrum(band, decoupling):
    # the energy state for a state in a K=1/2 band is proportional to the squared angular momentum and also the **decoupling parameter** a_i
    # the decoupling parameter a_i from `signature_decoupling.png` is denoted here by decoupling
    ai = decoupling
    E_K = lambda I: I * (I + 1.0) - ai * np.power(-1, I - 0.5) * (I + 0.5)
    energies = [E_K(I) for I in band]
    return energies


# Initial spin state
# The band-head state is I_0
I0 = 9 + ALPHA_0
I = Generate_Delta1_SpinBand(I0, 15)

print(f'The initial spin sequence:\nI: {I}\n')

# the energy spectrum
E = EnergySpectrum(I, -1.244)

print(f'The energy spectrum:\nE_I: {E}\n')

# create the favored signature partner by applying the Signature Split
I_f = Split(I)[0]
I_u = Split(I)[1]


print(
    f'{I_f} -> {Determine_BandSignature(I_f)} (alpha={Determine_SpinSignature(I_f[0])})\n')
print(
    f'{I_u} -> {Determine_BandSignature(I_u)} (alpha={Determine_SpinSignature(I_u[0])})')
