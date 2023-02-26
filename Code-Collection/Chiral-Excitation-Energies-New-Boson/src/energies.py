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

    def __init__(self, moi: tuple[float, float, float], odd_spin: float) -> None:
        self.A1, self.A2, self.A3 = (1.0/(2.0*moi_k) for moi_k in moi)
        self.j = odd_spin

    def show(self):
        print(self.A1, self.A2, self.A3, self.j1, self.j2)

    def j_vec(self, theta_deg: float, component_k: int) -> float:
        vec = (
            self.j*np.cos(theta_deg*np.pi/180.0), self.j*np.sin(theta_deg*np.pi/180.0), 0)
        return vec[component_k-1]

    def a21(self, spin: float, theta_deg: float) -> float:
        return self.A2-self.A1-(self.A2*self.j_vec(theta_deg, 2))/spin

    def omega(self, spin: float, theta_deg: float) -> float:
        a1j1 = self.A1*self.j_vec(theta_deg, 1)

        sub_term1 = (2.0*spin+1.0)*self.a21(spin, theta_deg)+2.0*a1j1
        sub_term2 = (2.0*spin+1.0)*(self.A3-self.A1)+2.0*a1j1
        sub_term3 = (self.A3-self.A1)*self.a21(spin, theta_deg)

        return np.sqrt(sub_term1 * sub_term2 - sub_term3)

    def omega_prime(self, spin: float, theta_deg: float) -> float:
        a1j1 = self.A1*self.j*np.cos(theta_deg*np.pi/180.0)

        sub_term1 = (2.0*spin+1.0)*self.a21(spin, theta_deg)-2.0*a1j1
        sub_term2 = (2.0*spin+1.0)*(self.A3-self.A1)-2.0*a1j1
        sub_term3 = (self.A3-self.A1)*self.a21(spin, theta_deg)

        return np.sqrt(sub_term1 * sub_term2 - sub_term3)

    def symmetric_excitation_energy(self, spin: float, theta_deg: float):
        symmetric_omega = (
            self.omega(spin, theta_deg) + self.omega(spin, theta_deg+180.0))

        return self.A1*np.power(spin, 2)+0.5*symmetric_omega

    def asymmetric_excitation_energy(self, spin: float, theta_deg: float):
        a1j1 = self.A1*self.j_vec(theta_deg, 1)
        a2j2 = self.A2*self.j_vec(theta_deg, 2)

        asymmetric_omega = (
            self.omega(spin, theta_deg) - self.omega(spin, theta_deg+180.0))

        return (2.0*spin+1.0)*a1j1-spin*a2j2*0.5*asymmetric_omega
