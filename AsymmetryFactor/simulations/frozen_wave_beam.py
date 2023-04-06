import sys
sys.path.append('./')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
from AsymmetryFactor.j1 import j1, j1_with_time, j1_with_time_parallel, j1_with_time_gn_parallel
from simulations.create_graph import plot_graphic
from simulations.time_operations import *
from timeit import default_timer as timer
from tqdm import tqdm
import csv
import numpy as np
import math

mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)
orange = '#ff6800'

calculate_average = True
max_executions = 5
qnt_points = 100

# dic_time = {'ponto':0, 'gn': 0, 'gn1': 0, 'ot': 0, 'op':0, 'j1':0}

def j1_frozen_wave_beam_with_three_size_parameters():
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

    z0 = np.linspace(0, 400*micro, qnt_points)

    if calculate_average:
        print("gn_parallel")
        total_time = 0
        
        pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points graph 1", leave=False)
        for i in range(max_executions):          
            start = timer()
            
            for i in z0:
                results_x01.append(j1_with_time_gn_parallel(particle_x_01, FrozenWaveAttributes(k, i, q, l, n)))
                results_x3.append(j1_with_time_gn_parallel(particle_x_3, FrozenWaveAttributes(k, i, q, l, n)))
                results_x8.append(j1_with_time_gn_parallel(particle_x_8, FrozenWaveAttributes(k, i, q, l, n)))
            
            total_time += timer()-start
            pbar.update()
    
        pbar.refresh()
        pbar.close()  
        average = total_time/max_executions      
        print(f'{average:.3f}')  
    
        print("Total time: ", end="")
        convert_time_to_more_readable(average)

    else:
        pbar = tqdm(colour=orange, total=len(z0), desc="Calculating")
        total_time = 0

        for i in z0:
            start = timer()
            results_x01.append(j1(particle_x_01, FrozenWaveAttributes(k, i, q, l, n))*2500)
            results_x3.append(j1(particle_x_3, FrozenWaveAttributes(k, i, q, l, n)))
            results_x8.append(j1(particle_x_8, FrozenWaveAttributes(k, i, q, l, n)))
            
            total_time += timer()-start
            pbar.update()

        pbar.refresh()
        pbar.close()

        convert_time_to_more_readable(total_time)

        z0 = np.linspace(0, 400, qnt_points)

        results = [results_x01, results_x3, results_x8]
        x_label = "Size Parameter x"
        y_label = "Asymmetry Factor $J_1(x)$"
        legend = ["x = 0.1", "x = 3", "x = 8"]
        plot_graphic(results, z0, x_label, y_label, legend)
        

def j1_frozen_wave_with_varing_z0_values():
    var_lambda = 1064 * nano
        
    k = (2*math.pi) / var_lambda
    n = -75
    q = 0.8*k
    l = 400*micro    

    fw_l2 = FrozenWaveAttributes(k, l/2, q, l, n)
    fw_l4 = FrozenWaveAttributes(k, l/4, q, l, n)

    ur = 1
    m_038 = 1.57 - 0.038j
    x = np.linspace(0.1, 20, qnt_points)

    results_l2 = []
    results_l4 = []

    if calculate_average:
        print("gn_parallel")
        total_time = 0
        
        pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points graph 2", leave=False)
        for i in range(max_executions):            
            start = timer()
            
            for i in x:
                results_l2.append(j1_with_time_gn_parallel(ParticleAttributes(i, m_038, ur), fw_l2))
                results_l4.append(j1_with_time_gn_parallel(ParticleAttributes(i, m_038, ur), fw_l4))
            
            total_time += timer()-start
            pbar.update()
    
        pbar.refresh()
        pbar.close()  
        average = total_time/max_executions      
        print(f'{average:.3f}')  
    
        print("Total time: ", end="")
        convert_time_to_more_readable(average)

    else:
        total_time = 0

        pbar = tqdm(colour=orange, total=len(x), desc="Calculating")
        for i in x:
            start = timer()
            result_of_l2, _ = j1_with_time_gn_parallel(ParticleAttributes(i, m_038, ur), fw_l2)
            result_of_l4, _ = j1_with_time_gn_parallel(ParticleAttributes(i, m_038, ur), fw_l4)
            
            results_l2.append(result_of_l2)
            results_l4.append(result_of_l4*250)

            # results_l2.append(j1(ParticleAttributes(i, m_038, ur), fw_l2))
            # results_l4.append(j1(ParticleAttributes(i, m_038, ur), fw_l4)*250)
            total_time += timer()-start

            pbar.update()

        pbar.refresh()
        pbar.close()

        convert_time_to_more_readable(total_time)

        results = [results_l2, results_l4]
        x_label = "Size Parameter x"
        y_label = "Asymmetry Factor $J_1(x)$"
        legend = ["$z_0 = L/2$", r'$z_0 = L/4 \times 250$']
        plot_graphic(results, x, x_label, y_label, legend)


def j1_frozen_wave_time_calculate():
    global dic_time
    var_lambda = 1064 * nano
        
    k = (2*math.pi) / var_lambda
    n = -75
    q = 0.8*k
    l = 400*micro    

    fw_l2 = FrozenWaveAttributes(k, l/2, q, l, n)
    fw_l4 = FrozenWaveAttributes(k, l/4, q, l, n)

    ur = 1
    m_038 = 1.57 - 0.038j
    qnt_points = 3
    
    z0 = np.linspace(0, 400*micro, qnt_points)
    particle_x_3 = ParticleAttributes(3, m_038, ur)

    x = np.linspace(0.1, 20, qnt_points)
    # x = np.linspace(0.1, 20, 3)

    # results_l2 = []

    time_file_name = "./simulations/outputs/time_result/"+ "j1_frozen_wave_with_x_3_and_3_values_with_n_max_after_parallel" + ".csv"
    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["ponto", "n_max", "j1", "gn", "gn1", "ot", "op"])
    writer_csv_file. writeheader()

    pbar = tqdm(colour=orange, total=len(x), desc="Calculating")
    # for i in x:
    for i in z0:
        # _, dic_receive = j1_with_time_parallel(ParticleAttributes(i, m_038, ur), fw_l2)
        # _, dic_receive = j1_with_time(ParticleAttributes(i, m_038, ur), fw_l4)
        # _, dic_receive = j1_with_time_parallel(ParticleAttributes(i, m_038, ur), fw_l4)
        _, dic_receive = j1_with_time_parallel(particle_x_3, FrozenWaveAttributes(k, i, q, l, n))
        # _, dic_receive = j1_with_time_gn_parallel(particle_x_3, FrozenWaveAttributes(k, i, q, l, n))
        # _, dic_receive = j1_with_time_gn_parallel(ParticleAttributes(i, m_038, ur), fw_l2)
        
        dic_receive["ponto"] = i
        writer_csv_file.writerow(dic_receive)

        # results_l2.append(j1_value)

        dic_time["j1"] += dic_receive["j1"]
        dic_time["gn"] += dic_receive["gn"]
        dic_time["gn1"] += dic_receive["gn1"]
        dic_time["ot"] += dic_receive["ot"]
        dic_time["op"] += dic_receive["op"]

        pbar.update()

    pbar.refresh()
    pbar.close()


    dic_time["j1"] = dic_time["j1"]/qnt_points  
    dic_time["gn"] = dic_time["gn"]/qnt_points  
    dic_time["gn1"] = dic_time["gn1"]/qnt_points  
    dic_time["ot"] = dic_time["ot"]/qnt_points  
    dic_time["op"] = dic_time["op"]/qnt_points   

    dic_time["ponto"] = "media"
    writer_csv_file.writerow(dic_time)

    time_file.close()
    
    # results = [results_l2]
    # x_label = "Size Parameter x"
    # y_label = "Asymmetry Factor $J_1(x)$"
    # legend = ["$z_0 = L/2$"]
    # plot_graphic(results, x, x_label, y_label, legend)

def j1_frozen_test():
    var_lambda = 1064 * nano
        
    k = (2*math.pi) / var_lambda
    n = -75
    q = 0.8*k
    l = 400*micro    

    fw_l2 = FrozenWaveAttributes(k, l/2, q, l, n)

    ur = 1
    m_038 = 1.57 - 0.038j
    x = np.linspace(0.1, 20, 3)

    # results_l2 = []

    # pbar = tqdm(colour=orange, total=len(x), desc="Calculating")
    for i in x:
        result_j1_before_changes, dic_receive_before_changes = j1_with_time(ParticleAttributes(i, m_038, ur), fw_l2)
        result_j1_gn_changes, dic_receive_gn_changes = j1_with_time_gn_parallel(ParticleAttributes(i, m_038, ur), fw_l2)
        result_j1, dic_receive = j1_with_time_parallel(ParticleAttributes(i, m_038, ur), fw_l2)
        result_j12 = j1(ParticleAttributes(i, m_038, ur), fw_l2)
        
        # dic_receive["ponto"] = i
     
        print("before all parallel")
        print(dic_receive_before_changes)
        print("------------------------------------------------------------------------")
        print("after j1 parallel")
        print(dic_receive)
        print("------------------------------------------------------------------------")
        print("after gn parallel")
        print(dic_receive_gn_changes)
        print()
        print(result_j1)
        print(result_j1_before_changes)
        print(result_j1_gn_changes)
        print(result_j12)

        print("\n\n")

    

    # pbar.refresh()
    # pbar.close()


if __name__ == '__main__':
    print("tres particulas")
    j1_frozen_wave_beam_with_three_size_parameters()
    print("z0 com l2 e l4")
    j1_frozen_wave_with_varing_z0_values()
    # j1_frozen_wave_time_calculate()
    # j1_frozen_test()
