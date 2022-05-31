
def tauMN(m, n, x):
    pmn = scipy.special.lpmn(m, n, x)[0][m][n]
    pmn1 = scipy.special.lpmn(m, n+1, x)[0][m][n+1]

    fristTerm = -(n + 1) * x * pmn
    secondTerm = (n - m + 1) * pmn1

    num = fristTerm + secondTerm
    
    if x == 1:
        x = 0.999999999
    
    den = math.sqrt(1 - (x**2))
    
    return num/den

def piMN(m, n, angle):
    cosAlpha = math.cos(math.radians(angle))
    num = scipy.special.lpmn(m, n, cosAlpha)[0][m][n]
    
    sinAlpha = math.sin(math.radians(angle))
    
    return num/sinAlpha