import wobbling
import fit
import numpy as np
import exporter


def fit_1() -> list[tuple]:
    params = fit.FittingParameters()
    wobb = wobbling.Wobbling(params.SET_1)
    spin_values = np.arange(7.5, 43.5, 2)
    numerical_values = [(spin, wobb.omega(spin), wobb.omega_chiral(spin))
                        for spin in spin_values]

    return numerical_values


def fit_2() -> list[tuple]:
    params = fit.FittingParameters()
    wobb = wobbling.Wobbling(params.SET_2)
    spin_values = np.arange(7.5, 43.5, 2)
    numerical_values = [(spin, wobb.omega(spin), wobb.omega_chiral(spin))
                        for spin in spin_values]

    return numerical_values


def fit_3() -> list[tuple]:
    params = fit.FittingParameters()
    wobb = wobbling.Wobbling(params.SET_3)
    spin_values = np.arange(7.5, 43.5, 2)
    numerical_values = [(spin, wobb.omega(spin), wobb.omega_chiral(spin))
                        for spin in spin_values]

    return numerical_values


def fit_all_omega() -> list[tuple]:
    """
    - returns data for all the fits with omega and omega_chiral
    """
    params = fit.FittingParameters()

    wobb_1 = wobbling.Wobbling(params.SET_1)
    wobb_2 = wobbling.Wobbling(params.SET_2)
    wobb_3 = wobbling.Wobbling(params.SET_3)

    spin_values = np.arange(7.5, 43.5, 2)

    numerical_values = [(
        spin,
        wobb_1.omega(spin), wobb_1.omega_chiral(spin),
        wobb_2.omega(spin), wobb_2.omega_chiral(spin),
        wobb_3.omega(spin), wobb_3.omega_chiral(spin))
        for spin in spin_values]
    return numerical_values


def fit_all_omega_prime() -> list[tuple]:
    """
    - returns data for all fits with omega' and omega'_chiral
    """
    params = fit.FittingParameters()

    wobb_1 = wobbling.Wobbling(params.SET_1)
    wobb_2 = wobbling.Wobbling(params.SET_2)
    wobb_3 = wobbling.Wobbling(params.SET_3)

    spin_values = np.arange(7.5, 43.5, 2)

    numerical_values = [(
        spin,
        wobb_1.omega_prime(spin), wobb_1.omega_prime_chiral(spin),
        wobb_2.omega_prime(spin), wobb_2.omega_prime_chiral(spin),
        wobb_3.omega_prime(spin), wobb_3.omega_prime_chiral(spin)
    ) for spin in spin_values]

    return numerical_values


def header(idx: str) -> tuple:
    return ('I', f'omega_{idx}', f'omega_{idx}_pi')


def main():
    """Main function"""
    exporter.export_to_csv(fit_all_omega_prime(), 'data_fit_all_prime', header=(
        'I',
        f"omega'_1", f"omega'_1_pi",
        f"omega'_2", f"omega'_2_pi",
        f"omega'_3", f"omega'_3_pi"))

    exporter.export_to_csv(fit_all_omega(), 'data_fit_all', header=(
        'I',
        f"omega_1", f"omega_1_pi",
        f"omega_2", f"omega_2_pi",
        f"omega_3", f"omega_3_pi"))


if __name__ == "__main__":
    main()
