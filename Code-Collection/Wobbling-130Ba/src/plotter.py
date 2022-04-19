import matplotlib.pyplot as plt


def plotData(spins, energies, plotname):
    plotfile = f'wobbling-plot-{str(plotname)}.pdf'

    plt.plot(spins, energies, 'r-o', label='data')
    plt.legend(loc='best')
    plt.xlabel('spins')
    plt.ylabel('energy')
    plt.savefig(plotfile, dpi=300, bbox_inches='tight')
    plt.close()
