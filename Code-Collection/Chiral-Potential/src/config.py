from dataclasses import dataclass


@dataclass
class FittingParameters:
    """
    - A class that contains all the fitting parameters used within calculations
    - The fitting parameters are taken from New Boson work (2020)
    """
    MOI_FIT1: tuple[float, float, float]
    MOI_FIT2: tuple[float, float, float]
    MOI_FIT3: tuple[float, float, float]
    ODD_SPIN: float
    THETA_DEG_FIT1: float
    THETA_DEG_FIT2: float
    THETA_DEG_FIT3: float

    def __init__(self):
        self.MOI_FIT1 = (91.0, 9.0, 51.0)
        self.MOI_FIT2 = (13.53, 101.76, 52.94)
        self.MOI_FIT3 = (89.0, 12.0, 48.0)
        self.ODD_SPIN = 5.5
        self.THETA_DEG_FIT1 = -117
        self.THETA_DEG_FIT2 = 140
        self.THETA_DEG_FIT3 = -71

    def fit1(self) -> tuple[tuple, float, float]:
        """
        - Returns the fitting parameters that are obtained from fitting all the excitation energies for 135Pr
        """
        return self.MOI_FIT1, self.ODD_SPIN, self.THETA_DEG_FIT1

    def fit2(self) -> tuple[tuple, float, float]:
        """
        - Returns the fitting parameters that were obtained by considering MOI_2 as maximal MOI
        """
        return self.MOI_FIT2, self.ODD_SPIN, self.THETA_DEG_FIT2

    def fit3(self) -> tuple[tuple, float, float]:
        """
        - Returns the fitting parameters obtained by using omega'
        """
        return self.MOI_FIT3, self.ODD_SPIN, self.THETA_DEG_FIT3
