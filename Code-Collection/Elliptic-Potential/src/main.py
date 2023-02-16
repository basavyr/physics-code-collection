import numpy as np
import elliptic_potential
import plotter
import exporter as csv


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


def generate_potential_data(q_values: list[float], moi_1: float, moi_2: float, moi_3: float, theta_deg: float, spin: float, odd_spin: float) -> list[float]:
    """
    - Returns a list of numerical values for the elliptic potential V(q)
    - Requires the list of q values
    """
    elliptic = elliptic_potential.EllipticFunctions(
        moi_1, moi_2, moi_3, odd_spin)
    return [elliptic.v_q_func(spin, theta_deg, q) for q in q_values]


def create_elliptic_plots(moi_1: float, moi_2: float, moi_3: float, theta_deg: float, spin: float, odd_spin: float, plot_name: str) -> None:
    x_label = "q [rad]"
    y_label = r'V(q) [$\hbar^2$]'
    plot_label = "V(q)"
    q_x_limit_left = -8
    q_x_limit_right = 8
    x_data = np.linspace(q_x_limit_left, q_x_limit_right, 100)
    y_data = generate_potential_data(
        x_data, moi_1, moi_2, moi_3, theta_deg, spin, odd_spin)
    p = plotter.Plotter(x_data, y_data)
    p.make_plot(plot_name, x_label, y_label, plot_label)

    # save the results to a csv file
    file_name = f'potential-spin-{int(2*spin)}-2'
    csv.save_to_csv(x_data, y_data, file_name)


if __name__ == '__main__':
    create_elliptic_plots(95, 100, 85, 100, 45/2, 6.5, "plot-test-moi")
    create_elliptic_plots(91, 9, 51, -119, 45/2, 5.5, "plot-fit-moi")
    create_elliptic_plots(91, 9, 51, 61, 45/2, 5.5, "plot-fit-moi-chiral")
