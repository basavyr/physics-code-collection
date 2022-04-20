import numpy as np
import math
MAXVAL = 69696969

# define a fragmented wobbling frequency for the rotor Hamiltonian


omega_file = 'omega_frequencies.dat'


def omega(I, I1, I2, I3):
    # implement fragmented stopping conditions
    if(I1 < 0.0):
        return MAXVAL
    if(I2 < 0.0):
        return MAXVAL
    if(I3 < 0.0):
        return MAXVAL
    if(I1 == 0):
        return MAXVAL
    if(I2 == 0):
        return MAXVAL
    if(I3 == 0):
        return MAXVAL
    if(I1 == I2):
        return MAXVAL
    if(I1 == I3):
        return MAXVAL
    if(I2 == I3):
        return MAXVAL
    if(I3 >= I2 and I3 <= I1):
        return MAXVAL
    if(I3 <= I2 and I3 >= I1):
        return MAXVAL

    # compute the pure product within the square root of the wobbling frequency
    t_pure = (1.0/(2.0*I1)-1.0/(2.0*I3))*(1.0/(2.0*I2)-1.0/(2.0*I3))
    try:
        t_sqrt = math.sqrt(t_pure)
    except ValueError as err:
        print(I1, I2, I3, err)
        return MAXVAL
    else:
        return t_sqrt


with open(omega_file, 'w+') as writer:
    writer.writelines("I1 I2 I3 t1 t2\n")
    for I1 in np.arange(-1, 6, 1):
        for I2 in np.arange(-1, 6, 1):
            for I3 in np.arange(-1, 6, 1):
                freq = omega(10, I1, I2, I3)
                if(freq is not MAXVAL):
                    writer.writelines(f'{I1} {I2} {I3} {freq}\n')
