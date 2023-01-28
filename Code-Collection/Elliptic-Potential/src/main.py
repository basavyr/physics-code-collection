import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as integrate
import scipy.special as special


class NumericalFactors:
    """
    - the numerical factors that are used to define the Rotational Hamiltonian
    """
    THETA = -80.0
    SPIN = 45.0/2.0
    ODD_SPIN = float(13.0/2.0)
    MOI_1 = 95.0
    MOI_2 = 100.0
    MOI_3 = 85.0

    def inertia_factor(self, moi):
        return float(1.0/(2.0*moi))

    def j_vec(self, j_abs, theta):
        """
        - calculate the three components of the odd-particle a.m. vector \vec{j}
        """
        def rad(angle): return float(angle*np.pi/180.0)

        vec = [j_abs*np.cos(rad(theta)), j_abs*np.sin(rad(theta)), 0]

        return vec

    def j_k(self, j_abs, theta, k):
        """
        - returns the k-th component of the single-particle angular momentum vector
        """
        return self.j_vec(j_abs, theta)[k-1]

    def A(self, spin, odd_spin, theta, A1, A2):
        """
        - returns the A term from Eq. (2.4)
        """
        I = spin
        j = odd_spin
        j2 = self.j_k(j, theta, 2)
        result = float(A2*(1.0-j2/I)-A1)
        return result

    def v0(self, spin, odd_spin, theta, A1, A2):
        """
        - returns the v0 term from Eq. (2.4)
        """
        I = spin
        j = odd_spin
        j1 = self.j_k(j, theta, 1)
        A_term = self.A(I, j, theta, A1, A2)
        result = float(-(A1*j1)/A_term)
        return result

    def u(self, spin, odd_spin, theta, A1, A2, A3):
        """
        - return the u term from Eq. (2.4)
        """
        I = spin
        j = odd_spin
        A_term = self.A(I, j, theta, A1, A2)
        result = float((A3-A1)/A_term)
        return result


class EllipticFunctions:
    """
    - a class containing all the Jacobi Elliptic Functions and the associated elliptic potential
    """

    def k(self, u):
        """
        - returns the value of k term from Eq. (2.10)
        """
        k_term = np.sqrt(np.abs(u))
        return k_term

    def k_prime(self, u):
        """
        - returns the value of k' term from Eq. (2.10)
        """
        k_squared = np.power(self.k(u), 2)
        k_prime_term = np.sqrt(1.0-k_squared)
        return k_prime_term

    def q_var(self, phi, k):
        """
        - returns the numerical value of the coordinate q, i.e., the inverse of the incomplete elliptic integral of first kind
        """
        k_squared = np.power(k, 2)
        def sin2x(x): return np.power(np.sin(x), 2)
        def q_term(x): return 1.0/np.sqrt(1-k_squared*sin2x(x))
        q_int = integrate.quad(q_term, 0, phi)
        return q_int[0]

    def phi_var(self, q, k):
        """
        - returns the Jacobi amplitude, connecting the coordinate q to the trigonometric variable \varphi
        """
        k_squared = np.power(k, 2)
        sn, cn, dn, amu = special.ellipj(q, k_squared)
        return amu

    def v_q(self, spin, q, k, v0):
        """
        - returns the expression for the elliptic potential V(q), given by Eq. (2.16)
        """
        I = spin
        k_squared = np.power(k, 2)
        v0_squared = np.power(v0, 2)
        s, c, d, _ = special.ellipj(q, k_squared)
        s_squared = np.power(s, 2)
        t1 = (I*(I+1.0)*k_squared+v0_squared)*s_squared
        t2 = (2.0*I+1.0)*v0*c*d
        v_term = t1+t2
        return v_term


def main():
    # create the class instances for usage
    E = EllipticFunctions()
    N = NumericalFactors()

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
        print(q,v_q)


if __name__ == '__main__':
    main()
