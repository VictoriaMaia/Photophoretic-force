import sys
sys.path.append('./')
from asymmetryFactorJ1.mathFunctions.besselFunctions import bessel
import plotFunctions
import numpy as np

z  = np.linspace(0, 20, 200)
z1  = np.linspace(0.01, 20, 200)

n = [0,1,2]

def testBesselFirstKind_Jn():
    results = []
    for i in n:
        results.append(bessel.besselJ_n(i, z))
        
    plotFunctions.PlotGraphic(n, 'Bessel functions of the frist kind, Jn(x)', 'J', results, z, -0.5, 1.3)

def testBesselSecondKind_Yn():
    results = []
    for i in n:
        results.append(bessel.besselY_n(i, z))

    plotFunctions.PlotGraphic(n, 'Bessel functions of the second kind, Yn(x)', 'Y', results, z, -2, 0.8)

def testSphericalBesselFirstKind_jn():
    results = []
    for i in n:
        results.append(bessel.besselj_n(i, z))
        
    plotFunctions.PlotGraphic(n, 'Spherical Bessel functions of the first kind, jn(x)', 'J', results, z, -0.40, 1.3)

def testSphericalBesselSecondKind_yn():
    results = []
    for i in n:
        results.append(bessel.bessely_n(i, z))

    plotFunctions.PlotGraphic(n, 'Spherical Bessel functions of the second kind, Yn(x)', 'Y', results, z, -3, 0.50)

if __name__ == '__main__':
    testBesselFirstKind_Jn()
    testBesselSecondKind_Yn()
    testSphericalBesselFirstKind_jn()
    testSphericalBesselSecondKind_yn()
