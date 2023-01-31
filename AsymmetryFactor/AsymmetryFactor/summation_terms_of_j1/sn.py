from .bessel_and_ricattib_funcs import ricatti_bessel_f_k
from .rn import term_r_n
import numpy as np


def term_s_n(m, x, n):
    """
    Calculates the value of s_n, where s_n is a term of the summation of j1.
    
    Parameters
    ----------
    m   : index of refraction of the particle
    x : particle size parameter
    n   : the current index of the summation
    """
    m_2 = m ** 2
    m_x = m * x
    conj_m = np.conj(m)
    
    rn = term_r_n(m, x, n)
    rn_1 = term_r_n(m, x, (n+1))
    
    mod_2_psi_m_x = abs(ricatti_bessel_f_k(n, m_x)) ** 2
    mod_2_psi_n1_m_x = abs(ricatti_bessel_f_k((n+1), m_x)) ** 2
    
    first_term = - (1j / (2 * m_2.imag))
    second_term = x * ((m * mod_2_psi_m_x) + (conj_m * mod_2_psi_n1_m_x))
    third_term = (m + ((2 * (n + 1)) * (m_2.real / m))) * rn
    fourth_term = ((2 * n) + 1) * conj_m * rn_1
    
    return first_term * (second_term - third_term + fourth_term)
