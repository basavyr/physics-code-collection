#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import gordan as CGC


def coeff(j1, m1, j2, m2, j, m):
    cgc = CGC.CG(j1, m1, j2, m2, j, m)
    return cgc.doit()


# from one value of j, generate all the possible values of m
def Generate_M(j):
    x = np.arange(-j, j + 1, 1)
    return x


# Initialize the two angular momenta which will be used for addition
j1 = 1
j2 = 1

# create the arrays with all the possible j-states
J_VALUES = np.arange(abs(j1 - j2), abs(j1 + j2) + 1, 1)

# for each a.m. vector, generate all the possible m values
M1_VALUES = np.arange(-j1, j1 + 1, 1)
M2_VALUES = np.arange(-j2, j2 + 1, 1)


# from one value of j=j1+j2, make all the possible |jm> statess
make_jm_state = lambda j: [j, Generate_M(j)]


def m1m2_basis(j):
    M_VALUES = make_jm_state(j)[1]
    JM_STATES = [[j, m] for m in M_VALUES]
    print(f'j={j}')
    for JM in JM_STATES:
        possible_states = []
        m = JM[1]
        print(f'|{j},{m}>')
        for m1 in M1_VALUES:
            for m2 in M2_VALUES:
                if(m2 + m1 == m):
                    possible_states.append(
                        f'{coeff(j1,m1,j2,m2,j,m)}|{j1},{j2};{m1},{m2}>')
        print(possible_states)
        possible_states.clear()


m1m2_basis(1)

# for jm in jm_states:
#     JJ=jm[0]
#     MM=jm[1]
#     for m in MM:
#         print(f'|{JJ},{m}>')
