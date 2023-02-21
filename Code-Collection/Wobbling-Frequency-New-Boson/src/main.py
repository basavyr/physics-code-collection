import wobbling
import fit
import numpy as np
import exporter


def fit_1() -> list[tuple]:
    params = fit.FittingParameters()
    wobb = wobbling.Wobbling(
        params.MOIS_1, params.ODD_SPIN, params.THETA_DEG_1)
    spin_values = np.arange(7.5, 41.5, 2)
    numerical_values = [(spin, wobb.omega(spin), wobb.omega_chiral(spin))
                        for spin in spin_values]

    return numerical_values


def fit_2():
    params = fit.FittingParameters()
    wobb = wobbling.Wobbling(
        params.MOIS_2, params.ODD_SPIN, params.THETA_DEG_2)


def fit_3():
    params = fit.FittingParameters()
    wobb = wobbling.Wobbling(
        params.MOIS_3, params.ODD_SPIN, params.THETA_DEG_3)


def main():
    """Main function"""
    data1 = fit_1()
    exporter.export_to_csv(data1, 'data_fit_1')


if __name__ == "__main__":

    main()
