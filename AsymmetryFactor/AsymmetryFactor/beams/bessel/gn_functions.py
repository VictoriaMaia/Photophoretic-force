from mpmath import exp
import scipy.special 
import math


def tau_m_n(m, n, x):
    """
    TO DO: add description
    
    Parameters
    ----------
    m :
    n :
    x :  
    """
    pmn = scipy.special.lpmn(m, n, x)[0][m][n]
    pmn1 = scipy.special.lpmn(m, n+1, x)[0][m][n+1]

    frist_term = -(n + 1) * x * pmn
    second_term = (n - m + 1) * pmn1

    num = frist_term + second_term
    
    if x == 1:
        den = math.sqrt(1 - 0.999999999)
    else:
        den = math.sqrt(1 - (x**2))
    
    return num/den


def pi_m_n(m, n, angle):
    """
    TO DO: add description
    
    Parameters
    ----------
    m     :
    n     :
    angle :  
    """
    cos_alpha = math.cos(math.radians(angle))
    num = scipy.special.lpmn(m, n, cos_alpha)[0][m][n]
    
    sin_alpha = math.sin(math.radians(angle))
    
    return num/sin_alpha


def gn_bessel_beam(n, k, z0, angle):
    """
    TO DO: add description
    
    Parameters
    ----------
    n     :
    k     :
    z0    :
    angle :  
    """
    i = 1j
    
    cos_angle = math.cos(math.radians(angle))

    tau_1_n = tau_m_n(1, n, cos_angle)
    pi_1_n = pi_m_n(1, n, angle)
    
    frist_term = - (1 / (n * (n + 1)))
    
    second_term = (tau_1_n/cos_angle) + pi_1_n
    
    arg_e = i * k * cos_angle * z0
    thir_term = exp(arg_e)

    return frist_term * second_term * thir_term
      