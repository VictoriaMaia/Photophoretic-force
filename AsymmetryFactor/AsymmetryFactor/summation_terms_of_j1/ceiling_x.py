import math


def ceiling_x(x):
    """
    Calculates the ceiling of x value. Is used to calculate the value of n_max based on 
    the Wiscombe criterion that determines the maximum number of partial waves that are
    considered to be interacting with the particle.
    
    Parameters
    ----------
    x : size parameter of particle
    """
    return math.ceil(x + (4.05 * (x ** (1/3))) + 2)
