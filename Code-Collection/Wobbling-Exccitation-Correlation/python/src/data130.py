import numpy as np

import correlations


def MeV(energy):
    return np.round(energy/1000.0, 3)


class Exp_Absolute_Energies:
    # absolute energies
    band1 = list(map(MeV, [3790.3, 4256.3, 4884.2, 5678.3, 6563.3,
                           7524.3, 8574.3, 9690.3, 10821.3, 11984.3]))
    # absolute energies
    band2 = list(map(MeV, [4456.2, 4986.2, 5647.2,
                           6442.2, 7319.3, 8265.3, 9283.3, 10436.3]))

    band_head_energy = band1[0]


class Exp_Excitation_Energies:
    band1 = [
        np.round(x-Exp_Absolute_Energies.band_head_energy, 3) for x in Exp_Absolute_Energies.band1[1:]]
    band2 = [
        np.round(x-Exp_Absolute_Energies.band_head_energy, 3) for x in Exp_Absolute_Energies.band2]


class Exp_Wobbling_Energy:
    band1 = [np.round(Exp_Absolute_Energies.band2[i]-0.5 *
             (Exp_Absolute_Energies.band1[i]+Exp_Absolute_Energies.band1[i+1]), 3) for i in range(len(Exp_Absolute_Energies.band2))]


class Spins:
    # full spin range
    band1 = np.arange(10, 30, 2)
    band2 = np.arange(11, 27, 2)
    band_head = band1[0]


print(Exp_Wobbling_Energy.band1)
print(Exp_Excitation_Energies.band1)
print(Exp_Excitation_Energies.band2)
