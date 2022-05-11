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


if __name__ == '__main__':
    get_task()
    # get the x-data
    print(Get_Data())
