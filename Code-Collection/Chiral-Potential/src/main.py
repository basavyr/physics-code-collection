import config
import chiral
import elliptic


def fit1() -> None:
    params = config.FittingParameters()
    moi_fit1, odd_spin, theta_deg_fit1 = params.fit1()
    ellip_func = elliptic.EllipticFunctions(
        moi_fit1[0], moi_fit1[0], moi_fit1[0], odd_spin)

def main():
    fit1()


if __name__ == '__main__':
    main()
