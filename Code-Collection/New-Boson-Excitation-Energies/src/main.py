import energies
import numpy as np


def main():
    energy = energies.EnergyFunction(91.0, 9.0, 51.0, 5.5, -119)
    spins_1 = np.arange(5.5, 27.5, 2)
    band_1 = [energy.excitation_energy(spin, 0) for spin in spins_1]
    band_2 = [energy.excitation_energy(spin, 0) for spin in spins_1]
    band_3 = [energy.excitation_energy(spin, 1) for spin in spins_1]


if __name__ == '__main__':
    main()
