import energies
import config


def main():
    params = config.FitParameters()
    moi, odd_spin, theta_deg = params.get_params()
    energy = energies.Energies(moi, odd_spin, theta_deg)
    energy.show()


if __name__ == '__main__':
    main()
