#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt
import finder
import importer
import plotter


RU_108_FILE = '108Ru.dat'
RU_110_FILE = '110Ru.dat'
RU_112_FILE = '112Ru.dat'


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


RU_108_DATA = importer.Import_Data(RU_108_FILE)
RU_110_DATA = importer.Import_Data(RU_110_FILE)
RU_112_DATA = importer.Import_Data(RU_112_FILE)


odd_stack = RU_112_DATA[0]
even_stack = RU_112_DATA[1]

t = Compute_Stagger(even_stack, odd_stack)

plot_112 = './plots/stagger_112.pdf'

plotter.Plot_Stagger_Bands(t, plot_112)

# print(Stagger_SPB(odd_stack, even_stack, odd_stack[1][0]))
# print(Stagger_Parameter(odd_stack[1][0], finder.Search_Energy_Partner(
# even_stack, odd_stack, odd_stack[1][0])))

# print(even_stack)
# print(odd_stack)

# print('Even-Spins')
# for data_point in even_stack:
#     result = finder.Search_Energies(even_stack, odd_stack, data_point[0])
#     if(result != -1):
#         print(data_point[0], result)

# print('Odd-Spins')
# for data_point in odd_stack:
#     result = finder.Search_Energies(odd_stack, even_stack, data_point[0])
#     if(result != -1):
#         print(data_point[0], result)


def TEST():
    print('EVEN-SPINS -> TEST')

    [print(f'I={spin} -> {finder.Search_Energy_Partner(even_stack, odd_stack, spin)}')
     for spin in range(0, 20, 2)]

    print('ODD-SPINS -> TEST')

    [print(f'I={spin} -> {finder.Search_Energy_Partner(even_stack, odd_stack, spin)}')
     for spin in range(1, 19, 2)]
