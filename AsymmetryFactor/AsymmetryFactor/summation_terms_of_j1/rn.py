from .bessel_and_ricattib_funcs import ricatti_bessel_f_k
import numpy as np


def term_r_n(m, x, n):
    """
    Calculates the value of r_n, where r_n is a term of the summation of j1.
    
    Parameters
    ----------
    m : index of refraction of the particle
    x : particle size parameter
    n : the current index of the summation
    """
    m_x = m * x
    psi_n1_m_x = ricatti_bessel_f_k((n+1), m_x)
    psi_m_x = ricatti_bessel_f_k(n, m_x)
    
    num = m * psi_n1_m_x * np.conj(psi_m_x)
    den = m ** 2
    
    return num.imag/den.imag
