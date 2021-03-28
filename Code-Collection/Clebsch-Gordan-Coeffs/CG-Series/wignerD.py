#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np

import matplotlib.pyplot as plt


import gordan as CGC

# define the imaginary unit
I = 1j

# define the Pauli matrix for a rotation around the Y-axis
Sigma_Y = [[0, -I], [I, 0]]

print(np.array(Sigma_Y))
