import sys
sys.path.append('./')

from asymmetryFactorJ1 import *

import numpy as np
import plotFunctions

mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)

def testJ1Value():
    m = 1.57 - 0.038j
    x = 10
    ur = 1

    resultJ1Expected = 0.054413290391591596
    resultJ1Current = J1(J1_attributes(x, m, ur))

    if  resultJ1Current != resultJ1Expected:
        print("The J1 result is wront!!")
        print("Expected: ", resultJ1Expected)
        print("Current: ", resultJ1Current)
    else:
        print("The J1 result is correct!!")
    

def testJ1For3Particles():
    mBlue = 1.57 - 0.038j
    mRed = 1.57 - 0.19j
    mBlack = 1.57 - 0.95j

    x = np.linspace(0.01, 20, 200)

    ur = 1

    resultsBlue = []
    resultsRed = []
    resultsBlack = []

    for i in x:
        resultsBlue.append(J1(J1_attributes(i, mBlue, ur)))
        resultsRed.append(J1(J1_attributes(i, mRed, ur)))
        resultsBlack.append(J1(J1_attributes(i, mBlack, ur)))

    
    resultsToPlot = []

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsBlue, 
                            'b', 
                            xLocText=12.5, 
                            yLocText=.03, 
                            messageText="M = 1.57 - i0.038")
                        )

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsRed, 
                            'r-.', 
                            xLocText= 9, 
                            yLocText= -0.2, 
                            messageText="M = 1.57 - i0.19")
                        )
    
    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsBlack, 
                            'k--', 
                            xLocText= 7.5, 
                            yLocText= -.33, 
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


def testJ1Fig1MACKOWSKI():
    m = 1.57 - 0.038j
    x = np.linspace(0.01, 20, 200)
    ur = 1
    results = []
    rzeros = []
    for i in x:
        results.append(J1(J1_attributes(i, m, ur)))
        rzeros.append(0)

    plotFunctions.PlotOneGraphic ("", "Eqn (62)", 'g', results, x, -0.10, 0.15, xLabel='Size Parameter x', yLabel='Asymmetry Factor J1')


def testJ1Fig2MACKOWSKI():
    m = 1.57 - 0.38j
    x = np.linspace(0.01, 20, 200)
    ur = 1
    results = []

    for i in x:
        results.append(J1(J1_attributes(i, m, ur)))

    resultsToPlot = [plotFunctions.ResultsGraficAttributes(
                        results, 
                        'g') ]

    graficInfo = plotFunctions.GraficAttributes(
                            imagSizeX = 7, 
                            imagSizeY = 5, 
                            xLabel = 'Size Parameter x', 
                            yLabel = 'Asymmetry Factor $J_1(x)$', 
                            yLowerLimit=-0.50, 
                            yUpperLimit=0.01, 
                            xLowerLimit=0, 
                            xUpperLimit=20 
                )
  
  
    plotFunctions.PlotGraphic (resultsToPlot,
                                graficInfo,
                                x,
                                ylimit=True, 
                                xlimit=True,
                                )
  

if __name__ == '__main__':
    print("We have these tests.")
    print("1 - testJ1Value")
    print("2 - testJ1For3Particles")
    print("3 - testJ1Fig1MACKOWSKI")
    print("4 - testJ1Fig2MACKOWSKI")

    numberTest = input("Which will execute? Please write the number ")

    switch = {
        "1": testJ1Value,
        "2": testJ1For3Particles,
        "3": testJ1Fig1MACKOWSKI,
        "4": testJ1Fig2MACKOWSKI
    }

    case = switch.get(numberTest)
    case()

    # testJ1Value()
    # testJ1For3Particles()
    # testJ1Fig1MACKOWSKI()
    # testJ1Fig2MACKOWSKI()
