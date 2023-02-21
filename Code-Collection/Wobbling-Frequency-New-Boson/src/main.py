import wobbling
import fit


def fit_1():
    params = fit.FittingParameters()
    wobb = wobbling.Wobbling(
        params.MOIS_1, params.ODD_SPIN, params.THETA_DEG_1)


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
    fit_1()


if __name__ == "__main__":
    main()
