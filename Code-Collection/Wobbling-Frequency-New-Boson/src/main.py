import wobbling
import fit


def main():
    """Main function"""
    params = fit.FittingParameters()
    fit_1 = wobbling.Wobbling(
        params.MOIS_1, params.ODD_SPIN, params.THETA_DEG_1)
    fit_2 = wobbling.Wobbling(
        params.MOIS_2, params.ODD_SPIN, params.THETA_DEG_2)
    fit_3 = wobbling.Wobbling(
        params.MOIS_3, params.ODD_SPIN, params.THETA_DEG_3)


if __name__ == "__main__":
    main()
