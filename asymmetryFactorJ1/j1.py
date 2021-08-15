from . import cn as CN
from . import dn as DN
from . import rn as RN
from . import sn as SN
from . import nMax as NMAX
import numpy as np
from mpmath import exp

class J1_attributes:
    def __init__(self, x, M, epislon2l, ur, k="False", z0="False", s="False") -> None:
        self.x = x
        self.M = M
        self.epislon2l = epislon2l
        self.ur = ur
        self.k = k
        self.z0 = z0
        self.s = s
        pass

    def printJ1Attributes(self):
        print("x: ", self.x)
        print("M: ", self.M)
        print("Eps: ", self.epislon2l)
        print("Ur: ", self.ur)
        print("k: ", self.k)
        print("z0: ", self.z0)
        print("s: ", self.s)

def epsilon(m, ur):
    epsilon = (m**2) / ur
    return - epsilon.imag

def eta_r(m, ur):
    epsilon = (m**2) / ur
    divUrEpsilon = ur/epsilon 
    return divUrEpsilon ** (1/2)    

def varQ(z0, s, k):
    i = 1j
    secondTermSub = i*2*z0*(s**2)*k
    
    return 1 / (1 + secondTermSub)

def varG_nGaussianBeam (n, k, x, z0, s):
    i = 1j
    
    q = varQ(z0, s, k)
    
    arg1 = s**2
    arg2 = ((n+(1/2))**2)
    argExp = -q*arg1*arg2
    resultExp = exp(argExp)

    argE = i*k*z0
    resultE = exp(argE)
    
    return q*resultExp*resultE

def Summation(parameters):
    summationResult = 0
    nMax = NMAX.ceilingX(parameters.x)
    etaR = eta_r(parameters.M, parameters.ur)
    mod2EtaR = abs(etaR) ** 2

    for i in range(1, (nMax+1)):
        cn = CN.varC_n (parameters.ur, parameters.M, parameters.x, i) 
        conjCn = np.conj(cn)
        cn1 = CN.varC_n (parameters.ur, parameters.M, parameters.x, (i+1))
        conjCn1 = np.conj(cn1)
        rn = RN.Rn (parameters.M, parameters.x, i)
        rn1 = RN.Rn (parameters.M, parameters.x, (i+1))
        dn = DN.varD_n (parameters.ur, parameters.M, parameters.x, i)
        conjDn = np.conj(dn)
        dn1 = DN.varD_n (parameters.ur, parameters.M, parameters.x, (i+1))
        conjDn1 = np.conj(dn1)
        sn = SN.Sn (parameters.M, parameters.x, i)
        
        fristTermFor = ((i*(i+2)) / parameters.M) * ((cn1*conjCn*rn1) + (mod2EtaR*dn1*conjDn*rn))
        secondTermFor = ((i*(i+2)) / (i+1)) * ((cn*conjCn1) + (mod2EtaR*dn1*conjDn))
        thirdTermFor =  np.conj(etaR) * (((2*i)+1) / (i*(i+1))) * (cn*conjDn)
        
        result = fristTermFor - ((secondTermFor + thirdTermFor) * sn)
        
        summationResult += result
    
    return summationResult


def SummationWithGn(parameters):
    nMax = NMAX.ceilingX(parameters.x)
    etaR = eta_r(parameters.M, parameters.ur)
    mod2EtaR = abs(etaR) ** 2
    summationResult = 0
    
    for i in range(1, (nMax+1)):
        cn = CN.varC_n (parameters.ur, parameters.M, parameters.x, i) 
        conjCn = np.conj(cn)
        cn1 = CN.varC_n (parameters.ur, parameters.M, parameters.x, (i+1))
        conjCn1 = np.conj(cn1)
        gn = varG_nGaussianBeam(i, parameters.k, parameters.x, parameters.z0, parameters.s)
        conjGn = np.conj(gn)
        gn1 = varG_nGaussianBeam((i+1), parameters.k, parameters.x, parameters.z0, parameters.s)
        conjGn1 = np.conj(gn1)
        rn = RN.Rn (parameters.M, parameters.x, i)
        rn1 = RN.Rn (parameters.M, parameters.x, (i+1))
        dn = DN.varD_n (parameters.ur, parameters.M, parameters.x, i)
        conjDn = np.conj(dn)
        dn1 = DN.varD_n (parameters.ur, parameters.M, parameters.x, (i+1))
        conjDn1 = np.conj(dn1)
        sn = SN.Sn (parameters.M, parameters.x, i)
        
        fristTermFor = ((i*(i+2)) / parameters.M) * ((gn1*conjGn*cn1*conjCn*rn1) + (mod2EtaR*gn1*conjGn*dn1*conjDn*rn))
        secondTermFor = ((i*(i+2)) / (i+1)) * ((gn*conjGn1*cn*conjCn1) + (mod2EtaR*gn1*conjGn*dn1*conjDn))
        thirdTermFor = np.conj(etaR) * (((2*i)+1) / (i*(i+1))) * (abs(gn)**2) * (cn*conjDn)
        
        result = fristTermFor - ((secondTermFor + thirdTermFor) * sn)
        
        summationResult += result
    
    return summationResult


def J1(parameters):
    if type(parameters) != J1_attributes:
        print("Error: parameters is not of type class J1_attributes")
        return 0
    
    firstTerm = (3 * parameters.epislon2l) / ((abs(parameters.M) ** 2) * (parameters.x ** 3))

    if parameters.k == "False" and parameters.z0 == "False" and parameters.s == "False":
        summationResult = Summation(parameters)
    else:
        summationResult = SummationWithGn(parameters) 
        
    return firstTerm * summationResult.imag
