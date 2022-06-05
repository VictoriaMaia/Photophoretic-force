from functools import partial
from timeit import default_timer as timer

import sys
sys.path.append('./')

from asymmetryFactorJ1 import *
from Tests.helperFunctionsToTests import plotFunctions
import asymmetryFactorJ1.structures.j1_parameters as s

import numpy as np


mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)


def test_j1_value():
    m = 1.57 - 0.038j
    x = 10
    ur = 1

    result_j1_expected = 0.054413290391591596
    result_j1_current = j1(s.J1Attributes(x, m, ur))

    if result_j1_current != result_j1_expected:
        print("The J1 result is wrong!!")
        print("Expected: ", result_j1_expected)
        print("Current: ", result_j1_current)
    else:
        print("The J1 result is correct!!")
    

def test_j1_for_3_particles(return_time_bool):
    m_blue = 1.57 - 0.038j
    m_red = 1.57 - 0.19j
    m_black = 1.57 - 0.95j

    x = np.linspace(0.01, 20, 200)

    ur = 1

    results_blue = []
    results_red = []
    results_black = []

    start = timer()
    for i in x:
        results_blue.append(j1(s.J1Attributes(i, m_blue, ur)))
        results_red.append(j1(s.J1Attributes(i, m_red, ur)))
        results_black.append(j1(s.J1Attributes(i, m_black, ur)))
    time = timer()-start
    
    if return_time_bool:
        print(time)
    
    results_to_plot = [plotFunctions.ResultsGraphicAttributes(
                            results_blue,
                            'b',
                            x_loc_text=12.5,
                            y_loc_text=.03,
                            message_text="M = 1.57 - i0.038"),
                       plotFunctions.ResultsGraphicAttributes(
                            results_red,
                            'r-.',
                            x_loc_text=9,
                            y_loc_text=-0.2,
                            message_text="M = 1.57 - i0.19"),
                       plotFunctions.ResultsGraphicAttributes(
                            results_black,
                            'k--',
                            x_loc_text=7.5,
                            y_loc_text=-.33,
                            message_text="M = 1.57 - i0.95")]

    graph_info = plotFunctions.GraphicAttributes(
                            image_size_x=7,
                            image_size_y=5,
                            x_label='Size Parameter x',
                            y_label='Asymmetry Factor $J_1(x)$', )

    plotFunctions.plot_graphic(results_to_plot,
                               graph_info,
                               x,
                               text=True,)


def test_j1_fig_1_mackowski(return_time_bool):
    m = 1.57 - 0.038j
    x = np.linspace(0.01, 20, 200)
    ur = 1
    results = []
    r_zeros = []
    start = timer()
    for i in x:
        results.append(j1(s.J1Attributes(i, m, ur)))
        r_zeros.append(0)
    time = timer()-start
    
    if return_time_bool:
        print(time)

    plotFunctions.plot_one_graphic("", "Eqn (62)", 'g', results, x, -0.10, 0.15,
                                   x_label='Size Parameter x', y_label='Asymmetry Factor J1')


def test_j1_fig_2_mackowski():
    m = 1.57 - 0.38j
    x = np.linspace(0.01, 20, 200)
    ur = 1
    results = []

    for i in x:
        results.append(j1(s.J1Attributes(i, m, ur)))

    results_to_plot = [plotFunctions.ResultsGraphicAttributes(
                        results, 
                        'g')]

    graph_info = plotFunctions.GraphicAttributes(
                            image_size_x=7,
                            image_size_y=5,
                            x_label='Size Parameter x',
                            y_label='Asymmetry Factor $J_1(x)$',
                            y_lower_limit=-0.50, 
                            y_upper_limit=0.01, 
                            x_lower_limit=0, 
                            x_upper_limit=20)

    plotFunctions.plot_graphic(results_to_plot,
                               graph_info,
                               x,
                               y_limit=True,
                               x_limit=True,)
  

def test_all_j1(return_time_bool):
    
    print("--------- Test 1: J1 value to m = 1.57 - 0.038j ----------")
    test_j1_value()
    
    print("--------- Test 2: J1 for 3 particles ----------")
    test_j1_for_3_particles(return_time_bool)

    print("--------- Test 3: J1 Fig 1 ----------")
    test_j1_fig_1_mackowski(return_time_bool)

    print("--------- Test 4: J1 Fig 2----------")
    test_j1_fig_2_mackowski()


if __name__ == '__main__':
    print("We have these tests.")
    print("1 - testJ1Value")
    print("2 - test_j1_for_3_particles")
    print("3 - test_j1_fig_1_mackowski")
    print("4 - test_j1_fig_2_mackowski")
    print("5 - All")

    numberTest = input("Which will execute? Please write the number: ")
    returnTime = input("Return runtime? (y/n): ")

    # sys.argv[1]
    switchRunTime = {
        "y": True,
        "n": False,
    }
    
    return_time_boolean = switchRunTime.get(returnTime)
    
    switchFuncsTest = {
        "1": test_j1_value,
        "2": partial(test_j1_for_3_particles, return_time_boolean),
        "3": partial(test_j1_fig_1_mackowski, return_time_boolean),
        "4": test_j1_fig_2_mackowski,
        "5": partial(test_all_j1, return_time_boolean)
    }

    case = switchFuncsTest.get(numberTest)
    case()
