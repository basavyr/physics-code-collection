#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt
import finder
import importer
import plotter


def E_gamma(E1, E2):
    return (E1 - E2)


# Definition of the staggering parameter as defined by Luo et al (2009)
def Stagger_Parameter(I, E):
    E_band = E[0]
    E_partner = E[1]
    S_I = (E_band - E_partner) / (2.0 * I)
    return S_I


# Definition of the staggering parameter in signature partner bands
# As defined by Uma et al (2015)
def Stagger_SPB(band, partner, I):
    E_I = finder.Search_Energies(band, partner, I)
    if(E_I != -1):
        E_g_IP1 = E_gamma(E_I[2], E_I[0])
        E_g_IM1 = E_gamma(E_I[3], E_I[1])
        E_g_I = E_gamma(E_I[0], E_I[3])
        S_I = E_g_I - 0.5 * (E_g_IP1 + E_g_IM1)
        return S_I
    return -1

#Find the staggering parameter for a pair of chiral bands
def Compute_Stagger(even_data, odd_data):
    even_stagger = []
    odd_stagger = []

    even_spins = []
    odd_spins = []

    for data_point in even_data:
        I = data_point[0]
        E = finder.Search_Energy_Partner(even_data, odd_data, I)
        if(E != -1):
            # print(E)
            current_stagger = Stagger_Parameter(I, E)
            even_stagger.append(current_stagger)
            even_spins.append(I)
            # print(current_stagger)

    for data_point in odd_data:
        I = data_point[0]
        E = finder.Search_Energy_Partner(even_data, odd_data, I)
        if(E != -1):
            # print(E)
            current_stagger = Stagger_Parameter(I, E)
            odd_stagger.append(current_stagger)
            odd_spins.append(I)
            # print(current_stagger)

    S_I_even = [even_spins, even_stagger]
    S_I_odd = [odd_spins, odd_stagger]
    return [S_I_even, S_I_odd]
