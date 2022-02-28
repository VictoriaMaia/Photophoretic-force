import sys
sys.path.append('./')
from asymmetryFactorJ1.variables import cn as CN
from asymmetryFactorJ1.variables import dn as DN
import numpy as np
import matplotlib.pyplot as plt
import plotFunctions 

color = ['g', 'r', 'b', 'c', 'm', 'y']

def testVarCAndD():
    linha = 6
    coluna = 2
    position = 1
    n = [1, 5, 10, 20, 40, 60]
    u_r = 1
    m = 1.57 - 0.038j
    x = np.linspace(0.01, 20, 200)

    for i in range(len(n)):
        cn = CN.Cn(u_r, m, x, n[i])
        dn = DN.Dn(u_r, m, x, n[i])
        labelStr = 'n='+ str(n[i])

        plt.subplot(linha, coluna, position)
        plt.plot(x, abs(cn), color[i], label=labelStr)
        plt.xlabel('x')
        plt.ylabel('|c_n|')
        plt.ylim(-1, 3)
        plt.legend(loc='best')
        plt.grid()
        
        plt.subplot(linha, coluna, position+1)
        plt.plot(x, abs(dn), color[i], label=labelStr)
        plt.xlabel('x')
        plt.ylabel('|d_n|')
        plt.ylim(-1, 3)
        plt.legend(loc='best')
        plt.grid()
        
        position = position + 2

    plt.show()


def testVarC():
    u_r = 1
    m = 1.57 - 0.038j
    x = 20 # x = ka

    n = list(range(1, 61))

    results = []

    for i in n:
        cn = CN.Cn(u_r, m, x, i)
        results.append(abs(cn))

    plotFunctions.PlotOneGraphic ('|c_n| x n', "", 'b.', results, n, -0.02, 0.73, 'n', '|c_n|')
    plotFunctions.PlotOneGraphic ('|c_n| x n', "", 'b', results, n, -0.02, 0.73, 'n', '|c_n|')

if __name__ == '__main__':
    testVarCAndD()
    testVarC()