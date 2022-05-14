import sys
sys.path.append('./')
from asymmetryFactorJ1.variables import nMax as n

if __name__ == '__main__':
    nMax = n.ceilingX(20)
    
    nMaxExpected = 33
    
    if nMax != nMaxExpected:
        print("The nMax is wrong!!!") 
        print("Expected: ", nMaxExpected)
        print("Current: ", nMax)
    else:
        print("The nMax is correct!!!") 