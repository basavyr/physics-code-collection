import elliptic
from dataclasses import dataclass


@dataclass
class Potential:
    """
    - Class that calculates the Elliptic potential V(q) and also the Chiral Potential (symmetric and asymmetric terms)
    """
    sn: float
    cn: float
    dn: float
    k: float

    def __init__(self, k: float, sn: float, cn: float, dn: float) -> None:
        self.sn = sn
        self.cn = cn
        self.dn = dn
        self.k = k

    def v_q(self, q: float, spin: float, theta: float) -> float:
        """
        - Calculate the potential using the elliptic functions
        """
        