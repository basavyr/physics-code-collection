import angular_momentum as am
from const import Constants
import energy_function as h

def main():
    constants = Constants(10, 40, 20, 11/2, 70)
    j_sp = am.j_SingleParticle(constants.j, constants.theta_degrees)
    print(j_sp.j_vec())


if __name__ == '__main__':
    main()
