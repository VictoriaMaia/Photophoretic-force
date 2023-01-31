from .bessel_and_ricattib_funcs import ricatti_bessel_s_k, ricatti_bessel_s_k_derivative
from .bessel_and_ricattib_funcs import ricatti_bessel_f_k, ricatti_bessel_f_k_derivative


def term_c_n(u_r, m, ka, n):
    """
    Calculates the value of c_n, where c_n is a term of the summation of j1.
    
    Parameters
    ----------
    TO DO: verify the information about the parameters
    u_r : the real part of the particle permeability
    m   : index of refraction of the particle
    ka  : the result of the product of k (wave number) and a (particle radius)
    n   : the current index of the summation
    """
    xi_ka = ricatti_bessel_s_k(n, ka)
    xi_derivative_ka = ricatti_bessel_s_k_derivative(n, ka)

    psi_ka = ricatti_bessel_f_k(n, ka)
    psi_m_ka = ricatti_bessel_f_k(n, (m*ka))
    psi_derivative_ka = ricatti_bessel_f_k_derivative(n, ka)
    psi_derivative_m_ka = ricatti_bessel_f_k_derivative(n, (m*ka))
    
    num = m * u_r * ((xi_ka * psi_derivative_ka) - (xi_derivative_ka * psi_ka))
    den = (u_r * xi_ka * psi_derivative_m_ka) - (m * xi_derivative_ka * psi_m_ka)
    
    return num/den
