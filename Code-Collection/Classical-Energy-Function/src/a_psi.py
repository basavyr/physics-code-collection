import matplotlib.pyplot as plt
import numpy as np


# local module with the canonical factors
import factors as A


plot_location = './results'
# path to the figure folder on MacBook Air
figure_path_air = "/Users/basavyr/Documents/Work/PhD/phdthesis/Chapters/Figures"


# generate angles
x = np.arange(0, 180, 5)


# evaluate the canonical factor
y1 = A.Canonical.A_psi([1, 3, 7], x)
y2 = A.Canonical.A_psi([1, 7, 3], x)
y3 = A.Canonical.A_psi([7, 3, 1], x)
y4 = A.Canonical.A_psi([7, 1, 3], x)
y5 = A.Canonical.A_psi([3, 1, 7], x)
y6 = A.Canonical.A_psi([3, 7, 1], x)


# use latex for matplotlib plot python
plt.rcParams.update({
    "text.usetex": True})


# use custom size
# source: https://stackoverflow.com/questions/332289/how-do-i-change-the-size-of-figures-drawn-with-matplotlib
# plt.rcParams["figure.figsize"] = (5, 4)
plt.rcParams["figure.figsize"] = (7, 6)
# reset the plot size
# plt.rcParams['figure.figsize'] = plt.rcParamsDefault['figure.figsize']


# change the font size
# source: https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
plt.rcParams.update({'font.size': 26})

# create the first plot
plt.xlabel(r'$\psi$ $[^\circ]$')
plt.ylabel(r'$\mathcal{A}_\psi\ [\hbar^{-2}$MeV$]$')
plt.plot(x, y1, '-r', label=r'$A_1<A_2<A_3$')
plt.plot(x, y2, '-b', label=r'$A_1<A_3<A_2$')
plt.plot(x, y3, '-k', label=r'$A_3<A_2<A_1$')
plt.rc('legend', fontsize=22)    # legend fontsize
plt.legend(loc='best', framealpha=0.0)
plt.tight_layout()
plt.savefig(f'{figure_path_air}/A_psi_1.pdf', dpi=300)
plt.close()

# create the second plot
plt.xlabel(r'$\psi$ $[^\circ]$')
plt.ylabel(r'$\mathcal{A}_\psi\ [\hbar^{-2}$MeV$]$')
plt.plot(x, y4, '-r', label=r'$A_2<A_3<A_1$')
plt.plot(x, y5, '-b', label=r'$A_2<A_1<A_3$')
plt.plot(x, y6, '-k', label=r'$A_3<A_1<A_2$')
plt.rc('legend', fontsize=22)    # legend fontsize
plt.legend(loc='best', framealpha=0.0)
plt.tight_layout()
plt.savefig(f'{figure_path_air}/A_psi_2.pdf', dpi=300)
plt.close()
