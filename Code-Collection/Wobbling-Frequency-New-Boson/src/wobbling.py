import numpy as np
from dataclasses import dataclass


@dataclass
class Wobbling:
    """
    - A class containing the functions for the wobbling frequency of a triaxial rotor.
    """
    A1: float
    A2: float
    A3: float
    theta: float
    theta_chiral: float
    j: float

    def __init__(self, mois: tuple[float, float, float], odd_spin: float, theta_deg: float) -> None:
        self.A1 = 1.0/(2.0*mois[0])
        self.A2 = 1.0/(2.0*mois[1])
        self.A3 = 1.0/(2.0*mois[2])
        self.theta = theta_deg*np.pi/180.0
        self.theta_chiral = (theta_deg+180.0)*np.pi/180.0
        self.j = odd_spin

    def j_k(self, theta_rad: float) -> tuple[float, float, float]:
        return (self.j * np.cos(theta_rad), self.j * np.sin(theta_rad), 0.0)

    def a_term(self, spin: float, theta_rad: float) -> float:
        """
        - Calculates the A term from 2.4
        """
        j2 = self.j_k(theta_rad)[1]
        return self.A2*(1.0-j2/spin)-self.A1

    def u_term(self, spin: float, theta_rad: float) -> float:
        """
        - Calculates the u term from 2.4
        """
        return (self.A3-self.A1)/self.a_term(spin, theta_rad)

    def v0_term(self, spin: float, theta_rad: float) -> float:
        """
        - Calculates the v0 term from 2.4
        """
        j1 = self.j_k(theta_rad)[0]
        return -((self.A1*j1)/self.a_term(spin, theta_rad))
