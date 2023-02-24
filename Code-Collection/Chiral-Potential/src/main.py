import config
import chiral
import elliptic


def fit1() -> None:
    params = config.FittingParameters()
    moi_fit1, odd_spin, theta_deg_fit1 = params.fit1()
    potential = chiral.Potential(moi_fit1, odd_spin)
    print(potential.v_q_chiral(1, 22.5, -119))


def main():
    fit1()


if __name__ == '__main__':
    main()
