import numpy as np
from matplotlib import pyplot as plt


class Elliptic:
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
