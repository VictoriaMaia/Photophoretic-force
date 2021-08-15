import sys
sys.path.append('./')
from asymmetryFactorJ1 import rn as RN
from asymmetryFactorJ1 import sn as SN

def TestVarRn():
    m = 1.57 - 0.038j
    n = 1
    for i in range(1, 11):
        print(RN.Rn(m, i, n))

def TestVarSn():
    m = 1.57 - 0.038j
    n = 1
    for i in range(1, 11):
        print(SN.Sn(m, i, n))

if __name__ == '__main__':
    # TestVarRn()
    TestVarSn()