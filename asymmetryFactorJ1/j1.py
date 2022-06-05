from asymmetryFactorJ1.variables import *
from asymmetryFactorJ1.structures import *
from asymmetryFactorJ1.gaussianBeam import *
from asymmetryFactorJ1.var_structure import *
import numpy as np


def compute_variables(parameters, i):
    cn = var_c_n(parameters.ur, parameters.M, parameters.x, i)
    conj_cn = np.conj(cn)
    cn1 = var_c_n(parameters.ur, parameters.M, parameters.x, (i + 1))
    conj_cn1 = np.conj(cn1)
    rn = Rn(parameters.M, parameters.x, i)
    rn1 = Rn(parameters.M, parameters.x, (i + 1))
    dn = var_d_n(parameters.ur, parameters.M, parameters.x, i)
    conj_dn = np.conj(dn)
    dn1 = var_d_n(parameters.ur, parameters.M, parameters.x, (i + 1))
    sn = Sn(parameters.M, parameters.x, i)

    return CommonVariables(cn, conj_cn, cn1, conj_cn1, rn, rn1, dn, conj_dn, dn1, sn)


def summation(parameters):
    summation_result = 0
    n_max = ceilingX(parameters.x)
    v_eta_r = eta_r(parameters.M, parameters.ur)
    mod2_eta_r = abs(v_eta_r) ** 2

    for i in range(1, (n_max+1)):
        # variables computed in i position
        vars_i = compute_variables(parameters, i)
        
        first_term_for = ((i*(i+2)) / parameters.M) * \
                         (
                                 (vars_i.cn1 * vars_i.conj_cn * vars_i.rn1) +
                                 (mod2_eta_r * vars_i.dn1 * vars_i.conj_dn * vars_i.rn)
                         )

        second_term_for = ((i*(i+2)) /
                           (i+1)) * ((vars_i.cn * vars_i.conj_cn1) + (mod2_eta_r * vars_i.dn1 * vars_i.conj_dn))

        third_term_for = np.conj(v_eta_r) * (((2*i)+1) / (i*(i+1))) * (vars_i.cn * vars_i.conj_dn)
        
        result = first_term_for - ((second_term_for + third_term_for) * vars_i.sn)
        
        summation_result += result
    
    return summation_result


def summation_with_gn(parameters):
    n_max = ceilingX(parameters.x)
    v_eta_r = eta_r(parameters.M, parameters.ur)
    mod2_eta_r = abs(v_eta_r) ** 2
    summation_result = 0
    
    for i in range(1, (n_max+1)):
        # variables computed in i position
        vars_i = compute_variables(parameters, i)

        if type(parameters) == J1Gauss:
            gn = gnGaussianBeam(i, parameters.k, parameters.z0, parameters.s)
            conj_gn = np.conj(gn)
            gn1 = gnGaussianBeam((i+1), parameters.k, parameters.z0, parameters.s)
            conj_gn1 = np.conj(gn1)
        else:
            return 0

        first_term_for = ((i*(i+2)) / parameters.M) * \
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


def j1(parameters):    
    epsilon2l = epsilon(parameters.M, parameters.ur)

    first_term = (3 * epsilon2l) / ((abs(parameters.M) ** 2) * (parameters.x ** 3))

    if type(parameters) == J1Attributes:
        summation_result = summation(parameters)
    elif type(parameters) == J1Gauss:
        summation_result = summation_with_gn(parameters) 
    else:
        print("Error. Type of parameters invalid.")
        return 0
        
    return first_term * summation_result.imag
