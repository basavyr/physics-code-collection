import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def get_task():
    TASK = """
        Iti trimit trei seturi de date.Vreau sa determini prin metoda celor mai 
        mici patrate parametrii a si b astfel ca: Gp=a/A+b 
        La fel sa determini c si d astfel ca Gp=c/A+d 

        A este numarul de masa iar Gp si Gn sunt strength-urile interactiilor de 
        pairing protonic respectiv neutronic. Dupa ce determini parametrii a, b, c 
        si d plotezi Gp=f(1/A) si Gn=f(1/A) OBTII 8 PUNCTE PE UN GRAFIC SI 8 
        PENTRU CELALALT. Pe acelasi grafic treci dreptele cu ecuatiile de mai sus, 
        respectiv. Te rog sa faci astea cat mai repede posibil. Multumesc! 
        """
    print(TASK)


def Get_Data():
    """
    returns:
    1) the X values (atomic mass
    2) the neutron pairing strenghts
    3) the proton pairing strengths
    """
    X = [int(x.strip()) for x in open("expdata/A-mass.bin", 'r+').readlines()]
    # use the inverse values for X for easier implementation of the linear model
    X_L = [np.round(float(1.0/x), 3) for x in X]

    # get the neutron pairing strengths
    G_n = [float(x.strip()) for x in open("expdata/Gn.bin", 'r+').readlines()]

    # get the neutron pairing strengths
    G_p = [float(x.strip()) for x in open("expdata/Gp.bin", 'r+').readlines()]

    return X_L, G_n, G_p


def squared(x):
    return np.power(x, 2)


def Linear_Model(x_data, y_data):
    """
    Performs a linear regression using the least-squares method
    Input: x_data, y_data
    Output: the two parameters b0, b1
    source: https://www.geeksforgeeks.org/linear-regression-python-implementation/
    """

    N1 = len(x_data)
    N2 = len(y_data)
    try:
        assert N1 == N2
    except AssertionError:
        print('The data format is invalid. Cannot perform regression')
        return -1
    else:
        N = N1
    x_mean = np.mean(x_data)
    y_mean = np.mean(y_data)

    # evaluate the squared-deviation sum for x_data Sxx
    # Sxx = sum(list(map(squared, x_data)))-N*x_mean
    Sxx = np.sum(np.array(x_data)*np.array(x_data))-N*x_mean

    # evaluate the cross-deviation sum for x_data and y_Data Sxy
    Sxy = np.sum(np.array(x_data)*np.array(y_data))-N*x_mean*y_mean

    # obtain the two fitting parameters of the model (b0, and b1)
    b1 = np.round(float(Sxy/Sxx), 4)
    b0 = y_mean-b1*x_mean

    print(f'b0 -> {b0}')
    print(f'b1 -> {b1}')

    return b0, b1


def plot_model(particle, params, x_data, y_data):
    _label = r'$\nu' if particle == 1 else r'$\pi'
    _plot_name = 'neutrons.pdf' if particle == 1 else 'protons.pdf'
    plt.plot(x_data, y_data, 'r*', label=_label)
    plt.savefig(f'results/{_plot_name}', bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    # show the main task
    # get_task()

    # get the x-data
    x_data, y_data1, y_data2 = Get_Data()

    # print("**** NEUTRONS ****")
    d, c = Linear_Model(x_data, y_data1)
    # print("**** PROTONS ****")
    b, a = Linear_Model(x_data, y_data2)
