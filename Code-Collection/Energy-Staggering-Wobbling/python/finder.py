#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import numpy.random as rd
from operator import itemgetter

band = [[x, rd.randint(1, 5)] for x in range(1, 17, 2)]
partner = [[x, rd.randint(2, 6)] for x in range(2, 16, 2)]


# Function that searches for the SPIN within a list of data-points of the form [(SPIN,ENERGY)] and returns the index of the found item
# The searching procedure is only looking for the first item within each pair (that is x1 from (x1,x2))
def Search_Spin(obj, spin):
    count = 0
    for data_point in obj:
        if(spin == data_point[0]):
            # print(f'Found {spin} on position {count+1} within the list -> E=data_point[1]}')
            return count
        else:
            count += 1
    return -1


# Function that searches for the ENERGY within a list of data-points of the form [(SPIN,ENERGY)] and returns the index of the found item
# The searching procedure is only looking for the first item within each pair (that is x1 from (x1,x2))
def Search_Energy(obj, energy):
    count = 0
    for data_point in obj:
        if(energy == data_point[1]):
            # print(f'Found {energy} on position {count+1} within the list -> I=data_point[0]}')
            return count
        else:
            count += 1
    return -1


def Random_Even(range):
    OK = 1
    while OK:
        even_test = rd.randint(range[0], range[1])
        if(even_test % 2 == 0):
            print(even_test)
            return even_test


def Random_Odd(range):
    OK = 1
    while OK:
        even_test = rd.randint(range[0], range[1])
        if(even_test % 2 != 0):
            print(even_test)
            return even_test


# check if the spin-state is a band-head for that particular data set
def Band_Head_Check(spin, data):
    return 1 if spin == min([data[i][0] for i in range(len(data))]) else 0


# check if the spin-state is a band-terminus for that particular data set
def Band_Terminus_Check(spin, data):
    return 1 if spin == max([data[i][0] for i in range(len(data))]) else 0


# search for the energy state corresponding to I+1, I-1 and I-2 for a band and its signature partner
# function assumes that the spin->band->partner are properly introduced
# no determination of the actual spin-state is made
def Search_Energies(band, partner, spin):
    DEBUG_MODE = False

    if(DEBUG_MODE):
        print(f'Band = {band}')
        print(f'Partner = {partner}')

    I = spin

    index_I = Search_Spin(band, I)
    if(index_I == -1):
        if(DEBUG_MODE):
            print(f'The state I={spin} does not exist within the band')
        E_b_I = False
        return -1
    else:
        E_b_I = band[index_I][1]

    if(Band_Head_Check(spin, band)):
        if(DEBUG_MODE):
            print(f'I={spin} is band-head -> can`t compute I-2')
        return -1

    max_partner_spin = max(partner, key=itemgetter(0))
    if(Band_Terminus_Check(spin, band) and spin > max_partner_spin[0]):
        if(DEBUG_MODE):
            print(
                f'The state I={spin} is a band terminus and it has no I+1 state in its partner band')
        return -1

    IM1 = I - 1
    IP1 = I + 1
    IM2 = I - 2

    E_b_IM2 = False
    E_p_IP1 = False
    E_p_IM1 = False

    if(DEBUG_MODE):
        print(f'I={band[index_I][0]} | E_b[{spin}]={E_b_I}')

    index_IM2 = Search_Spin(band, IM2)
    E_b_IM2 = band[index_IM2][1]
    if(DEBUG_MODE):
        print(f'I-2={band[index_IM2][0]} | E_b[{IM2}]={E_b_IM2}')

    index_IP1 = Search_Spin(partner, IP1)
    if(index_IP1 == -1):
        if(DEBUG_MODE):
            print(
                f'I={spin} is a band-terminus and it has no I+1 state in its partner band')
        return
    else:
        E_p_IP1 = partner[index_IP1][1]
        if(DEBUG_MODE):
            print(f'I+1={partner[index_IP1][0]} | E_p[{IP1}]={E_p_IP1}')

    index_IM1 = Search_Spin(partner, IM1)
    if(index_IM1 == -1):
        if(DEBUG_MODE):
            print(f'I={spin} does not have an I-1 spin state in its partner band')
        return
    else:
        E_p_IM1 = partner[index_IM1][1]
        if(DEBUG_MODE):
            print(
                f'I-1={partner[index_IM1][0]} | E_p[{IM1}]={E_p_IM1}')

    E_TUPLE = [E_b_I, E_b_IM2, E_p_IP1, E_p_IM1]

    if(all(E_TUPLE)):
        # print(f'E={E_b_I}', f'EM2={E_b_IM2}', f'EP1={E_p_IP1}', f'EM1={E_p_IM1}')
        if(DEBUG_MODE):
            print(f'Found all the energies for the spin-state I={spin}')
        return E_TUPLE
    else:
        if(DEBUG_MODE):
            print(
                f'Failed to obtain all the energies for the spin-state I={spin}')
        return -1
    return -1


# search for the energy corresponding to I within that band, and the energy of its I-1 state from the partner band
def Search_Energy_Partner(even_data, odd_data, spin):
    DEBUG_MODE = 0
    BAND_HEAD = 0
    if(spin % 2 == 0):
        band = even_data
        partner = odd_data
        index = Search_Spin(band, spin)
        # condition for a band-head
        if(Band_Head_Check(spin, band)):
            if(DEBUG_MODE):
                print(
                    f'🤦‍♂️ Even-Spin state ({band[index][0]},{band[index][1]}) is the band-head 🥺')
            pass
        # rest of conditional set
        if(index == -1):
            if(DEBUG_MODE):
                print(
                    f'🤷‍♂️ Even-Spin state I={int(spin)} not found within the data 🙈')
            return -1
        partner_index = Search_Spin(partner, spin - 1)
        if(partner_index == -1):
            if(DEBUG_MODE):
                print(
                    f'🤷‍♂️ The spin state I-1={int(spin-1)} does not exist within the partner band 😢')
            return -1
    else:
        band = odd_data
        partner = even_data
        index = Search_Spin(band, spin)
        # condition for a band-head
        if(Band_Head_Check(spin, band)):
            if(DEBUG_MODE):
                print(
                    f'🤦‍♂️ Even-Spin state ({band[index][0]},{band[index][1]}) is the band-head 🥺')
            pass
        # rest of conditional set
        if(index == -1):
            if(DEBUG_MODE):
                print(
                    f'🤷‍♂️ Odd-Spin state I={int(spin)} not found within the data 🙈')
            return -1
        partner_index = Search_Spin(partner, spin - 1)
        if(partner_index == -1):
            if(DEBUG_MODE):
                print(
                    f'🤷‍♂️ The spin state I-1={int(spin-1)} does not exist within the partner band 😢')
            return -1

    # find the spin and energy of the band, based on the current spin value
    I_band = band[index][0]
    E_band = band[index][1]

    # find the spin-1 and energy corresponding to the partner band, based on the current spin value
    I_partner = partner[partner_index][0]
    E_partner = partner[partner_index][1]

    # print(I_band, E_band)
    # print(I_partner, E_partner)
    return [E_band, E_partner]
    # return [[I_band, E_band], [I_partner, E_partner]]


# [print(f'I_band={x} -> partner: {Search_Partner(data_even, data_odd, x)}')
#  for x in range(1, 10, 1)]

# T = Search_Spin(data_even, Random_Even([0, 20]))
# if(T == -1):
#     print(T)
# else:
#     print(T + 1)

# T = Search_Spin(data_odd, Random_Odd([0, 20]))
# if(T == -1):
#     print(T)
# else:
#     print(T + 1)
