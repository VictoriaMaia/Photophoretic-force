from .summation_terms_of_j1 import *
from .particle.particle_class import ParticleAttributes
from .beams.beam_class import BeamAttributes
from .beams import *
from timeit import default_timer as timer
from itertools import repeat
import numpy as np
import multiprocessing


# dic_time = {'ponto':particle.x, 'n_max':0, 'gn': 0, 'gn1': 0, 'ot': 0, 'op':0, 'j1':0}

class CalculateTime:
    def __init__(self, result, dict_t) -> None:
        self.result = result
        self.dict_t = dict_t
        pass

    def print_info(self):
        print(self.result)
        print(self.dict_t)


def summation(particle, beam):
    """
    TODO: add description
    
    Parameters
    ----------
    particle :
    """
    n_max = ceiling_x(particle.x)
    v_eta_r = eta_r(particle.m, particle.ur)
    mod2_eta_r = abs(v_eta_r) ** 2
    summation_result = 0
    
    for i in range(1, (n_max+1)):
        # variables computed in i position
        vars_i = compute_variables(particle, i)

        if isinstance(beam, GaussAttributes):
            gn = beam.gn_beam(i)
            conj_gn = np.conj(gn)
            gn1 = beam.gn_beam((i+1))
            conj_gn1 = np.conj(gn1)
        elif isinstance(beam, BesselAttributes):
            gn = gn_bessel_beam(i, beam.k, beam.z0, beam.angle)
            conj_gn = np.conj(gn)
            gn1 = gn_bessel_beam((i+1), beam.k, beam.z0, beam.angle)
            conj_gn1 = np.conj(gn1)
        elif isinstance(beam, FrozenWaveAttributes):
            gn = gn_frozen_wave_beam(i, beam.n, beam.k, beam.z0, beam.l, beam.q)
            conj_gn = np.conj(gn)
            gn1 = gn_frozen_wave_beam((i+1), beam.n, beam.k, beam.z0, beam.l, beam.q)
            conj_gn1 = np.conj(gn1)
        else:
            gn = 1
            conj_gn = 1
            gn1 = 1
            conj_gn1 = 1


        first_term_for = ((i*(i+2)) / particle.m) * \
                         (
                                 (gn1 * conj_gn * vars_i.cn1 * vars_i.conj_cn * vars_i.rn1) +
                                 (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn * vars_i.rn)
                         )

        second_term_for = ((i*(i+2)) / (i+1)) * \
                          (
                                  (gn * conj_gn1 * vars_i.cn * vars_i.conj_cn1) +
                                  (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn)
                          )

        third_term_for = np.conj(v_eta_r) * (((2*i)+1) / (i*(i+1))) * (abs(gn)**2) * (vars_i.cn * vars_i.conj_dn)
        
        result = first_term_for - ((second_term_for + third_term_for) * vars_i.sn)
        
        summation_result += result
    
    return summation_result


def summation_calculate_gn_time(particle, beam):
    result_and_times = []

    start_j1_pre = timer() 
    
    n_max = ceiling_x(particle.x)
    v_eta_r = eta_r(particle.m, particle.ur)
    mod2_eta_r = abs(v_eta_r) ** 2

    finish_j1_pre = timer() - start_j1_pre

    for i in range(1, (n_max+1)):
        start_j1 = timer()

        # variables computed in i position
        start_ot = timer()
        vars_i = compute_variables(particle, i)
        time_other_terms = timer() - start_ot

        if isinstance(beam, GaussAttributes):
            gn = beam.gn_beam(i)
            conj_gn = np.conj(gn)
            gn1 = beam.gn_beam((i+1))
            conj_gn1 = np.conj(gn1)
        elif isinstance(beam, BesselAttributes):
            gn = gn_bessel_beam(i, beam.k, beam.z0, beam.angle)
            conj_gn = np.conj(gn)
            gn1 = gn_bessel_beam((i+1), beam.k, beam.z0, beam.angle)
            conj_gn1 = np.conj(gn1)
        elif isinstance(beam, FrozenWaveAttributes):
            
            start_gn = timer()
            # gn = gn_frozen_wave_beam(i, beam.n, beam.k, beam.z0, beam.l, beam.q)
            gn, gn_term_times = gn_frozen_wave_beam_with_calculate_time(i, beam.n, beam.k, beam.z0, beam.l, beam.q)
            time_gn = timer() - start_gn            

            conj_gn = np.conj(gn)

            start_gn1 = timer()
            gn1, _ = gn_frozen_wave_beam_with_calculate_time((i+1), beam.n, beam.k, beam.z0, beam.l, beam.q)
            time_gn1 = timer() - start_gn1

            conj_gn1 = np.conj(gn1)
        else:
            gn = 1
            conj_gn = 1
            gn1 = 1
            conj_gn1 = 1


        start_operations = timer()

        first_term_for = ((i*(i+2)) / particle.m) * \
                         (
                                 (gn1 * conj_gn * vars_i.cn1 * vars_i.conj_cn * vars_i.rn1) +
                                 (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn * vars_i.rn)
                         )

        second_term_for = ((i*(i+2)) / (i+1)) * \
                          (
                                  (gn * conj_gn1 * vars_i.cn * vars_i.conj_cn1) +
                                  (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn)
                          )

        third_term_for = np.conj(v_eta_r) * (((2*i)+1) / (i*(i+1))) * (abs(gn)**2) * (vars_i.cn * vars_i.conj_dn)
        
        result = first_term_for - ((second_term_for + third_term_for) * vars_i.sn)
    
        time_operations = timer() - start_operations
        
        dic_time = {'ponto':particle.x, 'n_max':0, 'gn': 0, 'gn1': 0, 'ot': 0, 'op':0, 'j1':0}
        dic_time['j1'] = (timer() - start_j1) + finish_j1_pre
        dic_time['gn'] = time_gn
        dic_time['gn1'] = time_gn1
        dic_time['ot'] = time_other_terms
        dic_time['op'] = time_operations
        dic_time['n_max'] = n_max

        dic_time.update({'gn_term_times': gn_term_times})

        result_and_times.append(CalculateTime(result, dic_time))

        finish_j1_pre = 0


    return result_and_times




def summation_with_compute_time(particle, beam):
    
    result_and_times = []

    start_j1_pre = timer() 
    
    n_max = ceiling_x(particle.x)
    v_eta_r = eta_r(particle.m, particle.ur)
    mod2_eta_r = abs(v_eta_r) ** 2

    finish_j1_pre = timer() - start_j1_pre

    for i in range(1, (n_max+1)):
        start_j1 = timer()

        # variables computed in i position
        start_ot = timer()
        vars_i = compute_variables(particle, i)
        time_other_terms = timer() - start_ot

        if isinstance(beam, GaussAttributes):
            gn = beam.gn_beam(i)
            conj_gn = np.conj(gn)
            gn1 = beam.gn_beam((i+1))
            conj_gn1 = np.conj(gn1)
        elif isinstance(beam, BesselAttributes):
            gn = gn_bessel_beam(i, beam.k, beam.z0, beam.angle)
            conj_gn = np.conj(gn)
            gn1 = gn_bessel_beam((i+1), beam.k, beam.z0, beam.angle)
            conj_gn1 = np.conj(gn1)
        elif isinstance(beam, FrozenWaveAttributes):
            
            start_gn = timer()
            gn = gn_frozen_wave_beam(i, beam.n, beam.k, beam.z0, beam.l, beam.q)
            time_gn = timer() - start_gn            

            conj_gn = np.conj(gn)

            start_gn1 = timer()
            gn1 = gn_frozen_wave_beam((i+1), beam.n, beam.k, beam.z0, beam.l, beam.q)
            time_gn1 = timer() - start_gn1

            conj_gn1 = np.conj(gn1)
        else:
            gn = 1
            conj_gn = 1
            gn1 = 1
            conj_gn1 = 1


        start_operations = timer()

        first_term_for = ((i*(i+2)) / particle.m) * \
                         (
                                 (gn1 * conj_gn * vars_i.cn1 * vars_i.conj_cn * vars_i.rn1) +
                                 (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn * vars_i.rn)
                         )

        second_term_for = ((i*(i+2)) / (i+1)) * \
                          (
                                  (gn * conj_gn1 * vars_i.cn * vars_i.conj_cn1) +
                                  (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn)
                          )

        third_term_for = np.conj(v_eta_r) * (((2*i)+1) / (i*(i+1))) * (abs(gn)**2) * (vars_i.cn * vars_i.conj_dn)
        
        result = first_term_for - ((second_term_for + third_term_for) * vars_i.sn)
    
        time_operations = timer() - start_operations
        
        dic_time = {'ponto':particle.x, 'n_max':0, 'gn': 0, 'gn1': 0, 'ot': 0, 'op':0, 'j1':0}
        dic_time['j1'] = (timer() - start_j1) + finish_j1_pre
        dic_time['gn'] = time_gn
        dic_time['gn1'] = time_gn1
        dic_time['ot'] = time_other_terms
        dic_time['op'] = time_operations
        dic_time['n_max'] = n_max
    
        result_and_times.append(CalculateTime(result, dic_time))

        finish_j1_pre = 0



    return result_and_times




def summation_with_compute_time_gn_parallel(particle, beam):
    
    result_and_times = []

    start_j1_pre = timer() 
    
    n_max = ceiling_x(particle.x)
    v_eta_r = eta_r(particle.m, particle.ur)
    mod2_eta_r = abs(v_eta_r) ** 2

    finish_j1_pre = timer() - start_j1_pre

    for i in range(1, (n_max+1)):
        start_j1 = timer()

        # variables computed in i position
        start_ot = timer()
        vars_i = compute_variables(particle, i)
        time_other_terms = timer() - start_ot

        if isinstance(beam, GaussAttributes):
            gn = beam.gn_beam(i)
            conj_gn = np.conj(gn)
            gn1 = beam.gn_beam((i+1))
            conj_gn1 = np.conj(gn1)
        elif isinstance(beam, BesselAttributes):
            gn = gn_bessel_beam(i, beam.k, beam.z0, beam.angle)
            conj_gn = np.conj(gn)
            gn1 = gn_bessel_beam((i+1), beam.k, beam.z0, beam.angle)
            conj_gn1 = np.conj(gn1)
        elif isinstance(beam, FrozenWaveAttributes):
            
            start_gn = timer()
            # gn = gn_frozen_wave_beam(i, beam.n, beam.k, beam.z0, beam.l, beam.q)
            gn = gn_frozen_wave_beam_with_parallel(i, beam.n, beam.k, beam.z0, beam.l, beam.q)
            time_gn = timer() - start_gn            

            conj_gn = np.conj(gn)

            start_gn1 = timer()
            gn1 = gn_frozen_wave_beam_with_parallel((i+1), beam.n, beam.k, beam.z0, beam.l, beam.q)
            time_gn1 = timer() - start_gn1

            conj_gn1 = np.conj(gn1)
        else:
            gn = 1
            conj_gn = 1
            gn1 = 1
            conj_gn1 = 1


        start_operations = timer()

        first_term_for = ((i*(i+2)) / particle.m) * \
                         (
                                 (gn1 * conj_gn * vars_i.cn1 * vars_i.conj_cn * vars_i.rn1) +
                                 (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn * vars_i.rn)
                         )

        second_term_for = ((i*(i+2)) / (i+1)) * \
                          (
                                  (gn * conj_gn1 * vars_i.cn * vars_i.conj_cn1) +
                                  (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn)
                          )

        third_term_for = np.conj(v_eta_r) * (((2*i)+1) / (i*(i+1))) * (abs(gn)**2) * (vars_i.cn * vars_i.conj_dn)
        
        result = first_term_for - ((second_term_for + third_term_for) * vars_i.sn)
    
        time_operations = timer() - start_operations
        
        dic_time = {'ponto':particle.x, 'n_max':0, 'gn': 0, 'gn1': 0, 'ot': 0, 'op':0, 'j1':0}
        dic_time['j1'] = (timer() - start_j1) + finish_j1_pre
        dic_time['gn'] = time_gn
        dic_time['gn1'] = time_gn1
        dic_time['ot'] = time_other_terms
        dic_time['op'] = time_operations
        dic_time['n_max'] = n_max
    
        result_and_times.append(CalculateTime(result, dic_time))

        finish_j1_pre = 0

    return result_and_times


def summation_with_compute_time_with_parallel(particle, beam, i):    
    
    start_j1 = timer() 
    
    v_eta_r = eta_r(particle.m, particle.ur)
    mod2_eta_r = abs(v_eta_r) ** 2

    # variables computed in i position
    start_ot = timer()
    vars_i = compute_variables(particle, i)
    time_other_terms = timer() - start_ot

    if isinstance(beam, GaussAttributes):
        gn = beam.gn_beam(i)
        conj_gn = np.conj(gn)
        gn1 = beam.gn_beam((i+1))
        conj_gn1 = np.conj(gn1)
    elif isinstance(beam, BesselAttributes):
        gn = gn_bessel_beam(i, beam.k, beam.z0, beam.angle)
        conj_gn = np.conj(gn)
        gn1 = gn_bessel_beam((i+1), beam.k, beam.z0, beam.angle)
        conj_gn1 = np.conj(gn1)
    elif isinstance(beam, FrozenWaveAttributes):
        
        start_gn = timer()
        gn = gn_frozen_wave_beam(i, beam.n, beam.k, beam.z0, beam.l, beam.q)
        time_gn = timer() - start_gn

        conj_gn = np.conj(gn)

        start_gn1 = timer()
        gn1 = gn_frozen_wave_beam((i+1), beam.n, beam.k, beam.z0, beam.l, beam.q)
        time_gn1 = timer() - start_gn1

        conj_gn1 = np.conj(gn1)
    else:
        gn = 1
        conj_gn = 1
        gn1 = 1
        conj_gn1 = 1


    start_operations = timer()

    first_term_for = ((i*(i+2)) / particle.m) * \
                        (
                                (gn1 * conj_gn * vars_i.cn1 * vars_i.conj_cn * vars_i.rn1) +
                                (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn * vars_i.rn)
                        )

    second_term_for = ((i*(i+2)) / (i+1)) * \
                        (
                                (gn * conj_gn1 * vars_i.cn * vars_i.conj_cn1) +
                                (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn)
                        )

    third_term_for = np.conj(v_eta_r) * (((2*i)+1) / (i*(i+1))) * (abs(gn)**2) * (vars_i.cn * vars_i.conj_dn)
    
    result = first_term_for - ((second_term_for + third_term_for) * vars_i.sn)
        
    time_operations = timer() - start_operations
    
    dic_time = {'ponto':particle.x, 'n_max':0, 'gn': 0, 'gn1': 0, 'ot': 0, 'op':0, 'j1':0}
    dic_time['j1'] = timer() - start_j1
    dic_time['gn'] = time_gn
    dic_time['gn1'] = time_gn1
    dic_time['ot'] = time_other_terms
    dic_time['op'] = time_operations

    result_and_times = CalculateTime(result, dic_time)
    
    return result_and_times


def j1_with_time_gn_term_calculate(particle, beam):    
    """
    TODO: add description
    
    Parameters
    ----------
    particle :
    beam     :
    """
    if isinstance(particle, ParticleAttributes) and isinstance(beam, BeamAttributes):
        epsilon2l = epsilon_imag(particle.m, particle.ur)

        first_term = (3 * epsilon2l) / ((abs(particle.m) ** 2) * (particle.x ** 3))

        results = summation_calculate_gn_time(particle, beam)
       
        dic_time = {'execucao':0, 'ponto':particle.x, 'z':"", 'n_max':0, 'gn': 0, 'gns_terms':[], 'gn1': 0, 'ot': 0, 'op':0, 'j1':0}

        summation_result = 0

        for i in results:
            # print(i.dict_t)
            summation_result += i.result
            dic_time['gn'] += i.dict_t['gn']
            dic_time['gn1'] += i.dict_t['gn1']
            dic_time['ot'] += i.dict_t['ot']
            dic_time['op'] += i.dict_t['op']
            dic_time['j1'] += i.dict_t['j1']

            gn_terms = i.dict_t['gn_term_times']

            dic_time['gns_terms'].append(gn_terms)
            
        dic_time['n_max'] = results[0].dict_t['n_max']
        
        # print("*************************************************************")

    else:
        print("Error. Type of particle invalid. Type is", type(particle))
        print("And is expected: ", ParticleAttributes)
        return 0
    
    result = first_term * summation_result.imag
    
    return result, dic_time




def j1_with_time(particle, beam):    
    """
    TODO: add description
    
    Parameters
    ----------
    particle :
    beam     :
    """
    if isinstance(particle, ParticleAttributes) and isinstance(beam, BeamAttributes):
        epsilon2l = epsilon_imag(particle.m, particle.ur)

        first_term = (3 * epsilon2l) / ((abs(particle.m) ** 2) * (particle.x ** 3))

        results = summation_with_compute_time(particle, beam)
       
        dic_time = {'ponto':particle.x, 'n_max':0, 'gn': 0, 'gn1': 0, 'ot': 0, 'op':0, 'j1':0}

        summation_result = 0

        for i in results:
            # print(i.dict_t)
            summation_result += i.result
            dic_time['gn'] += i.dict_t['gn']
            dic_time['gn1'] += i.dict_t['gn1']
            dic_time['ot'] += i.dict_t['ot']
            dic_time['op'] += i.dict_t['op']
            dic_time['j1'] += i.dict_t['j1']
            
        dic_time['n_max'] = results[0].dict_t['n_max']
        
        # print("*************************************************************")

    else:
        print("Error. Type of particle invalid. Type is", type(particle))
        print("And is expected: ", ParticleAttributes)
        return 0
    
    result = first_term * summation_result.imag
    
    return result, dic_time

def j1_with_time_gn_parallel(particle, beam):    
    """
    TODO: add description
    
    Parameters
    ----------
    particle :
    beam     :
    """
    if isinstance(particle, ParticleAttributes) and isinstance(beam, BeamAttributes):
        epsilon2l = epsilon_imag(particle.m, particle.ur)

        first_term = (3 * epsilon2l) / ((abs(particle.m) ** 2) * (particle.x ** 3))

        results = summation_with_compute_time_gn_parallel(particle, beam)
       
        dic_time = {'execucao':0, 'ponto':particle.x, 'z':"", 'n_max':0, 'gn': 0, 'gn1': 0, 'ot': 0, 'op':0, 'j1':0}

        summation_result = 0

        for i in results:
            # print(i.dict_t)
            summation_result += i.result
            dic_time['gn'] += i.dict_t['gn']
            dic_time['gn1'] += i.dict_t['gn1']
            dic_time['ot'] += i.dict_t['ot']
            dic_time['op'] += i.dict_t['op']
            dic_time['j1'] += i.dict_t['j1']
            
        dic_time['n_max'] = results[0].dict_t['n_max']
        
        # print("*************************************************************")

    else:
        print("Error. Type of particle invalid. Type is", type(particle))
        print("And is expected: ", ParticleAttributes)
        return 0
    
    result = first_term * summation_result.imag
    
    return result, dic_time


def j1_with_time_parallel(particle, beam):    
    """
    TODO: add description
    
    Parameters
    ----------
    particle :
    beam     :
    """
    if isinstance(particle, ParticleAttributes) and isinstance(beam, BeamAttributes):
        epsilon2l = epsilon_imag(particle.m, particle.ur)

        first_term = (3 * epsilon2l) / ((abs(particle.m) ** 2) * (particle.x ** 3))

        pool_size = multiprocessing.cpu_count()      
        # if pool_size > 1:
        #     pool_size = int(pool_size/2)
        
        pool = multiprocessing.Pool(processes=pool_size)

        n_max = ceiling_x(particle.x)
        n_values = [(i) for i in range(1, (n_max+1))]

        results = pool.starmap(summation_with_compute_time_with_parallel, zip(repeat(particle), repeat(beam), n_values))
        pool.close() 
        pool.join() 

        dic_time = {'execucao':0, 'ponto':particle.x, 'z':"", 'n_max':n_max, 'gn': 0, 'gn1': 0, 'ot': 0, 'op':0, 'j1':0}

        summation_result = 0

        for i in results:
            summation_result += i.result
            dic_time['gn'] += i.dict_t['gn']
            dic_time['gn1'] += i.dict_t['gn1']
            dic_time['ot'] += i.dict_t['ot']
            dic_time['op'] += i.dict_t['op']
            dic_time['j1'] += i.dict_t['j1']            
            # print(i.dict_t)
        
        # print("*************************************************************")

    else:
        print("Error. Type of particle invalid. Type is", type(particle))
        print("And is expected: ", ParticleAttributes)
        return 0
    
    result = first_term * summation_result.imag
    
    return result, dic_time



def j1(particle, beam):    
    """
    TODO: add description
    
    Parameters
    ----------
    particle :
    beam     :
    """
    if isinstance(particle, ParticleAttributes) and isinstance(beam, BeamAttributes):
        epsilon2l = epsilon_imag(particle.m, particle.ur)

        first_term = (3 * epsilon2l) / ((abs(particle.m) ** 2) * (particle.x ** 3))

        summation_result = summation(particle, beam)
        
    else:
        print("Error. Type of particle invalid. Type is", type(particle))
        print("And is expected: ", ParticleAttributes)
        return 0
    
    result = first_term * summation_result.imag
    
    return result



# def summation_with_compute_time(particle, beam):
#     time_gn = 0
#     time_gn1 = 0
#     time_other_terms = 0
#     time_operations = 0


#     start_j1 = timer() 
    
#     n_max = ceiling_x(particle.x)
#     v_eta_r = eta_r(particle.m, particle.ur)
#     mod2_eta_r = abs(v_eta_r) ** 2
#     summation_result = 0

#     for i in range(1, (n_max+1)):
#         # variables computed in i position
#         start_ot = timer()
#         vars_i = compute_variables(particle, i)
#         time_other_terms += timer() - start_ot

#         if isinstance(beam, GaussAttributes):
#             gn = beam.gn_beam(i)
#             conj_gn = np.conj(gn)
#             gn1 = beam.gn_beam((i+1))
#             conj_gn1 = np.conj(gn1)
#         elif isinstance(beam, BesselAttributes):
#             gn = gn_bessel_beam(i, beam.k, beam.z0, beam.angle)
#             conj_gn = np.conj(gn)
#             gn1 = gn_bessel_beam((i+1), beam.k, beam.z0, beam.angle)
#             conj_gn1 = np.conj(gn1)
#         elif isinstance(beam, FrozenWaveAttributes):
            
#             start_gn = timer()
#             gn = gn_frozen_wave_beam(i, beam.n, beam.k, beam.z0, beam.l, beam.q)
#             time_gn += timer() - start_gn

#             conj_gn = np.conj(gn)

#             start_gn1 = timer()
#             gn1 = gn_frozen_wave_beam((i+1), beam.n, beam.k, beam.z0, beam.l, beam.q)
#             time_gn1 += timer() - start_gn1

#             conj_gn1 = np.conj(gn1)
#         else:
#             gn = 1
#             conj_gn = 1
#             gn1 = 1
#             conj_gn1 = 1


#         start_operations = timer()

#         first_term_for = ((i*(i+2)) / particle.m) * \
#                          (
#                                  (gn1 * conj_gn * vars_i.cn1 * vars_i.conj_cn * vars_i.rn1) +
#                                  (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn * vars_i.rn)
#                          )

#         second_term_for = ((i*(i+2)) / (i+1)) * \
#                           (
#                                   (gn * conj_gn1 * vars_i.cn * vars_i.conj_cn1) +
#                                   (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn)
#                           )

#         third_term_for = np.conj(v_eta_r) * (((2*i)+1) / (i*(i+1))) * (abs(gn)**2) * (vars_i.cn * vars_i.conj_dn)
        
#         result = first_term_for - ((second_term_for + third_term_for) * vars_i.sn)
        
#         summation_result += result

#         time_operations += timer() - start_operations
    
    
#     dic_time['j1'] = timer() - start_j1
#     dic_time['gn'] = time_gn
#     dic_time['gn1'] = time_gn1
#     dic_time['ot'] = time_other_terms
#     dic_time['op'] = time_operations

#     return summation_result, dic_time
