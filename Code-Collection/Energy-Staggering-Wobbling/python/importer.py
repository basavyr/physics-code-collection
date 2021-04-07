#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import numpy.random as rd


def Import_Data(FILE):
    with open(FILE, 'r+') as DATA_STACK:
        # debug mode for extra output
        DEBUG = 0
        if(DEBUG):
            print(f'Importing data with debug mode ACTIVE')
        else:
            print(f'Importing data with debug mode INACTIVE')

        # read the entire data file
        lines = DATA_STACK.readlines()

        # first line contains the information with regards to the band sequences
        # must be removed before making calculations
        lines.pop(0)

        DATA = []
        sub_data = []
        eol_check = len(lines)
        count = 0

        for line in lines:
            x = line.strip('\n')
            x = x.split(' ')
            count = count + 1
            if(DEBUG == 1):
                print(x, count)
            if (len(x) == 2):
                if(DEBUG == 1):
                    print('IN STACK-BUILD')
                    print(x, count)
                spin = float(x[0])
                energy = float(x[1])
                data_tuple = [spin, energy]
                sub_data.append(data_tuple)
            if (count == eol_check and len(x) == 2):
                if(DEBUG == 1):
                    print('IN EOL CHECK')
                    print(sub_data)
                    print(DATA)
                DATA.append(sub_data)
                if(DEBUG == 1):
                    print(DATA)
                sub_data = []
            elif (len(x) == 1 or x[0] == '-'):
                if(DEBUG == 1):
                    print('IN MULTI-BAND')
                    print(sub_data)
                DATA.append(sub_data)
                if(DEBUG == 1):
                    print(DATA)
                sub_data = []
    if(len(DATA) == 0):
        return 'The experimental data stack is empty!'
    else:
        return DATA
