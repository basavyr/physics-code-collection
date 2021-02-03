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
    ax.legend(loc='best')
    plt.savefig(FILE, dpi=MAX_DPI, bbox_inches=BBOX)
    plt.close()
