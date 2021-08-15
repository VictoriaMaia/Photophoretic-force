from ..besselFunctions import bessel

def ricattiBessel_jn(n, z):
    return z * bessel.besselj_n(n, z)

def ricattiBessel_jn_derivative(n, z):
    return (1+n) * bessel.besselj_n(n, z) - z * bessel.besselj_n((1+n), z)

def spherical_hankel_2k(n, z):
    jn = bessel.besselj_n(n, z)
    yn = bessel.bessely_n(n, z)
    
    return jn - (yn * 1j)

def ricattiBessel_hn(n, z):
    return z * spherical_hankel_2k(n, z)
    
def ricattiBessel_hn_derivative(n, z):
    return (1+n) * spherical_hankel_2k(n, z) - z * spherical_hankel_2k((1+n), z)