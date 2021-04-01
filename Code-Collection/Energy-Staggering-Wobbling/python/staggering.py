#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt

data_file = 'data.dat'

with open(data_file, 'r+') as data:
    lines = data.readlines()
    data = []
    for line in lines:
        x = line.strip('\n')
        x = x.split(' ')
        if(len(x) == 2):
            spin = float(x[0])
            energy = float(x[1])
            # print(spin, energy)
            data_tuple = [spin, energy]
            data.append(data_tuple)
    print(data)
