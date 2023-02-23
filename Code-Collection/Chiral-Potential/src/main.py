import config
import chiral


def main():
    params = config.FittingParameters()
    moi_fit1, odd_spin, theta_deg_fit1 = params.fit1()
    print(moi_fit1)


if __name__ == '__main__':
    main()
