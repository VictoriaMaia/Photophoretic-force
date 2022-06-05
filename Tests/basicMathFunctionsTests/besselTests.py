import sys
sys.path.append('./')

from asymmetryFactorJ1.mathFunctions import mathFuncs as Bessel
from Tests.helperFunctionsToTests import plotFunctions
import numpy as np

z = np.linspace(0, 20, 200)
z1 = np.linspace(0.01, 20, 200)

n = [0, 1, 2]


def test_bessel_first_kind_jn():
    results = []
    for i in n:
        results.append(Bessel.besselJ_n(i, z))
        
    plotFunctions.plot_graphic_math(n, 'Bessel functions of the first kind, Jn(x)', 'J', results, z, -0.5, 1.3)


def test_bessel_second_kind_yn():
    results = []
    for i in n:
        results.append(Bessel.besselY_n(i, z))

    plotFunctions.plot_graphic_math(n, 'Bessel functions of the second kind, Yn(x)', 'Y', results, z, -2, 0.8)


def test_spherical_bessel_first_kind_jn():
    results = []
    for i in n:
        results.append(Bessel.besselj_n(i, z))
        
    plotFunctions.plot_graphic_math(n, 'Spherical Bessel functions of the first kind, jn(x)', 'J', results, z, -0.40, 1.3)


def test_spherical_bessel_second_kind_yn():
    results = []
    for i in n:
        results.append(Bessel.bessely_n(i, z))

    plotFunctions.plot_graphic_math(n, 'Spherical Bessel functions of the second kind, Yn(x)', 'Y', results, z, -3, 0.50)


if __name__ == '__main__':
    test_bessel_first_kind_jn()
    test_bessel_second_kind_yn()
    test_spherical_bessel_first_kind_jn()
    test_spherical_bessel_second_kind_yn()
