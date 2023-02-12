import energies
import numpy as np
import tests


def do_tests_absolute_energies(energy):
    tests.AbsoluteEnergies.band_1_data(
        energy.absolute_energy,
        energy.absolute_energy_prime)
    tests.AbsoluteEnergies.band_2_data(
        energy.absolute_energy,
        energy.absolute_energy_prime)
    tests.AbsoluteEnergies.band_3_data(
        energy.absolute_energy,
        energy.absolute_energy_prime)


def do_tests_excitation_energies(energy):
    tests.ExcitationEnergies.band_1_data(
        energy.excitation_energy,
        energy.excitation_energy_prime)
    tests.ExcitationEnergies.band_2_data(
        energy.excitation_energy,
        energy.excitation_energy_prime)
    tests.ExcitationEnergies.band_3_data(
        energy.excitation_energy,
        energy.excitation_energy_prime)


def give_experimental_energies(energy) -> None:

    band1_exp = tests.ExperimentalEnergies.band_energies_absolute(
        [], tests.ExperimentalEnergies.gamma1, tests.ExperimentalEnergies.e01)
    energy.math_print(band1_exp, f'band1_exp'.replace(
        "_", "").replace("exp", "Exp"))

    band2_exp = tests.ExperimentalEnergies.band_energies_absolute(
        [], tests.ExperimentalEnergies.gamma2, tests.ExperimentalEnergies.e02)
    energy.math_print(band2_exp, f'band2_exp'.replace(
        "_", "").replace("exp", "Exp"))

    band3_exp = tests.ExperimentalEnergies.band_energies_absolute(
        [], tests.ExperimentalEnergies.gamma3, tests.ExperimentalEnergies.e03)
    energy.math_print(band3_exp, f'band3_exp'.replace(
        "_", "").replace("exp", "Exp"))


def main():
    band_head = 5.5
    theta = -119
    j = 5.5
    energy = energies.EnergyFunction(91.0, 9.0, 51.0, j, theta, band_head)
    # do_tests_excitation_energies(energy)
    give_experimental_energies(energy)


if __name__ == '__main__':
    main()
