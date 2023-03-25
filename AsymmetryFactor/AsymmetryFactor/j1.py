from .summation_terms_of_j1 import *
from .particle.particle_class import ParticleAttributes
from .beams.beam_class import BeamAttributes
from .beams import *
import numpy as np
from timeit import default_timer as timer

dic_time = {'ponto':0, 'gn': 0, 'gn1': 0, 'ot': 0, 'op':0, 'j1':0}


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


def summation_with_compute_time(particle, beam):
    time_gn = 0
    time_gn1 = 0
    time_other_terms = 0
    time_operations = 0


    start_j1 = timer() 
    
    n_max = ceiling_x(particle.x)
    v_eta_r = eta_r(particle.m, particle.ur)
    mod2_eta_r = abs(v_eta_r) ** 2
    summation_result = 0

    for i in range(1, (n_max+1)):
        # variables computed in i position
        start_ot = timer()
        vars_i = compute_variables(particle, i)
        time_other_terms += timer() - start_ot

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
            time_gn += timer() - start_gn

            conj_gn = np.conj(gn)

            start_gn1 = timer()
            gn1 = gn_frozen_wave_beam((i+1), beam.n, beam.k, beam.z0, beam.l, beam.q)
            time_gn1 += timer() - start_gn1

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
        
        summation_result += result

        time_operations += timer() - start_operations
    
    
    dic_time['j1'] = timer() - start_j1
    dic_time['gn'] = time_gn
    dic_time['gn1'] = time_gn1
    dic_time['ot'] = time_other_terms
    dic_time['op'] = time_operations

    return summation_result, dic_time


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

        # summation_result = summation(particle, beam)
        summation_result, dic_time = summation_with_compute_time(particle, beam)
        
    else:
        print("Error. Type of particle invalid. Type is", type(particle))
        print("And is expected: ", ParticleAttributes)
        return 0
    
    result = first_term * summation_result.imag
    
    return result, dic_time
