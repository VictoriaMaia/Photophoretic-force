import sys
sys.path.append('./')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.bessel.bessel_class import BesselAttributes
from AsymmetryFactor.beams.beam_class import BeamAttributes
from AsymmetryFactor.j1 import j1
from simulations.create_graph import plot_graphic
from simulations.time_operations import *
from timeit import default_timer as timer
from tqdm import tqdm
import numpy as np
import math


mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)
orange = '#ff6800'

calculate_average = True
max_executions = 10
qnt_points = 300

def j1_bessel_beam_with_three_particles():
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
        
    ur = 1
    x = np.linspace(0.01, 20, qnt_points)

    z0 = 0
    angle = 10
    bessel_b = BesselAttributes(k, z0, angle)

    m_038 = 1.57 - 0.038j
    m_019 = 1.57 - 0.19j
    m_095 = 1.57 - 0.95j

    pw = BeamAttributes()

    results_038 = []
    results_019 = []
    results_095 = []
    results_038_pw = []
    results_019_pw = []
    results_095_pw = []

    if calculate_average:
        total_time = 0
        
        pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
        for i in range(max_executions):            
            start = timer()
            
            for i in x:
                results_038.append(j1(ParticleAttributes(i, m_038, ur), bessel_b))
                results_038_pw.append(j1(ParticleAttributes(i, m_038, ur), pw))

                results_019.append(j1(ParticleAttributes(i, m_019, ur), bessel_b))
                results_019_pw.append(j1(ParticleAttributes(i, m_019, ur), pw))

                results_095.append(j1(ParticleAttributes(i, m_095, ur), bessel_b))
                results_095_pw.append(j1(ParticleAttributes(i, m_095, ur), pw))
            
            total_time += timer()-start
            pbar.update()
    
        pbar.refresh()
        pbar.close()  
        average = total_time/max_executions      
        print(f'{average:.3f}')  
    
        print("Total time: ", end="")
        convert_time_to_more_readable(average)

    else:
        pbar = tqdm(colour=orange, total=len(x), desc="Calculating")
    
        for i in x:
            results_038.append(j1(ParticleAttributes(i, m_038, ur), bessel_b))
            results_019.append(j1(ParticleAttributes(i, m_019, ur), bessel_b))
            results_095.append(j1(ParticleAttributes(i, m_095, ur), bessel_b))
            pbar.update()

        pbar.refresh()
        pbar.close()


        results = [results_038, results_019, results_095]
        x_label = "Size Parameter x"
        y_label = "Asymmetry Factor $J_1(x)$"
        legend = ["M = 1.57 - i0.038", "M = 1.57 - i0.19", "M = 1.57 - i0.95"]

        plot_graphic(results, x, x_label, y_label, legend)
    

def j1_bessel_beam_with_different_alpha_values():
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda

    z0 = 0
    angle_13 = 13.916
    angle_6 = 6.907
    angle_1 = 1.378

    bessel_angle13 = BesselAttributes(k, z0, angle_13)
    bessel_angle6 = BesselAttributes(k, z0, angle_6)
    bessel_angle1 = BesselAttributes(k, z0, angle_1)

    plane_wave = BeamAttributes()

    m_038 = 1.57 - 0.038j
    ur = 1
    x = np.linspace(20, 100, qnt_points)

    results_angle13 = []
    results_angle6 = []
    results_angle1 = []
    results_pw = []

    if calculate_average:
        total_time = 0
        
        pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
        for i in range(max_executions):            
            start = timer()
            
            for i in x:
                results_angle13.append(j1(ParticleAttributes(i, m_038, ur), bessel_angle13))
                results_angle6.append(j1(ParticleAttributes(i, m_038, ur), bessel_angle6))
                results_angle1.append(j1(ParticleAttributes(i, m_038, ur), bessel_angle1))
                results_pw.append(j1(ParticleAttributes(i, m_038, ur), plane_wave))
            
            total_time += timer()-start
            pbar.update()
    
        pbar.refresh()
        pbar.close()  
        average = total_time/max_executions      
        print(f'{average:.3f}')  
    
        print("Total time: ", end="")
        convert_time_to_more_readable(average)

    else:
        pbar = tqdm(colour=orange, total=len(x), desc="Calculating")
    
        for i in x:
            results_angle13.append(j1(ParticleAttributes(i, m_038, ur), bessel_angle13))
            results_angle6.append(j1(ParticleAttributes(i, m_038, ur), bessel_angle6))
            results_angle1.append(j1(ParticleAttributes(i, m_038, ur), bessel_angle1))
            results_pw.append(j1(ParticleAttributes(i, m_038, ur), plane_wave))
            pbar.update()

        pbar.refresh()
        pbar.close()


        results = [results_angle13, results_angle6, results_angle1, results_pw]
        x_label = "Size Parameter x"
        y_label = "Asymmetry Factor $J_1(x)$"
        legend = ["α =13.916°", "α = 6.907°", "α = 1.378°", "OP"]

        plot_graphic(results, x, x_label, y_label, legend)
    

def j1_bessel_beam_with_different_x_values():
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
        
    z0 = 0
    alpha = np.linspace(0.01, 45, qnt_points)

    plane_wave = BeamAttributes()

    m_038 = 1.57 - 0.038j
    ur = 1
    x_3 = 3
    x_8 = 8

    particle_x_3 = ParticleAttributes(x_3, m_038, ur)
    particle_x_8 = ParticleAttributes(x_8, m_038, ur)

    results_x_3 = []
    results_x_8 = []
    results_x_3_pw = []
    results_x_8_pw = []

    if calculate_average:
        total_time = 0
        
        pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
        for i in range(max_executions):            
            start = timer()
            
            for i in alpha:
                results_x_3.append(j1(particle_x_3, BesselAttributes(k, z0, i)))
                results_x_3_pw.append(j1(particle_x_3, plane_wave))

                results_x_8.append(j1(particle_x_8, BesselAttributes(k, z0, i)))     
                results_x_8_pw.append(j1(particle_x_8, plane_wave))           
            
            total_time += timer()-start
            pbar.update()
    
        pbar.refresh()
        pbar.close()  
        average = total_time/max_executions      
        print(f'{average:.3f}')  
    
        print("Total time: ", end="")
        convert_time_to_more_readable(average)

    else:
        pbar = tqdm(colour=orange, total=len(alpha), desc="Calculating")

        for i in alpha:
            results_x_3.append(j1(particle_x_3, BesselAttributes(k, z0, i)))
            results_x_8.append(j1(particle_x_8, BesselAttributes(k, z0, i)))                
            pbar.update()

        pbar.refresh()
        pbar.close()


        results = [results_x_3, results_x_8]
        x_label = "Axicon angle (degrees)"
        y_label = "Asymmetry Factor $J_1(x)$"
        legend = ["x = 3", "x = 8"]

        plot_graphic(results, alpha, x_label, y_label, legend)
    

if __name__ == '__main__':
    j1_bessel_beam_with_three_particles()
    j1_bessel_beam_with_different_alpha_values()
    j1_bessel_beam_with_different_x_values()
    