#!/Users/robertpoenaru/.pyenv/shims/python

# used for random data testing
from numpy import random as rd


def Give_RandomArray():
    x_original = sorted(rd.randint(0, 100, 20))
    x_curated = []
    [x_curated.append(x) for x in x_original if x not in x_curated]
    return x_curated
