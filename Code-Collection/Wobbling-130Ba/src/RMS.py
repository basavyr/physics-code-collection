import numpy as np
import math


def Compute_Chi_Squared(exp_data, th_data):
    """
    Evaluates the root mean square value (chi-squared) for a set of theoretical energies
    The theoretical energies are obtained from a fitting procedure
    Comparison with the experimental data from the available data sets
    """

    # stop if any of the experimental values are null
    contains_null = any(x == 0 for x in exp_data)
    if (contains_null):
        return -1

    # define the number of data-points
    N = len(th_data)+1

    chi_sum = 0
    for idx in range(len(exp_data)):
        f1 = np.power(th_data[idx]-exp_data[idx], 2)
        f2 = exp_data[idx]
        chi_sum += float(f1/f2)

    chi_2 = math.sqrt(1.0/N*chi_sum)

    return chi_2
