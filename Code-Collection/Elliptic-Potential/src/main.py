import numpy as np
import elliptic_potential
import plotter


def main():
    # create the class instances for usage
    E = elliptic_potential.EllipticFunctions()
    N = elliptic_potential.NumericalFactors()

    # define the inertia factors
    A1_N = N.inertia_factor(N.MOI_1)
    A2_N = N.inertia_factor(N.MOI_2)
    A3_N = N.inertia_factor(N.MOI_3)

    u_N = N.u(N.SPIN, N.ODD_SPIN, N.THETA, A1_N, A2_N, A3_N)
    A_N = N.A(N.SPIN, N.ODD_SPIN, N.THETA, A1_N, A2_N)
    v0_N = N.v0(N.SPIN, N.ODD_SPIN, N.THETA, A1_N, A2_N)

    k_N = E.k(u_N)
    k_prime_N = E.k_prime(u_N)

    q_values = np.arange(-8, 8, 0.2)
    for q in q_values:
        v_q = E.v_q(N.SPIN, q, k_N, v0_N)
        print(q, v_q)


def generate_potential_data(spin: float, q_values: list[float]) -> list[float]:
    """
    - Returns a list of numerical values for the elliptic potential V(q)
    - Requires the list of q values
    """
    elliptic = elliptic_potential.EllipticFunctions(
        91.0, 5.0, 51.0, 5.5, -119.0)
    return [elliptic.v_q_func(spin, q) for q in q_values]


def create_elliptic_plots():
    x_label = "q [rad]"
    y_label = r'V(q) [$\hbar^2$]'
    plot_label = "V(q)"
    x_data = np.linspace(-8.0, 8.0, 10)
    print(f'Will create plots for q: {x_data}')
    y_data = generate_potential_data(22.5, x_data)
    print(f'The potential values are: {y_data}')
    p = plotter.Plotter([1, 2, 3], [1, 2, 3])
    p.make_plot("test_plot_1", x_label, y_label, plot_label)


if __name__ == '__main__':
    create_elliptic_plots()
