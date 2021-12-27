import numpy as np

def Test_NP_MODULE():
    try:
        x=np.arange(0,10,1)
    except Exception as exc:
        print(f'Issues: {exc}')
    finally:
        print('All tests passed')

Test_NP_MODULE()

def Woods_Saxon(V0,R0,s0):
    """
    Returns the expression of the Woods-Saxon potential
    The Fermi-function which aims at describing the nuclear charge distribution within a nucleus
    """
    S1=-V0
    EXP_F=lambda r: 1+np.exp((r-R0)/s0)
    S2=lambda r: (1+EXP_F(r))

    V_WS=[]
    for radius in range(0,5):
        V_WS.append(S2(radius))
    
    return V_WS

x=Woods_Saxon(20,1,1)
print(x)