import numpy as np
from math import sin, cos, radians, degrees, pi, atan, sqrt

def phi(p):
    phi = atan(p[1] / p[0])
    if phi < 0 and p[1] > 0:
        return phi + pi
    elif phi < 0 and p[1] < 0:
        return phi + 2 * pi
    elif phi > 0 and p[0] < 0 and p[1] < 0:
        return phi + pi
    return phi


def rotate(p, angle): # angle in radians
    m = np.array([[cos(angle), sin(angle)],[-sin(angle), cos(angle)]])
    return np.matmul(p,m)
