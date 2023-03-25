import sys
sys.path.append('./')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.gaussian.gaussian_class import GaussAttributes
from AsymmetryFactor.beams.beam_class import BeamAttributes
from AsymmetryFactor.j1 import j1
from simulations.create_graph import plot_graphic
from simulations.time_operations import *
from timeit import default_timer as timer
from functools import partial
from tqdm import tqdm
import numpy as np
import math

mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)
orange = '#ff6800'

calculate_average = False
max_executions = 10
qnt_points = 300



def j1_gaussian_beam_with_three_particles():
    var_lambda = 10.63 * micro
        
    ur = 1
    x = np.linspace(0.01, 20, qnt_points)

    k = (2*math.pi) / var_lambda
    z0 = 0
    s = 0.1
    gauss_b = GaussAttributes(k, z0, s)

    m_038 = 1.57 - 0.038j
    m_019 = 1.57 - 0.19j
    m_095 = 1.57 - 0.95j

    results_038 = []
    results_019 = []
    results_095 = []

    if calculate_average:
        total_time = 0
        
        pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
        for i in range(max_executions):            
            start = timer()
            
            for i in x:
                results_038.append(j1(ParticleAttributes(i, m_038, ur), gauss_b))
                results_019.append(j1(ParticleAttributes(i, m_019, ur), gauss_b))
                results_095.append(j1(ParticleAttributes(i, m_095, ur), gauss_b))
            
            total_time += timer()-start
            pbar.update()
    
        pbar.refresh()
        pbar.close()  
        average = total_time/max_executions      
        print(average)  
    
        print("Total time: ", end="")
        convert_time_to_more_readable(average)

    else:

        for i in x:
            results_038.append(j1(ParticleAttributes(i, m_038, ur), gauss_b))
            results_019.append(j1(ParticleAttributes(i, m_019, ur), gauss_b))
            results_095.append(j1(ParticleAttributes(i, m_095, ur), gauss_b))

        results = [results_038, results_019, results_095]
        x_label = "Size Parameter x"
        y_label = "Asymmetry Factor $J_1(x)$"
        legend = ["M = 1.57 - i0.038", "M = 1.57 - i0.19", "M = 1.57 - i0.95"]

        plot_graphic(results, x, x_label, y_label, legend)
    

def j1_gaussian_beam_with_varing_s_values():
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    z0 = 0
    s = np.linspace(0.01, 0.16, qnt_points)
        
    ur = 1
    x3 = 3
    x8 = 8
    m_038 = 1.57 - 0.038j

    particle_x3 = ParticleAttributes(x3, m_038, ur)
    particle_x8 = ParticleAttributes(x8, m_038, ur)

    results_x3 = []
    results_x8 = []

    # start = timer()
    for i in s:
        results_x3.append(j1(particle_x3, GaussAttributes(k, z0, i)))
        results_x8.append(j1(particle_x8, GaussAttributes(k, z0, i)))
    # time = timer()-start

    # print("time: ", time)

    results = [results_x3, results_x8]
    x_label = "Confinement factor s"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["x=3", "x=8"]

    plot_graphic(results, s, x_label, y_label, legend)
    

def j1_gaussian_beam_with_varing_z0_values_s_001():
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    s = 0.01
    z0 = np.linspace(-15*mili, 15*mili, qnt_points)


    ur = 1
    
    x01 = 0.1
    x3 = 3
    x8 = 8
    m_038 = 1.57 - 0.038j

    particle_x01 = ParticleAttributes(x01, m_038, ur)
    particle_x3 = ParticleAttributes(x3, m_038, ur)
    particle_x8 = ParticleAttributes(x8, m_038, ur)

    results_x01 = []
    results_x3 = []
    results_x8 = []

    # start = timer()
    for i in z0:
        results_x01.append(j1(particle_x01, GaussAttributes(k, i, s))*10000)
        results_x3.append(j1(particle_x3, GaussAttributes(k, i, s)))
        results_x8.append(j1(particle_x8, GaussAttributes(k, i, s)))
    # time = timer()-start

    # print("time: ", time)

    z0 = np.linspace(-15, 15, qnt_points)
    
    results = [results_x01, results_x3, results_x8]
    x_label = "Relative position $z_0$ (mm)"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["x = 0.1*10000", "x = 3", "x = 8"]

    plot_graphic(results, z0, x_label, y_label, legend)
    

def j1_gaussian_beam_with_varing_z0_values_s_010():
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    s = 0.10
    z0 = np.linspace(-150*micro, 150*micro, qnt_points)


    ur = 1
    
    x01 = 0.1
    x3 = 3
    x8 = 8
    m_038 = 1.57 - 0.038j

    particle_x01 = ParticleAttributes(x01, m_038, ur)
    particle_x3 = ParticleAttributes(x3, m_038, ur)
    particle_x8 = ParticleAttributes(x8, m_038, ur)

    results_x01 = []
    results_x3 = []
    results_x8 = []

    # start = timer()
    for i in z0:
        results_x01.append(j1(particle_x01, GaussAttributes(k, i, s))*5000)
        results_x3.append(j1(particle_x3, GaussAttributes(k, i, s)))
        results_x8.append(j1(particle_x8, GaussAttributes(k, i, s)))
    # time = timer()-start

    # print("time: ", time)

    z0 = np.linspace(-150, 150, qnt_points)
    
    results = [results_x01, results_x3, results_x8]
    x_label = "Relative position $z_0$ ($\mu_m$)"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["x = 0.1*5000", "x = 3", "x = 8"]

    plot_graphic(results, z0, x_label, y_label, legend)
   

def j1_gaussian_beam_with_varing_z0_values_s_016():
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    s = 0.16
    z0 = np.linspace(-60*micro, 60*micro, qnt_points)


    ur = 1
    
    x01 = 0.1
    x3 = 3
    x8 = 8
    m_038 = 1.57 - 0.038j

    particle_x01 = ParticleAttributes(x01, m_038, ur)
    particle_x3 = ParticleAttributes(x3, m_038, ur)
    particle_x8 = ParticleAttributes(x8, m_038, ur)

    results_x01 = []
    results_x3 = []
    results_x8 = []

    # start = timer()
    for i in z0:
        results_x01.append(j1(particle_x01, GaussAttributes(k, i, s))*1000)
        results_x3.append(j1(particle_x3, GaussAttributes(k, i, s)))
        results_x8.append(j1(particle_x8, GaussAttributes(k, i, s)))
    # time = timer()-start

    # print("time: ", time)

    z0 = np.linspace(-60, 60, qnt_points)
    
    results = [results_x01, results_x3, results_x8]
    x_label = "Relative position $z_0$ ($\mu_m$)"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["x = 0.1*1000", "x = 3", "x = 8"]

    plot_graphic(results, z0, x_label, y_label, legend)
   

def j1_gaussian_beam_with_varing_x_values():
    print(calculate_average)
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    s01 = 0.1
    s005 = 0.05
    s001 = 0.01
    z0 = 0

    gauss_b_s01 = GaussAttributes(k, z0, s01)
    gauss_b_s005 = GaussAttributes(k, z0, s005)
    gauss_b_s001 = GaussAttributes(k, z0, s001)
    pw = BeamAttributes()

    ur = 1
    x = np.linspace(20, 100, qnt_points)
    m_038 = 1.57 - 0.038j


    results_s01 = []
    results_s005 = []
    results_s001 = []
    results_pw = []

    # start = timer()
    for i in x:
        results_s01.append(j1(ParticleAttributes(i, m_038, ur), gauss_b_s01))
        results_s005.append(j1(ParticleAttributes(i, m_038, ur), gauss_b_s005))
        results_s001.append(j1(ParticleAttributes(i, m_038, ur), gauss_b_s001))
        results_pw.append(j1(ParticleAttributes(i, m_038, ur), pw))
    # time = timer()-start

    # print("time: ", time)
    
    results = [results_s01, results_s005, results_s001, results_pw]
    x_label = "Size parameter x"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["s = 0.1", "s = 0.05", "s = 0.01", "plane wave"]

    plot_graphic(results, x, x_label, y_label, legend)
   


def all_j1_gaussian_beam_simulations(return_time_bool):
    
    print("--------- Simulation 1: Gauss to 3 particles ----------")
    j1_gaussian_beam_with_three_particles(return_time_bool)
    
    print("--------- Simulation 2: Gauss varying s value to x = [3,8] and m = 1.57 - 0.038j ----------")
    j1_gaussian_beam_with_varing_s_values(return_time_bool)

    print("--------- Simulation 3: Gauss varying z0 values to different x values with s=0.01 ----------")
    j1_gaussian_beam_with_varing_z0_values_s_001(return_time_bool)

    print("--------- Simulation 3: Gauss varying z0 values to different x values with s=0.10 ----------")
    j1_gaussian_beam_with_varing_z0_values_s_010(return_time_bool)

    print("--------- Simulation 3: Gauss varying z0 values to different x values with s=0.16 ----------")
    j1_gaussian_beam_with_varing_z0_values_s_016(return_time_bool)

    print("--------- Simulation 4: Gauss x PW varying x value to s = [0.1, 0.05, 0.01] ----------")
    j1_gaussian_beam_with_varing_x_values(return_time_bool)


if __name__ == '__main__':
    print("We have these tests.")
    print("1 - j1_gaussian_beam_with_three_particles")
    print("2 - j1_gaussian_beam_with_varing_s_values")
    print("3 - j1_gaussian_beam_with_varing_z0_values_s_001")
    print("4 - j1_gaussian_beam_with_varing_z0_values_s_010")
    print("5 - j1_gaussian_beam_with_varing_z0_values_s_016")
    print("6 - j1_gaussian_beam_with_varing_x_values")
    print("7 - All")

    numberTest = input("Which will execute? Please write the number: ")
    returnTime = input("Return runtime? (y/n): ")
   
    switchRunTime = {
        "y": True,
        "n": False,
    }
    
    calculate_average = switchRunTime.get(returnTime)
    
    switchFuncsTest = {
        "1": partial(j1_gaussian_beam_with_three_particles),
        "2": partial(j1_gaussian_beam_with_varing_s_values),
        "3": partial(j1_gaussian_beam_with_varing_z0_values_s_001),
        "4": partial(j1_gaussian_beam_with_varing_z0_values_s_010),
        "5": partial(j1_gaussian_beam_with_varing_z0_values_s_016),
        "6": partial(j1_gaussian_beam_with_varing_x_values),
        "7": partial(all_j1_gaussian_beam_simulations)
    }

    case = switchFuncsTest.get(numberTest)
    case()

