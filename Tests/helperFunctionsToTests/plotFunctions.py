from cProfile import label
import matplotlib.pyplot as plt
import matplotlib as mpl

color = ['g', 'r', 'b', 'c', 'm', 'y']

def PlotGraphicMath (n, title, variable, results, z, yLowerLimit, yUpperLimit) :
    plt.figure(figsize=[10,5])
    for i in n:
        labelStr = variable + '_'+ str(i) + '(x)'
        plt.plot(z, results[i], color[i], label=labelStr)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(yLowerLimit, yUpperLimit)
    plt.legend(loc='best')
    plt.grid()
    plt.show()
    
def PlotGraphicRealAndImageParts (title, labelInput, color, results, z, yLowerLimit, yUpperLimit) :
    plt.figure(figsize=[10,5])
    plt.plot(z, results.real, color, label=labelInput+' (real)')
    plt.plot(z, results.imag, color+'-.', label=labelInput+' (imag)')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(yLowerLimit, yUpperLimit)
    plt.legend(loc='best')
    plt.grid()
    plt.show()

def PlotGraphicRealAndImagePartsMpmath (title, labelInput, color, resultsReal, resultsImag, z, yLowerLimit, yUpperLimit):
    plt.figure(figsize=[10,5])
    plt.plot(z, resultsReal, color, label=labelInput+' (real)')
    plt.plot(z, resultsImag, color+'-.', label=labelInput+' (imag)')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(yLowerLimit, yUpperLimit)
    plt.legend(loc='best')
    plt.grid()
    plt.show()
    
def PlotOneGraphic (title, labelInput, color, results, z, yLowerLimit, yUpperLimit, xLabel='x', yLabel='y'):
    plt.figure(figsize=[10,5])
    plt.plot(z, results, color, label=labelInput)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.ylim(yLowerLimit, yUpperLimit)
    plt.legend(loc='best')
    plt.grid()
    plt.show()


class ResultsGraficAttributes:
    def __init__(self, results, color, xLocText=0, yLocText=0, messageText="", label="") -> None:
        self.results = results
        self.color = color
        self.label = label
        self.xLocText = xLocText
        self.yLocText = yLocText
        self.messageText = messageText
        pass

class GraficAttributes:
    def __init__(self, imagSizeX, imagSizeY, xLabel, yLabel, title="", yLowerLimit=0, yUpperLimit=0, xLowerLimit=0, xUpperLimit=0 ) -> None:
        self.imagSizeX = imagSizeX
        self.imagSizeY = imagSizeY
        self.title = title
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.yLowerLimit = yLowerLimit
        self.yUpperLimit = yUpperLimit
        self.xLowerLimit = xLowerLimit
        self.xUpperLimit = xUpperLimit
        pass


def PlotGraphic (resultsToPlot,
                 graficInfo,
                 xValues,
                 latex=True,
                 ylimit=False, 
                 xlimit=False,
                 text=False,
                 legend=False,
                 saveFig=False
                 ):

    if len(resultsToPlot) == 0:
        print("Error. Don't have grafics to plot")
        return 

    for i in resultsToPlot:
        if type(i) != ResultsGraficAttributes:
            print("Error: parameters is not of type class ResultsGraficAttributes. Type returned: ", type(resultsToPlot))
            return 0
    
    if type(graficInfo) != GraficAttributes:
        print("Error: parameters is not of type class GraficAttributes. Type returned: ", type(graficInfo))
        return 0
        
    
    plt.figure(figsize=[graficInfo.imagSizeX, graficInfo.imagSizeY])
    mpl.rcParams["text.usetex"] = latex

    for i in resultsToPlot:
        if i.label != "":
            plt.plot(xValues, i.results, i.color, label=i.label)            
        else:
            plt.plot(xValues, i.results, i.color)
    
    plt.title(graficInfo.title)
    plt.xlabel(graficInfo.xLabel)
    plt.ylabel(graficInfo.yLabel)

    if legend:
        plt.legend(loc='best')
    
    if ylimit:
        plt.ylim(graficInfo.yLowerLimit, graficInfo.yUpperLimit)

    if xlimit:
        plt.xlim(graficInfo.xLowerLimit, graficInfo.xUpperLimit)

    if saveFig:
        plt.savefig(graficInfo.title+".png", format='png', dpi=500)
    
    if text:
        for i in resultsToPlot:
            plt.text(i.xLocText, i.yLocText, i.messageText)

    plt.grid()
    plt.show()



