import numpy as np


class EnergyFunction:
    def __init__(
            self,
            moi1: float,
            moi2: float,
            moi3: float,
            j: float,
            theta: int) -> None:
        self.A1 = 1.0 / (2.0 * moi1)
        self.A2 = 1.0 / (2.0 * moi2)
        self.A3 = 1.0 / (2.0 * moi3)
        self.j1 = j * np.cos(theta * np.pi / 180.0)
        self.j2 = j * np.sin(theta * np.pi / 180.0)

    def wobbling_frequency(self, spin: float) -> float:
        """
        - Returns the wobbling frequency from Eq. (4.4)
        """
        I = spin

        sub_term_1 = (2.0 * I + 1.0) * (self.A2 - self.A1 -
                                        (self.A2 * self.j2) / I) + 2.0 * self.A1 * self.j1
        sub_term_2 = (2.0 * I + 1) * (self.A3 - self.A1) + \
            2.0 * self.A1 * self.j1
        sub_term_3 = (self.A3 - self.A1) * \
            (self.A2 - self.A1 - (self.A2 * self.j2) / I)

        return np.round(np.sqrt(sub_term_1 * sub_term_2 - sub_term_3), 3)

    def absolute_energy(self, spin: float, n: int) -> float:
        """
        - Returns the Excitation energy E_n from Eq. (4.3)
        """
        I = spin

        h_omega = self.wobbling_frequency(I) * (n + 0.5)

        sub_term_1 = self.A1 * np.power(I, 2) - \
            (2.0 * I + 1.0) * self.A1 * self.j1 - I * self.A2 * self.j2
        sub_term_2 = self.A1 * np.power(self.j1, 2) + \
            self.A2 * np.power(self.j2, 2)

        return np.round(sub_term_1 + h_omega + sub_term_2, 3)
