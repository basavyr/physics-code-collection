import matplotlib.pyplot as plt
import numpy as np


# local module with the canonical factors
import factors as A


plot_location = './results'
# path to the figure folder on MacBook Air
figures_path_air = "/Users/basavyr/Documents/Work/PhD/phdthesis/Chapters/Figures"
figures_path_mini = "/Users/basavyr/Desktop/phd/phdthesis/Chapters/Figures"

# set the canonical coordinates
varphi_list = np.linspace(0, 180, 100)
psi_list = np.linspace(0, 180, 100)
X, Y = np.meshgrid(varphi_list, psi_list)
Z_123 = A.Canonical.A_mixed([1, 3, 7], X, Y)
Z_132 = A.Canonical.A_mixed([1, 7, 3], X, Y)
Z_213 = A.Canonical.A_mixed([3, 1, 7], X, Y)
Z_231 = A.Canonical.A_mixed([7, 1, 3], X, Y)
Z_312 = A.Canonical.A_mixed([3, 7, 1], X, Y)
Z_321 = A.Canonical.A_mixed([7, 3, 1], X, Y)


# use latex for matplotlib plot python
plt.rcParams.update({
    "text.usetex": True})


# use custom size
# source: https://stackoverflow.com/questions/332289/how-do-i-change-the-size-of-figures-drawn-with-matplotlib
plt.rcParams["figure.figsize"] = (13, 7)
# plt.rcParams["figure.figsize"] = (8,5)
# reset the plot size
# plt.rcParams['figure.figsize'] = plt.rcParamsDefault['figure.figsize']


# change the font size
# source: https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
plt.rcParams.update({'font.size': 17})

plt.rc('axes', titlesize=15)  # fontsize of the figure title

# plt.rcParams["contour.linewidth"] = 1.1
plt.rcParams["image.cmap"] = 'RdBu_r'
# plt.rcParams["image.cmap"] = 'PuBuGn'


# fig, ax = plt.subplots(2, 3, sharex=True, sharey=True)
fig = plt.figure()

gs = fig.add_gridspec(2, 3, hspace=0.11,wspace=0.1)
ax = gs.subplots(sharex=True, sharey=True)

plt.xticks(np.arange(0, 181, 60))
plt.yticks(np.arange(0, 181, 60))

im1 = ax[0, 0].contourf(X, Y, Z_123, levels=21, antialiased=True)
ax[0, 0].set_title(r'$A_1<A_2<A_3$')
im2 = ax[0, 1].contourf(X, Y, Z_132,  levels=21, antialiased=True)
ax[0, 1].set_title(r'$A_1<A_3<A_2$')
im3 = ax[0, 2].contourf(X, Y, Z_213,  levels=21, antialiased=True)
ax[0, 2].set_title(r'$A_2<A_1<A_3$')
im4 = ax[1, 0].contourf(X, Y, Z_231,  levels=21, antialiased=True)
ax[1, 0].set_title(r'$A_2<A_3<A_1$')
ax[1, 0].set(xlabel=r'$\varphi$ $[^\circ]$', ylabel=r'$\psi$ $[^\circ]$')
im5 = ax[1, 1].contourf(X, Y, Z_312,  levels=21, antialiased=True)
ax[1, 1].set_title(r'$A_3<A_1<A_2$')
im6 = ax[1, 2].contourf(X, Y, Z_321,  levels=21, antialiased=True)
ax[1, 2].set_title(r'$A_3<A_2<A_1$')

imgs = [im1, im2, im3, im4, im5, im6]
axis_list = [ax[0, 0], ax[0, 1], ax[0, 2], ax[1, 0], ax[1, 1], ax[1, 2]]

for bars in zip(imgs, axis_list):
    fig.colorbar(bars[0], ax=bars[1])

# for axx in ax.flat:
#     axx.set(xlabel='x-label', ylabel='y-label')

plt.tight_layout()
plt.savefig(f'{figures_path_mini}/A_mixed.pdf', dpi=300, pad_inches=0)
plt.savefig(f'{plot_location}/A_mixed.pdf', dpi=300, pad_inches=0)
plt.close()
