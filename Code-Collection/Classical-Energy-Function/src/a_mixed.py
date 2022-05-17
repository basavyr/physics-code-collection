import matplotlib.pyplot as plt
import numpy as np


# local module with the canonical factors
import factors as A


plot_location = './results'
# path to the figure folder on MacBook Air
figure_path_air = "/Users/basavyr/Documents/Work/PhD/phdthesis/Chapters/Figures"


# set the canonical coordinates
varphi_list = np.linspace(0, 180, 100)
psi_list = np.linspace(0, 180, 100)
X, Y = np.meshgrid(varphi_list, psi_list)
Z = A.Canonical.A_mixed([1, 3, 7], X, Y)


# use latex for matplotlib plot python
plt.rcParams.update({
    "text.usetex": True})


# use custom size
# source: https://stackoverflow.com/questions/332289/how-do-i-change-the-size-of-figures-drawn-with-matplotlib
# plt.rcParams["figure.figsize"] = (5, 4)
plt.rcParams["figure.figsize"] = (10, 5)
# reset the plot size
# plt.rcParams['figure.figsize'] = plt.rcParamsDefault['figure.figsize']


# change the font size
# source: https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
plt.rcParams.update({'font.size': 24})

fig, ax = plt.subplots(2, 3)
# ax.set_xlabel(r'$\varphi$ $[^\circ]$')
# ax.set_ylabel(r'$\psi$ $[^\circ]$')
ax[0, 0].contourf(X, Y, Z)
ax[0, 1].contourf(X, Y, Z)
ax[0, 2].contourf(X, Y, Z)
ax[1, 0].contourf(X, Y, Z)
ax[1, 1].contourf(X, Y, Z)
ax[1, 2].contourf(X, Y, Z)
# ax.set_title('Filled Contours Plot')
plt.tight_layout()
plt.savefig(f'{plot_location}/A_mixed_1.pdf', dpi=300)
plt.close()
