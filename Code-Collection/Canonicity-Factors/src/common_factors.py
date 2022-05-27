import numpy as np


class Factors:
    """
    - Implement the terms that appear in the canonicity factors as well as the oscillator frequencies 
    - Use consistent notations with the thesis (starting with Eq. 6.44)
    """

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

    # # define the G-terms from Eq. 6.26
    # @staticmethod
    # def G_1(OddSpin, V):
