import numpy as np
import elliptic_potential
import plotter
import exporter as csv


def create_elliptic_plots(elliptic_potential_func: elliptic_potential.EllipticFunctions, theta_deg: float, spin_values: list[float], plot_name: str) -> tuple[list[float], list[float]]:
    """
    - create a plot with the elliptic potential V(q)
    - the plot contains a line for each spin value that is given as argument
    """
    x_label = "q [rad]"
    y_label = r'V(q) [$\hbar^2$]'
    plot_label = "V(q)"
    q_x_limit_left = -8.0
    q_x_limit_right = 8.0

    x_data = np.linspace(q_x_limit_left, q_x_limit_right, 100)
    y_data = [elliptic_potential_func(
        spin_values, theta_deg, q) for q in x_data]

    p = plotter.Plotter(x_data, y_data, spin_values)
    p.make_plot(plot_name, x_label, y_label, plot_label)

    return x_data, y_data


def make_plot_batch(moi_values: list[float], theta_deg_values: list[float], spin_values: list[float], odd_spin: float) -> None:
    """
    - create a set of plots for a list of theta values (given in degrees)
    """
    moi_1, moi_2, moi_3 = moi_values
    elliptic = elliptic_potential.EllipticFunctions(
        moi_1, moi_2, moi_3, odd_spin)
    for theta_deg in theta_deg_values:
        plot_name_k = f'potential-k-plot-theta-{int(abs(theta_deg))}'
        plot_name_k_squared = f'potential-k2-plot-theta-{int(abs(theta_deg))}'
        csv_file_name = f'numerical-data-theta-{int(abs(theta_deg))}'
        # create the plot for modulus k
        q_values, v_values_k = create_elliptic_plots(
            elliptic.v_q_func_k, theta_deg, spin_values, plot_name_k)
        # create the plot for modulus k^2
        q_values, v_values_k_squared = create_elliptic_plots(
            elliptic.v_q_func_k_squared, theta_deg, spin_values, plot_name_k_squared)


def main():
    theta_deg_values_fit = [-119, 61]
    theta_deg_values_test = [-80, 100]
    spin_values = [29/2, 37/2, 45/2]
    moi_values_fit = [91, 9, 51]
    moi_values_test = [95, 100, 85]
    odd_spin112 = 5.5
    odd_spin132 = 6.5
    make_plot_batch(moi_values_test, theta_deg_values_test,
                    spin_values, odd_spin132)


if __name__ == '__main__':
    main()
