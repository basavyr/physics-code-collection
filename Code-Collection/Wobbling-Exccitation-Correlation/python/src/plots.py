
def chi_plotter(exp_data, th_data):
    # unpacking
    spins, experimental_energy = exp_data
    # no need to unpack the spins twice
    _, theoretical_energy = th_data
    plt.plot(spins, exp_data, 'ok', label='Exp.')
    plt.plot(spins, th_data, '--*b', label='Th.')
    plt.legend(loc='best')
    plt.savefig('chi_plot.pdf', dpi=300)
    plt.close()