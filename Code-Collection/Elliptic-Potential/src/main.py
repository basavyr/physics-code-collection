import numpy as np
import elliptic_potential
import plotter
import exporter as csv
import JacobiFunctions as jacobi_func


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


def generate_points(y_0: float, y_1: float, x_values: list[float]) -> list[tuple[list[float], list[float]]]:
    """
    - returns a list of points [(p0_0,p1_0),...] based on a list of x values
    - p0_0=[x_0,y_0]
    - p1_0=[x_0,y_1]
    """
    points = []
    for x in x_values:
        p0 = [x, y_0]
        p1 = [x, y_1]
        points.append((p0, p1))
    return points


def elliptic_func_comparison(k):
    jacobi = jacobi_func.Jacobi(k, 6)
    q_values = np.linspace(0, 7, 100)
    s_values_k = [jacobi.sn_k(q, k) for q in q_values]
    s_values_k_squared = [jacobi.sn_k_squared(q, k) for q in q_values]
    period = jacobi.period(k)
    period_line_x_1 = [period for _ in q_values]
    period_line_x_2 = [2*period for _ in q_values]
    period_line_x_3 = [3*period for _ in q_values]
    period_line_x_4 = [4*period for _ in q_values]
    period_line_y = np.linspace(
        min(s_values_k), max(s_values_k), len(s_values_k))
    x_values = [1, 2, 3]
    N = 2
    y0, y1 = -1, 1
    points = generate_points(y0, y1, x_values)
    # add vertical lines to a plot using the axvline function from within matplotlib
    # source: https://stackoverflow.com/questions/52757586/python-plotting-lines-parallel-to-y-axis-from-array
    # for l in x_values:
    #     plotter.plt.axvline(l)

    for p in points:
        p0, p1 = p
        print(p0)
        print(p1)
    # plots a vertical line at x->1, between -1 and 1
    plotter.plt.plot([1, 1], [-1, 1], '-k', label='fakey')
    plotter.plt.plot([3, 3], [-1, 1], '-k', label='fakey')
    plotter.plt.plot([2, 2], [-1, 1], '-k', label='fakey')
    # plotter.plt.plot([period_line_x_2], [period_line_y])
    # plotter.plt.plot(period_line_x_3, period_line_y)
    # plotter.plt.plot(period_line_x_4, period_line_y)
    # plotter.plt.plot(q_values, s_values_k, '-r', label=r'$k=m$')
    # plotter.plt.plot(q_values, s_values_k_squared, '--r',  label=r'$k^2=m$')
    plotter.plt.legend(loc='best')
    plotter.plt.savefig(f'../data/elliptic_sn_comparison.pdf',
                        dpi=450, bbox_inches='tight')
    plotter.plt.close()
    # plotter.Plotter.plot_data(
    #     q_values, [s_values_k, s_values_k_squared], [
    #         r'$m=k$', r'$m=k^2$'], 'elliptic_sn_comparison')


def main():
    theta_deg_values_fit = [-119, 61]
    theta_deg_values_test = [-80, 100]
    spin_values = [29/2, 37/2, 45/2]
    moi_values_fit = [91, 9, 51]
    moi_values_test = [95, 100, 85]
    odd_spin112 = 5.5
    odd_spin132 = 6.5
    # make_plot_batch(moi_values_test, theta_deg_values_test,
    #                 spin_values, odd_spin132)
    elliptic_func_comparison(0.5)


if __name__ == '__main__':
    main()
