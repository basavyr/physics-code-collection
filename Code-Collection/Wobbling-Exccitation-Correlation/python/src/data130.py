import numpy as np

import correlations

# absolute energies
band1_exp = [3790.3, 4256.3, 4884.2, 5678.3, 6563.3,
             7524.3, 8574.3, 9690.3, 10821.3, 11984.3]
# absolute energies
band2_exp = [4456.2, 4986.2, 5647.2, 6442.2, 7319.3, 8265.3, 9283.3, 10436.3]

# full spin range
spins_1 = np.arange(10, 30, 2)
spins_2 = np.arange(11, 27, 2)

band_head = 10

for spin in spins_2:
    print(spin, correlations.Wobbling_Energy(spin, 1, 0.5, 0.3, 0.1))
