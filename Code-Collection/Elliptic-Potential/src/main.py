import numpy as np
import plotter
import exporter as csv
import JacobiFunctions as jacobi_func
import config
from itertools import repeat


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

    # calculate the k value for all the spins, where k=fct(spin)
    k_values = [potential.k_term(spin) for spin in spin_values]
    # for a given k value, calculate the period K, and create an array K,2K,3K,4K
    periods = [[idx*jacobi.period(k) for idx in range(1, 5)] for k in k_values]

    # determines the maximum period (i.e., 4K) that is obtained from all k values across all spins
    max_q = max([max(period) for period in periods])

    # set the x-axis to only have q values between the -4K and 4K range
    q_values = np.linspace(-max_q, max_q, 100)

    potentials = [
        [potential.v_q(q, spin) for q in q_values] for spin in spin_values]
    max_potentials = max([max(potential) for potential in potentials])
    min_potentials = min([min(potential) for potential in potentials])

    period_points = [generate_points(
        min_potentials, max_potentials, period) for period in periods]

    plot_styles = iter(['-r', '-b', '-k', 'g'])
    spin_iter = iter(spin_values)

    for potential in potentials:
        plotter.plt.plot(
            q_values, potential, next(plot_styles), label=f'I={int(2*next(spin_iter))}/2')

    plotter.plt.legend(loc='best')
    plotter.plt.savefig(f'../data/{plot_name}.pdf',
                        dpi=450, bbox_inches='tight')
    plotter.plt.close()


def evaluate_function_2_args(func: jacobi_func.Jacobi, arg_1: list[float], arg_2: float) -> list[float]:
    """
    - returns a list with the numerical values for func(arg_1, arg_2) where arg_1 is a list and arg_2 a number
    """
    return np.round(list(map(func, arg_1, repeat(arg_2))), 3)


def numerical_data_export(spin: float) -> None:
    """
    - helper method that exports to a CSV file the numerical values of q, phi, sn, cn, dn, and V(q)
    - requires a 
    """
    moi1, moi2, moi3 = config.MOI_VALUES_FIT

    jacobi = jacobi_func.Jacobi()
    potential = jacobi_func.Potential(
        moi1, moi2, moi3, config.ODD_SPIN112, config.THETA_DEG_FIT)
    # determine the value of the modulus k
    k = potential.k_term(spin)

    # fix the values for the coordinate q
    q_values = np.round(np.linspace(-8, 8, 10), 3)

    # calculate the numerical values for the elliptic functions
    phi_values = evaluate_function_2_args(jacobi.amu_squared, q_values, k)
    for idx in range(len(q_values)):
        print(q_values[idx], phi_values[idx])


def make_elliptic_plots():
    elliptic_potential(
        config.SPIN_VALUES, config.MOI_VALUES_FIT,
        config.ODD_SPIN112, config.THETA_DEG_FIT, 'jacobi_potential_fit_1')
    elliptic_potential(
        config.SPIN_VALUES, config.MOI_VALUES_FIT,
        config.ODD_SPIN112, config.THETA_DEG_FIT + 180.0, 'jacobi_potential_fit_2')
    elliptic_potential(
        config.SPIN_VALUES, config.MOI_VALUES_TEST,
        config.ODD_SPIN132, config.MOI_VALUES_TEST, 'jacobi_potential_1')
    elliptic_potential(
        config.SPIN_VALUES, config.MOI_VALUES_TEST,
        config.ODD_SPIN132, config.MOI_VALUES_TEST + 180.0, 'jacobi_potential_2')
    elliptic_potential(
        config.SPIN_VALUES, config.MOI_VALUES_RADUTA,
        config.ODD_SPIN112, config.MOI_VALUES_RADUTA, 'jacobi_potential_raduta_1')
    elliptic_potential(
        config.SPIN_VALUES, config.MOI_VALUES_RADUTA,
        config.ODD_SPIN112, config.MOI_VALUES_RADUTA + 180.0, 'jacobi_potential_raduta_2')


def main():
    spin = config.SPIN_VALUES[0]
    numerical_data_export(spin)


if __name__ == '__main__':
    main()
