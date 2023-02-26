import numpy as np
from dataclasses import dataclass


@dataclass
class Energies:
    """
    - class that contains the excitation energies for the 135Pr nucleus
    """
    A1: float
    A2: float
    A3: float
    j: float
    j1: float
    j2: float

    def __init__(self, moi: tuple[float, float, float], odd_spin: float, theta_deg: float) -> None:
        self.A1, self.A2, self.A3 = (1.0/(2.0*moi_k) for moi_k in moi)
        self.j = odd_spin
        self.j1 = odd_spin*np.cos(theta_deg*np.pi/180.0)
        self.j2 = odd_spin*np.sin(theta_deg*np.pi/180.0)

    def show(self):
        print(self.A1, self.A2, self.A3, self.j1, self.j2)
