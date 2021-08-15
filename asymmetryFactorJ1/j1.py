from . import cn as CN
from . import dn as DN
from . import rn as RN
from . import sn as SN
from . import nMax as NMAX
import numpy as np

def epsilon(m, ur):
    epsilon = (m**2) / ur
    return - epsilon.imag

def eta_r(m, ur):
    epsilon = (m**2) / ur
    divUrEpsilon = ur/epsilon 
    return divUrEpsilon ** (1/2)    

def J1(x, M, epislon2l, ur):
    firstTerm = (3 * epislon2l) / ((abs(M) ** 2) * (x ** 3))
    summationResult = 0
    nMax = NMAX.ceilingX(x)
    etaR = eta_r(M, ur)
    mod2EtaR = abs(etaR) ** 2
    
    for i in range(1, (nMax+1)):
        cn = CN.varC_n (ur, M, x, i) 
        conjCn = np.conj(cn)
        cn1 = CN.varC_n (ur, M, x, (i+1))
        conjCn1 = np.conj(cn1)
        rn = RN.Rn (M, x, i)
        rn1 = RN.Rn (M, x, (i+1))
        dn = DN.varD_n (ur, M, x, i)
        conjDn = np.conj(dn)
        dn1 = DN.varD_n (ur, M, x, (i+1))
        conjDn1 = np.conj(dn1)
        sn = SN.Sn (M, x, i)
        
        fristTermFor = ((i*(i+2)) / M) * ((cn1*conjCn*rn1) + (mod2EtaR*dn1*conjDn*rn))
        secondTermFor = ((i*(i+2)) / (i+1)) * ((cn*conjCn1) + (mod2EtaR*dn1*conjDn))
        thirdTermFor =  np.conj(etaR) * (((2*i)+1) / (i*(i+1))) * (cn*conjDn)
        
        result = fristTermFor - ((secondTermFor + thirdTermFor) * sn)
        
        summationResult += result
        
    return firstTerm * summationResult.imag