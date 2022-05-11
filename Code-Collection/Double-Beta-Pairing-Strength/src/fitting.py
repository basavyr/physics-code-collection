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
    gp = b+a*np.float64(1.0/x)
    return gp


def model_n(x, c, d):
    gn = d+c*np.float64(1.0/x)
    return gn


def Plot_Model(particle, params, x_data, y_data):
    """
    Plot the experimental and fitted data using the set of parameters given as arguments\n
    Particle == 1 => NEUTRONS\n
    Particle == O => PROTONS\n
    """
    _label = r'$\nu' if particle == 1 else r'$\pi'
    _plot_name = 'neutrons.pdf' if particle == 1 else 'protons.pdf'

    if(particle == 1):
        y_data_th = [model_n(x, params[0], params[1]) for x in x_data]
    else:
        y_data_th = [model_p(x, params[0], params[1]) for x in x_data]

    plt.plot(x_data, y_data, 'bo', label=_label)
    plt.plot(x_data, y_data_th, 'r-', label='model')
    ax = plt.gca()
    # ax.set_xlim([xmin, xmax])
    ax.set_ylim([0, 0.5])
    plt.savefig(f'results/{_plot_name}', bbox_inches='tight')
    plt.close()


def Main():
    # PROTONS
    protonParams, _ = curve_fit(model_p, x_data, y_data_p)
    print(protonParams)
    Plot_Model(0, protonParams, x_data, y_data_p)

    # NEUTRONS
    neutronParams, _ = curve_fit(model_n, x_data, y_data_n)
    print(neutronParams)
    Plot_Model(1, neutronParams, x_data, y_data_n)


if __name__ == '__main__':
    Main()
