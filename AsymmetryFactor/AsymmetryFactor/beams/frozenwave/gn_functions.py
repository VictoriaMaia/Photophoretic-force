from mpmath import exp
import scipy.special 
import scipy.integrate
import numpy as np
import math


def pi_m_n(m, n, x):
    """
    TO DO: add description
    
    Parameters
    ----------
    m :
    n :
    x :  
    """
    num = scipy.special.lpmn(m, n, x)[0][m][n]
    den = math.sqrt(1 - (x**2))
    
    return num/den


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
    den = math.sqrt(1 - (x**2))

    return num/den


def Kz_q(q_i, L, q):
    """
    TO DO: add description
    
    Parameters
    ----------  
    q_i :
    L   :
    q   :
    """
    return q + ((2*math.pi*q_i)/L)


def A_q(l, q):
    """
    TO DO: add description
    
    Parameters
    ----------  
    l :
    q :
    """
    pi = math.pi
    
    inferior_limit = l/12
    upper_limit = (11*l)/12

    frist_term = 1/l    
    common = (2*pi*q)/l
    
    fun_cos = lambda iz: exp(-5 * (((iz - (0.5 * l)) ** 2)/(l**2))) * math.cos(((6 * math.pi * iz) / l)) * math.cos(common * iz)
    fun_sen = lambda iz: exp(-5 * (((iz - (0.5 * l)) ** 2)/(l**2))) * math.cos(((6 * math.pi * iz) / l)) * math.sin(common * iz)
    
    integral_cos = scipy.integrate.quad(fun_cos, inferior_limit, upper_limit, epsrel = 1e-19)[0]
    integral_sin = scipy.integrate.quad(fun_sen, inferior_limit, upper_limit, epsrel = 1e-15)[0]
        
    integrate_result = integral_cos + 1j*integral_sin
    
    return frist_term * integrate_result
    


def gn_frozen_wave_beam(n, n_to_q, k, z0, l, q):
    """
    TO DO: add description
    
    Parameters
    ----------
    n      :
    n_to_q :
    k      :
    z0     :
    l      :  
    q      :
    """
    q_values = np.arange(n_to_q, (-n_to_q + 1))   
    result_sum = 0

    for q_i in q_values:
        kz_q = Kz_q(q_i, l, q)
        div_kz_q_k = kz_q / k

        frist_term_sum = A_q(l,q_i) / (1 + div_kz_q_k)
        second_term_sum = pi_m_n(1, n, div_kz_q_k) + tau_m_n(1, n, div_kz_q_k)
        third_term_sum = exp(1j*kz_q*z0)
        
        result = frist_term_sum * second_term_sum * third_term_sum

        result_sum += result
                
    return (-2)/(n*(n+1)) * result_sum
