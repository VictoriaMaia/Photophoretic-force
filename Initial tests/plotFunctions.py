import matplotlib.pyplot as plt

color = ['g', 'r', 'b', 'c', 'm', 'y']

def PlotGraphic (n, title, variable, results, z, yLowerLimit, yUpperLimit) :
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
