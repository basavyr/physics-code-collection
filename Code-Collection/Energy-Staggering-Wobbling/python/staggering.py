#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt


DATA_STACK_1 = 'data_stack1.dat'
DATA_STACK_2 = 'data_stack2.dat'


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


print(Import_Data(DATA_STACK_1))
