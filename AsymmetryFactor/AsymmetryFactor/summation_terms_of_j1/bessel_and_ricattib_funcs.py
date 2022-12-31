import scipy.special


# def bessel_j_n(n, x):
def bessel_f_k(n, x):
    """
    Bessel function of the first kind of "n" order calculated using the special.jv function

    Parameters
    ----------
    n : order of the Bessel function
    x : input parameter or argument
    """
    return scipy.special.jv(n, x)


# def bessel_j_n_without_derivative(n, x):
def spherical_bessel_f_k(n, x):
    """
    Spherical Bessel function of the first kind of "n" order calculated using the 
    scipy.special.spherical_jn function

    Parameters
    ----------
    n : order of the Spherical Bessel function
    x : input parameter or argument
    """
    return scipy.special.spherical_jn(n, x, derivative=False)


# def bessel_y_n(n, x):
def bessel_s_k(n, x):
    """
    Bessel function of the second kind of "n" order calculated using the special.yv function

    Parameters
    ----------
    n : order of the Bessel function
    x : input parameter or argument
    """
    return scipy.special.yv(n, x)


# def bessel_y_n_without_derivative(n, x):
def spherical_bessel_s_k(n, x):
    """
    Spherical Bessel function of the second kind of "n" order calculated using the 
    scipy.special.spherical_yn function

    Parameters
    ----------
    n : order of the Spherical Bessel function 
    x : input parameter or argument
    """
    return scipy.special.spherical_yn(n, x, derivative=False)


# def ricatti_bessel_j_n(n, x):
def ricatti_bessel_f_k(n, x):
    """
    Ricatti-Bessel function of the first kind.
    This function can be defined as x * spherical_bessel_jn(x). 
    Where spherical_bessel_jn(x) is the spherical Bessel function of the first kind of order n.

    Parameters
    ----------
    n : order of the spherical Bessel function
    x : input parameter or argument
    """
    
    return x * spherical_bessel_f_k(n, x)


# def ricatti_bessel_j_n_derivative(n, x):
def ricatti_bessel_f_k_derivative(n, x):
    """
    Derivative of Ricatti-Bessel function of the first kind.
    
    Parameters
    ----------
    n : order of the spherical Bessel function
    x : input parameter or argument
    """
    return (n + 1) * spherical_bessel_f_k(n, x) - x * spherical_bessel_f_k((n + 1), x)


# def spherical_hankel_2_k(n, z):
def spherical_hankel_s_k(n, x):
    """
    Spherical Hankel Function of the second kind

    Parameters
    ----------
    n : order of the spherical Bessel functions
    x : input parameter or argument
    """
    jn = spherical_bessel_f_k(n, x)
    yn = spherical_bessel_s_k(n, x)

    return jn - (1j * yn)


# def ricatti_bessel_h_n(n, x):
def ricatti_bessel_s_k(n, x):
    """
    Ricatti-Bessel function of the second kind.
    This function can be defined as x * spherical_hankel_h2(x). 
    Where spherical_hankel_h2(x) is the spherical Hankel function of the second kind.
    
    Parameters
    ----------
    n : order of the spherical Bessel functions inside spherical_hankel_s_k function
    x : input parameter or argument
    """
    return x * spherical_hankel_s_k(n, x)


# def ricatti_bessel_h_n_derivative(n, z):
def ricatti_bessel_s_k_derivative(n, x):
    """
    Derivative of Ricatti-Bessel function of the second kind.
    
    Parameters
    ----------
    n : order of the spherical Bessel functions inside spherical_hankel_s_k function
    x : input parameter or argument
    """
    # TO DO verify which formula is correct
    return (1+n) * spherical_hankel_s_k(n, x) - x * spherical_hankel_s_k((1+n), x)  # old
    # return x * spherical_hankel_s_k((n - 1), x) - (n - 1) * spherical_hankel_s_k(n,x) #new
