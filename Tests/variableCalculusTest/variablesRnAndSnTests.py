import sys
sys.path.append('./')
from asymmetryFactorJ1.variables import rn as RN
from asymmetryFactorJ1.variables import sn as SN

def TestVarRn():
    m = 1.57 - 0.038j
    n = 1
    for i in range(1, 11):
        print(RN.Rn(m, i, n))

def TestVarSn():
    m = 1.57 - 0.038j
    n = 1
    x = 0.1

    print(SN.Sn(m, x, n))

    for i in range(1, 11):
        print(SN.Sn(m, i, n))

if __name__ == '__main__':
    TestVarRn()
    TestVarSn()