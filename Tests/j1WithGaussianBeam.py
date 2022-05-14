import sys
sys.path.append('./')

from asymmetryFactorJ1 import *
from asymmetryFactorJ1.gaussianBeam import *
from Tests.helperFunctionsToTests import plotFunctions

import numpy as np
import math
import matplotlib.pyplot as plt
from timeit import default_timer as timer

mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)


def testJ1GaussianBeamWithJ1PlaneWave():
    l = 10.63 * micro 
    k = (2*math.pi) / l
    z0 = 0
    s = 0.1
    ur = 1 
    mBlue = 1.57 - 0.038j
    mRed = 1.57 - 0.19j
    mBlack = 1.57 - 0.95j

    x = np.linspace(0.01, 20, 200)


    resultsBlueJ1GB = []
    resultsRedJ1GB = []
    resultsBlackJ1GB = []
    resultsBlueJ1 = []
    resultsRedJ1 = []
    resultsBlackJ1 = []

    start = timer()
    for i in x:
        resultsBlueJ1GB.append(J1(J1Gauss(i, mBlue, ur, k, z0, s)))
        resultsRedJ1GB.append(J1(J1Gauss(i, mRed, ur, k, z0, s)))
        resultsBlackJ1GB.append(J1(J1Gauss(i, mBlack, ur, k, z0, s)))
        resultsBlueJ1.append(J1(J1_attributes(i, mBlue, ur)))
        resultsRedJ1.append(J1(J1_attributes(i, mRed, ur)))
        resultsBlackJ1.append(J1(J1_attributes(i, mBlack, ur)))
    tempo = timer()-start
    print(tempo)

    resultsToPlot = []

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsBlueJ1GB, 
                            'b', 
                            label="GB",
                            xLocText=12.5, 
                            yLocText=.03, 
                            messageText="M = 1.57 - i0.038")
                        )
    
    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsBlueJ1, 
                            'b-.', 
                            label="OP ($g_n$ = 1)")                            
                        )

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsRedJ1, 
                            'r-.', 
                            label="OP")                          
                        )

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsBlackJ1, 
                            'g-.', 
                            label="OP")                          
                        )

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsRedJ1GB, 
                            'r', 
                            label="GB",
                            xLocText=10, 
                            yLocText=-0.1, 
                            messageText="M = 1.57 - i0.19")
                        )

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsBlackJ1GB, 
                            'g', 
                            label="GB",
                            xLocText=7.5, 
                            yLocText=-.33, 
                            messageText="M = 1.57 - i0.95")
                        )


    graficInfo = plotFunctions.GraficAttributes(
                            imagSizeX = 7, 
                            imagSizeY = 5, 
                            xLabel = 'Size Parameter x', 
                            yLabel = 'Asymmetry Factor $J_1(x)$', 
                )
    
    
    plotFunctions.PlotGraphic (resultsToPlot,
                                graficInfo,
                                x,
                                text=True,
                                )


def testJ1GaussianVaryingSValue():
    l = 10.63 * micro 
    k = (2*math.pi) / l
    z0 = 0
    ur = 1
    m = 1.57 - 0.038j
    x3 = 3
    x8 = 8

    s = np.linspace(0.01, 0.16, 200)


    resultsX3J1GB = []
    resultsX8J1GB = []
    resultsX3J1 = []
    resultsX8J1 = []

    start = timer()
    for i in s:
        resultsX3J1GB.append(J1(J1Gauss(x3, m, ur, k, z0, i)))
        resultsX8J1GB.append(J1(J1Gauss(x8, m, ur, k, z0, i)))
        resultsX3J1.append(J1(J1_attributes(x3, m, ur)))
        resultsX8J1.append(J1(J1_attributes(x8, m, ur)))
    tempo = timer()-start
    print(tempo)

    resultsToPlot = []

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsX3J1GB, 
                            'k', 
                            label="GB",
                            xLocText=0.1, 
                            yLocText=.045, 
                            messageText="x=3"
                            )
                        )
    
    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsX3J1, 
                            'k-.', 
                            label="OP ($g_n$ = 1)")                            
                        )

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsX8J1GB, 
                            'b', 
                            label="GB",
                            xLocText=0.06, 
                            yLocText=.02, 
                            messageText="x=8")                          
                        )

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsX8J1, 
                            'b-.', 
                            label="OP")                          
                        )

    
    graficInfo = plotFunctions.GraficAttributes(
                            imagSizeX = 7, 
                            imagSizeY = 5, 
                            xLabel = 'Confinement factor s', 
                            yLabel = 'Asymmetry Factor $J_1(x)$', 
                )
    
    
    plotFunctions.PlotGraphic (resultsToPlot,
                                graficInfo,
                                s,
                                text=True,
                                )


def testJ1GaussianVaryingSAndXValues():
    l = 10.63 * micro 
    k = (2*math.pi) / l
    z0 = 0
    ur = 1
    m = 1.57 - 0.038j

    s = [0.01, 0.10, 0.16]
    
    x1 = 0.1
    x3 = 3
    x8 = 8
    
    z0fig1 = np.linspace(-15*mili, 15*mili, 250)
    z0fig2 = np.linspace(-150*micro, 150*micro, 250)
    z0fig3 = np.linspace(-60*micro, 60*micro, 250)

    resultsX1s001 = []
    resultsX3s001 = []
    resultsX8s001 = []

    resultsX1s01 = []
    resultsX3s01 = []
    resultsX8s01 = []

    resultsX1s016 = []
    resultsX3s016 = []
    resultsX8s016 = []

    start = timer()
    for i in z0fig1:
        resultsX1s001.append(J1(J1Gauss(x1, m, ur, k, i, s[0]))*10000)
        resultsX3s001.append(J1(J1Gauss(x3, m, ur, k, i, s[0])))
        resultsX8s001.append(J1(J1Gauss(x8, m, ur, k, i, s[0])))
    tempo = timer()-start
    print(tempo)

    start = timer()
    for i in z0fig2:
        resultsX1s01.append(J1(J1Gauss(x1, m, ur, k, i, s[1]))*5000)
        resultsX3s01.append(J1(J1Gauss(x3, m, ur, k, i, s[1])))
        resultsX8s01.append(J1(J1Gauss(x8, m, ur, k, i, s[1])))
    tempo = timer()-start
    print(tempo)

    start = timer()
    for i in z0fig3:
        resultsX1s016.append(J1(J1Gauss(x1, m, ur, k, i, s[2]))*1000)
        resultsX3s016.append(J1(J1Gauss(x3, m, ur, k, i, s[2])))
        resultsX8s016.append(J1(J1Gauss(x8, m, ur, k, i, s[2])))
    tempo = timer()-start
    print(tempo)

    z0fig1 = np.linspace(-15, 15, 250)
    z0fig2 = np.linspace(-150, 150, 250)
    z0fig3 = np.linspace(-60, 60, 250)

    fig, (fig1, fig2, fig3) = plt.subplots(1, 3, figsize=(17, 5))

    fig1.plot(z0fig1, resultsX1s001, 'b', label= "x = 0.1 * 10000 ")
    fig1.plot(z0fig1, resultsX3s001, 'r', label= "x = 3")
    fig1.plot(z0fig1, resultsX8s001, 'g', label= "x = 8")
    fig1.grid(True)
    fig1.set_xlabel('Relative position $z_0$ (mm)')
    fig1.set_ylabel('Asymmetry Factor J1')
    fig1.text(4.5, .085, '$x=8$')
    fig1.text(0, .055, '$x=3$')
    fig1.text(0, -.02, '$x=0.1*(10^4)$')

    fig2.plot(z0fig2, resultsX1s01, 'b', label= "x = 0.1 * 5000 ")
    fig2.plot(z0fig2, resultsX3s01, 'r', label= "x = 3")
    fig2.plot(z0fig2, resultsX8s01, 'g', label= "x = 8")
    fig2.grid(True)
    fig2.set_xlabel('Relative position $z_0$ ($\mu_m$)')
    fig2.set_ylabel('Asymmetry Factor J1')
    fig2.text(-15, .011, '$x=8$')
    fig2.text(0, .04, '$x=3$')
    fig2.text(-60, -.01, '$x=0.1*5000$')

    fig3.plot(z0fig3, resultsX1s016, 'b', label= "x = 0.1 * 1000 ")
    fig3.plot(z0fig3, resultsX3s016, 'r', label= "x = 3")
    fig3.plot(z0fig3, resultsX8s016, 'g', label= "x = 8")
    fig3.grid(True)
    fig3.set_xlabel('Relative position $z_0$ ($\mu_m$)')
    fig3.set_ylabel('Asymmetry Factor J1')
    fig3.text(20, -.01, '$x=8$')
    fig3.text(0, .03, '$x=3$')
    fig3.text(-30, 0, '$x=0.1*1000$')

    plt.show()


if __name__ == '__main__':
    # testJ1GaussianBeam()
    testJ1GaussianBeamWithJ1PlaneWave()
    # testJ1GaussianVaryingSValue()
    # testJ1GaussianVaryingSAndXValues()