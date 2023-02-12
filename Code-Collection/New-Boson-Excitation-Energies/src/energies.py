import numpy as np


class EnergyFunction:
    def __init__(
            self,
            moi1: float,
            moi2: float,
            moi3: float,
            j: float,
            theta: int,
            band_head: float) -> None:
        self.A1 = 1.0 / (2.0 * moi1)
        self.A2 = 1.0 / (2.0 * moi2)
        self.A3 = 1.0 / (2.0 * moi3)
        self.j1 = j * np.cos(theta * np.pi / 180.0)
        self.j2 = j * np.sin(theta * np.pi / 180.0)
        self.I0 = band_head

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

        return np.round(np.sqrt(sub_term_1 * sub_term_2 - sub_term_3), 4)

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

        return np.round(sub_term_1 + h_omega + sub_term_2, 4)

    def excitation_energy(self, spin: float, n: int) -> float:
        """
        - returns the absolute energy of a spin state, minus the band head energy
        """
        band_head_energy = self.absolute_energy(self.I0, 0)
        return np.round(self.absolute_energy(spin, n) - band_head_energy, 4)

    def generate_energy_band(
            self,
            band_head_energy: float,
            gammas: list[float]) -> np.ndarray:
        """
        - Generate a list of energies based on the ground-state energy and the gamma transitions between adjacent levels
        """
        energies = [band_head_energy]
        for idx in range(len(gammas)):
            energies.append(gammas[idx] + energies[idx])

        return np.array(np.round(energies, 4))

    def generate_excitation_band(self, band_head_energy: float, absolute_band: np.ndarray[float]) -> np.ndarray[float]:
        """
        - generate the excitation energies from the absolute energies and the band-head level
        """
        return np.round(0.001*(absolute_band-band_head_energy), 4)

    def math_print(self, array: np.ndarray[float], array_name: str) -> str:
        """
        - return a list in math output (ready for copy/paste in Mathematica)
        - requires the array name so that it can write it in front of the {} object
        """
        string = f"{array_name} = {{"
        for idx in range(len(array)):
            if (idx == len(array)-1):
                string = string+f"{array[idx]}}};"
            else:
                string = string+f"{array[idx]},"

        print(string)
