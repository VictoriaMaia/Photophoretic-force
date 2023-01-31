from mpmath import exp


def var_q(z0, s, k):
    """
    TO DO: add description
    
    Parameters
    ----------
    z0 :
    s  :
    k  :  
    """
    i = 1j
    second_term_sub = i*2*z0*(s**2)*k
    
    return 1 / (1 + second_term_sub)


def gn_gaussian_beam (n, k, z0, s):
    """
    TO DO: add description
    
    Parameters
    ----------
    n  :
    k  :
    z0 :
    s  :
    """
    i = 1j
    
    q = var_q(z0, s, k)
    
    arg_1 = s**2
    arg_2 = ((n+(1/2))**2)
    arg_exp = -q*arg_1*arg_2
    result_exp = exp(arg_exp)

    arg_e = i*k*z0
    result_e = exp(arg_e)
    
    return q*result_exp*result_e
