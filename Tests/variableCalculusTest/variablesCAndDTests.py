import sys
sys.path.append('./')
from asymmetryFactorJ1.variables import cn as pack_cn
from asymmetryFactorJ1.variables import dn as pack_dn
from Tests.helperFunctionsToTests import plotFunctions
import numpy as np
import matplotlib.pyplot as plt

color = ['g', 'r', 'b', 'c', 'm', 'y']


def test_var_c_and_d():
    row = 6
    column = 2
    position = 1
    n = [1, 5, 10, 20, 40, 60]
    u_r = 1
    m = 1.57 - 0.038j
    x = np.linspace(0.01, 20, 200)

    for i in range(len(n)):
        cn = pack_cn.Cn(u_r, m, x, n[i])
        dn = pack_dn.Dn(u_r, m, x, n[i])
        label_str = 'n='+str(n[i])

        plt.subplot(row, column, position)
        plt.plot(x, abs(cn), color[i], label=label_str)
        plt.xlabel('x')
        plt.ylabel('|c_n|')
        plt.ylim(-1, 3)
        plt.legend(loc='best')
        plt.grid()
        
        plt.subplot(row, column, position+1)
        plt.plot(x, abs(dn), color[i], label=label_str)
        plt.xlabel('x')
        plt.ylabel('|d_n|')
        plt.ylim(-1, 3)
        plt.legend(loc='best')
        plt.grid()
        
        position = position + 2

    plt.show()


def test_var_c():
    u_r = 1
    m = 1.57 - 0.038j
    x = 20 # x = ka

    n = list(range(1, 61))

    results = []

    for i in n:
        cn = pack_cn.Cn(u_r, m, x, i)
        results.append(abs(cn))

    plotFunctions.plot_one_graphic('|c_n| x n', " ", 'b.', results, n, -0.02, 0.73, 'n', '|c_n|')
    plotFunctions.plot_one_graphic('|c_n| x n', " ", 'b', results, n, -0.02, 0.73, 'n', '|c_n|')


if __name__ == '__main__':
    test_var_c_and_d()
    test_var_c()
    