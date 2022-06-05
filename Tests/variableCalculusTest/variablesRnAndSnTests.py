import sys
sys.path.append('./')
from asymmetryFactorJ1.variables import rn as pack_rn
from asymmetryFactorJ1.variables import sn as pack_sn


def test_var_rn():
    m = 1.57 - 0.038j
    n = 1
    for i in range(1, 11):
        print(pack_rn.Rn(m, i, n))


def test_var_sn():
    m = 1.57 - 0.038j
    n = 1
    x = 0.1

    print(pack_sn.Sn(m, x, n))

    for i in range(1, 11):
        print(pack_sn.Sn(m, i, n))


if __name__ == '__main__':
    test_var_rn()
    test_var_sn()
