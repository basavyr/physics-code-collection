#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
from sympy.physics.quantum.cg import CG
from sympy import S
from sympy import *


# calculates the Clebsch-Gordan coefficient for a given set of parameters j1,j2,m1,m2,j,m=m1+m2


# Checks wether a spin-quantum-number is half-integer or not
def HalfInteger(x):
    half = 1 / 2
    x_half = x + half
    if(x_half.is_integer()):
        return 1
    return 0


# show a quantum number j or m in proper format
def QuantumNumber(x):
    if(HalfInteger(x)):
        X = f'{int(2*x)}/2'
    else:
        X = int(x)
    return X


# shows all the angular momentum states |J,M> which result from coupling the two angular momenta j1 and j2
def ShowJM_States(j1, j2):
    if(not HalfInteger(j1)):
        j1 = int(j1)
    if(not HalfInteger(j2)):
        j2 = int(j2)

    j_vals = np.arange(abs(j1 - j2), j1 + j2 + 1, 1)
    # print(f'j={j_vals}')
    JM_printer = []
    JM = []
    for j in j_vals:
        if(j == 0):
            m_vals = np.arange(0, 1, 1)
        else:
            m_vals = np.arange(-j, j + 1, 1)
        # print(f'm={m_vals}')
        for m in m_vals:
            pair = (j, m)
            pair_printer = (QuantumNumber(j), QuantumNumber(m))
            JM.append(pair)
            JM_printer.append(pair_printer)
    # for state in JM:
    #     print(f'|j,m> = |{state[0]},{state[1]}>')
    return JM


# shows all the states that form the basis {s=|j1,j2;m1,m2>=s1+s2}
# where s1,s2 are the two subspaces which correspond to each of the two angular momenta
# i.e., s1=|j1,m1> and s2=|j2,m2>
def ShowJ1J2M1M2_States(j1, j2):
    if(not HalfInteger(j1)):
        j1 = int(j1)
    if(not HalfInteger(j2)):
        j1 = int(j2)
    m1_vals = np.arange(-j1, j1 + 1, 1)
    m2_vals = np.arange(-j2, j2 + 1, 1)
    # print(f'm1={m1_vals}')
    # print(f'm2={m2_vals}')
    J12M12_printer = []
    J12M12 = []
    for m1 in m1_vals:
        for m2 in m2_vals:
            state = (j1, j2, m1, m2)
            state_printer = (QuantumNumber(j1), QuantumNumber(j2),
                             QuantumNumber(m1), QuantumNumber(m2))
            J12M12.append(state)
            J12M12_printer.append(state_printer)
    return J12M12
    # for state in J12M12:
    #     print(f'j1,j2;m1,m2> = |{state[0]},{state[1]};{state[2]},{state[3]}>')


def GenerateSpinStates(j1, j2):
    JM = ShowJM_States(j1, j2)
    J12M12 = ShowJ1J2M1M2_States(j1, j2)
    clebsch_matrix = [[1, 2], [1, 2]]
    # clebsch_matrix = np.ndarray(
    #     shape=(1, len(JM)), dtype=float,buffer=np.array(1))
    # for jm_state in JM:
    #     line = [j12m12_state for j12m12_state in J12M12]
    #     clebsch_matrix.append(line)
    print(np.array(J12M12[0]))
    # for jm_state in JM:
    #     stringg = [
    #         f'<{j12m12_state[0]},{j12m12_state[1]},{j12m12_state[2]},{j12m12_state[3]}|{jm_state[0]},{jm_state[1]}>' for j12m12_state in J12M12]
    #     print(
    #         f'|{jm_state[0]},{jm_state[1]}>={stringg}')


GenerateSpinStates(1, 1)


def GenerateQuantumNumbers(j1, j2):
    if(j1 < 0 or j2 < 0):
        return -1
    if(HalfInteger(j1)):
        J1 = f'{int(2*j1)}/2'
    else:
        J1 = j1
    if(HalfInteger(j2)):
        J2 = f'{int(2*j2)}/2'
    else:
        J2 = j2
    m1 = np.arange(-j1, j1 + 1, 1)
    m2 = np.arange(-j2, j2 + 1, 1)
    j12 = np.arange(abs(j1 - j2), j1 + j2 + 1, 1)
    count_j = 1
    JM = []
    J1J2_M1M1 = []
    for m11 in m1:
        if(HalfInteger(m11)):
            M1 = f'{int(2*m11)}/2'
        else:
            M1 = m11
        for m21 in m2:
            if(HalfInteger(m21)):
                M2 = f'{int(m21*2)}/2'
            else:
                M2 = m21
            print(f'|j1,j2;m1,m2> = |{J1},{J2},{M1},{M2}>')
    for j in j12:
        m12 = np.arange(-j, j + 1, 1)
        # print(f'j_{count_j}={j}')
        if(HalfInteger(j)):
            J = f'{int(j*2)}/2'
        else:
            J = j
        for m in m12:
            if(HalfInteger(m)):
                M = f'{int(2*m)}/2'
            else:
                M = m
            # print(f'|j,m> = |{J},{M}>')
            JM.append((j, m))
        count_j = count_j + 1
    print(f'The |J,M> states')
    print(JM)


qn = GenerateQuantumNumbers
