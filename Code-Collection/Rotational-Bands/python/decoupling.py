#! /Users/robertpoenaru/.pyenv/versions/3.8.6/envs/numerical/bin/python

import numpy as np
import matplotlib.pyplot as plt

# The angular momentum component along the x-axis (rotational axis)
# I_x is the total angular momentum projected ono the x-axis


def I_x(I):
    I_m = I - 1
    K_values = np.arange(-I + 1, I, 1)
    I_x_components = []
    for K in K_values:
        I_m_squared = np.power(I_m + 1 / 2, 2)
        IK_diff = I_m_squared - np.power(K, 2)
        current_I_m = np.sqrt(IK_diff)
        I_x_components.append([K, current_I_m])
    return I_x_components


print(I_x(4))
