from mpmath import exp


def varQ(z0, s, k):
    i = 1j
    secondTermSub = i*2*z0*(s**2)*k
    
    return 1 / (1 + secondTermSub)

def gnGaussianBeam (n, k, z0, s):
    i = 1j
    
    q = varQ(z0, s, k)
    
    arg1 = s**2
    arg2 = ((n+(1/2))**2)
    argExp = -q*arg1*arg2
    resultExp = exp(argExp)

    argE = i*k*z0
    resultE = exp(argE)
    
    return q*resultExp*resultE


