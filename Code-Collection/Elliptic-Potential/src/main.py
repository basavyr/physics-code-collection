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


def generate_points(y_0: float, y_1: float, x_values: list[float]) -> list[tuple]:
    """
    - returns a list of points [(px_0,py_0),...] based on a list of x values
    - px_0=[x_0,x_0]
    - py_0=[y_0,y_1]
    """
    points = []
    y_points = [y_0, y_1]
    for x in x_values:
        px = [x, x]
        py = y_points
        points.append((px, py))
    return points


def elliptic_func_comparison(jacobi_function, k, periods, plot_name):
    q_values = np.linspace(0, 7, 100)
    s_values_k_squared = [jacobi_function(q, k) for q in q_values]

    y0, y1 = min(s_values_k_squared), max(s_values_k_squared)
    # generate the list of points for each of the periods 0, K, 2K, 3K, 4K
    period_points = generate_points(y0, y1, periods)

    idx = 1
    for point in period_points:
        # unwraps the tuple ([x_0,x_0], [y_0,y_1])
        p_x, p_y = point
        # plots a vertical line at x -> x_0, between y0 and y1
        plotter.plt.plot(p_x, p_y, '--k', label=f'{idx}K')
        idx = idx+1
    plotter.plt.plot(q_values, s_values_k_squared, '-r',  label=r'$m=k^2$')
    # add vertical lines to a plot using the axvline function from within matplotlib
    # source: https://stackoverflow.com/questions/52757586/python-plotting-lines-parallel-to-y-axis-from-array
    # for l in x_values:
    #     plotter.plt.axvline(l)
    plotter.plt.legend(loc='best')
    plotter.plt.savefig(f'../data/{plot_name}.pdf',
                        dpi=450, bbox_inches='tight')
    plotter.plt.close()


def jacobi_functions():
    k = 0.5
    jacobi = jacobi_func.Jacobi()
    periods = [idx*jacobi.period(k) for idx in range(1, 5)]

    elliptic_func_comparison(
        jacobi.sn_k_squared, k, periods, 'elliptic_sn_comparison')
    elliptic_func_comparison(
        jacobi.cn_k_squared, k, periods, 'elliptic_cn_comparison')
    elliptic_func_comparison(
        jacobi.dn_k_squared, k, periods, 'elliptic_dn_comparison')


def elliptic_potential(spin_values, mois, oddspin, theta_deg, plot_name):
    jacobi = jacobi_func.Jacobi()
    potential = jacobi_func.Potential(
        mois[0], mois[1], mois[2], oddspin, theta_deg)

    q_values = np.linspace(-8, 8, 100)

    potentials = [
        [potential.v_q(q, spin) for q in q_values] for spin in spin_values]

    max_potentials = max([max(potential) for potential in potentials])
    min_potentials = min([min(potential) for potential in potentials])

    k_values = [potential.k_term(spin) for spin in spin_values]
    periods = [[idx*jacobi.period(k) for idx in range(1, 5)] for k in k_values]
    period_points = generate_points(min_potentials, max_potentials, periods[0])

    plot_styles = iter(['-r', '-b', '-k', 'g'])
    spin_iter = iter(spin_values)

    idx = 1
    for point in period_points:
        # unwraps the tuple ([x_0,x_0], [y_0,y_1])
        p_x, p_y = point
        # plots a vertical line at x -> x_0, between y0 and y1
        plotter.plt.plot(p_x, p_y, '--k', label=f'{idx}K')
        idx = idx+1

    # for potential in potentials:
    #     plotter.plt.plot(
    #         q_values, potential, next(plot_styles), label=f'I={int(2*next(spin_iter))}/2')
    plotter.plt.plot(
        q_values, potentials[0], next(plot_styles), label=f'I={int(2*next(spin_iter))}/2')

    plotter.plt.legend(loc='best')
    plotter.plt.savefig(f'../data/{plot_name}.pdf',
                        dpi=450, bbox_inches='tight')
    plotter.plt.close()


def main():
    moi_values_fit = [91, 9, 51]
    moi_values_test = [95, 100, 85]
    moi_values_raduta = [89, 12, 48]

    theta_deg_fit = -119
    theta_deg_test = -80
    theta_deg_raduta = -71

    spin_values = [45/2, 37/2, 29/2]
    odd_spin112 = 5.5
    odd_spin132 = 6.5
    elliptic_potential(
        spin_values, moi_values_fit,
        odd_spin112, theta_deg_fit, 'jacobi_potential_fit_1')
    elliptic_potential(
        spin_values, moi_values_fit,
        odd_spin112, theta_deg_fit + 180.0, 'jacobi_potential_fit_2')
    elliptic_potential(
        spin_values, moi_values_test,
        odd_spin132, theta_deg_test, 'jacobi_potential_1')
    elliptic_potential(
        spin_values, moi_values_test,
        odd_spin132, theta_deg_test + 180.0, 'jacobi_potential_2')
    elliptic_potential(
        spin_values, moi_values_raduta,
        odd_spin112, theta_deg_raduta, 'jacobi_potential_raduta_1')
    elliptic_potential(
        spin_values, moi_values_raduta,
        odd_spin112, theta_deg_raduta + 180.0, 'jacobi_potential_raduta_2')


if __name__ == '__main__':
    main()
