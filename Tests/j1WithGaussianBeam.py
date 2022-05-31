import sys
sys.path.append('./')

from asymmetryFactorJ1 import *
from asymmetryFactorJ1.gaussianBeam import *
from Tests.helperFunctionsToTests import plotFunctions, timeConvert

import math
import numpy as np
from tqdm import tqdm
from functools import partial
import matplotlib.pyplot as plt
from timeit import default_timer as timer


mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)
orange = '#ff6800'


# yLabel = J1
# xLabel = x [0.01 to 20]
# To:
    # m =[ 1.57 - 0.038j, 
         # 1.57 - 0.19j, 
         # 1.57 - 0.95j ]
def testJ1GaussianBeamWithJ1PlaneWave(returnTimeBool):
    l = 10.63 * micro 
    k = (2*math.pi) / l
    z0 = 0
    s = 0.1
    ur = 1 
    mBlue = 1.57 - 0.038j
    mRed = 1.57 - 0.19j
    mBlack = 1.57 - 0.95j

    x = np.linspace(0.01, 20, 300)


    resultsBlueJ1GB = []
    resultsRedJ1GB = []
    resultsBlackJ1GB = []
    resultsBlueJ1 = []
    resultsRedJ1 = []
    resultsBlackJ1 = []

    totalTime = 0
    pbar = tqdm(colour=orange, total=len(x), desc="Test 1. Calculating")

    for i in x:
        timeBegin = timer()

        resultsBlueJ1GB.append(J1(J1Gauss(i, mBlue, ur, k, z0, s)))
        resultsRedJ1GB.append(J1(J1Gauss(i, mRed, ur, k, z0, s)))
        resultsBlackJ1GB.append(J1(J1Gauss(i, mBlack, ur, k, z0, s)))
        resultsBlueJ1.append(J1(J1_attributes(i, mBlue, ur)))
        resultsRedJ1.append(J1(J1_attributes(i, mRed, ur)))
        resultsBlackJ1.append(J1(J1_attributes(i, mBlack, ur)))


        timeEnd = timer()
        totalTime += timeEnd - timeBegin
        pbar.update()

    pbar.refresh()
    pbar.close()
    
    if returnTimeBool:
        timeConvert.convertTimeToMoreReadable(totalTime)

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


# yLabel = J1
# xLabel = s [0.01 to 0.16]
# To:
    # m = 1.57 - 0.038j
    # x = [3, 8]
def testJ1GaussianWithPlaneWaveVaryingSValue(returnTimeBool):
    l = 10.63 * micro 
    k = (2*math.pi) / l
    z0 = 0
    ur = 1
    m = 1.57 - 0.038j
    x3 = 3
    x8 = 8

    s = np.linspace(0.01, 0.16, 300)


    resultsX3J1GB = []
    resultsX8J1GB = []
    resultsX3J1 = []
    resultsX8J1 = []

    totalTime = 0
    pbar = tqdm(colour=orange, total=len(s), desc="Test 2. Calculating")


    for i in s:
        timeBegin = timer()

        resultsX3J1GB.append(J1(J1Gauss(x3, m, ur, k, z0, i)))
        resultsX8J1GB.append(J1(J1Gauss(x8, m, ur, k, z0, i)))
        resultsX3J1.append(J1(J1_attributes(x3, m, ur)))
        resultsX8J1.append(J1(J1_attributes(x8, m, ur)))
       
        timeEnd = timer()
        totalTime += timeEnd - timeBegin
        pbar.update()

    pbar.refresh()
    pbar.close()

    
    if returnTimeBool:
        timeConvert.convertTimeToMoreReadable(totalTime)


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


# yLabel = J1
# xLabel = z0fig1 [-15mili to 15mili]
         # z0fig2 [-150mili to 150mili]
         # z0fig3 [-60mili to 60mili]
# To:
    # m = 1.57 - 0.038j
    # s = [0.01, 0.10, 0.16]
    # x = [0.1, 3, 8]
def testJ1GaussianVaryingSAndZ0AndXValues(returnTimeBool):
    l = 10.63 * micro 
    k = (2*math.pi) / l
    z0 = 0
    ur = 1
    m = 1.57 - 0.038j

    s = [0.01, 0.10, 0.16]
    
    x1 = 0.1
    x3 = 3
    x8 = 8

    qntPoints = 300
    
    z0fig1 = np.linspace(-15*mili, 15*mili, qntPoints)
    z0fig2 = np.linspace(-150*micro, 150*micro, qntPoints)
    z0fig3 = np.linspace(-60*micro, 60*micro, qntPoints)

    resultsX1s001 = []
    resultsX3s001 = []
    resultsX8s001 = []

    resultsX1s01 = []
    resultsX3s01 = []
    resultsX8s01 = []

    resultsX1s016 = []
    resultsX3s016 = []
    resultsX8s016 = []

    totalTime = 0
    pbar1 = tqdm(colour=orange, total=len(z0fig1), desc="Test 3.1. Calculating")
    
    for i in z0fig1:
        timeBegin = timer()

        resultsX1s001.append(J1(J1Gauss(x1, m, ur, k, i, s[0]))*10000)
        resultsX3s001.append(J1(J1Gauss(x3, m, ur, k, i, s[0])))
        resultsX8s001.append(J1(J1Gauss(x8, m, ur, k, i, s[0])))
        
        timeEnd = timer()
        totalTime += timeEnd - timeBegin
        pbar1.update()

    pbar1.close()

    if returnTimeBool:
        timeConvert.convertTimeToMoreReadable(totalTime)


    totalTime = 0
    pbar2 = tqdm(colour=orange, total=len(z0fig2), desc="Test 3.2. Calculating")

    for i in z0fig2:
        timeBegin = timer()

        resultsX1s01.append(J1(J1Gauss(x1, m, ur, k, i, s[1]))*5000)
        resultsX3s01.append(J1(J1Gauss(x3, m, ur, k, i, s[1])))
        resultsX8s01.append(J1(J1Gauss(x8, m, ur, k, i, s[1])))
     
        timeEnd = timer()
        totalTime += timeEnd - timeBegin
        pbar2.update()

    pbar2.close()

    if returnTimeBool:
        timeConvert.convertTimeToMoreReadable(totalTime)

    
    totalTime = 0
    pbar3 = tqdm(colour=orange, total=len(z0fig3), desc="Test 3.3. Calculating")
    
    for i in z0fig3:
        timeBegin = timer()

        resultsX1s016.append(J1(J1Gauss(x1, m, ur, k, i, s[2]))*1000)
        resultsX3s016.append(J1(J1Gauss(x3, m, ur, k, i, s[2])))
        resultsX8s016.append(J1(J1Gauss(x8, m, ur, k, i, s[2])))
        
        timeEnd = timer()
        totalTime += timeEnd - timeBegin
        pbar3.update()
    
    pbar3.close()
    
    if returnTimeBool:
        timeConvert.convertTimeToMoreReadable(totalTime)

    
    z0fig1 = np.linspace(-15, 15, qntPoints)
    z0fig2 = np.linspace(-150, 150, qntPoints)
    z0fig3 = np.linspace(-60, 60, qntPoints)

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


# yLabel = J1
# xLabel = x [20 to 100]
# To:
    # m = 1.57 - 0.038j
    # s = [0.1, 0.05, 0.01]
def testJ1GaussianWithPlaneWaveVaryingXValue(returnTimeBool):
    l = 10.63 * micro 
    k = (2*math.pi) / l
    z0 = 0
    m = 1.57 - 0.038j

    x = np.linspace(20, 100, 300)
    ur = 1

    resultsS0J1GB = []
    resultsS1J1GB = []
    resultsS2J1GB = []
    resultsJ1 = []


    totalTime = 0
    pbar = tqdm(colour=orange, total=len(x), desc="Test 4. Calculating")

    for i in x:
        timeBegin = timer()

        resultsS0J1GB.append(J1(J1Gauss(i, m, ur, k, z0, 0.1)))
        resultsS1J1GB.append(J1(J1Gauss(i,  m, ur, k, z0, 0.05)))
        resultsS2J1GB.append(J1(J1Gauss(i,  m, ur, k, z0, 0.01)))
        resultsJ1.append(J1(J1_attributes(i, m, ur)))

        timeEnd = timer()
        totalTime += timeEnd - timeBegin
        pbar.update()

    pbar.refresh()
    pbar.close()

    
    if returnTimeBool:
        timeConvert.convertTimeToMoreReadable(totalTime)


    resultsToPlot = []

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsJ1, 
                            'k-.', 
                            label="OP")
                        )
    
    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsS0J1GB, 
                            'g', 
                            label="s=0.1")                            
                        )

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsS1J1GB, 
                            'r', 
                            label="s=0.05")
                        )

    resultsToPlot.append(plotFunctions.ResultsGraficAttributes(
                            resultsS2J1GB, 
                            'b', 
                            label="s=0.01")                          
                        )

    
    graficInfo = plotFunctions.GraficAttributes(
                            imagSizeX = 7, 
                            imagSizeY = 5, 
                            xLabel = 'Size parameter x', 
                            yLabel = 'Asymmetry Factor $J_1(x)$', 
                )
    
    
    plotFunctions.PlotGraphic (resultsToPlot,
                                graficInfo,
                                xValues=x,
                                legend=True
                                )


def testAllJ1Gaussian(returnTimeBool):
    
    print("--------- Test 1: Gauss x PW to 3 particles ----------")
    testJ1GaussianBeamWithJ1PlaneWave(returnTimeBool)
    
    print("--------- Test 2: Gauss x PW varying s value to x = [3,8] and m = 1.57 - 0.038j ----------")
    testJ1GaussianWithPlaneWaveVaryingSValue(returnTimeBool)

    print("--------- Test 3: Gauss varying z0 values to different s and x values. NOTE.. are 3 graphics ----------")
    testJ1GaussianVaryingSAndZ0AndXValues(returnTimeBool)

    print("--------- Test 4: Gauss x PW varying x value to s = [0.1, 0.05, 0.01] ----------")
    testJ1GaussianWithPlaneWaveVaryingXValue(returnTimeBool)


if __name__ == '__main__':
    print("We have these tests.")
    print("1 - testJ1GaussianBeamWithJ1PlaneWave")
    print("2 - testJ1GaussianWithPlaneWaveVaryingSValue")
    print("3 - testJ1GaussianVaryingSAndZ0AndXValues")
    print("4 - testJ1GaussianWithPlaneWaveVaryingXValue")
    print("5 - All")

    numberTest = input("Which will execute? Please write the number: ")
    returnTime = input("Return runtime? (y/n): ")
   
    switchRunTime = {
        "y": True,
        "n": False,
    }
    
    returnTimeBool = switchRunTime.get(returnTime)
    
    switchFuncsTest = {
        "1": partial(testJ1GaussianBeamWithJ1PlaneWave, returnTimeBool),
        "2": partial(testJ1GaussianWithPlaneWaveVaryingSValue, returnTimeBool),
        "3": partial(testJ1GaussianVaryingSAndZ0AndXValues, returnTimeBool),
        "4": partial(testJ1GaussianWithPlaneWaveVaryingXValue, returnTimeBool),
        "5": partial(testAllJ1Gaussian, returnTimeBool)
    }

    case = switchFuncsTest.get(numberTest)
    case()
