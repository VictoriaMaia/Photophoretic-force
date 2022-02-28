import sys
sys.path.append('./')

from asymmetryFactorJ1 import *
from asymmetryFactorJ1.gaussianBeam import *

import numpy as np
import math
import plotFunctions

mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)


def testJ1GaussianBeamWithJ1PlaneWave():
    micro = 10**(-6) 
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

    for i in x:
        resultsBlueJ1GB.append(J1(J1Gauss(i, mBlue, ur, k, z0, s)))
        resultsRedJ1GB.append(J1(J1Gauss(i, mRed, ur, k, z0, s)))
        resultsBlackJ1GB.append(J1(J1Gauss(i, mBlack, ur, k, z0, s)))
        resultsBlueJ1.append(J1(J1_attributes(i, mBlue, ur)))
        resultsRedJ1.append(J1(J1_attributes(i, mRed, ur)))
        resultsBlackJ1.append(J1(J1_attributes(i, mBlack, ur)))
        
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



# def testJ1GaussianBeam_s():
#     l = 10.63 * micro 
#     k = (2*math.pi) / l
#     z0 = 0
#     m = 1.57 - 0.038j
#     x3 = 3
#     x8 = 8

#     s = np.linspace(0.01, 0.16, 200)
#     ur = 1
#     eps_r2l = EP.epsilon(m, ur)

#     resultsX3 = []
#     resultsX3Tick = []
#     resultsX8 = []
#     resultsX8Tick = []

#     for i in s:
#         resultsX3Tick.append(J.J1(J.J1_attributes(x3, m, eps_r2l, ur)))
#         resultsX3.append(J.J1(J.J1_attributes(x3, m, eps_r2l, ur, k, z0, i)))
#         resultsX8Tick.append(J.J1(J.J1_attributes(x8, m, eps_r2l, ur)))
#         resultsX8.append(J.J1(J.J1_attributes(x8,  m, eps_r2l, ur, k, z0, i)))
        
        
#     plt.figure(figsize=[10,5])
#     plt.plot(s, resultsX3Tick, 'k-.', label= "onda plana (g_n = 1)")
#     plt.plot(s, resultsX3, 'k', label= "gaussian beam")
#     plt.plot(s, resultsX8Tick, 'b-.', label= "onda plana")
#     plt.plot(s, resultsX8, 'b', label= "gaussian beam")
#     plt.xlabel('Confinement factor s')
#     plt.ylabel('Asymmetry Factor J1')
#     plt.xlim(0, 0.165)
#     plt.grid()
#     plt.legend(loc='best')
#     plt.text(0.1, .045, 'x=3')
#     plt.text(0.06, .02, 'x=8')
#     plt.show()


if __name__ == '__main__':
    # testJ1GaussianBeam()
    testJ1GaussianBeamWithJ1PlaneWave()