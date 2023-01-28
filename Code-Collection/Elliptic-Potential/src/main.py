import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as integrate
import scipy.special as special


class NumericalFactors:
    """
    - the numerical factors that are used to define the Rotational Hamiltonian
    """
    THETA = -80.0
    ODD_SPIN = float(13.0/2.0)
    MOI_1 = 95.0
    MOI_2 = 100.0
    MOI_3 = 85.0

    def inertia_factor(moi):
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


def main():
    E = EllipticFunctions()
    print(E.q_var(np.pi/2.0, 1.0/2.0))


if __name__ == '__main__':
    main()
