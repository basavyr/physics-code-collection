from configparser import Interpolation
import matplotlib.pyplot as plt
import numpy as np


# local module with the canonical factors
import factors as A


plot_location = './results'
figures_path_air = "/Users/basavyr/Documents/Work/PhD/phdthesis/Chapters/Figures"
figures_path_mini = "/Users/basavyr/Desktop/phd/phdthesis/Chapters/Figures"

# set the single-particle j-shell
jshell = 6.5

# set the canonical coordinates
f_list = np.linspace(0, 2*jshell, 200)
psi_list = np.linspace(0, 180, 200)
X, Y = np.meshgrid(f_list, psi_list)
Z_123 = A.Canonical.A_gamma(-30, jshell, X, Y)
Z_132 = A.Canonical.A_gamma(0, jshell, X, Y)
Z_213 = A.Canonical.A_gamma(25, jshell, X, Y)
Z_231 = A.Canonical.A_gamma(55, jshell, X, Y)
# Z_312 = A.Canonical.A_gamma(30, jshell, X, Y)
# Z_321 = A.Canonical.A_gamma(45, jshell, X, Y)


plt.rcParams.update({"text.usetex": True})
plt.rcParams["figure.figsize"] = (8, 7)
plt.rcParams.update({'font.size': 16})
plt.rc('axes', titlesize=14)
plt.rcParams["image.cmap"] = 'RdBu_r'

fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)


plt.xticks(np.arange(0, 2*jshell, 3))
plt.yticks(np.arange(0, 181, 60))

im1 = ax[0, 0].contourf(X, Y, Z_123, levels=21)
ax[0, 0].set_title(r'$\gamma=-30^\circ$')
im2 = ax[0, 1].contourf(X, Y, Z_132,  levels=21, antialiased=True)
ax[0, 1].set_title(r'$\gamma=0^\circ$')
im3 = ax[1, 0].contourf(X, Y, Z_213,  levels=21, antialiased=True)
ax[1, 0].set_title(r'$\gamma=20^\circ$')
im4 = ax[1, 1].contourf(X, Y, Z_231,  levels=21, antialiased=True)
ax[1, 1].set_title(r'$\gamma=30^\circ$')
ax[1, 0].set(xlabel=r'$f [\hbar]$', ylabel=r'$\psi$ $[^\circ]$')
# im5 = ax[2, 0].contourf(X, Y, Z_312,  levels=21, antialiased=True)
# ax[2, 0].set_title(r'\gamma=30^\circ')
# im6 = ax[2, 1].contourf(X, Y, Z_321,  levels=21, antialiased=True)
# ax[2, 1].set_title(r'$\gamma=45^\circ$')

imgs = [im1, im2, im3, im4]
axis_list = [ax[0, 0], ax[0, 1], ax[1, 0], ax[1, 1]]

for bars in zip(imgs, axis_list):
    fig.colorbar(bars[0], ax=bars[1], drawedges=False,
                 extend=None, ticks=[-0.8, -0.4, 0, 0.4, 0.8])


plt.tight_layout()
plt.subplots_adjust(wspace=0.18, hspace=0.15)
plt.savefig(f'{figures_path_mini}/A_gamma.pdf', dpi=600, pad_inches=0)
plt.savefig(f'{plot_location}/A_gamma.pdf', dpi=600, pad_inches=0)
plt.close()
