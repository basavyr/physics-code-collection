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
        result = A2*(1.0-j2/I)-A1
        return result
