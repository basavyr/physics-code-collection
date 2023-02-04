import numpy as np


class j_SingleParticle:
    """
    - define the single-particle angular momentum components in terms of the polar coordinates
    - the polar coordinates are $\theta,\varphi$.
    """

    def __init__(self, j_abs: float, theta_degrees: float) -> None:
        self.j = j_abs
        self.theta_degrees = theta_degrees
        self.theta_rad = np.pi*theta_degrees/180.0

    def j_vec(self) -> tuple[float, float, float]:
        """
        - returns a tuple (j1, j2, j3) containing the three components of the angular momentum vector $\\vec{j}$
        """
        j1 = self.j*np.cos(self.theta_rad)
        j2 = self.j*np.sin(self.theta_rad)
        j3 = 0
        return (j1, j2, j3)


class x_AngularMomentum:
    """
    - the classical components of the total angular momentum I written in terms of the polar coordinates \theta,\varphi
    """
    @staticmethod
    def x1(spin: float, theta_2_deg: float, varphi_2_deg: float) -> float:
        I = spin
        theta_2_rad = theta_2_deg*np.pi/180.0
        varphi_2_rad = varphi_2_deg*np.pi/180.0
        return float(I*np.sin(theta_2_rad)*np.sin(varphi_2_rad))

    @staticmethod
    def x2(spin: float, theta_2_deg: float, varphi_2_deg: float) -> float:
        I = spin
        theta_2_rad = theta_2_deg*np.pi/180.0
        return float(I*np.cos(theta_2_rad))

    @staticmethod
    def x3(spin: float, theta_2_deg: float, varphi_2_deg: float) -> float:
        I = spin
        theta_2_rad = theta_2_deg*np.pi/180.0
        varphi_2_rad = varphi_2_deg*np.pi/180.0
        return float(I*np.sin(theta_2_rad)*np.cos(varphi_2_rad))
