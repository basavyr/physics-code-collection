#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt

data_file = 'data.dat'

with open(data_file, 'r+') as data:
    lines = data.readlines()
    data = []
    sub_data = []
    eol_check = len(lines)
    count = 0
    for line in lines:
        x = line.strip('\n')
        x = x.split(' ')
        count = count + 1
        if(len(x) == 1):
            data.append(sub_data)
            sub_data = []
        elif count == eol_check:
            data.append(sub_data)
            sub_data = []
        elif (len(x) == 2):
            spin = float(x[0])
            energy = float(x[1])
            data_tuple = [spin, energy]
            sub_data.append(data_tuple)
for big_data in data:
    print(big_data)
