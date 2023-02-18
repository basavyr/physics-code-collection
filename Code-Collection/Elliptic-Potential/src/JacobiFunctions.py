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
        - Helper function that gives the Jacobi Amplitude `amu(q,m)`, where `m=k^2`
        - Use this method if a 1:1 correspondence with the calculations in New-Boson paper is required
        - Similarly, `m=k^2` is the modulus considered in Wolfram Mathematica for `JacobiAmplitude[q,k]`
        """
        k_squared = np.power(k, 2)
        return special.ellipj(q, k_squared)[3]

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
        phi_k_squared = self.amu_squared(q, k)
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
        phi_k_squared = self.amu_squared(q, k)
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


@dataclass
class Potential:
    """
    - Class that evaluates the Elliptic potential V(q), which is given in terms of the Jacobi functions
    """
    A1: float
    A2: float
    A3: float
    j1: float
    j2: float

    def __init__(self, moi1: float, moi2: float, moi3: float, odd_spin: float, theta_deg: float) -> None:
        self.A1 = 1.0/(2.0*moi1)
        self.A2 = 1.0/(2.0*moi2)
        self.A3 = 1.0/(2.0*moi3)
        self.j1 = odd_spin*np.cos(theta_deg*np.pi/180.0)
        self.j2 = odd_spin*np.sin(theta_deg*np.pi/180.0)

    def a_term(self, spin: float) -> float:
        I = spin
        return self.A2*(1.0-self.j2/I)-self.A1

    def u_term(self, spin: float) -> float:
        return (self.A3-self.A1)/self.a_term(spin)

    def v0(self, spin: float) -> float:
        return -((self.A1*self.j1)/self.a_term(spin))
