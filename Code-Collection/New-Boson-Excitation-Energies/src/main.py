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
    # print("B1")
    # print(spins_1)
    # print(band_1)

    # print("B2")
    # print(spins_2)
    # print(band_2)

    # print("B3")
    # print(spins_3)
    # print(band_3)

    gamma1Exp = [
        372.9, 659.8, 854.3, 999.7,
        1075.6, 843.7, 882.2, 922.4, 957.0, 1005]
    e01 = 358.0
    band_1_exp = [e01]
    for id in range(len(gamma1Exp)):
        band_1_exp.append(np.round(band_1_exp[id]+gamma1Exp[id], 3))
    print(band_1_exp)

    gamma2Exp = [726.5, 795.7, 955.7, 1111.7]
    e02 = 1477.9
    band_2_exp = [e02]
    for id in range(len(gamma2Exp)):
        band_2_exp.append(np.round(band_2_exp[id]+gamma2Exp[id], 3))
    print(band_2_exp)

    gamma3Exp = [726.5, 795.7, 955.7, 1111.7]
    e03 = 358.0 + 372.9 + 1197.1
    band_3_exp = [e03]
    for id in range(len(gamma3Exp)):
        band_3_exp.append(np.round(band_3_exp[id]+gamma3Exp[id], 3))
    print(band_3_exp)


if __name__ == '__main__':
    main()
