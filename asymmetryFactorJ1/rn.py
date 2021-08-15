import numpy as np
from .mathFunctions.ricattiBesselFunctions import ricattiBessel as rb

def Rn (M, x, n):
    Mx = M * x
    psi_n1Mx = rb.ricattiBessel_jn((n+1), Mx)
    psi_Mx = rb.ricattiBessel_jn(n, Mx)
    
    num = M * psi_n1Mx * np.conj(psi_Mx)
    den = M ** 2
    
    return num.imag/den.imag