from dataclasses import dataclass


@dataclass
class FittingParameters:
    """
    Class containing all the fitting parameters
    """
    MOIS_1: tuple[float, float, float]
    MOIS_2: tuple[float, float, float]
    MOIS_3: tuple[float, float, float]
    THETA_DEG_1: float
    THETA_DEG_2: float
    THETA_DEG_3: float
    ODD_SPIN: float

    MOIS_1 = (91.0, 9.0, 51.0)
    MOIS_2 = (13.53, 101.76, 52.94)
    MOIS_3 = (89.0, 12.0, 48.0)
    THETA_DEG_1 = -119.0
    THETA_DEG_2 = 140.0
    THETA_DEG_3 = -71.0
    ODD_SPIN = 5.5
