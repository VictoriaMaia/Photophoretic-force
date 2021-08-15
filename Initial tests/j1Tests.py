import sys
sys.path.append('./')
from asymmetryFactorJ1 import j1 as J
import numpy as np
import matplotlib.pyplot as plt
import plotFunctions


def testJ1Value():
    m = 1.57 - 0.038j
    x = 10
    ur = 1
    eps_r2l = J.epsilon(m, ur)

    print(J.J1(x, m, eps_r2l, ur))


def testJ1For3Particles():
    mBlue = 1.57 - 0.038j
    mRed = 1.57 - 0.19j
    mBlack = 1.57 - 0.95j

    x = np.linspace(0.01, 20, 200)

    ur = 1
    eps_r2lBlue = J.epsilon(mBlue, ur) 
    eps_r2lRed = J.epsilon(mRed, ur) 
    eps_r2lBlack = J.epsilon(mBlack, ur)

    resultsBlue = []
    resultsRed = []
    resultsBlack = []
    for i in x:
        resultsBlue.append(J.J1(i, mBlue, eps_r2lBlue, ur))
        resultsRed.append(J.J1(i, mRed, eps_r2lRed, ur))
        resultsBlack.append(J.J1(i, mBlack, eps_r2lBlack, ur))

    plt.figure(figsize=[7,5])
    plt.plot(x, resultsBlue, 'b')
    plt.plot(x, resultsRed, 'r-.')
    plt.plot(x, resultsBlack, 'k--')
    # plt.plot(x, resultsBlue, 'b', label= "M = 1.57 - 0.038j")
    # plt.plot(x, resultsRed, 'r-.', label= "M = 1.57 - 0.19j")
    # plt.plot(x, resultsBlack, 'k--', label= "M = 1.57 - 0.95j")
    plt.xlabel('Size Parameter, x')
    plt.ylabel('Asymmetry Factor, J1(x)')
    plt.grid()
    plt.text(12.5, .03, 'M = 1.57 - i0.038')
    plt.text(9, -0.2, 'M = 1.57 - i0.19')
    plt.text(7.5, -.33, 'M = 1.57 - i0.95')
    # plt.legend(loc='best')
    plt.show()

def testJ1Fig1MACKOWSKI():
    m = 1.57 - 0.038j
    x = np.linspace(0.01, 20, 200)
    ur = 1
    eps_r2l = J.epsilon(m, ur)
    results = []
    rzeros = []
    for i in x:
        results.append(J.J1(i, m, eps_r2l, ur))
        rzeros.append(0)

    plotFunctions.PlotOneGraphic ("", "Eqn (62)", 'g', results, x, -0.10, 0.15, xLabel='Size Parameter x', yLabel='Asymmetry Factor J1')

def testJ1Fig2MACKOWSKI():
    # micro = 10**(-6) 
    m = 1.57 - 0.38j
    x = np.linspace(0.01, 20, 200)
    ur = 1
    eps_r2l = J.epsilon(m, ur)
    results = []

    for i in x:
        results.append(J.J1(i, m, eps_r2l, ur))

    plt.figure(figsize=[7,5])
    plt.plot(x, results, 'g', label= "M = 1.57 - 0.38j")
    plt.xlabel('Size Parameter x')
    plt.ylabel('Asymmetry Factor J1')
    plt.ylim(-0.50, 0.01)
    # plt.ylim(-0.10, 0.15)
    # plt.ylim(-0.50, 0.001)
    plt.xlim(0, 20)
    plt.grid()
    # plt.legend(loc='best', title="")
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    testJ1For3Particles()
    testJ1Value()
    testJ1Fig1MACKOWSKI()
    testJ1Fig2MACKOWSKI()