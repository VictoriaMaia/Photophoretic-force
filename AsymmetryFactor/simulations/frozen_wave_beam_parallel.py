import sys
sys.path.append('./')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
from AsymmetryFactor.j1 import j1
from simulations.create_graph import plot_graphic
from simulations.time_operations import *
from timeit import default_timer as timer
from tqdm import tqdm
from itertools import repeat
import multiprocessing
import functools
import numpy as np
import math

orange = '#ff6800'
qnt_points = 200

def j1_frozen_wave_beam_with_three_size_parameters_multiprosses():
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

    z0 = np.linspace(0, 400*micro, qnt_points)
    beams = [(FrozenWaveAttributes(k, i, q, l, n)) for i in z0]

    pool_size = multiprocessing.cpu_count()


    # outputs_x01_new = []
    # start = timer() 
    # with multiprocessing.Pool(processes=pool_size) as pool:
    #     for result in tqdm(pool.imap_unordered(functools.partial(j1, particle_x_01), beams), total=len(beams)):
    #         outputs_x01_new.append(result*2500)
    #     pool.close()
    #     pool.join()
    # time_x01 = timer()-start

    # outputs_x3 = []
    # start = timer() 
    # with multiprocessing.Pool(processes=pool_size) as pool:
    #     for result in tqdm(pool.imap_unordered(functools.partial(j1, particle_x_3), beams), total=len(beams)):
    #         outputs_x3.append(result)
    #     pool.close()
    #     pool.join()
    # time_x3 = timer()-start

    # outputs_x8 = []
    # start = timer() 
    # with multiprocessing.Pool(processes=pool_size) as pool:
    #     for result in tqdm(pool.imap_unordered(functools.partial(j1, particle_x_8), beams), total=len(beams)):
    #         outputs_x8.append(result)
    #     pool.close()
    #     pool.join()
    # time_x8 = timer()-start

    # time = time_x01 + time_x3 + time_x8

    # print("time: ", convert_time_to_more_readable(time))

    # results = [outputs_x01_new, outputs_x3, outputs_x8]
    # x_label = "Size Parameter x"
    # y_label = "Asymmetry Factor $J_1(x)$"
    # legend = ["x = 0.1", "x = 3", "x = 8"]
    # z0 = np.linspace(0, 400, 50)
    # plot_graphic(results, z0, x_label, y_label, legend)
    
    
    pool = multiprocessing.Pool(processes=pool_size)
    print("Começando x_01")
    start = timer() 
    outputs_x01 = pool.starmap(j1, zip(repeat(particle_x_01), beams))
    pool.close() 
    pool.join() 
    outputs_x01_new = [i * 2500 for i in outputs_x01]
    time_x01 = timer()-start
    
    
    pool = multiprocessing.Pool(processes=pool_size)
    print("Começando x_3")
    start = timer() 
    outputs_x3 = pool.starmap(j1, zip(repeat(particle_x_3), beams))
    pool.close() 
    pool.join()
    time_x3 = timer()-start

    
    pool = multiprocessing.Pool(processes=pool_size)
    print("Começando x_8")
    start = timer() 
    outputs_x8 = pool.starmap(j1, zip(repeat(particle_x_8), beams))
    pool.close() 
    pool.join()
    time_x8 = timer()-start


    time = time_x01 + time_x3 + time_x8

    print("time: ", convert_time_to_more_readable(time))

    results = [outputs_x01_new, outputs_x3, outputs_x8]
    x_label = "Size Parameter x"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["x = 0.1", "x = 3", "x = 8"]
    z0 = np.linspace(0, 400, qnt_points)
    plot_graphic(results, z0, x_label, y_label, legend)


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

    z0 = np.linspace(0, 400*micro, 100)

    pbar = tqdm(colour=orange, total=len(z0), desc="Calculating x_01", leave=False)
    start = timer()
    for i in z0:
        results_x01.append(j1(particle_x_01, FrozenWaveAttributes(k, i, q, l, n))*2500)
        pbar.update()

    time_x01 = timer()-start
    # pbar.refresh()
    # pbar.close()

    # pbar = tqdm(colour=orange, total=len(z0), desc="Calculating x_3")
    start = timer()
    for i in z0:
        results_x3.append(j1(particle_x_3, FrozenWaveAttributes(k, i, q, l, n)))
        # pbar.update()

    time_x3 = timer()-start
    # pbar.refresh()
    # pbar.close()

    # pbar = tqdm(colour=orange, total=len(z0), desc="Calculating x_8")
    start = timer()
    for i in z0:
        results_x8.append(j1(particle_x_8, FrozenWaveAttributes(k, i, q, l, n)))
        # pbar.update()

    time_x8 = timer()-start
    # pbar.refresh()
    # pbar.close()

    time = time_x01 + time_x3 + time_x8

    print("time: ", convert_time_to_more_readable(time))

    # results = [results_x01, results_x3, results_x8]
    # x_label = "Size Parameter x"
    # y_label = "Asymmetry Factor $J_1(x)$"
    # legend = ["x = 0.1", "x = 3", "x = 8"]
    # z0 = np.linspace(0, 400, 50)
    # plot_graphic(results, z0, x_label, y_label, legend)
    
def j1_fwb_with_one_point_and_three_particles():
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

    # z0 = np.linspace(400*micro, 401*micro, 1)
    z0 = 0*micro
    print(f'Usando z0 = {z0}')

    start = timer()
    j1(particle_x_01, FrozenWaveAttributes(k, z0, q, l, n))*2500
    
    time_x01 = timer()-start
    print("tempo do ponto quando x=0.1: ", end="")
    convert_time_to_more_readable(time_x01)
    print()

    start = timer()
    j1(particle_x_3, FrozenWaveAttributes(k, z0, q, l, n))

    time_x3 = timer()-start
    print("tempo do ponto quando x=3: ",end="")
    convert_time_to_more_readable(time_x3)
    print()

    start = timer()
    j1(particle_x_8, FrozenWaveAttributes(k, z0, q, l, n))

    time_x8 = timer()-start
    print("tempo do ponto quando x=8: ", end="")
    convert_time_to_more_readable(time_x8)
    print()

    # time_x3 = 0
    # time_x8 = 0

    time = time_x01 + time_x3 + time_x8

    print("total time: ", end="")
    convert_time_to_more_readable(time)

    # results = [results_x01, results_x3, results_x8]
    # x_label = "Size Parameter x"
    # y_label = "Asymmetry Factor $J_1(x)$"
    # legend = ["x = 0.1", "x = 3", "x = 8"]
    # z0 = np.linspace(0, 400, 50)
    # plot_graphic(results, z0, x_label, y_label, legend)
    # print(f'{time:.6f}')
    



if __name__ == '__main__':
    # j1_frozen_wave_beam_with_three_size_parameters()
    j1_frozen_wave_beam_with_three_size_parameters_multiprosses()   
    # j1_fwb_with_one_point_and_three_particles() 