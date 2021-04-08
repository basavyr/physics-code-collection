#!/Users/robertpoenaru/.pyenv/shims/python

import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter


def Plot_Stagger_Bands(data, plot_file):
    spins1 = data[0][0]
    staggers1 = data[0][1]
    spins2 = data[1][0]
    staggers2 = data[1][1]
    for spin2 in spins2:
        spins1.append(spin2)
    for stagger2 in staggers2:
        staggers1.append(stagger2)
    data = []
    for x in zip(spins1, staggers1):
        data.append(x)
    data.sort(key=itemgetter(0))
    spins = [x[0] for x in data]
    staggers = [x[1] for x in data]
    plt.plot(spins, staggers, '-or', label=r'Bands (4,5)')
    plt.ylim(6,30)
    plt.legend(loc='best')
    # plt.plot(spins2, staggers2, '-ob', label=r'S2')
    plt.savefig(plot_file, dpi=1200, bbox_inches='tight')
    plt.close()
