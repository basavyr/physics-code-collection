import numpy as np
from matplotlib import pyplot as plt


class Elliptic:
    THETA = -80.0
    ODD_SPIN = float(13.0/2.0)

    def j_vec(self, j_abs, theta):
        """
        - calculate the three components of the odd-particle a.m. vector \vec{j}
        """
        def rad(angle): return float(angle*np.pi/180.0)
        vec = [j_abs*np.cos(rad(theta)), j_abs*np.sin(rad(theta)), 0]
        return vec


e = Elliptic()
j1 = e.j_vec(e.ODD_SPIN, e.THETA)[0]
j2 = e.j_vec(e.ODD_SPIN, e.THETA)[1]
j3 = e.j_vec(e.ODD_SPIN, e.THETA)[2]
