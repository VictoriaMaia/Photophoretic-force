import sys
sys.path.append('./')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
from AsymmetryFactor.j1 import j1
from simulations.create_graph import plot_graphic
from simulations.time_operations import *
from timeit import default_timer as timer
from tqdm import tqdm
import numpy as np
import math

orange = '#ff6800'

def j1_frozen_wave_beam_with_three_size_parameters():
    micro = 10**(-6) 
    nano = 10**(-9)

    var_lambda = 1064 * nano
        
    ur = 1

    k = (2*math.pi) / var_lambda
    n = -75
    q = 0.8*k
    l = 400*micro

    m_038 = 1.57 - 0.038j
    x_01 = 0.1
    x_3 = 3
    x_8 = 8

    particle_x_01 = ParticleAttributes(x_01, m_038, ur)
    particle_x_3 = ParticleAttributes(x_3, m_038, ur)
    particle_x_8 = ParticleAttributes(x_8, m_038, ur)

    results_x01 = []
    results_x3 = []
    results_x8 = []

    z0 = np.linspace(200*micro, 400*micro, 50)

    pbar = tqdm(colour=orange, total=len(z0), desc="Test 1. Calculating")
    start = timer()
    for i in z0:
        # print(i)
        # print(f'x=0.1 : {j1(particle_x_01, FrozenWaveAttributes(k, i, q, l, n))}')
        # print(f'x=3 : {j1(particle_x_3, FrozenWaveAttributes(k, i, q, l, n))}')
        # print(f'x=8 : {j1(particle_x_8, FrozenWaveAttributes(k, i, q, l, n))}')
        # return
        results_x01.append(j1(particle_x_01, FrozenWaveAttributes(k, i, q, l, n))*2500)
        results_x3.append(j1(particle_x_3, FrozenWaveAttributes(k, i, q, l, n)))
        results_x8.append(j1(particle_x_8, FrozenWaveAttributes(k, i, q, l, n)))
        pbar.update()

    time = timer()-start
    pbar.refresh()
    pbar.close()

    print("time: ", convert_time_to_more_readable(time))
    print(z0)
    print("**************************")
    print(results_x01)
    print("**************************")
    print(results_x3)
    print("**************************")
    print(results_x8)

    results = [results_x01, results_x3, results_x8]
    x_label = "Size Parameter x"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["x = 0.1", "x = 3", "x = 8"]
    z0 = np.linspace(0, 400, 50)
    plot_graphic(results, z0, x_label, y_label, legend)
    

if __name__ == '__main__':
    j1_frozen_wave_beam_with_three_size_parameters()
    