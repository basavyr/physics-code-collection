import numpy as np


class Constants:
    """
    - contains all the constants that are used within the calculations for the classical energy function
    """

    def __init__(self, moi_1, moi_2, moi_3, odd_spin, theta_degrees):
        self.j = odd_spin
        self.A1 = 1.0/(2.0 * moi_1)
        self.A2 = 1.0/(2.0 * moi_2)
        self.A3 = 1.0/(2.0 * moi_3)
        self.theta_degrees = theta_degrees
        self.theta_rad = theta_degrees * np.pi / 180.0
