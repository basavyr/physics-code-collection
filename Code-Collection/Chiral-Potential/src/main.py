import config
import chiral
import numpy as np


def fit1() -> None:
    params = config.FittingParameters()
    moi_fit1, odd_spin, theta_deg_fit1 = params.fit1()
    potential = chiral.Potential(moi_fit1, odd_spin)
    q_values = np.linspace(-8, 8, 100)
    potential.plot_symm_potential(q_values, [22.5], theta_deg_fit1)


def main():
    fit1()


if __name__ == '__main__':
    main()
