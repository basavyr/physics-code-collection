#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt


RU_108_FILE = '108Ru.dat'
RU_110_FILE = '110Ru.dat'
RU_112_FILE = '112Ru.dat'


def Import_Data(FILE):
    with open(FILE, 'r+') as DATA_STACK:
        lines = DATA_STACK.readlines()
        lines.pop(0)
        # print(lines)
        DATA = []
        sub_data = []
        eol_check = len(lines)
        count = 0
        DEBUG = 1
        if(DEBUG == 1):
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
                elif (len(x) == 1 or x[0] == '-'):
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


RU_108_DATA = Import_Data(RU_108_FILE)
RU_110_DATA = Import_Data(RU_110_FILE)
RU_112_DATA = Import_Data(RU_112_FILE)

# for stack in RU_108_DATA:
#     print(stack)

# for stack in RU_110_DATA:
#     print(stack)

for stack in RU_112_DATA:
    print(stack)
