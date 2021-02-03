#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
from numpy import random as rd

import plotter as plt

# choose the path for the file that will contain any debug information during code execution
DEBUG_PATH = 'DEBUG_INFO.DAT'

# units are in keV
SD_BAND2 = [8577.7, 7781.2, 7016.0, 6283.3, 5583.4, 4917.2, 4285.1,
            3687.9, 3126.3, 2601.1, 2113.0, 1662.7, 1250.9, 878.2, 545.1, 252.4, 0]
SD_BAND3 = [8793.2, 7992.6, 7221.3, 6481.3, 5772.8, 5096.7, 4454.0,
            3844.5, 3269.5, 2729.8, 2225.9, 1758.8, 1329.1, 937.6, 585.1, 272.0, 0]
SD_BAND4 = [7659.9, 6870.9, 6114.9, 5391.7, 4704.1, 4053.3,
            3439.0, 2864.0, 2328.6, 1834.5, 1381.9, 971.6, 604.5, 280.9, 0]

# sort and transform to MeV
SD_BAND2 = [x / 1 for x in SD_BAND2]
SD_BAND2 = sorted(SD_BAND2)
SD_BAND3 = [x / 1 for x in SD_BAND3]
SD_BAND3 = sorted(SD_BAND3)
SD_BAND4 = [x / 1 for x in SD_BAND4]
SD_BAND4 = sorted(SD_BAND4)

SPIN_0_B2 = 21.0 / 2.0
SPIN_0_B3 = 23.0 / 2.0
SPIN_0_B4 = 25.0 / 2.0

# the spin sequences for each superdeformed band
SPINS_2 = [SPIN_0_B2 + 2 * N for N in np.arange(0, len(SD_BAND2))]
SPINS_3 = [SPIN_0_B3 + 2 * N for N in np.arange(0, len(SD_BAND3))]
SPINS_4 = [SPIN_0_B4 + 2 * N for N in np.arange(0, len(SD_BAND4))]


# print(
#     f'Max spin-states from each band are: IM_2={int(2*SPINS_2[len(SPINS_2)-1])}/2 | IM_3={int(2*SPINS_3[len(SPINS_3)-1])}/2 | IM_2={int(2*SPINS_3[len(SPINS_3)-1])}/2')

# print(f'B2: {int(2*SPINS_2[0])}/2 --->{int(2*SPINS_2[len(SPINS_2)-1])}/2')
# print(f'B3: {int(2*SPINS_3[0])}/2 --->{int(2*SPINS_3[len(SPINS_3)-1])}/2')
# print(f'B4: {int(2*SPINS_4[0])}/2 --->{int(2*SPINS_4[len(SPINS_4)-1])}/2')

# the energy corresponding to each spin state from the superdeformed bands
BAND2 = list(zip(SPINS_2, SD_BAND2))
BAND3 = list(zip(SPINS_3, SD_BAND3))
BAND4 = list(zip(SPINS_4, SD_BAND4))


debug_file = open(DEBUG_PATH, 'w')


# calculates the (in-band) transition between two states within a given band
# the transition energy is given by the difference E(I1)-E(I2), where I2=I1-2
# any in-band transition is given by the quadrupole e.m. decay I->I-2
def Gamma_Transitions(band):
    gammas = []
    for id in range(len(band) - 1):
        gamma = band[id + 1] - band[id]
        gammas.append(gamma)
    return gammas


# gives the difference in energy between the I-state and (I-2)-state
def E_gamma(band, spin, type):
    # unpack the band tuple list in order to generate an array with spins and one with energies
    # both arrays will be used for calculating the energy difference of a certain spin-state
    S, E = zip(*band)
    I = spin
    IM2 = I - 2
    # print(f'searching for the transition {I} -> {IM2} in the {type} band...')
    debug_file.writelines(
        f'searching for the transition {I} -> {IM2} in the {type} band...\n')
    first_index = '0'
    second_index = '0'
    try:
        id_I = S.index(I)
    except ValueError:
        first_index = '0'
    else:
        first_index = '1'

    try:
        id_IM2 = S.index(IM2)
    except ValueError:
        second_index = '0'
    else:
        second_index = '1'

    if(first_index == '1' and second_index == '1'):
        # print('OK')
        debug_file.writelines(
            'Transition found. Computing the E_gamma energy is successful...\n')
        E_gamma = round(E[id_I] - E[id_IM2], 3)
        return E_gamma

    # print(f'There is no transition {I}->{IM2} in the {type} band:')
    debug_file.writelines(
        f'There is no transition {I}->{IM2} in the {type} band:\n')

    if(first_index == '0'):
        # print(f'State {I} does not belong to the {type} band!')
        debug_file.writelines(
            f'State {I} does not belong to the {type} band!\n')
        return 6969

    if(second_index == '0'):
        debug_file.writelines(
            f'State {IM2} does not belong to the {type} band!\n')
        return 6969

    return 6969


# calculate the staggering parameter $\Delta E_gamma2$
# formula taken from the "staggering_formula.png" file
# any e_gamma will be evaluated from I -> I-2 transition scheme
# E.g., if the state is I+2, then the Stagger method will calculate the transitions (I+2)+2->I+2, I+2->I, and (I+2)+1->(I+2)-1
def Stagger(band_1, band_2, spin):
    I = spin
    IP1 = I + 1
    IP2 = I + 2
    # print(f'I={I}')
    debug_file.writelines(f'**********\n')
    debug_file.writelines(
        f'Evaluating the staggering parameter for state I={I}\n')
    # print(
    #     f'Staggering will look for the transitions: {I+2}->{I} | {I}->{I-2} | {I+1}->{I-1}')
    debug_file.writelines(
        f'Staggering will look for the transitions: {I+2}->{I} | {I}->{I-2} | {I+1}->{I-1}\n')
    # print('E_gamma | I+2->I')
    debug_file.writelines('E_gamma | I+2->I\n')
    e_gamma_plus = E_gamma(band_1, IP2, 'favored')
    # print('E_gamma | I->I-2')
    debug_file.writelines('E_gamma | I->I-2\n')
    e_gamma_minus = E_gamma(band_1, I, 'favored')
    # print('E_gamma | I+1->I-1')
    debug_file.writelines('E_gamma | I+1->I-1\n')
    e_gamma_partner = E_gamma(band_2, IP1, 'un-favored')
    if(e_gamma_partner == 6969 or e_gamma_minus == 6969 or e_gamma_plus == 6969):
        return 6969
    stagger = 0.5 * (e_gamma_plus + e_gamma_minus) - e_gamma_partner
    debug_file.writelines(f'\n')
    return stagger


# based on the value of a single stagger parameter associated to a spin-state I
# generate an array of staggering parameters, for all I's from a given band
# the stagger parameter for an I-state belonging on band_1 needs information with regards to a transition from band_2
def GenerateStaggerBands(band_1, band_2):
    ret_spins = []
    ret_staggers = []
    for I, E_I in band_1:
        S_I = Stagger(band_1, band_2, I)
        if(S_I != 6969):
            ret_spins.append(I)
            ret_staggers.append(round(S_I, 4))
    return [ret_spins, ret_staggers]


band2_spins, band2_staggers = GenerateStaggerBands(BAND2, BAND3)
band3_spins, band3_staggers = GenerateStaggerBands(BAND3, BAND4)

plot_data = [[band2_spins, band2_staggers, '^-r', 'band2'],
             [band3_spins, band3_staggers, 'o-k', 'band3']]

plt.PlotData(plot_data, 'staggering.png', 'x', 'y', 'extra')

# plt.rcParams.update({'font.size': 15})

# fig, ax = plt.subplots()

# plt.plot(x_2, y_2, 'o-r', label='band2')
# plt.plot(x_3, y_3, 'o-k', label='band3')
# ax.legend(loc='best')
# ax.set_xlabel(r'$I\ [\hbar]$')
# ax.set_ylabel(r'$E_\gamma(relative)$')
# plt.text(0.5, 0.5, r'$^{191}Hg$', horizontalalignment='center',
#          verticalalignment='center', transform=ax.transAxes)
# plt.savefig('staggering.pdf', dpi=600, bbox_inches='tight')
# plt.close()


# x_2 = []
# y_2 = []
# for spin in SPINS_BAND2:
#     s = Stagger(BAND2, BAND3, spin)
#     if(s != 6969):
#         x_2.append(spin)
#         y_2.append(s)
#         # print(spin, s)

# x_3 = []
# y_3 = []
# for spin in SPINS_BAND3:
#     s = Stagger(BAND3, BAND4, spin)
#     if(s != 6969):
#         x_3.append(spin)
#         y_3.append(s)
#         # print(spin, s)

# plt.plot(x_2, y_2, 'o-r', label='favored-b2')
# plt.plot(x_3, y_3, 's-k', label='unfavored-b3')
# plt.legend(loc='best')
# plt.savefig('Delta_staggering.pdf', dpi=600, bbox_inches='tight')
# plt.close()
