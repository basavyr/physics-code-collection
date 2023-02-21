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
        - Calculates the A term from 2.4 (New Boson 2020)
        """
        j2 = self.j_k(theta_rad)[1]
        return self.A2*(1.0-j2/spin)-self.A1

    def v0_term(self, spin: float, theta_rad: float) -> float:
        """
        - Calculates the v0 term from 2.4 (New Boson 2020)
        """
        j1 = self.j_k(theta_rad)[0]
        return -((self.A1*j1)/self.a_term(spin, theta_rad))

    def u_term(self, spin: float, theta_rad: float) -> float:
        """
        - Calculates the u term from 2.4 (New Boson 2020)
        """
        return (self.A3-self.A1)/self.a_term(spin, theta_rad)

    def a21(self, spin: float, theta_rad: float) -> float:
        """
        - returns a sub-term from omega containing the delta(A2,A1)
        """
        j2 = self.j_k(theta_rad)[1]
        return self.A2-self.A1-(self.A2*j2/spin)

    def omega(self, spin: float) -> float:
        """
        - returns the wobbling frequency from 4.4 (New Boson 2020)
        - evaluated for theta
        """
        spin2p1 = (2.0*spin+1.0)
        a1j1 = self.A1*self.j_k(self.theta)[0]

        sub_term_1 = spin2p1*self.a21(spin, self.theta)+2.0*a1j1
        sub_term_2 = spin2p1*(self.A3-self.A1)+2.0*a1j1
        sub_term_3 = (self.A3-self.A1)*self.a21(spin, self.theta)

        return np.power(sub_term_1*sub_term_2-sub_term_3, 0.5)

    def omega_chiral(self, spin: float) -> float:
        """
        - returns the wobbling frequency from 4.4 (New Boson 2020)
        - evaluated for theta+pi
        """
        spin2p1 = (2.0*spin+1.0)
        a1j1 = self.A1*self.j_k(self.theta_chiral)[0]

        sub_term_1 = spin2p1*self.a21(spin, self.theta_chiral)+2.0*a1j1
        sub_term_2 = spin2p1*(self.A3-self.A1)+2.0*a1j1
        sub_term_3 = (self.A3-self.A1)*self.a21(spin, self.theta_chiral)

        return np.power(sub_term_1*sub_term_2-sub_term_3, 0.5)

    def omega_prime(self, spin: float) -> float:
        """
        - returns the wobbling frequency from 4.7
        - evaluated for theta
        """
        spin2p1 = 2.0*spin+1.0
        a1j1 = self.A1*self.j_k(self.theta)[0]

        sub_term_1 = spin2p1*self.a21(spin, self.theta)-2.0*a1j1
        sub_term_2 = spin2p1*(self.A3-self.A1)-2.0*a1j1
        sub_term_3 = (self.A3-self.A1)*self.a21(spin, self.theta)

        return np.power(sub_term_1*sub_term_2-sub_term_3, 0.5)

    def omega_prime_chiral(self, spin: float) -> float:
        """
        - returns the wobbling frequency from 4.7
        - evaluated for theta+pi
        """
        spin2p1 = 2.0*spin+1.0
        a1j1 = self.A1*self.j_k(self.theta_chiral)[0]

        sub_term_1 = spin2p1*self.a21(spin, self.theta_chiral)-2.0*a1j1
        sub_term_2 = spin2p1*(self.A3-self.A1)-2.0*a1j1
        sub_term_3 = (self.A3-self.A1)*self.a21(spin, self.theta_chiral)

        return np.power(sub_term_1*sub_term_2-sub_term_3, 0.5)
