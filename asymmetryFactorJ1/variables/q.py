
def Q(z0, s, k):
    i = 1j
    secondTermSub = i*2*z0*(s**2)*k
    
    return 1 / (1 + secondTermSub)
