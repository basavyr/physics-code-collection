import numpy as np


class EnergyFunction:
    """
    - class that contains the numerical methods required for constructing the analytical expression of H'
    """
    def A_term(A1: float, A2: float, spin: float, j2: float) -> float:
        I = spin
        return A2*(1.0-(j2/I))-A1

    def u_term(A1: float, A3: float, A: float) -> float:
        return (A3-A1)/A

    def v0_term(A1: float,  A: float, j1: float) -> float:
        return -float(A1*j1/A)

    def H_polar(spin: float, x2: float, theta_2_deg: float, varphi_2_rad: float, u: float, v0: float) -> float:
        """
        - H' from Eq. (5.16)
        """
        I = spin
        t1 = 1.0-u*np.power(np.cos(varphi_2_rad), 2) - \
            (v0/I)*np.sin(varphi_2_rad)
        t2 = u*np.power(I, 2)*np.power(np.cos(varphi_2_rad), 2)
        t3 = 2.0*v0*I*np.sin(varphi_2_rad)

        h_prime = np.power(x2, 2)*t1+t2+t3
        return h_prime
