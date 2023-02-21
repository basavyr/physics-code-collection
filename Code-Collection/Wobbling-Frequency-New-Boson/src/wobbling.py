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
    j1: float
    j2: float

    def __init__(self, mois: tuple[float, float, float], odd_spin: float, theta_deg: float) -> None:
        self.A1 = 1.0/(2.0*mois[0])
        self.A2 = 1.0/(2.0*mois[1])
        self.A3 = 1.0/(2.0*mois[2])
        self.j1 = float(odd_spin*np.cos(theta_deg*np.pi/180.0))
        self.j2 = float(odd_spin*np.sin(theta_deg*np.pi/180.0))
