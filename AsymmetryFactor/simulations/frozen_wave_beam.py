import sys
sys.path.append('./')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
from AsymmetryFactor.j1 import j1, j1_with_time, j1_with_time_parallel, j1_with_time_gn_parallel, j1_with_time_gn_term_calculate
from simulations.create_graph import plot_graphic
from simulations.time_operations import *
from timeit import default_timer as timer
from tqdm import tqdm
import csv
import numpy as np
import math

from itertools import repeat
import multiprocessing
import functools

mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)
orange = '#ff6800'

calculate_average = True
max_executions = 10
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
        

def j1_frozen_wave_with_varing_z0_values_gn_term_calculate():
    path = "./simulations/outputs/time_result/"
    title = "j1_frozen_wave_"
    simulation2 = "with_z0_l2_l4_and_1_times_1_values_calculate_gn_terms_aq_integral_definida"
    
    time_file_name2 = path + title + simulation2 + ".csv"
    print(time_file_name2)

    time_file2 = open(time_file_name2, 'w', newline='')
    writer_csv_file = csv.DictWriter(
        time_file2, 
        fieldnames= ["execucao", "valor_de_j1", "valor_de_j1_serial", "ponto", "z", "n_max", "j1",  \
                     "gn", "n", "qnt_q_values", "Aq", "pi_tau", "frac_exp", "ops_gn", \
                     "gn1", "ot", "op" ])
    

    # times_terms = {'qnt_q_values': len(q_values), 'Aq':0, 'pi_tau':0, 'frac_exp':0, 'op': 0}

    dic_to_write = {"execucao":0, "valor_de_j1":0, "valor_de_j1_serial":0, "ponto":0, "z":0, "n_max":0, "j1":0,  \
                     "gn":0, "n":0, "qnt_q_values":0, "Aq":0, "pi_tau":0, "frac_exp":0, "ops_gn":0, \
                     "gn1":0, "ot":0, "op":0}
    
    writer_csv_file. writeheader()

    var_lambda = 1064 * nano
        
    k = (2*math.pi) / var_lambda
    n = -75
    q = 0.8*k
    l = 400*micro   

    fw_l2 = FrozenWaveAttributes(k, l/2, q, l, n)
    # fw_l4 = FrozenWaveAttributes(k, l/4, q, l, n)

    ur = 1
    m_038 = 1.57 - 0.038j
    x = np.linspace(0.1, 20, qnt_points)

    # results_l2 = []
    # results_l4 = []

    # pbar = tqdm(colour=orange, total=max_executions, desc="Calculating")        
    for e in range(max_executions):

        for i in x:
            # _, dic_receive_l2 = j1_with_time_gn_parallel(ParticleAttributes(i, m_038, ur), fw_l2)
            # _, dic_receive_l4 = j1_with_time_gn_parallel(ParticleAttributes(i, m_038, ur), fw_l4)

            # _, dic_receive_l2 = j1_with_time_parallel(ParticleAttributes(i, m_038, ur), fw_l2)
            # _, dic_receive_l4 = j1_with_time_parallel(ParticleAttributes(i, m_038, ur), fw_l4)

            value_j1, dic_receive_l2 = j1_with_time_gn_term_calculate(ParticleAttributes(i, m_038, ur), fw_l2)
            value_j1_serial = j1(ParticleAttributes(i, m_038, ur), fw_l2)

            print(value_j1)
            print(value_j1_serial)

            # dic_receive_l2["ponto"] = i
            # dic_receive_l4["ponto"] = i
            # dic_receive_l2["execucao"] = e
            # dic_receive_l4["execucao"] = e
            
            # dic_receive_l2["z"] = "l2"
            # dic_receive_l4["z"] = "l4"

            dic_to_write["valor_de_j1"] = value_j1
            dic_to_write["valor_de_j1_serial"] = value_j1_serial
            dic_to_write["execucao"] = e
            dic_to_write["z"] = "l2"
            dic_to_write["ponto"] = dic_receive_l2["ponto"]
            dic_to_write["n_max"] = dic_receive_l2["n_max"]
            dic_to_write["j1"] = dic_receive_l2["j1"]
            dic_to_write["gn"] = dic_receive_l2["gn"]
            dic_to_write["gn1"] = dic_receive_l2["gn1"]
            dic_to_write["ot"] = dic_receive_l2["ot"]
            dic_to_write["op"] = dic_receive_l2["op"]

            
            qnt_n_max = dic_receive_l2["n_max"]
            for n in range(qnt_n_max):
                dic_to_write["n"] = dic_receive_l2["gns_terms"][n]['n']
                dic_to_write["qnt_q_values"] = dic_receive_l2["gns_terms"][n]['qnt_q_values']
                dic_to_write["Aq"] = dic_receive_l2["gns_terms"][n]['Aq']
                dic_to_write["pi_tau"] = dic_receive_l2["gns_terms"][n]['pi_tau']
                dic_to_write["frac_exp"] = dic_receive_l2["gns_terms"][n]['frac_exp']
                dic_to_write["ops_gn"] = dic_receive_l2["gns_terms"][n]['ops_gn']
                writer_csv_file.writerow(dic_to_write)


            # dic_to_write = {"execucao":0, "ponto":0, "z":0, "n_max":0, "j1":0,  \
            #          "gn":0, "qnt_q_values":0, "Aq":0, "pi_tau":0, "frac_exp":0, "ops_gn":0, \
            #          "gn1":0, "ot":0, "op":0}

            # writer_csv_file.writerow(dic_receive_l2)
            # writer_csv_file.writerow(dic_receive_l4)
            
    #     pbar.update()

    # pbar.refresh()
    # pbar.close()  




def j1_frozen_wave_with_varing_z0_values():
    path = "./simulations/outputs/time_result/"
    title = "j1_frozen_wave_"
    caracteristicas = "with_z0_l2_l4_and_10_times_100_values_"
    version = "after_gn_parallel_2_processes"
    # version = "serial"
    
    time_file_name2 = path + title + caracteristicas + version + ".csv"
    print(time_file_name2)

    time_file2 = open(time_file_name2, 'w', newline='')
    writer_csv_file = csv.DictWriter(
        time_file2, 
        fieldnames= ["execucao", "tempo"])
    
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}


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
        total_time = 0
        
        pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points graph 2", leave=False)
        for i in range(max_executions):            
            start = timer()
            
            for i_x in x:
                results_l2.append(j1_with_time_gn_parallel(ParticleAttributes(i_x, m_038, ur), fw_l2))
                results_l4.append(j1_with_time_gn_parallel(ParticleAttributes(i_x, m_038, ur), fw_l4))
                # results_l2.append(j1(ParticleAttributes(i_x, m_038, ur), fw_l2))
                # results_l4.append(j1(ParticleAttributes(i_x, m_038, ur), fw_l4))
            
            total_time = timer()-start
            
            dic_time["execucao"] = i+1
            dic_time["tempo"] = total_time
            
            
            writer_csv_file.writerow(dic_time)
            # total_time += timer()-start
            pbar.update()
    
        pbar.refresh()
        pbar.close()  
        # average = total_time/max_executions      
        # print(f'{average:.3f}')  
    
        # print("Total time: ", end="")
        # convert_time_to_more_readable(average)

    # else:
    #     total_time = 0

    #     pbar = tqdm(colour=orange, total=len(x), desc="Calculating")
    #     for i in x:
    #         start = timer()
    #         result_of_l2, _ = j1_with_time_gn_parallel(ParticleAttributes(i, m_038, ur), fw_l2)
    #         result_of_l4, _ = j1_with_time_gn_parallel(ParticleAttributes(i, m_038, ur), fw_l4)
            
    #         results_l2.append(result_of_l2)
    #         results_l4.append(result_of_l4*250)

    #         # results_l2.append(j1(ParticleAttributes(i, m_038, ur), fw_l2))
    #         # results_l4.append(j1(ParticleAttributes(i, m_038, ur), fw_l4)*250)
    #         total_time += timer()-start

    #         pbar.update()

    #     pbar.refresh()
    #     pbar.close()

    #     convert_time_to_more_readable(total_time)

    #     results = [results_l2, results_l4]
    #     x_label = "Size Parameter x"
    #     y_label = "Asymmetry Factor $J_1(x)$"
    #     legend = ["$z_0 = L/2$", r'$z_0 = L/4 \times 250$']
    #     plot_graphic(results, x, x_label, y_label, legend)


def j1_frozen_wave_with_varing_z0_values_with_time_calculate():
    path = "./simulations/outputs/time_result/"
    title = "j1_frozen_wave_"
    simulation = "with_z0_l2_l4_and_1_times_3_values_n_max_after_j1_parallel_4_processes"
    
    time_file_name = path + title + simulation + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(
        time_file, 
        fieldnames= ["execucao", "ponto", "z", "n_max", "j1", "gn", "gn1", "ot", "op"])
    
    writer_csv_file. writeheader()

    # COLOQUEI AQUI O 3
    qnt_points = 3

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

    # results_l2 = []
    # results_l4 = []

    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating")        
    for e in range(max_executions):

        for i in x:
            # _, dic_receive_l2 = j1_with_time_gn_parallel(ParticleAttributes(i, m_038, ur), fw_l2)
            # _, dic_receive_l4 = j1_with_time_gn_parallel(ParticleAttributes(i, m_038, ur), fw_l4)

            _, dic_receive_l2 = j1_with_time_parallel(ParticleAttributes(i, m_038, ur), fw_l2)
            _, dic_receive_l4 = j1_with_time_parallel(ParticleAttributes(i, m_038, ur), fw_l4)

            # dic_receive_l2["ponto"] = i
            # dic_receive_l4["ponto"] = i
            dic_receive_l2["execucao"] = e
            dic_receive_l4["execucao"] = e
            
            dic_receive_l2["z"] = "l2"
            dic_receive_l4["z"] = "l4"

            writer_csv_file.writerow(dic_receive_l2)
            writer_csv_file.writerow(dic_receive_l4)
            
        pbar.update()

    pbar.refresh()
    pbar.close()  


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
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["ponto_x", "n_max", "j1", "gn", "gn1", "ot", "op"])
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


def j1_frozen_wave_beam_with_three_size_parameters_multiprosses():
    path = "./simulations/outputs/time_result/"
    title = "j1_frozen_wave_"
    caracteristicas = "with_z0_l2_l4_and_10_times_100_values_"
    version = "after_j1_parallel_4_processes"
    
    time_file_name2 = path + title + caracteristicas + version + ".csv"
    
    print(time_file_name2)

    time_file2 = open(time_file_name2, 'w', newline='')
    writer_csv_file = csv.DictWriter(
        time_file2, 
        fieldnames= ["execucao", "tempo"])
    
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}


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
    particles = [(ParticleAttributes(i_x, m_038, ur)) for i_x in x]

    pool_size = multiprocessing.cpu_count()

    if calculate_average:        
        pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points graph 2", leave=False)
        
        for i in range(max_executions):            
            print("Começando l/2")
            pool = multiprocessing.Pool(processes=pool_size)
            startl2 = timer() 
            outputs_l2 = pool.starmap(j1, zip(particles, repeat(fw_l2)))
            pool.close() 
            pool.join() 
            
            time_l2 = timer() - startl2


            print("Começando l/4")
            pool_l4 = multiprocessing.Pool(processes=pool_size)
            startl4 = timer() 
            outputs_l4 = pool_l4.starmap(j1, zip(particles, repeat(fw_l4)))
            pool_l4.close() 
            pool_l4.join() 
            time_l4 = timer() - startl4
            
            time_total = time_l2 + time_l4

            dic_time["execucao"] = i
            dic_time["tempo"] = time_total
           
            writer_csv_file.writerow(dic_time)

            pbar.update()

        time_file2.close()
        pbar.refresh()
        pbar.close()  
       

    # outputs_l4_m = [i * 250 for i in outputs_l4]

    # results = [outputs_l2, outputs_l4_m]
    # x_label = "Size Parameter x"
    # y_label = "Asymmetry Factor $J_1(x)$"
    # legend = ["$z_0 = L/2$", r'$z_0 = L/4 \times 250$']
    # plot_graphic(results, x, x_label, y_label, legend)



if __name__ == '__main__':
    # print("tres particulas")
    # j1_frozen_wave_beam_with_three_size_parameters()
    # print("z0 com l2 e l4")
    # j1_frozen_wave_with_varing_z0_values_gn_term_calculate()
    j1_frozen_wave_with_varing_z0_values()
    # j1_frozen_wave_with_varing_z0_values_with_time_calculate()
    # j1_frozen_wave_beam_with_three_size_parameters_multiprosses()
    # j1_frozen_wave_time_calculate()
    # j1_frozen_test()
