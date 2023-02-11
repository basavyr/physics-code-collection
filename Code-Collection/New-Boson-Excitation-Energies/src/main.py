import energies
import numpy as np


def main():
    energy = energies.EnergyFunction(91.0, 9.0, 51.0, 5.5, -119)
    spins_1 = np.arange(5.5, 27.5, 2)
    spins_2 = np.arange(8.5, 18.5, 2)
    spins_3 = np.arange(9.5, 17.5, 2)
    band_1 = [energy.absolute_energy(spin, 0) for spin in spins_1]
    band_2 = [energy.absolute_energy(spin, 0) for spin in spins_2]
    band_3 = [energy.absolute_energy(spin, 1) for spin in spins_3]
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
