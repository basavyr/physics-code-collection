import energies
import numpy as np


def main():
    band_head = 5.5
    theta = -119
    j = 5.5
    energy = energies.EnergyFunction(91.0, 9.0, 51.0, j, theta, band_head)
    spins_1 = np.arange(5.5, 27.5, 2)
    spins_2 = np.arange(8.5, 18.5, 2)
    spins_3 = np.arange(9.5, 17.5, 2)
    band_1 = energy.excitation_energy(spins_1, 0)
    band_2 = energy.excitation_energy(spins_2, 0)
    band_3 = energy.excitation_energy(spins_3, 1)
    print("B1")
    print(spins_1)
    print(band_1)

    print("B2")
    print(spins_2)
    print(band_2)

    print("B3")
    print(spins_3)
    print(band_3)


if __name__ == '__main__':
    main()
