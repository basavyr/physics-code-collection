from dataclasses import dataclass
import numpy as np


@dataclass
class FitParameters:
    """
    - class that contains the fitting parameters and other relevant constants from New Boson work
    """
    SPIN_VALUE: float
    ODD_SPIN: float
    THETA_DEG: float
    MOI: tuple[float, float, float]
    SPINS_BAND1: np.ndarray

    def __init__(self) -> None:
        self.SPIN_VALUE = 22.5
        self.ODD_SPIN = 5.5
        self.THETA_DEG = -119.0
        self.MOI = (91.0, 9.0, 51.0)
        self.SPINS_BAND1 = np.arange(7.5, 29.5, 2.0)

    def get_params(self) -> tuple:
        return self.MOI, self.ODD_SPIN, self.THETA_DEG
