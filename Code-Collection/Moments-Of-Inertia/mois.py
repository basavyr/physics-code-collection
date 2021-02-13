#! /Users/robertpoenaru/.pyenv/shims/python

import numpy as np


class MOI:

    def __init__(self, I_0):
        self.I_0 = I_0
        # self.beta = beta
        # self.gamma = gamma

    # R0 = lambda A: 1.20 * np.power(A, 1.0 / 3.0)
    R0 = lambda A: 1.20

    def Hydro(self, gamma):
        c = 4.0 / 3.0 * self.I_0
        hydro = lambda k: np.power(np.sin(gamma + 2.0 * np.pi / 3.0 * k), 2)
        mois = [c * hydro(1), c * hydro(2), c * hydro(3)]
        return mois

    def Rigid(self, beta, gamma):
        c = self.I_0 / (1.0 + np.sqrt(5.0 / (16.0 * np.pi) * beta))
        rigid = lambda k: 1 - \
            np.sqrt(5.0 / (4.0 * np.pi)) * beta * \
            np.cos(gamma + 2.0 * np.pi * k / 3.0)
        mois = [c * rigid(1), c * rigid(2), c * rigid(3)]
        return mois

    @ staticmethod
    def Irr(A, m, beta, gamma):
        c = 3.0 / (2.0 * np.pi) * m * A * np.power(MOI.R0(A), 2)
        irr_k = lambda k: np.power(
            beta, 2) * np.power(np.sin(gamma - (2.0 * np.pi) / 3.0 * k))
        mois = [irr_k(1), irr_k(2), irr_k(3)]
        return c * mois

    @ staticmethod
    def Rig(A, m, beta, gamma):
        c = 2.0 / 5.0 * m * A * np.power(MOI.R0(A), 2)
        rig_k = lambda k: 1 - \
            np.sqrt(5.0 / (4.0 * np.pi)) * beta * \
            np.cos(gamma - (2 * np.pi) / 3.0 * k)
        mois = [rig_k(1), rig_k(2), rig_k(3)]
        return c * mois

    @ staticmethod
    def I_k(B_2, beta, gamma):
        c = 4.0 * B_2
        i_k = lambda k: np.power(beta, 2) * \
            np.sin(gamma - (2.0 * np.pi) / 3.0 * k)
        mois = [i_k(1), i_k(2), i_k(3)]
        return c * mois
