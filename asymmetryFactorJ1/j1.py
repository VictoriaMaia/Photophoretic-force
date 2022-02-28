import imp
from asymmetryFactorJ1.variables import *
from asymmetryFactorJ1.gaussianBeam import *
import numpy as np
from mpmath import exp

class J1_attributes:
    def __init__(self, x, M, ur) -> None:
        self.x = x
        self.M = M
        self.ur = ur
        pass

    def printJ1Attributes(self):
        print("x: ", self.x)
        print("M: ", self.M)
        print("Ur: ", self.ur)

class J1Gauss(J1_attributes):
    def __init__(self, x, M, ur, k, z0, s) -> None:
        super().__init__(x, M, ur)
        
        self.k = k
        self.z0 = z0
        self.s = s
        pass

    def printJ1GaussAttributes(self):
        print("x: ", self.x)
        print("M: ", self.M)
        print("Ur: ", self.ur)
        print("k: ", self.k)
        print("z0: ", self.z0)
        print("s: ", self.s)



def Summation(parameters):
    summationResult = 0
    nMax = ceilingX(parameters.x)
    etaR = eta_r(parameters.M, parameters.ur)
    mod2EtaR = abs(etaR) ** 2

    for i in range(1, (nMax+1)):
        cn = Cn (parameters.ur, parameters.M, parameters.x, i) 
        conjCn = np.conj(cn)
        cn1 = Cn (parameters.ur, parameters.M, parameters.x, (i+1))
        conjCn1 = np.conj(cn1)
        rn = Rn (parameters.M, parameters.x, i)
        rn1 = Rn (parameters.M, parameters.x, (i+1))
        dn = Dn (parameters.ur, parameters.M, parameters.x, i)
        conjDn = np.conj(dn)
        dn1 = Dn (parameters.ur, parameters.M, parameters.x, (i+1))
        conjDn1 = np.conj(dn1)
        sn = Sn (parameters.M, parameters.x, i)
        
        fristTermFor = ((i*(i+2)) / parameters.M) * ((cn1*conjCn*rn1) + (mod2EtaR*dn1*conjDn*rn))
        secondTermFor = ((i*(i+2)) / (i+1)) * ((cn*conjCn1) + (mod2EtaR*dn1*conjDn))
        thirdTermFor =  np.conj(etaR) * (((2*i)+1) / (i*(i+1))) * (cn*conjDn)
        
        result = fristTermFor - ((secondTermFor + thirdTermFor) * sn)
        
        summationResult += result
    
    return summationResult


def SummationWithGn(parameters):
    nMax = ceilingX(parameters.x)
    etaR = eta_r(parameters.M, parameters.ur)
    mod2EtaR = abs(etaR) ** 2
    summationResult = 0
    
    for i in range(1, (nMax+1)):
        cn = Cn (parameters.ur, parameters.M, parameters.x, i) 
        conjCn = np.conj(cn)
        cn1 = Cn (parameters.ur, parameters.M, parameters.x, (i+1))
        conjCn1 = np.conj(cn1)
        rn = Rn (parameters.M, parameters.x, i)
        rn1 = Rn (parameters.M, parameters.x, (i+1))
        dn = Dn (parameters.ur, parameters.M, parameters.x, i)
        conjDn = np.conj(dn)
        dn1 = Dn (parameters.ur, parameters.M, parameters.x, (i+1))
        conjDn1 = np.conj(dn1)
        sn = Sn (parameters.M, parameters.x, i)

        if type(parameters) == J1Gauss:
            gn = gnGaussianBeam(i, parameters.k, parameters.z0, parameters.s)
            conjGn = np.conj(gn)
            gn1 = gnGaussianBeam((i+1), parameters.k, parameters.z0, parameters.s)
            conjGn1 = np.conj(gn1)


        fristTermFor = ((i*(i+2)) / parameters.M) * ((gn1*conjGn*cn1*conjCn*rn1) + (mod2EtaR*gn1*conjGn*dn1*conjDn*rn))
        secondTermFor = ((i*(i+2)) / (i+1)) * ((gn*conjGn1*cn*conjCn1) + (mod2EtaR*gn1*conjGn*dn1*conjDn))
        thirdTermFor = np.conj(etaR) * (((2*i)+1) / (i*(i+1))) * (abs(gn)**2) * (cn*conjDn)
        
        result = fristTermFor - ((secondTermFor + thirdTermFor) * sn)
        
        summationResult += result
    
    return summationResult


def J1(parameters):    
    epislon2l = epsilon(parameters.M, parameters.ur)

    firstTerm = (3 * epislon2l) / ((abs(parameters.M) ** 2) * (parameters.x ** 3))

    if type(parameters) == J1_attributes:
        summationResult = Summation(parameters)
    elif type(parameters) == J1Gauss:
        summationResult = SummationWithGn(parameters) 
    else:
        print("Error. Type of parameters invalid.")
        return 0
        
    return firstTerm * summationResult.imag
