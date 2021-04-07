#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt


RU_108 = '108Ru.dat'
RU_110 = '110Ru.dat'
RU_112 = '112Ru.dat'


def Import_Data(FILE):
    with open(FILE, 'r+') as DATA_STACK:
        lines = DATA_STACK.readlines()
        DATA = []
        sub_data = []
        eol_check = len(lines)
        count = 0
        for line in lines:
            x = line.strip('\n')
            x = x.split(' ')
            count = count + 1
            # print(x, count)
            if (len(x) == 2):
                # print('IN STACK-BUILD')
                # print(x, count)
                spin = float(x[0])
                energy = float(x[1])
                data_tuple = [spin, energy]
                sub_data.append(data_tuple)
            if (count == eol_check and len(x) == 2):
                # print('IN EOL CHECK')
                # print(sub_data)
                # print(DATA)
                DATA.append(sub_data)
                # print(DATA)
                sub_data = []
            elif (len(x) == 1):
                # print('IN MULTI-BAND')
                # print(sub_data)
                DATA.append(sub_data)
                # print(DATA)
                sub_data = []
    if(len(DATA) == 0):
        return 'The experimental data stack is empty!'
    else:
        return DATA


# Definition of the staggering parameter as defined by Luo et al (2009)
def Stagger_Parameter(I, E1, E2):
    return (E2 - E1) / 2.0 * I


# Definition of the staggering parameter in signature partner bands
# As defined by Uma et al (2015)


for stack in Import_Data(RU_112):
    print(stack)
