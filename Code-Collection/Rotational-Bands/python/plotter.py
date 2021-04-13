import matplotlib.pyplot as plt

import numpy.random as rd


def PlotData(data):
    print(f'The program is evaluating N={len(data)} data sets')
    a_label = data[1]
    count = 0
    for data_set in data[0]:
        random_color = (rd.random(), rd.random(), rd.random())
        spins = data_set[0]
        energies = data_set[1]
        plt.plot(spins, energies, color=random_color, linestyle=rd.choice(['-', '--', '-.', ':']), linewidth=0.5, marker='o', markersize=2,
                 label=f'a={a_label[count]}')
        count += 1
    plt.legend(loc='best')
    plt.xlabel(r'I [$\hbar$]')
    plt.ylabel(r'E(I)')
    plt.title('The energy spectrum for a K=1/2 band\nfor different coupling parameters')
    plt.savefig('good.pdf', dpi=1200, bbox_inches='tight')
    plt.close()
