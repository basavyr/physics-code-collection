import numpy as np
import scipy.integrate as integrate
import scipy.special as special


class NumericalFactors:
    """
    - the numerical factors that are used to define the Rotational Hamiltonian
    """
    THETA = -80.0
    SPIN = 45.0 / 2.0
    ODD_SPIN = float(13.0 / 2.0)
    MOI_1 = 95.0
    MOI_2 = 100.0
    MOI_3 = 85.0

    def inertia_factor(self, moi):
        return float(1.0 / (2.0 * moi))

    def j_vec(self, j_abs, theta):
        """
        - calculate the three components of the odd-particle a.m. vector \vec{j}
        """
        def rad(angle): return float(angle * np.pi / 180.0)

        vec = [j_abs * np.cos(rad(theta)), j_abs * np.sin(rad(theta)), 0]

        return vec

    def j_k(self, j_abs, theta, k):
        """
        - returns the k-th component of the single-particle angular momentum vector
        """
        return self.j_vec(j_abs, theta)[k - 1]

    def a_term(self, spin, odd_spin, theta, A1, A2):
        """
        - returns the A term from Eq. (2.4)
        """
        I = spin
        j = odd_spin
        j2 = self.j_k(j, theta, 2)
        result = float(A2 * (1.0 - j2 / I) - A1)
        return result

    def v0(self, spin, odd_spin, theta, A1, A2):
        """
        - returns the v0 term from Eq. (2.4)
        """
        I = spin
        j = odd_spin
        j1 = self.j_k(j, theta, 1)
        a_term = self.a_term(I, j, theta, A1, A2)
        result = float(-(A1 * j1) / a_term)
        return result

    def u(self, spin, odd_spin, theta, A1, A2, A3):
        """
        - return the u term from Eq. (2.4)
        """
        I = spin
        j = odd_spin
        a_term = self.a_term(I, j, theta, A1, A2)
        result = float((A3 - A1) / a_term)
        return result


class EllipticFunctions:
    """
    - A class containing the Jacobi Elliptic Functions and the elliptic potential
    - Requires the moments of inertia, $\theta$ angle, and the single-particle angular momentum
    """

    def __init__(self, moi_1: float, moi_2: float, moi_3: float, odd_spin: float) -> None:
        self.I1 = moi_1
        self.I2 = moi_2
        self.I3 = moi_3
        self.j = odd_spin
        self.A1 = 1.0/(2.0*moi_1)
        self.A2 = 1.0/(2.0*moi_2)
        self.A3 = 1.0/(2.0*moi_3)

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
        k_prime_term = np.sqrt(1.0 - k_squared)
        return k_prime_term

    def q_var(self, phi, k):
        """
        - returns the numerical value of the coordinate q, i.e., the inverse of the incomplete elliptic integral of first kind
        """
        k_squared = np.power(k, 2)
        def sin2x(x): return np.power(np.sin(x), 2)
        def q_term(x): return 1.0 / np.sqrt(1 - k_squared * sin2x(x))
        q_int = integrate.quad(q_term, 0, phi)
        return q_int[0]

    def amu(self, q: float, k: float) -> float:
        """
        - returns the Jacobi amplitude for the variable q and modulus k
        - the function takes the argument k as is, and it produces similar results to the Mathematica's equivalent JacobiAmplitude[u,m] (ref/JacobiAmplitude)
        """
        return special.ellipj(q, k)[3]

    def phi_var(self, q, k):
        """
        - returns the Jacobi amplitude, connecting the coordinate q to the trigonometric variable \varphi
        """
        _, _, _, amu = special.ellipj(q, k)
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
        t1 = (I * (I + 1.0) * k_squared + v0_squared) * s_squared
        t2 = (2.0 * I + 1.0) * v0 * c * d
        v_term = t1 + t2
        return v_term

    def v_q_func(self, spin: float, theta_deg: float, q: float) -> float:
        """
        - Calculate the elliptic potential only from the angular momentum, the angle theta, and q variable
        """
        I = spin
        theta_rad = theta_deg*np.pi/180.0
        j1 = self.j*np.cos(theta_rad)
        j2 = self.j*np.sin(theta_rad)
        a = self.A2*(1.0-j2/I)-self.A1
        v0 = -(self.A1*j1)/a
        u = (self.A3-self.A1)/a
        k = np.sqrt(np.abs(u))
        k_squared = np.power(k, 2)
        phi_q = self.amu(q, k)
        # print(q, k, phi_q)
        # print(self.amu(4.0, 2/3))
        s = np.sin(phi_q)
        s_squared = np.power(s, 2)
        c = np.cos(phi_q)
        d = np.sqrt(1.0-k_squared*s_squared)
        v = (I*(I+1.0)*k_squared+np.power(v0, 2)) * \
            s_squared+(2.0*I+1.0)*v0*c*d
        return np.round(v, 3)
