import numpy as np
import matplotlib.pyplot as plt

MAXVAL = 69696969696969


def energy(n, spin, moi1, moi2, moi3):
    if(moi1 == moi2 or moi1 == moi3 or moi2 == moi3):
        return MAXVAL

    t_rotor = 1.0/(2.0*moi1)*spin*(spin+1.0)
    t_wobbling = 2.0*spin * \
        np.sqrt((1.0/(2.0*moi1)-1.0/(2.0*moi3))
                * (1.0/(2.0*moi2)-1.0/(2.0*moi3)))

    return t_rotor+t_wobbling


def search_energy():
    moi1 = np.arange(0.5, 120, 0.1)
    moi2 = np.arange(0.5, 120, 0.1)
    moi3 = np.arange(0.5, 120, 0.1)
    for i1 in moi1:
        print(energy(0, 10, i1, 10, 20))


search_energy()
