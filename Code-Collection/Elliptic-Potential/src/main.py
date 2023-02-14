import numpy as np
import elliptic_potential


def main():
    # create the class instances for usage
    E = elliptic_potential.EllipticFunctions()
    N = elliptic_potential.NumericalFactors()

    # define the inertia factors
    A1_N = N.inertia_factor(N.MOI_1)
    A2_N = N.inertia_factor(N.MOI_2)
    A3_N = N.inertia_factor(N.MOI_3)

    u_N = N.u(N.SPIN, N.ODD_SPIN, N.THETA, A1_N, A2_N, A3_N)
    A_N = N.A(N.SPIN, N.ODD_SPIN, N.THETA, A1_N, A2_N)
    v0_N = N.v0(N.SPIN, N.ODD_SPIN, N.THETA, A1_N, A2_N)

    k_N = E.k(u_N)
    k_prime_N = E.k_prime(u_N)

    q_values = np.arange(-8, 8, 0.2)
    for q in q_values:
        v_q = E.v_q(N.SPIN, q, k_N, v0_N)
        print(q, v_q)


if __name__ == '__main__':
    main()
