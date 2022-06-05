import sys
sys.path.append('./')
from asymmetryFactorJ1.mathFunctions import mathFuncs as Rb
from Tests.helperFunctionsToTests import plotFunctions
import numpy as np

z = np.linspace(0, 20, 200)
z1 = np.linspace(0.01, 20, 200)

n = [0, 1, 2]


def test_ricatti_bessel_phi_n():
    results = []
    for i in n:
        results.append(Rb.ricattiBessel_jn(i, z))
        
    plotFunctions.plot_graphic_math(n, 'Ricatti-Bessel ψ_n(z)', 'ψ', results, z, -1.5, 2)


def test_ricatti_bessel_derivative_phi_n ():
    results = []
    for i in n:
        results.append(Rb.ricattiBessel_jn_derivative(i, z))
        
    plotFunctions.plot_graphic_math(n, 'Ricatti-Bessel ψ\'_n(z)', 'ψ\'', results, z, -1.5, 2)


def test_ricatti_bessel_xi_n():
    plotFunctions.plot_graphic_real_and_imaginary_parts("Ricatti-Bessel ξ_n(z)", "n=0", 'g', Rb.ricattiBessel_hn(0, z1), z1, -1.5, 4)
    plotFunctions.plot_graphic_real_and_imaginary_parts("Ricatti-Bessel ξ_n(z)", "n=1", 'r', Rb.ricattiBessel_hn(1, z1), z1, -1.5, 4)
    plotFunctions.plot_graphic_real_and_imaginary_parts("Ricatti-Bessel ξ_n(z)", "n=2", 'b', Rb.ricattiBessel_hn(2, z1), z1, -1.5, 4)


def test_ricatti_besselDerivative_xi_n():
    plotFunctions.plot_graphic_real_and_imaginary_parts("Ricatti-Bessel ξ'_n(z)", "n=0", 'g', Rb.ricattiBessel_hn_derivative(0, z1), z1, -2, 2)
    plotFunctions.plot_graphic_real_and_imaginary_parts("Ricatti-Bessel ξ'_n(z)", "n=1", 'r', Rb.ricattiBessel_hn_derivative(1, z1), z1, -4, 3)
    plotFunctions.plot_graphic_real_and_imaginary_parts("Ricatti-Bessel ξ'_n(z)", "n=2", 'b', Rb.ricattiBessel_hn_derivative(2, z1), z1, -4, 3)


if __name__ == '__main__':
    test_ricatti_bessel_phi_n()
    test_ricatti_bessel_derivative_phi_n()
    test_ricatti_bessel_xi_n()
    test_ricatti_besselDerivative_xi_n()