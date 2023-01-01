"""

This subpackage has the functions of calculating each term of summation of the asymmetry factor (j1)
and has a class with all the terms and a function that encompasses all the calculations.

"""

from .ceiling_x import ceiling_x
from .epsilon_imag import epsilon_imag
from .eta_r import eta_r
from . import cn, dn, rn, sn
from .variables_class import SummationVariables, compute_variables
