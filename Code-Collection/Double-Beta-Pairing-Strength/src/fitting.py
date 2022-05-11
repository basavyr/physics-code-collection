import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x_data = [int(x.strip()) for x in open('expdata/A-mass.bin').readlines()]
y_data_p = [float(x.strip()) for x in open('expdata/Gp.bin').readlines()]
y_data_n = [float(x.strip()) for x in open('expdata/Gn.bin').readlines()]

x_data = np.asarray(x_data)
y_data_p = np.asarray(y_data_p)
y_data_n = np.asarray(y_data_n)


def model_p(x, a, b):
    gp = b+a*1.0/x
    return gp


def model_n(x, c, d):
    gn = d+c*1.0/x
    return gn


# PROTONS
protonParams, _ = curve_fit(model_p, x_data, y_data_p)
print(protonParams)

# NEUTRONS
neutronParams, _ = curve_fit(model_n, x_data, y_data_n)
print(neutronParams)
