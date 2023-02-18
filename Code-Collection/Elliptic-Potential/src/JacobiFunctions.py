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
        - Returns the JacobiAmplitude (amu) of modulus m=k^2 and also m=k
        - If the amu(q,k)=phi, then s=sin(phi)...s
        """
        k_squared = np.power(k, 2)
        amu_k = special.ellipj(q, k)[3]
        amu_k_squared = special.ellipj(q, k_squared)[3]

        return [amu_k, amu_k_squared]
