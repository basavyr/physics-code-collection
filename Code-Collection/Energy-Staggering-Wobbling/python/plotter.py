#!/Users/robertpoenaru/.pyenv/shims/python

import matplotlib.pyplot as plt
import numpy.random as rd
from operator import itemgetter


def Plot_Stagger_Bands(STAGGER_DATA, plot_file):
    colors = []
    for _ in STAGGER_DATA:
        random_color = (rd.random(), rd.random(), rd.random())
        colors.append(random_color)
    count = 0
    for data in STAGGER_DATA:
        spins = data[0][0] + data[1][0]
        staggers = data[0][1] + data[1][1]
        final_data = []
        for x in zip(spins, staggers):
            final_data.append(x)
        final_data.sort(key=itemgetter(0))
        spins = [x[0] for x in final_data]
        staggers = [x[1] for x in final_data]
        plt.plot(spins, staggers, '-o', c=colors[count], label=r'Bands (4,5)')
        plt.ylim(0, 30)
        count += 1
    plt.legend(loc='best')
    plt.savefig(plot_file, dpi=1200, bbox_inches='tight')
    plt.close()
