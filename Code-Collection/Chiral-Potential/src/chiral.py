import elliptic as elliptic_functions
from dataclasses import dataclass
import numpy as np


@dataclass
class Potential:
    """
    - Class that calculates the Elliptic potential V(q) and also the Chiral Potential (symmetric and asymmetric terms)
    """
    elliptic: elliptic_functions.EllipticFunctions

    def __init__(self, moi: tuple[float, float, float], odd_spin: float) -> None:
        moi1, moi2, moi3 = moi
        self.elliptic = elliptic_functions.EllipticFunctions(
            moi1, moi2, moi3, odd_spin)

    def v_q(self, q: float, spin: float, theta_deg: float) -> float:
        """
        - Calculate the potential using the elliptic functions
        """
        k = self.elliptic.modulus_k(spin, theta_deg)
        s = self.elliptic.sn(q, k)
        c = self.elliptic.cn(q, k)
        d = self.elliptic.dn(q, k)
        v0 = self.elliptic.v0_factor(spin, theta_deg)
        return spin*(spin+1.0)*np.power(k, 2)+np.power(v0, 2)+(2.0*spin+1.0)*v0*c*d

    def v_q_chiral(self, q: float, spin: float, theta_deg: float)
