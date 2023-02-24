import config
import chiral
import numpy as np


def fit1() -> None:
    params = config.FittingParameters()
    moi_fit1, odd_spin, theta_deg_fit1 = params.fit1()
    potential = chiral.Potential(moi_fit1, odd_spin)
    q_values = np.linspace(-8, 8, 450)
    spin_values = [22.5, 18.5, 14.5]
    potential.plot_symm_potential(q_values, spin_values, theta_deg_fit1)
    potential.plot_asymm_potential(q_values, spin_values, theta_deg_fit1)


def main():
    fit1()


if __name__ == '__main__':
    main()
