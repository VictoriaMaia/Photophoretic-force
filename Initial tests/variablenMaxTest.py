import sys
sys.path.append('./')
from asymmetryFactorJ1 import nMax as n

if __name__ == '__main__':
    nMax = n.ceilingX(20)
    print(nMax)