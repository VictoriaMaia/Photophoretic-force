from . import rn as RN
import numpy as np
from .mathFunctions.ricattiBesselFunctions import ricattiBessel as rb

def Sn (M, x, n):
    M2 = M ** 2
    Mx = M * x
    conjM = np.conj(M)
    rn = RN.Rn(M, x, n)
    rn1 = RN.Rn(M, x, (n+1))
    mod2Psi_Mx = abs(rb.ricattiBessel_jn(n, Mx)) ** 2
    mod2Psin1_Mx = abs(rb.ricattiBessel_jn((n+1), Mx)) ** 2
    
    fristTerm = -(1j / (2 * M2.imag))
    secondTerm = x * ((M * mod2Psi_Mx) + (conjM * mod2Psin1_Mx))
    thirdTerm = (M + ((2 * (n+1)) * (M2.real / M))) * rn
    fourthTerm = ((2*n) + 1) * conjM * rn1
    
    return fristTerm * (secondTerm - thirdTerm + fourthTerm)