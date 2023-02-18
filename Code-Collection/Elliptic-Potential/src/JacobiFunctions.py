import numpy as np
import scipy.special as special
from dataclasses import dataclass


@dataclass
class Jacobi:
    """
    - A class containing the Jacobi Elliptic Functions, such as sn, cn, dn
    - It uses the scipy module to get the Jacobi Amplitude of modulus m
    """
    q: float
    k: float
    v0: float

    def __init__(self,  q: float, k: float, v0: float) -> None:
        self.q = q
        self.v0 = v0
        self.k = k

    def amu(self, q: float, k: float) -> tuple[float, float]:
        """
        - Returns the JacobiAmplitude (amu) of modulus m=k^2 and m=k
        - If the amu(q,k)=phi, then s=sin(phi)...s
        """
        amu_k_squared = special.ellipj(q, np.power(k, 2))[3]
        amu_k = special.ellipj(q, k)[3]

        return (amu_k_squared, amu_k)

    def sn_k(self, q: float, k: float) -> float:
        """
        - returns the Jacobi Elliptic function sn=sin(amu(q,k))
        """
        _, phi_k = self.amu(q, k)
        return np.sin(phi_k)

    def sn_k_squared(self, q: float, k: float) -> float:
        """
        - returns the Jacobi Elliptic function sn=sin(amu(q,k^2))
        """
        phi_k_squared, _ = self.amu(q, k)
        return np.sin(phi_k_squared)

    def cn_k(self, q: float, k: float) -> float:
        """
        - returns the Jacobi Elliptic function cn=cos(amu(q,k))
        """
        _, phi_k = self.amu(q, k)
        return np.cos(phi_k)

    def cn_k_squared(self, q: float, k: float) -> float:
        """
        - returns the Jacobi Elliptic function cn=cos(amu(q,k^2))
        """
        phi_k_squared, _ = self.amu(q, k)
        return np.cos(phi_k_squared)

    def dn_k(self, q: float, k: float) -> float:
        """
        - returns the Jacobi Elliptic function dn(q,k)
        """
        s = self.sn_k(q, k)
        return np.sqrt(1-np.power(k, 2)*np.power(s, 2))

    def dn_k_squared(self, q: float, k: float) -> float:
        """
        - returns the Jacobi Elliptic function dn(q,k^2)
        """
        s = self.sn_k_squared(q, k)
        return np.sqrt(1-np.power(k, 2)*np.power(s, 2))
