import numpy as np


class Factors:
    """
    - Implement the terms that appear in the canonicity factors as well as the oscillator frequencies 
    - Use consistent notations with the thesis (starting with Eq. 6.44)
    """

    rad3 = np.sqrt(3.0)

    # define the Sigma and Delta terms from Eq. 6.44
    @staticmethod
    def Delta_I(Spin, OddSpin, A1, A):
        # re-define spins for cohesive formulas
        I = Spin
        j = OddSpin

        Delta_A = (A-A1)
        Const_j = 2.0*j*A1
        Delta = (2.0*I-1.0)*Delta_A+Const_j

        return Delta

    # define the Sigma and Delta terms from Eq. 6.44
    @staticmethod
    def Delta_j(Spin, OddSpin, A1, A):
        # re-define spins for cohesive formulas
        I = Spin
        j = OddSpin

        Delta_A = (A-A1)
        Const_I = 2.0*A1
        Delta = (2.0*j-1.0)*Delta_A+Const_I

        return Delta

    # define the G-terms from Eq. 6.26
    @staticmethod
    def G_1(OddSpin, gamma):
        j = OddSpin
        gm = gamma

        Trig1 = 2.0*Factors.rad3*np.sin(gm)
        G1 = (2.0*j-1.0)/(j(j+1.0))*Trig1

        return G1

    # define the G-terms from Eq. 6.26
    @staticmethod
    def G_2(OddSpin, gamma):
        j = OddSpin
        gm = gamma

        Trig2 = Factors.rad3*(Factors.rad3*np.cos(gm)+np.sin(gm))
        G2 = (2.0*j-1.0)/(j(j+1.0))*Trig2

        return G2
