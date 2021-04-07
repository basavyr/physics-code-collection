#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import numpy.random as rd

data_odd = [[x, rd.randint(1, 5)] for x in range(1, 15, 2)]
data_even = [[x, rd.randint(2, 6)] for x in range(2, 16, 2)]

print(data_even)
print(data_odd)


# Function that searches within a list of data-points of the form [(SPIN,ENERGY)] and returns the index of the found item
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


def Search_Partner(even_data, odd_data, spin):
    OK = 0
    if(spin % 2 == 0):
        band = even_data
        partner = odd_data
        index = Search_Spin(band, spin)
        if(index == -1):
            # print(
            #     f'Even-Spin state ({band[index][0]},{band[index][1]}) not found within the data')
            return -1
        if(index == 0):
            # print(
            #     f'Even-Spin state ({band[index][0]},{band[index][1]}) is the band-head')
            return -1
        partner_index = Search_Spin(partner, spin - 1)
    else:
        band = odd_data
        partner = even_data
        index = Search_Spin(band, spin)
        if(index == -1):
            # print(
            #     f'Odd-Spin state ({band[index][0]},{band[index][1]}) not found within the data')
            return -1
        if(index == 0):
            # print(
            #     f'Odd-Spin state ({band[index][0]},{band[index][1]}) is the band-head')
            return -1
        partner_index = Search_Spin(partner, spin - 1)

    # find the spin and energy of the band, based on the current spin value
    I_band = band[index][0]
    E_band = band[index][1]

    # find the spin-1 and energy corresponding to the partner band, based on the current spin value
    I_partner = partner[partner_index][0]
    E_partner = partner[partner_index][1]

    # print(I_band, E_band)
    # print(I_partner, E_partner)
    return [I_partner, E_partner]
    # return [[I_band, E_band], [I_partner, E_partner]]


[print(f'I_band={x} -> partner: {Search_Partner(data_even, data_odd, x)}')
 for x in range(1, 10, 1)]

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
