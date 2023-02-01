import numpy as np


class j_SingleParticle:
    """
    - define the single-particle angular momentum components in terms of the polar coordinates
    - the polar coordinates are $\theta,\varphi$.
    """

    def __init__(self, j_abs, theta_degrees):
        self.j = j_abs
        self.theta_degrees = theta_degrees
        self.theta_rad = np.pi*theta_degrees/180.0

    def j_vec(self):
        """
        - returns a tuple [j1, j2, j3] containing the three components of the angular momentum vector $\\vec{j}$
        """
        j1 = self.j*np.cos(self.theta_rad)
        j2 = self.j*np.sin(self.theta_rad)
        j3 = 0
        return [j1, j2, j3]
