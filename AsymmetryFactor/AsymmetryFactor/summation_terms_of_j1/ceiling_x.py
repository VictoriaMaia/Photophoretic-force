import math


def ceiling_x(x):
    """
    Calculates the ceiling of x value.
    TO DO: describe better, please!
    
    Parameters
    ----------
    x : size parameter of particle
    """

    return math.ceil(x + (4.05 * (x ** (1/3))) + 2)
