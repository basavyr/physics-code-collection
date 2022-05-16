import matplotlib.pyplot as plt
import numpy as np

import factors as A

plot_location = './results'


# generate angles
x = np.arange(0, 180, 5)


# evaluate the canonical factor
y1 = A.Canonical.A_varphi([1, 3, 7], x)
y2 = A.Canonical.A_varphi([1, 7, 3], x)
y3 = A.Canonical.A_varphi([7, 3, 1], x)
y4 = A.Canonical.A_varphi([7, 1, 3], x)
y5 = A.Canonical.A_varphi([3, 1, 7], x)
y6 = A.Canonical.A_varphi([3, 7, 1], x)


# use latex for matplotlib plot python
plt.rcParams.update({
    "text.usetex": True})

# use custom size
plt.rcParams["figure.figsize"] = (5, 4)

# create the first plot
plt.xlabel(r'$\varphi$')
plt.ylabel(r'$\mathcal{A}_\varphi$')
plt.plot(x, y1, '-r', label=r'$A_1<A_2<A_3$')
plt.plot(x, y2, '-b', label=r'$A_1<A_3<A_2$')
plt.plot(x, y3, '-k', label=r'$A_3<A_2<A_1$')
plt.legend(loc='best')
plt.savefig(f'{plot_location}/A_varphi_1.pdf', dpi=300)
plt.close()

# create the second plot
plt.xlabel(r'$\varphi$')
plt.ylabel(r'$\mathcal{A}_\varphi$')
plt.plot(x, y4, '-r', label=r'$A_2<A_3<A_1$')
plt.plot(x, y5, '-b', label=r'$A_2<A_1<A_3$')
plt.plot(x, y6, '-k', label=r'$A_3<A_1<A_3$')
plt.legend(loc='best')
plt.savefig(f'{plot_location}/A_varphi_2.pdf', dpi=300)
plt.close()
