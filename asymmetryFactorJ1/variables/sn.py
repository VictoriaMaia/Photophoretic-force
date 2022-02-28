from .rn import Rn
from asymmetryFactorJ1.mathFunctions import mathFuncs as rb
import numpy as np

def Sn (M, x, n):
    M2 = M ** 2
    Mx = M * x
    conjM = np.conj(M)
    rn = Rn(M, x, n)
    rn1 = Rn(M, x, (n+1))
    mod2Psi_Mx = abs(rb.ricattiBessel_jn(n, Mx)) ** 2
    mod2Psin1_Mx = abs(rb.ricattiBessel_jn((n+1), Mx)) ** 2
    
    fristTerm = -(1j / (2 * M2.imag))
    secondTerm = x * ((M * mod2Psi_Mx) + (conjM * mod2Psin1_Mx))
    thirdTerm = (M + ((2 * (n+1)) * (M2.real / M))) * rn
    fourthTerm = ((2*n) + 1) * conjM * rn1
    
    return fristTerm * (secondTerm - thirdTerm + fourthTerm)