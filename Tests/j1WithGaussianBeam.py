from tqdm import tqdm
from functools import partial
from timeit import default_timer as timer

import sys
sys.path.append('./')

from asymmetryFactorJ1 import *
from Tests.helperFunctionsToTests import plotFunctions, timeConvert
import asymmetryFactorJ1.gaussianBeam.gauss_parameters as gs
import asymmetryFactorJ1.structures.j1_parameters as sj

import math
import numpy as np
import matplotlib.pyplot as plt

mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)
orange = '#ff6800'


# yLabel = J1
# xLabel = x [0.01 to 20]
# To:
# m =[1.57 - 0.038j,
#     1.57 - 0.19j,
#     1.57 - 0.95j ]
def test_j1_gaussian_beam_with_j1_plane_wave(return_time_bool):
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    z0 = 0
    s = 0.1
    ur = 1 
    m_blue = 1.57 - 0.038j
    m_red = 1.57 - 0.19j
    m_black = 1.57 - 0.95j

    x = np.linspace(0.01, 20, 300)

    results_blue_j1_gb = []
    results_red_j1_gb = []
    results_black_j1_gb = []
    results_blue_j1 = []
    results_red_j1 = []
    results_black_j1 = []

    total_time = 0
    pbar = tqdm(colour=orange, total=len(x), desc="Test 1. Calculating")

    for i in x:
        time_begin = timer()

        results_blue_j1_gb.append(j1(gs.J1Gauss(i, m_blue, ur, k, z0, s)))
        results_red_j1_gb.append(j1(gs.J1Gauss(i, m_red, ur, k, z0, s)))
        results_black_j1_gb.append(j1(gs.J1Gauss(i, m_black, ur, k, z0, s)))
        results_blue_j1.append(j1(sj.J1Attributes(i, m_blue, ur)))
        results_red_j1.append(j1(sj.J1Attributes(i, m_red, ur)))
        results_black_j1.append(j1(sj.J1Attributes(i, m_black, ur)))

        time_end = timer()
        total_time += time_end - time_begin
        pbar.update()

    pbar.refresh()
    pbar.close()
    
    if return_time_bool:
        timeConvert.convert_time_to_more_readable(total_time)

    results_to_plot = [plotFunctions.ResultsGraphicAttributes(
                            results_blue_j1_gb, 
                            'b', 
                            label="GB",
                            x_loc_text=12.5, 
                            y_loc_text=.03, 
                            message_text="M = 1.57 - i0.038"),
                       plotFunctions.ResultsGraphicAttributes(
                            results_blue_j1, 
                            'b-.', 
                            label="OP ($g_n$ = 1)"),
                       plotFunctions.ResultsGraphicAttributes(
                            results_red_j1, 
                            'r-.', 
                            label="OP"),
                       plotFunctions.ResultsGraphicAttributes(
                            results_black_j1, 
                            'g-.', 
                            label="OP"),
                       plotFunctions.ResultsGraphicAttributes(
                            results_red_j1_gb, 
                            'r', 
                            label="GB",
                            x_loc_text=10, 
                            y_loc_text=-0.1, 
                            message_text="M = 1.57 - i0.19"),
                       plotFunctions.ResultsGraphicAttributes(
                            results_black_j1_gb, 
                            'g', 
                            label="GB",
                            x_loc_text=7.5, 
                            y_loc_text=-.33, 
                            message_text="M = 1.57 - i0.95")]

    graphic_info = plotFunctions.GraphicAttributes(
                            image_size_x=7,
                            image_size_y=5,
                            x_label='Size Parameter x',
                            y_label='Asymmetry Factor $J_1(x)$')
    
    plotFunctions.plot_graphic(results_to_plot,
                               graphic_info,
                               x,
                               text=True)


# yLabel = J1
# xLabel = s [0.01 to 0.16]
# To:
#    m = 1.57 - 0.038j
#    x = [3, 8]
def test_j1_gaussian_with_plane_wave_varying_s__value(return_time_bool):
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    z0 = 0
    ur = 1
    m = 1.57 - 0.038j
    x3 = 3
    x8 = 8

    s = np.linspace(0.01, 0.16, 300)

    results_x3_j1_gb = []
    results_x8_j1_gb = []
    results_x3_j1 = []
    results_x8_j1 = []

    total_time = 0
    pbar = tqdm(colour=orange, total=len(s), desc="Test 2. Calculating")

    for i in s:
        time_begin = timer()

        results_x3_j1_gb.append(j1(gs.J1Gauss(x3, m, ur, k, z0, i)))
        results_x8_j1_gb.append(j1(gs.J1Gauss(x8, m, ur, k, z0, i)))
        results_x3_j1.append(j1(sj.J1Attributes(x3, m, ur)))
        results_x8_j1.append(j1(sj.J1Attributes(x8, m, ur)))
       
        time_end = timer()
        total_time += time_end - time_begin
        pbar.update()

    pbar.refresh()
    pbar.close()
    
    if return_time_bool:
        timeConvert.convert_time_to_more_readable(total_time)

    results_to_plot = [plotFunctions.ResultsGraphicAttributes(
                            results_x3_j1_gb, 
                            'k', 
                            label="GB",
                            x_loc_text=0.1, 
                            y_loc_text=.045, 
                            message_text="x=3"
                            ),
                       plotFunctions.ResultsGraphicAttributes(
                            results_x3_j1, 
                            'k-.', 
                            label="OP ($g_n$ = 1)"),
                       plotFunctions.ResultsGraphicAttributes(
                            results_x8_j1_gb, 
                            'b', 
                            label="GB",
                            x_loc_text=0.06, 
                            y_loc_text=.02, 
                            message_text="x=8"),
                       plotFunctions.ResultsGraphicAttributes(
                            results_x8_j1, 
                            'b-.', 
                            label="OP")]

    graphic_info = plotFunctions.GraphicAttributes(
                            image_size_x=7,
                            image_size_y=5,
                            x_label='Confinement factor s',
                            y_label='Asymmetry Factor $J_1(x)$')

    plotFunctions.plot_graphic(results_to_plot,
                               graphic_info,
                               s,
                               text=True)


# yLabel = J1
# xLabel = z0fig1 [-15mili to 15mili]
#          z0fig2 [-150mili to 150mili]
#          z0fig3 [-60mili to 60mili]
# To:
    # m = 1.57 - 0.038j
    # s = [0.01, 0.10, 0.16]
    # x = [0.1, 3, 8]
def test_j1_gaussian_varying_s_and_z0_and_x_values(return_time_bool):
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    ur = 1
    m = 1.57 - 0.038j

    s = [0.01, 0.10, 0.16]
    
    x1 = 0.1
    x3 = 3
    x8 = 8

    qnt_points = 300
    
    z0fig1 = np.linspace(-15*mili, 15*mili, qnt_points)
    z0fig2 = np.linspace(-150*micro, 150*micro, qnt_points)
    z0fig3 = np.linspace(-60*micro, 60*micro, qnt_points)

    results_x1_s001 = []
    results_x3_s001 = []
    results_x8_s001 = []

    results_x1_s01 = []
    results_x3_s01 = []
    results_x8_s01 = []

    results_x1_s016 = []
    results_x3_s016 = []
    results_x8_s016 = []

    total_time = 0
    pbar1 = tqdm(colour=orange, total=len(z0fig1), desc="Test 3.1. Calculating")
    
    for i in z0fig1:
        time_begin = timer()

        results_x1_s001.append(j1(gs.J1Gauss(x1, m, ur, k, i, s[0]))*10000)
        results_x3_s001.append(j1(gs.J1Gauss(x3, m, ur, k, i, s[0])))
        results_x8_s001.append(j1(gs.J1Gauss(x8, m, ur, k, i, s[0])))
        
        time_end = timer()
        total_time += time_end - time_begin
        pbar1.update()

    pbar1.close()

    if return_time_bool:
        timeConvert.convert_time_to_more_readable(total_time)

    total_time = 0
    pbar2 = tqdm(colour=orange, total=len(z0fig2), desc="Test 3.2. Calculating")

    for i in z0fig2:
        time_begin = timer()

        results_x1_s01.append(j1(gs.J1Gauss(x1, m, ur, k, i, s[1]))*5000)
        results_x3_s01.append(j1(gs.J1Gauss(x3, m, ur, k, i, s[1])))
        results_x8_s01.append(j1(gs.J1Gauss(x8, m, ur, k, i, s[1])))
     
        time_end = timer()
        total_time += time_end - time_begin
        pbar2.update()

    pbar2.close()

    if return_time_bool:
        timeConvert.convert_time_to_more_readable(total_time)

    total_time = 0
    pbar3 = tqdm(colour=orange, total=len(z0fig3), desc="Test 3.3. Calculating")
    
    for i in z0fig3:
        time_begin = timer()

        results_x1_s016.append(j1(gs.J1Gauss(x1, m, ur, k, i, s[2]))*1000)
        results_x3_s016.append(j1(gs.J1Gauss(x3, m, ur, k, i, s[2])))
        results_x8_s016.append(j1(gs.J1Gauss(x8, m, ur, k, i, s[2])))
        
        time_end = timer()
        total_time += time_end - time_begin
        pbar3.update()
    
    pbar3.close()
    
    if return_time_bool:
        timeConvert.convert_time_to_more_readable(total_time)

    z0fig1 = np.linspace(-15, 15, qnt_points)
    z0fig2 = np.linspace(-150, 150, qnt_points)
    z0fig3 = np.linspace(-60, 60, qnt_points)

    fig, (fig1, fig2, fig3) = plt.subplots(1, 3, figsize=(17, 5))

    fig1.plot(z0fig1, results_x1_s001, 'b', label="x = 0.1 * 10000 ")
    fig1.plot(z0fig1, results_x3_s001, 'r', label="x = 3")
    fig1.plot(z0fig1, results_x8_s001, 'g', label="x = 8")
    fig1.grid(True)
    fig1.set_xlabel('Relative position $z_0$ (mm)')
    fig1.set_ylabel('Asymmetry Factor J1')
    fig1.text(4.5, .085, '$x=8$')
    fig1.text(0, .055, '$x=3$')
    fig1.text(0, -.02, '$x=0.1*(10^4)$')

    fig2.plot(z0fig2, results_x1_s01, 'b', label="x = 0.1 * 5000 ")
    fig2.plot(z0fig2, results_x3_s01, 'r', label="x = 3")
    fig2.plot(z0fig2, results_x8_s01, 'g', label="x = 8")
    fig2.grid(True)
    fig2.set_xlabel('Relative position $z_0$ ($\mu_m$)')
    fig2.set_ylabel('Asymmetry Factor J1')
    fig2.text(-15, .011, '$x=8$')
    fig2.text(0, .04, '$x=3$')
    fig2.text(-60, -.01, '$x=0.1*5000$')

    fig3.plot(z0fig3, results_x1_s016, 'b', label="x = 0.1 * 1000 ")
    fig3.plot(z0fig3, results_x3_s016, 'r', label="x = 3")
    fig3.plot(z0fig3, results_x8_s016, 'g', label="x = 8")
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
def test_j1_gaussian_with_plane_wave_varying_x_value(return_time_bool):
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    z0 = 0
    m = 1.57 - 0.038j

    x = np.linspace(20, 100, 300)
    ur = 1

    results_s0_j1_gb = []
    results_s1_j1_gb = []
    results_s2_j1_gb = []
    results_j1 = []

    total_time = 0
    pbar = tqdm(colour=orange, total=len(x), desc="Test 4. Calculating")

    for i in x:
        time_begin = timer()

        results_s0_j1_gb.append(j1(gs.J1Gauss(i, m, ur, k, z0, 0.1)))
        results_s1_j1_gb.append(j1(gs.J1Gauss(i,  m, ur, k, z0, 0.05)))
        results_s2_j1_gb.append(j1(gs.J1Gauss(i,  m, ur, k, z0, 0.01)))
        results_j1.append(j1(sj.J1Attributes(i, m, ur)))

        time_end = timer()
        total_time += time_end - time_begin
        pbar.update()

    pbar.refresh()
    pbar.close()

    if return_time_bool:
        timeConvert.convert_time_to_more_readable(total_time)

    results_to_plot = [plotFunctions.ResultsGraphicAttributes(
                            results_j1, 
                            'k-.', 
                            label="OP"),
                       plotFunctions.ResultsGraphicAttributes(
                            results_s0_j1_gb, 
                            'g', 
                            label="s=0.1"),
                       plotFunctions.ResultsGraphicAttributes(
                            results_s1_j1_gb, 
                            'r', 
                            label="s=0.05"),
                       plotFunctions.ResultsGraphicAttributes(
                            results_s2_j1_gb, 
                            'b', 
                            label="s=0.01")]

    graphic_info = plotFunctions.GraphicAttributes(
                            image_size_x=7,
                            image_size_y=5,
                            x_label='Size parameter x',
                            y_label='Asymmetry Factor $J_1(x)$',
                )

    plotFunctions.plot_graphic(results_to_plot,
                               graphic_info,
                               x_values=x,
                               legend=True
                               )


def test_all_j1_gaussian(return_time_bool):
    
    print("--------- Test 1: Gauss x PW to 3 particles ----------")
    test_j1_gaussian_beam_with_j1_plane_wave(return_time_bool)
    
    print("--------- Test 2: Gauss x PW varying s value to x = [3,8] and m = 1.57 - 0.038j ----------")
    test_j1_gaussian_with_plane_wave_varying_s__value(return_time_bool)

    print("--------- Test 3: Gauss varying z0 values to different s and x values. NOTE.. are 3 graphics ----------")
    test_j1_gaussian_varying_s_and_z0_and_x_values(return_time_bool)

    print("--------- Test 4: Gauss x PW varying x value to s = [0.1, 0.05, 0.01] ----------")
    test_j1_gaussian_with_plane_wave_varying_x_value(return_time_bool)


if __name__ == '__main__':
    print("We have these tests.")
    print("1 - test_j1_gaussian_beam_with_j1_plane_wave")
    print("2 - test_j1_gaussian_with_plane_wave_varying_s__value")
    print("3 - test_j1_gaussian_varying_s_and_z0_and_x_values")
    print("4 - test_j1_gaussian_with_plane_wave_varying_x_value")
    print("5 - All")

    numberTest = input("Which will execute? Please write the number: ")
    returnTime = input("Return runtime? (y/n): ")
   
    switchRunTime = {
        "y": True,
        "n": False,
    }
    
    return_time_boolean = switchRunTime.get(returnTime)
    
    switchFuncsTest = {
        "1": partial(test_j1_gaussian_beam_with_j1_plane_wave, return_time_boolean),
        "2": partial(test_j1_gaussian_with_plane_wave_varying_s__value, return_time_boolean),
        "3": partial(test_j1_gaussian_varying_s_and_z0_and_x_values, return_time_boolean),
        "4": partial(test_j1_gaussian_with_plane_wave_varying_x_value, return_time_boolean),
        "5": partial(test_all_j1_gaussian, return_time_boolean)
    }

    case = switchFuncsTest.get(numberTest)
    case()
