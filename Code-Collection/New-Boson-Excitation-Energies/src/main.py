import energies
import numpy as np


def show_excitation_energies_th(excitation_energy: energies.EnergyFunction.excitation_energy) -> None:
    spins_1 = np.arange(5.5, 27.5, 2)
    spins_2 = np.arange(8.5, 18.5, 2)
    spins_3 = np.arange(9.5, 17.5, 2)
    band_1 = excitation_energy(spins_1, 0)
    band_2 = excitation_energy(spins_2, 0)
    band_3 = excitation_energy(spins_3, 1)
    print("B1")
    print(spins_1)
    print(band_1)

    print("B2")
    print(spins_2)
    print(band_2)

    print("B3")
    print(spins_3)
    print(band_3)


def main():
    band_head = 5.5
    theta = -119
    j = 5.5
    energy = energies.EnergyFunction(91.0, 9.0, 51.0, j, theta, band_head)

    gamma1_exp = [
        372.9, 659.8, 854.3, 999.7,
        1075.6, 843.7, 834.3, 882.2, 922.4, 957.0, 1005]
    e01 = 358.0
    band1_exp = energy.generate_excitation_band(
        e01, energy.generate_energy_band(e01, gamma1_exp))
    energy.math_print(band1_exp[1:], f'band1_exp'.replace(
        "_", "").replace("exp", "Exp"))

    gamma2_exp = [726.5, 795.7, 955.7, 1111.7]
    e02 = 1477.9
    band2_exp = energy.generate_excitation_band(
        e01, energy.generate_energy_band(e02, gamma2_exp))
    energy.math_print(band2_exp, f'band2_exp'.replace(
        "_", "").replace("exp", "Exp"))

    gamma3_exp = [826.3, 763.8, 1009.0]
    e03 = 358.0 + 372.9 + 1197.1
    band3_exp = energy.generate_excitation_band(
        e01, energy.generate_energy_band(e03, gamma3_exp))
    energy.math_print(band3_exp, f'band3_exp'.replace(
        "_", "").replace("exp", "Exp"))


if __name__ == '__main__':
    main()
