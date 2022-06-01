# evaluating the semi-axes lengths for a triaxial ellipsoid
# the required parameters are $\gamma$, $\beta_2$
# each semi-axis has a specific index k

from cProfile import label
from operator import indexOf
import numpy as np
from matplotlib import pyplot as plt

r0 = 1.2


def R_k(k, R_0, beta, gamma):
    # constants
    rad = np.sqrt(5.0/(4.0*np.pi))
    gm = gamma*np.pi/180.0
    pi_23 = 2.0*np.pi/3.0

    # the cosine term defined in terms of the k-index
    cos_term = np.cos(gm-pi_23*k)

    # define the term that depends on the quadrupole deformation
    beta_term = rad*beta*cos_term

    RK = R_0*(1+beta_term)

    return RK


def Show_Axes(beta, gamma):
    R1 = R_k(1, r0, beta, gamma)
    R2 = R_k(2, r0, beta, gamma)
    R3 = R_k(3, r0, beta, gamma)

    # axes = {"R1": R1,
    #         "R2": R2,
    #         "R3": R3,
    #         }
    # print(axes)

    # max_axes = max([ax for _, ax in axes.items()])
    # index_of_max_axes = indexOf(
    #     [ax for _, ax in axes.items()], max_axes)+1
    # # print(index_of_max_axes)
    # print(f'long-axis: {index_of_max_axes}-axis')

    axes = [R1, R2, R3]
    print(f'l-axis: {indexOf(axes,max(axes))+1}')
    axes.pop()
    print(f'm-axis: {indexOf(axes,max(axes))+1}')
    print(f's-axis: {indexOf(axes,min(axes))+1}')


def main():
    beta = 0.35
    gamma = 20

    Show_Axes(beta, gamma)
    do_it = 0

    if(do_it):
        # generate the gamma parameter
        gamma_data = np.arange(-120, 120, 1)
        gamma_1 = [x for x in gamma_data if Show_Axes(beta, x) == 1]
        gamma_2 = [x for x in gamma_data if Show_Axes(beta, x) == 2]
        gamma_3 = [x for x in gamma_data if Show_Axes(beta, x) == 3]

        # generate the semi-axes lengths
        largest_axes_data = [Show_Axes(beta, x) for x in gamma_data]
        largest_axes_data1 = [x for x in largest_axes_data if x == 1]
        largest_axes_data2 = [x for x in largest_axes_data if x == 2]
        largest_axes_data3 = [x for x in largest_axes_data if x == 3]

        fig, ax = plt.subplots()
        plt.plot(gamma_1, largest_axes_data1, '-r', label='s-axis')
        plt.plot(gamma_2, largest_axes_data2, '-b', label='m-axis')
        plt.plot(gamma_3, largest_axes_data3, '-k', label='l-axis')
        plt.legend(loc='best')
        plt.xlabel(r'$\gamma$')
        plt.ylabel(r'$R_k^{max}$')
        fig.tight_layout()
        plt.savefig('local_plot.pdf', dpi=300)
        plt.close()


if __name__ == '__main__':
    main()
