import scipy.special 


# bessel functions

def besselJ_n(i, z):
    return scipy.special.jv(i, z)

def besselY_n(i, z):
    return scipy.special.yv(i, z)

def besselj_n(i,z):
    return scipy.special.spherical_jn(i, z, derivative=False)

def bessely_n(i, z):
    return scipy.special.spherical_yn(i, z, derivative=False)

# ricatti bessel functions


def ricattiBessel_jn(n, z):
    return z * besselj_n(n, z)

def ricattiBessel_jn_derivative(n, z):
    return (1+n) * besselj_n(n, z) - z * besselj_n((1+n), z)

def spherical_hankel_2k(n, z):
    jn = besselj_n(n, z)
    yn = bessely_n(n, z)
    
    return jn - (yn * 1j)

def ricattiBessel_hn(n, z):
    return z * spherical_hankel_2k(n, z)
    
def ricattiBessel_hn_derivative(n, z):
    return (1+n) * spherical_hankel_2k(n, z) - z * spherical_hankel_2k((1+n), z)