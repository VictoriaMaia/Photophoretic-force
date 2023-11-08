from .summation_terms_of_j1 import ceiling_x, eta_r, epsilon_imag
from .summation_terms_of_j1 import SummationVariables
from .particle import ParticleAttributes
from .beams import BeamAttributes
import numpy as np


def summation(particle, beam):
    """
    Calculates the summation of j1

    Parameters
    ----------
    particle : is the particle object that contains informations about the particle
    beam     : is the bem object that contains informations about the beam and your gn function
    """
    n_max = ceiling_x(particle.x)
    v_eta_r = eta_r(particle.m, particle.ur)
    mod2_eta_r = abs(v_eta_r) ** 2
    summation_result = 0

    for i in range(1, (n_max+1)):
        # variables computed in i position
        vars_i = SummationVariables(particle, i)

        gn = beam.gn(i)
        conj_gn = np.conj(gn)
        gn1 = beam.gn(i+1)
        conj_gn1 = np.conj(gn1)

        first_term_for = ((i*(i+2)) / particle.m) *\
            (
            (gn1 * conj_gn * vars_i.cn1 * vars_i.conj_cn * vars_i.rn1) +
            (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn * vars_i.rn)  # noqa: E501
            )

        second_term_for = ((i*(i+2)) / (i+1)) * \
            (
            (gn * conj_gn1 * vars_i.cn * vars_i.conj_cn1) +
            (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn)
            )

        third_term_for = np.conj(v_eta_r) *\
            (((2*i)+1) / (i*(i+1))) *\
            (abs(gn)**2) *\
            (vars_i.cn * vars_i.conj_dn)

        result = first_term_for -\
            ((second_term_for + third_term_for) * vars_i.sn)

        summation_result += result

    return summation_result


def j1(particle, beam):
    """
    Calculate the asymmetry factor value

    Parameters
    ----------
    particle : is the particle object that contains informations about the particle
    beam     : is the bem object that contains informations about the beam and your gn function
    """
    if isinstance(particle, ParticleAttributes) and\
       isinstance(beam, BeamAttributes):

        epsilon2l = epsilon_imag(particle.m, particle.ur)

        first_term = (3 * epsilon2l) / \
            ((abs(particle.m) ** 2) * (particle.x ** 3))

        summation_result = summation(particle, beam)
    else:
        print("Error. Type of particle invalid. Type is", type(particle))
        print("And is expected: ", ParticleAttributes)
        return 0

    return first_term * summation_result.imag
