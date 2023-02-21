import wobbling
import fit
import numpy as np
import exporter


def fit_1() -> list[tuple]:
    params = fit.FittingParameters()
    wobb = wobbling.Wobbling(
        params.MOIS_1, params.ODD_SPIN, params.THETA_DEG_1)
    spin_values = np.arange(7.5, 43.5, 2)
    numerical_values = [(spin, wobb.omega(spin), wobb.omega_chiral(spin))
                        for spin in spin_values]

    return numerical_values


def fit_2() -> list[tuple]:
    params = fit.FittingParameters()
    wobb = wobbling.Wobbling(
        params.MOIS_2, params.ODD_SPIN, params.THETA_DEG_2)
    spin_values = np.arange(7.5, 43.5, 2)
    numerical_values = [(spin, wobb.omega(spin), wobb.omega_chiral(spin))
                        for spin in spin_values]

    return numerical_values


def fit_3() -> list[tuple]:
    params = fit.FittingParameters()
    wobb = wobbling.Wobbling(
        params.MOIS_3, params.ODD_SPIN, params.THETA_DEG_3)
    spin_values = np.arange(7.5, 43.5, 2)
    numerical_values = [(spin, wobb.omega(spin), wobb.omega_chiral(spin))
                        for spin in spin_values]

    return numerical_values


def fit_all() -> list[tuple]:
    """
    - returns data for all the fits
    """
    params = fit.FittingParameters()
    wobb_1 = wobbling.Wobbling(
        params.MOIS_1, params.ODD_SPIN, params.THETA_DEG_1)
    wobb_2 = wobbling.Wobbling(
        params.MOIS_2, params.ODD_SPIN, params.THETA_DEG_2)
    wobb_3 = wobbling.Wobbling(
        params.MOIS_3, params.ODD_SPIN, params.THETA_DEG_3)
    spin_values = np.arange(7.5, 43.5, 2)

    numerical_values = [(
        spin,
        wobb_1.omega(spin), wobb_1.omega_chiral(spin),
        wobb_2.omega(spin), wobb_2.omega_chiral(spin),
        wobb_3.omega(spin), wobb_3.omega_chiral(spin))
        for spin in spin_values]
    return numerical_values


def main():
    """Main function"""
    def header(idx: str) -> tuple: return (
        'I',
        f'omega_{idx}', f'omega_{idx}_pi')
    exporter.export_to_csv(fit_1(), 'data_fit_1', header('1'))
    exporter.export_to_csv(fit_2(), 'data_fit_2', header('2'))
    exporter.export_to_csv(fit_3(), 'data_fit_3', header('3'))
    exporter.export_to_csv(fit_all(), 'data_fit_all', header=(
        'I',
        'omega_1', 'omega_1_pi',
        'omega_2', 'omega_2_pi',
        'omega_3', 'omega_3_pi'))


if __name__ == "__main__":
    main()
