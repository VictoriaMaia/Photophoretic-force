import sys
sys.path.append('./')
from asymmetryFactorJ1.mathFunctions import mathFuncs as rb
import plotFunctions
import numpy as np

z  = np.linspace(0, 20, 200)
z1  = np.linspace(0.01, 20, 200)

n = [0,1,2]

def testRicatteBessel_Phi_n():
    results = []
    for i in n:
        results.append(rb.ricattiBessel_jn(i, z))
        
    plotFunctions.PlotGraphicMath(n, 'Ricatti-Bessel ψ_n(z)', 'ψ', results, z, -1.5, 2)

def testRicatteBesselDerivative_Phi_n ():
    results = []
    for i in n:
        results.append(rb.ricattiBessel_jn_derivative(i, z))
        
    plotFunctions.PlotGraphicMath(n, 'Ricatti-Bessel ψ\'_n(z)', 'ψ\'', results, z, -1.5, 2)

def testRicatteBessel_Xi_n():
    plotFunctions.PlotGraphicRealAndImageParts("Ricatti-Bessel ξ_n(z)", "n=0", 'g', rb.ricattiBessel_hn(0, z1), z1, -1.5, 4)
    plotFunctions.PlotGraphicRealAndImageParts("Ricatti-Bessel ξ_n(z)", "n=1", 'r', rb.ricattiBessel_hn(1, z1), z1, -1.5, 4)
    plotFunctions.PlotGraphicRealAndImageParts("Ricatti-Bessel ξ_n(z)", "n=2", 'b', rb.ricattiBessel_hn(2, z1), z1, -1.5, 4)

def testRicatteBesselDerivative_Xi_n():
    plotFunctions.PlotGraphicRealAndImageParts("Ricatti-Bessel ξ'_n(z)", "n=0", 'g', rb.ricattiBessel_hn_derivative(0, z1), z1, -2, 2)
    plotFunctions.PlotGraphicRealAndImageParts("Ricatti-Bessel ξ'_n(z)", "n=1", 'r', rb.ricattiBessel_hn_derivative(1, z1), z1, -4, 3)
    plotFunctions.PlotGraphicRealAndImageParts("Ricatti-Bessel ξ'_n(z)", "n=2", 'b', rb.ricattiBessel_hn_derivative(2, z1), z1, -4, 3)

if __name__ == '__main__':
    testRicatteBessel_Phi_n()
    testRicatteBesselDerivative_Phi_n()
    testRicatteBessel_Xi_n()
    testRicatteBesselDerivative_Xi_n()