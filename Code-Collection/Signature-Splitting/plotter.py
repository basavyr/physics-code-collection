#!/Users/robertpoenaru/.pyenv/shims/python

import matplotlib.pyplot as plt
from matplotlib import rc


MAX_DPI = 800
BBOX = 'tight'


# data is a list of tuples with the form [SPINS,STAGGERS,PLOT-STYLE,PLOT-LABEL]
def PlotData(data, FILE, xlabel, ylabel, extra_text):
    # preamble set
    plt.rcParams.update({'font.size': 15})

    fig, ax = plt.subplots()
    for x, y, plot_style, plot_label in data:
        plt.plot(x, y, plot_style, label=plot_label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.text(0.15, 0.15, extra_text, horizontalalignment='center',
             verticalalignment='center', transform=ax.transAxes)
    ax.legend(loc='best')
    plt.savefig(FILE, dpi=MAX_DPI, bbox_inches=BBOX)
    plt.close()


def LinePlot(E_DATA, SPINS, styles, labels, file, extra_text):
    # preamble set
    plt.rcParams.update({'font.size': 13})

    fig, ax = plt.subplots()
    x_0 = 1
    x_1 = 2
    for E, Spin, Style, Label in zip(E_DATA, SPINS, styles, labels):
        ys = [[e, e] for e in E]
        y0 = ys[0]
        for y, s in zip(ys, Spin):
            if(y == y0):
                plt.plot([x_0, x_1], y, Style, label=Label)
                plt.text(x_0, y[0] + 5, f'{int(2*s)/2}' + r'$^+$')

            else:
                plt.plot([x_0, x_1], y, Style)
                plt.text(x_0, y[0] + 5, f'{int(2*s)/2}' + r'$^+$')
        x_0 = x_1 + 0.5
        x_1 = x_1 + 1.5
    ax.set_xlabel('')
    # plt.axis('off')
    plt.xticks([])
    ax.set_ylabel(r'$E\ [keV]$')
    ax.legend(loc='best')
    plt.text(0.15, 0.07, extra_text, horizontalalignment='center',
             verticalalignment='center', transform=ax.transAxes)
    plt.savefig(file, dpi=MAX_DPI, bbox_inches=BBOX)
    plt.close()
