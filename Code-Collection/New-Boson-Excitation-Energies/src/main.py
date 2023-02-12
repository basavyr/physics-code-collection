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
        energy.absolute_energy,
        energy.absolute_energy_prime)
    tests.ExcitationEnergies.band_2_data(
        energy.absolute_energy,
        energy.absolute_energy_prime)
    tests.ExcitationEnergies.band_3_data(
        energy.absolute_energy,
        energy.absolute_energy_prime)


def main():
    band_head = 5.5
    theta = -119
    j = 5.5
    energy = energies.EnergyFunction(91.0, 9.0, 51.0, j, theta, band_head)
    # do_tests_absolute_energies(energy)
    do_tests_excitation_energies(energy)
    # gamma1_exp = [
    #     372.9, 659.8, 854.3, 999.7,
    #     1075.6, 843.7, 834.3, 882.2, 922.4, 957.0, 1005]
    # e01 = 358.0
    # band1_exp = energy.generate_excitation_band(
    #     e01, energy.generate_energy_band(e01, gamma1_exp))
    # energy.math_print(band1_exp[1:], f'band1_exp'.replace(
    #     "_", "").replace("exp", "Exp"))

    # gamma2_exp = [726.5, 795.7, 955.7, 1111.7]
    # e02 = 1477.9
    # band2_exp = energy.generate_excitation_band(
    #     e01, energy.generate_energy_band(e02, gamma2_exp))
    # energy.math_print(band2_exp, f'band2_exp'.replace(
    #     "_", "").replace("exp", "Exp"))

    # gamma3_exp = [826.3, 763.8, 1009.0]
    # e03 = 358.0 + 372.9 + 1197.1
    # band3_exp = energy.generate_excitation_band(
    #     e01, energy.generate_energy_band(e03, gamma3_exp))
    # energy.math_print(band3_exp, f'band3_exp'.replace(
    #     "_", "").replace("exp", "Exp"))


if __name__ == '__main__':
    main()
