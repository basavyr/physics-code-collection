import energies
import numpy as np


class AbsoluteEnergies:
    @staticmethod
    def band_1_data(absolute_energies: energies.EnergyFunction.absolute_energy, absolute_energies_prime: energies.EnergyFunction.absolute_energy_prime):
        spins_1 = np.arange(5.5, 29.5, 2)
        band_1 = absolute_energies(spins_1, 0)
        band_1_prime = absolute_energies_prime(spins_1, 0)
        print("**********************")
        print("B1 - Absolute Energies")
        print("**********************")
        print(spins_1)
        print(f"E -> {band_1}")
        print(F"E' -> {band_1_prime}")
        print(f'\n')

    @staticmethod
    def band_2_data(absolute_energies: energies.EnergyFunction.absolute_energy, absolute_energies_prime: energies.EnergyFunction.absolute_energy_prime):
        spins_2 = np.arange(8.5, 18.5, 2)
        band_2 = absolute_energies(spins_2, 0)
        band_2_prime = absolute_energies_prime(spins_2, 0)
        print("**********************")
        print("B2 - Absolute Energies")
        print("**********************")
        print(spins_2)
        print(f"E -> {band_2}")
        print(F"E' -> {band_2_prime}")
        print(f'\n')

    @staticmethod
    def band_3_data(absolute_energies: energies.EnergyFunction.absolute_energy, absolute_energies_prime: energies.EnergyFunction.absolute_energy_prime):
        spins_3 = np.arange(9.5, 17.5, 2)
        band_3 = absolute_energies(spins_3, 1)
        band_3_prime = absolute_energies_prime(spins_3, 1)
        print("**********************")
        print("B3 - Absolute Energies")
        print("**********************")
        print(spins_3)
        print(f"E -> {band_3}")
        print(F"E' -> {band_3_prime}")
        print(f'\n')
