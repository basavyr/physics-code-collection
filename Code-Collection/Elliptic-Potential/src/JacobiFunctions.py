import numpy as np
import scipy.special as special
import scipy.integrate as integrate

from dataclasses import dataclass


@dataclass
class Jacobi:
    """
    - A class containing the Jacobi Elliptic Functions, such as sn, cn, dn
    - It uses the scipy module to get the Jacobi Amplitude of modulus m
    - The class contains methods that give numerical results for m=k and also m=k^2
    """
    k: float

    def __init__(self, k) -> None:
        self.k = k

    def amu(self, q: float, k: float) -> tuple[float, float]:
        """
        - Returns a tuple with the Jacobi Amplitudes (i.e., `amu`) for modulus `k^2` and `k`, respectively
        - If `amu(q,k)=phi`, then `sn=sin(phi)`, `cn=cos(phi)`, ...
        - 1:1 correspondence with the Figure 1 from New-Boson is achieved for modulus k^squared
        - A 1:1 correspondence means that the intrinsic periods of `sn(phi), cn(phi)...`, coincide with the true period K, given the values of `q` and `k`
        - The correct phi is calculated thus as `amu(q,k^2)`
        """
        amu_k_squared = special.ellipj(q, np.power(k, 2))[3]
        amu_k = special.ellipj(q, k)[3]

        return (amu_k_squared, amu_k)

    def amu_squared(self, q: float, k: float) -> float:
        """
        - Helper function that gives the Jacobi Amplitude amu(q,m), where m=k^2
        - Use this method if a 1:1 correspondence with the calculations in New-Boson paper is required
        - Similarly, m=k^2 is the modulus considered in Wolfram Mathematica for JacobiAmplitude[q,k]
        """
        k_squared = np.power(k, 2)
        phi = special.ellipj(q, k_squared)[3]

        return phi

    def sn_k(self, q: float, k: float) -> float:
        """
        - returns the Jacobi Elliptic function sn=sin(amu(q,k))
        """
        _, phi_k = self.amu(q, k)
        return np.sin(phi_k)

    def sn_k_squared(self, q: float, k: float) -> float:
        """
        - returns the Jacobi Elliptic function sn=sin(amu(q,k^2))
        - 1:1 correspondence with the period K and the Figure 1 from New-Boson (2020 paper)
        """
        phi_k_squared, _ = self.amu(q, k)
        return np.sin(phi_k_squared)

    def cn_k(self, q: float, k: float) -> float:
        """
        - returns the Jacobi Elliptic function cn=cos(amu(q,k))
        """
        _, phi_k = self.amu(q, k)
        return np.cos(phi_k)

    def cn_k_squared(self, q: float, k: float) -> float:
        """
        - returns the Jacobi Elliptic function cn=cos(amu(q,k^2))
        - 1:1 correspondence with the period K and the Figure 1 from New-Boson (2020 paper)
        """
        phi_k_squared, _ = self.amu(q, k)
        return np.cos(phi_k_squared)

    def dn_k(self, q: float, k: float) -> float:
        """
        - returns the Jacobi Elliptic function dn(q,k)
        """
        s = self.sn_k(q, k)
        return np.sqrt(1-np.power(k, 2)*np.power(s, 2))

    def dn_k_squared(self, q: float, k: float) -> float:
        """
        - returns the Jacobi Elliptic function dn(q,k^2)
        - 1:1 correspondence with the period K and the Figure 1 from New-Boson (2020 paper)
        """
        s = self.sn_k_squared(q, k)
        return np.sqrt(1-np.power(k, 2)*np.power(s, 2))

    def q_var(self, phi: float, k: float) -> float:
        """
        - Returns the numerical value of the coordinate q when the Jacobi Amplitude phi and the modulus are known
        """
        a, b = 0, phi
        def sin_func(t): return np.power(
            1.0-np.power(k, 2)*np.power(np.sin(t), 2), -0.5)

        return integrate.quad(sin_func, a, b)[0]

    def period(self, k: float) -> float:
        """
        - Returns the period K of the Jacobi elliptic functions
        """
        a, b = 0, np.pi/2.0

        def sin_func(t): return np.power(
            1.0-np.power(k, 2)*np.power(np.sin(t), 2), -0.5)
        return integrate.quad(sin_func, a, b)[0]
