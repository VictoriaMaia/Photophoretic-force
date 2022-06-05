import sys
sys.path.append('./')
from asymmetryFactorJ1.variables import nMax as n

if __name__ == '__main__':
    n_max = n.ceilingX(20)
    
    n_maxExpected = 33
    
    if n_max != n_maxExpected:
        print("The n_max is wrong!!!") 
        print("Expected: ", n_maxExpected)
        print("Current: ", n_max)
    else:
        print("The n_max is correct!!!")
