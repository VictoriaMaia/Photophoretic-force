import sys
sys.path.append('./')
from asymmetryFactorJ1 import j1 as J
import numpy as np
import matplotlib.pyplot as plt
import plotFunctions
import math

micro = 10**(-6) 

def testJ1Value():
    m = 1.57 - 0.038j
    x = 10
    ur = 1
    eps_r2l = J.epsilon(m, ur)

    print(J.J1(J.J1_attributes(x, m, eps_r2l, ur)))


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
        resultsBlue.append(J.J1(J.J1_attributes(i, mBlue, eps_r2lBlue, ur)))
        resultsRed.append(J.J1(J.J1_attributes(i, mRed, eps_r2lRed, ur)))
        resultsBlack.append(J.J1(J.J1_attributes(i, mBlack, eps_r2lBlack, ur)))

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
        results.append(J.J1(J.J1_attributes(i, m, eps_r2l, ur)))
        rzeros.append(0)

    plotFunctions.PlotOneGraphic ("", "Eqn (62)", 'g', results, x, -0.10, 0.15, xLabel='Size Parameter x', yLabel='Asymmetry Factor J1')

def testJ1Fig2MACKOWSKI():
    m = 1.57 - 0.38j
    x = np.linspace(0.01, 20, 200)
    ur = 1
    eps_r2l = J.epsilon(m, ur)
    results = []

    for i in x:
        results.append(J.J1(J.J1_attributes(i, m, eps_r2l, ur)))

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


def testJ1GaussianBeam():
    l = 10.63 * micro 
    k = (2*math.pi) / l
    z0 = 0
    s = 0.1

    mBlue = 1.57 - 0.038j
    mRed = 1.57 - 0.19j
    mBlack = 1.57 - 0.95j

    x = np.linspace(0.01, 20, 200)
    ur = 1
    eps_r2lBlue = J.epsilon(mBlue, ur)
    eps_r2lRed = J.epsilon(mRed, ur)
    eps_r2lBlack = J.epsilon(mBlack, ur)

    resultsBlue = []
    resultsBlueTick = []
    resultsRed = []
    resultsRedTick = []
    resultsBlack = []
    resultsBlackTick = []
    for i in x:
        resultsBlueTick.append(J.J1(J.J1_attributes(i, mBlue, eps_r2lBlue, ur)))
        resultsBlue.append(J.J1(J.J1_attributes(i, mBlue, eps_r2lBlue, ur, k, z0, s)))
        resultsRedTick.append(J.J1(J.J1_attributes(i, mRed, eps_r2lRed, ur)))
        resultsRed.append(J.J1(J.J1_attributes(i,  mRed, eps_r2lRed, ur, k, z0, s)))
        resultsBlackTick.append(J.J1(J.J1_attributes(i, mBlack, eps_r2lBlack, ur)))
        resultsBlack.append(J.J1(J.J1_attributes(i, mBlack, eps_r2lBlack, ur, k, z0, s)))

    plt.figure(figsize=[10,5])
    plt.plot(x, resultsBlueTick, 'b-.', label= "onda plana (g_n = 1)")
    plt.plot(x, resultsBlue, 'b', label= "gaussian beam")
    plt.plot(x, resultsRedTick, 'r-.', label= "onda plana")
    plt.plot(x, resultsRed, 'r', label= "gaussian beam")
    plt.plot(x, resultsBlackTick, 'g-.', label= "onda plana")
    plt.plot(x, resultsBlack, 'g', label= "gaussian beam")
    plt.xlabel('Size Parameter x')
    plt.ylabel('Asymmetry Factor J1')
    plt.grid()
    plt.legend(loc='best')
    plt.text(12.5, .03, 'M = 1.57 - 0.038j')
    plt.text(10, -.1, 'M = 1.57 - 0.19j')
    plt.text(7.5, -.33, 'M = 1.57 - 0.95j')
    plt.show()

def testJ1GaussianBeam_s():
    l = 10.63 * micro 
    k = (2*math.pi) / l
    z0 = 0
    m = 1.57 - 0.038j
    x3 = 3
    x8 = 8

    s = np.linspace(0.01, 0.16, 200)
    ur = 1
    eps_r2l = J.epsilon(m, ur)

    resultsX3 = []
    resultsX3Tick = []
    resultsX8 = []
    resultsX8Tick = []

    for i in s:
        resultsX3Tick.append(J.J1(J.J1_attributes(x3, m, eps_r2l, ur)))
        resultsX3.append(J.J1(J.J1_attributes(x3, m, eps_r2l, ur, k, z0, i)))
        resultsX8Tick.append(J.J1(J.J1_attributes(x8, m, eps_r2l, ur)))
        resultsX8.append(J.J1(J.J1_attributes(x8,  m, eps_r2l, ur, k, z0, i)))
        
        
    plt.figure(figsize=[10,5])
    plt.plot(s, resultsX3Tick, 'k-.', label= "onda plana (g_n = 1)")
    plt.plot(s, resultsX3, 'k', label= "gaussian beam")
    plt.plot(s, resultsX8Tick, 'b-.', label= "onda plana")
    plt.plot(s, resultsX8, 'b', label= "gaussian beam")
    plt.xlabel('Confinement factor s')
    plt.ylabel('Asymmetry Factor J1')
    plt.xlim(0, 0.165)
    plt.grid()
    plt.legend(loc='best')
    plt.text(0.1, .045, 'x=3')
    plt.text(0.06, .02, 'x=8')
    plt.show()

def testJ1GaussianBeam_z0():
    l = 10.63 * micro 
    k = (2*math.pi) / l

    m = 1.57 - 0.038j
    s = 0.16

    x1 = 0.1
    x3 = 3
    x8 = 8

    ur = 1
    eps_r2l = J.epsilon(m, ur)

    z0 = np.linspace(-70*micro, 70*micro, 250)
    # z0 = np.linspace(0, 60, 200)

    resultsX1 = []
    resultsX3 = []
    resultsX8 = []

    for i in z0:
        resultsX1.append(J.J1(J.J1_attributes(x1, m, eps_r2l, ur, k, i, s))*500)
        resultsX3.append(J.J1(J.J1_attributes(x3, m, eps_r2l, ur, k, i, s)))
        resultsX8.append(J.J1(J.J1_attributes(x8, m, eps_r2l, ur, k, i, s)))
        

    z0 = np.linspace(-70, 70, 250)
    plt.figure(figsize=[10,5])
    plt.plot(z0, resultsX1, 'b', label= "x = 0.1 * 500 ")
    plt.plot(z0, resultsX3, 'r', label= "x = 3")
    plt.plot(z0, resultsX8, 'g', label= "x = 8")
    plt.xlabel('Relative position z_0 (u_m) ')
    plt.ylabel('Asymmetry Factor J1')
    plt.grid()
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    testJ1For3Particles()
    testJ1Value()
    testJ1Fig1MACKOWSKI()
    testJ1Fig2MACKOWSKI()
    testJ1GaussianBeam()
    testJ1GaussianBeam_s()
    testJ1GaussianBeam_z0()
