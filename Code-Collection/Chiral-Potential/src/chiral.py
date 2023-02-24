import elliptic as elliptic_functions
from dataclasses import dataclass
import numpy as np
import os
from matplotlib import pyplot as plt
from itertools import repeat


@dataclass
class Potential:
    """
    - Class that calculates the Elliptic potential V(q) and also the Chiral Potential (symmetric and asymmetric terms)
    """
    elliptic: elliptic_functions.EllipticFunctions

    def __init__(self, moi: tuple[float, float, float], odd_spin: float) -> None:
        os.makedirs('../data', exist_ok=True)
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
        return (spin*(spin+1.0)*np.power(k, 2)+np.power(v0, 2))*np.power(s, 2)+(2.0*spin+1.0)*v0*c*d

    def v_q_chiral(self, q: float, spin: float, theta_deg: float) -> tuple[float, float]:
        """
        returns a tuple with V(q, theta) and V(q, theta+pi)
        """
        return self.v_q(q, spin, theta_deg), self.v_q(q, spin, theta_deg+180.0)

    def v_symm(self, q: float, spin: float, theta_deg: float) -> float:
        """
        - returns the symmetric potential from Eq. 7.3 (new boson work)
        """
        v_theta, v_theta_pi = self.v_q_chiral(q, spin, theta_deg)
        return 0.5*(v_theta+v_theta_pi)

    def v_asymm(self, q: float, spin: float, theta_deg: float) -> float:
        """
        - returns the asymmetric potential from Eq. 7.3 (new boson work)
        """
        v_theta, v_theta_pi = self.v_q_chiral(q, spin, theta_deg)
        return 0.5*(v_theta-v_theta_pi)

    def plot_symm_potential(self, q_values: list[float], spin_values: list[float], theta_deg: float) -> None:
        """
        - create a plot with the chiral symmetric and asymmetric potentials
        """
        symmetric_plot = f'../data/symmetric_plot.pdf'

        k_values = [self.elliptic.modulus_k(
            spin, theta_deg) for spin in spin_values]
        periods = [self.elliptic.period(k) for k in k_values]
        q_range = max(list((4.0*period) for period in periods))

        plt.xlabel(r"$q\ [rad]$")
        plt.ylabel(r"$V_{symm}(q)$ [MeV]")
        plt.xlim(-q_range, q_range)
        for spin in spin_values:
            v_symm_values = list(
                map(self.v_symm, q_values, repeat(spin), repeat(theta_deg)))
            plt.plot(q_values, v_symm_values, label=f'{int(2*spin)}/2')
            plt.legend(loc='best')
        plt.savefig(symmetric_plot, dpi=450, bbox_inches='tight')
        plt.close()

    def plot_asymm_potential(self, q_values: list[float], spin_values: list[float], theta_deg: float) -> None:
        """
        - create a plot with the chiral asymmetric and asymmetric potentials
        """
        asymmetric_plot = f'../data/asymmetric_plot.pdf'

        k_values = [self.elliptic.modulus_k(
            spin, theta_deg) for spin in spin_values]
        periods = [self.elliptic.period(k) for k in k_values]
        q_range = max(list((4.0*period) for period in periods))

        plt.xlabel(r"$q\ [rad]$")
        plt.ylabel(r"$V_{asymm}(q)$ [$\hbar^2$]")
        plt.xlim(-q_range, q_range)
        for spin in spin_values:
            v_symm_values = list(
                map(self.v_asymm, q_values, repeat(spin), repeat(theta_deg)))
            plt.plot(q_values, v_symm_values, label=f'{int(2*spin)}/2')
            plt.legend(loc='best')
        plt.savefig(asymmetric_plot, dpi=450, bbox_inches='tight')
        plt.close()
