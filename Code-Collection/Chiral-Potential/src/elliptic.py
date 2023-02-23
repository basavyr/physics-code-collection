from scipy.special import ellipj
from dataclasses import dataclass
import numpy as np


@dataclass
class EllipticFunctions:
    """
    - A class that contains Jacobi elliptic functions sn,cn,dn
    - These functions are used inside the elliptic potential V(q) employed in New Boson work (2020)
    """
    A1: float
    A2: float
    A3: float
    odd_spin: float

    def __init__(self, moi1: float, moi2: float, moi3: float, odd_spin: float) -> None:
        self.A1, self.A2, self.A3 = (
            1.0/(2.0*moi1), 1.0/(2.0*moi2), 1.0/(2.0*moi3))
        self.odd_spin = odd_spin

    def j(self, theta_deg: float) -> tuple[float, float, float]:
        """
        - returns the three components of the single-particle a.m. (j_1,j_2,j_3)
        - assumes rigid coupling, i.e., j_3=0
        """
        j1 = self.odd_spin*np.cos(theta_deg*np.pi/180.0)
        j2 = self.odd_spin*np.sin(theta_deg*np.pi/180.0)
        return j1, j2, 0

    def a_factor(self, spin: float, theta_deg: float) -> float:
        """
        - Returns the A-factor from Eq. 2.4
        """
        _, j2, _ = self.j(theta_deg)
        return self.A2*(1.0-j2/spin)-self.A1

    def v0_factor(self, spin: float, theta_deg: float) -> float:
        """
        - Returns the v0 factor from Eq. 2.4
        """
        # use Extended Iterable Unpacking (https://peps.python.org/pep-3132/)
        j1, *_ = self.j(theta_deg)
        return -(self.A1*j1)/self.a_factor(spin, theta_deg)

    def u_factor(self, spin: float, theta_deg: float) -> float:
        """
        - Returns the u factor from Eq. 2.4
        """
        return (self.A3-self.A1)/self.a_factor(spin, theta_deg)

    def modulus_k(self, spin: float, theta_deg: float) -> float:
        """
        - Returns the modulus "k" that is used within Jacobi functions
        """
        return np.sqrt(self.u_factor(spin, theta_deg))

    def amu(self, q: float, k: float) -> float:
        """
        - Returns the JacobiAmplitude `amu` of modulus m=k^2
        - The amplitude is used to determine sn,cn,dn functions
        - If amu=phi, then sn=sin(phi), cn=cos(phi),...
        """
        *_, phi = ellipj(q, np.power(k, 2))
        return phi

    def sn(self, q: float, k: float) -> float:
        """
        - Returns Jacobi elliptic function sn=sin(amu(q,k))
        """
        phi = self.amu(q, k)
        return np.sin(phi)

    def cn(self, q: float, k: float) -> float:
        """
        - Returns Jacobi elliptic function sn=cos(amu(q,k))
        """
        phi = self.amu(q, k)
        return np.cos(phi)

    def dn(self, q: float, k: float) -> float:
        """
        - Returns Jacobi elliptic function dn
        """
        return np.sqrt(1-np.power(k, 2)*np.power(self.sn(q, k), 2))
