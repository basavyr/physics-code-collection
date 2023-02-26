import energies
import config
from itertools import repeat


def excitation_energies():
    params = config.FitParameters()
    moi, odd_spin, _ = params.get_params()
    energy = energies.Energies(moi, odd_spin)
    x_data = params.SPINS_BAND1
    symm_data = list(
        map(energy.symmetric_excitation_energy,
            x_data, repeat(params.THETA_DEG)))
    asymm_data = list(
        map(energy.asymmetric_excitation_energy,
            x_data, repeat(params.THETA_DEG)))
    for p in zip(x_data, symm_data, asymm_data):
        print(p)


def main():
    excitation_energies()


if __name__ == '__main__':
    main()
