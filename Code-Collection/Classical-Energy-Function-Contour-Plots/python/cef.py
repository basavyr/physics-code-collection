import numpy as np

# create the function terms for the Classical Energy Function


class CEF:

    @staticmethod
    def T_core(I, A1, A2, A3):
        ret_val = 0.5*I*(A1+A2)+A3*np.power(I, 2)

        return ret_val

    @staticmethod
    def T_sp(j, A1, A2, A3, V, gm):
        pi6 = np.pi/6.0
        gm_rad = gm*np.pi/180.0
        ret_val = 0.5*j*(A2+A3)+A1*np.power(j, 2)-V * \
            (2.0*j-1.0)/(j+1.0)*np.sin(gm_rad+pi6)

        return ret_val

    @staticmethod
    def A_phi(phi, A1, A2, A3):
        ret_val = A1*np.power(np.cos(phi), 2)+A2*np.power(np.sin(phi), 2)-A3

        return ret_val

    @staticmethod
    def H_min(theta, phi, I, j, A1, A2, A3, V, gm):
        t1 = I*(I-0.5)*np.power(np.sin(theta), 2)*CEF.A_phi(phi, A1, A2, A3)
        t2 = 2.0*A1*I*j*np.sin(theta)
        t3 = CEF.T_core(I, A1, A2, A3)+CEF.T_sp(j, A1, A2, A3, V, gm)
        ret_val = t1-t2+t3

        return ret_val


def main():
    print('CEF')
    step = 0.5
    theta_values = np.arange(0, np.pi, step)
    for theta in theta_values:
        print(CEF.H_min(theta, np.pi, 25/2, 13/2, 0.1, 0.2, 0.3, 2.1, 22))


if __name__ == '__main__':
    main()
