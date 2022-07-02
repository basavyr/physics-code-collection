import numpy as np
from scipy.optimize import curve_fit

import data130
import correlations as model


def fitting_procedure():
    x_data = (np.concatenate((data130.Spins.band1[1:], data130.Spins.band2)))

    print(x_data)


fitting_procedure()
