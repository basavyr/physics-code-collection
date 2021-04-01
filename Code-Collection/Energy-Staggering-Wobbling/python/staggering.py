#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt

data_file = 'data.dat'

with open(data_file, 'r+') as data:
    lines = data.readlines()
    lines.pop(len(lines)-1)
    numbers=[]
    for line in lines:
        x=line.strip('\n')
        print(x.split(' '))
