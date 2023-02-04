import angular_momentum as am
from const import Constants
import energy_function as h
import numpy as np


def main():
    constants = Constants(10, 40, 20, 11/2, 70)
    j_sp = am.j_SingleParticle(constants.j, constants.theta_degrees)
    j1, j2, j3 = j_sp.j_vec()
    print(j1, j2, j3)

    x2_values = np.linspace(0, 19.0/2.0, 5)
    varphi2_rad_values = np.linspace(-np.pi/2.0, np.pi/2, 5)

    # set a constant spin value
    SPIN = 19.0/2.0

    with open(f'results.csv', 'w+') as writer:
        for idx in range(len(x2_values)):
            A_idx = h.EnergyFunction.A_term(
                constants.A1, constants.A2, SPIN, j2)
            u_idx = h.EnergyFunction.u_term(constants.A1, constants.A3, A_idx)
            v0_idx = h.EnergyFunction.v0_term(constants.A1, A_idx, j1)
            h_prime = h.EnergyFunction.H_polar(
                19.0/2.0, x2_values[idx], varphi2_rad_values[idx], u_idx, v0_idx)
            # print(
            #     f"H'({x2_values[idx]},{varphi2_rad_values[idx]}) = {h_prime}")
            writer.write(
                f'{x2_values[idx]},{varphi2_rad_values[idx]},{h_prime}\n')


if __name__ == '__main__':
    main()
