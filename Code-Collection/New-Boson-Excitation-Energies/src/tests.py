import energies
import numpy as np


class AbsoluteEnergies:
    @staticmethod
    def band_1_data(
            absolute_energies: energies.EnergyFunction.absolute_energy,
            absolute_energies_prime: energies.EnergyFunction.absolute_energy_prime):
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
    def band_2_data(
            absolute_energies: energies.EnergyFunction.absolute_energy,
            absolute_energies_prime: energies.EnergyFunction.absolute_energy_prime):
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
    def band_3_data(
            absolute_energies: energies.EnergyFunction.absolute_energy,
            absolute_energies_prime: energies.EnergyFunction.absolute_energy_prime):
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


class ExcitationEnergies:
    @staticmethod
    def band_1_data(
            excitation_energies: energies.EnergyFunction.excitation_energy,
            excitation_energies_prime: energies.EnergyFunction.excitation_energy_prime):
        spins_1 = np.arange(5.5, 29.5, 2)
        band_1 = excitation_energies(spins_1, 0)
        band_1_prime = excitation_energies_prime(spins_1, 0)
        print("**********************")
        print("B1 - Excitation Energies")
        print("**********************")
        print(spins_1)
        print(f"E -> {band_1}")
        print(F"E' -> {band_1_prime}")
        print(f'\n')

    @staticmethod
    def band_2_data(
            excitation_energies: energies.EnergyFunction.excitation_energy,
            excitation_energies_prime: energies.EnergyFunction.excitation_energy_prime):
        spins_2 = np.arange(8.5, 18.5, 2)
        band_2 = excitation_energies(spins_2, 0)
        band_2_prime = excitation_energies_prime(spins_2, 0)
        print("**********************")
        print("B2 - Excitation Energies")
        print("**********************")
        print(spins_2)
        print(f"E -> {band_2}")
        print(F"E' -> {band_2_prime}")
        print(f'\n')

    @staticmethod
    def band_3_data(
            excitation_energies: energies.EnergyFunction.excitation_energy,
            excitation_energies_prime: energies.EnergyFunction.excitation_energy_prime):
        spins_3 = np.arange(9.5, 17.5, 2)
        band_3 = excitation_energies(spins_3, 1)
        band_3_prime = excitation_energies_prime(spins_3, 1)
        print("**********************")
        print("B3 - Excitation Energies")
        print("**********************")
        print(spins_3)
        print(f"E -> {band_3}")
        print(F"E' -> {band_3_prime}")
        print(f'\n')


class ExperimentalEnergies:
    gamma1 = [
        372.9, 659.8, 854.3, 999.7,
        1075.6, 843.7, 834.3, 882.2, 922.4, 957.0, 1005]
    e01 = 358.0
    gamma2 = [726.5, 795.7, 955.7, 1111.7]
    e02 = 358.0 + 372.9 + 746.6
    gamma3 = [826.3, 763.8, 1009.0]
    e03 = 358.0 + 372.9 + 1197.1
    band_head = 358.0

    @staticmethod
    def band_energies_absolute(
            spins: list[float],
            gammas: list[float],
            band_head: float) -> list[float]:
        """
        - returns the experimental data for a band, based on the band-head level and the gamma transitions
        """
        energies = [band_head]
        for idx in range(1, len(gammas)):
            e_idx = energies[idx - 1] + gammas[idx - 1]
            energies.insert(idx, e_idx)
        return energies
