import numpy as np
from .cn import term_c_n
from .rn import term_r_n
from .dn import term_d_n
from .sn import term_s_n


class SummationVariables:
    def __init__(self, cn, conj_cn, cn1, conj_cn1, rn, rn1, dn, conj_dn, dn1, sn):
        self.cn = cn
        self.conj_cn = conj_cn
        self.cn1 = cn1
        self.conj_cn1 = conj_cn1
        self.rn = rn
        self.rn1 = rn1
        self.dn = dn
        self.conj_dn = conj_dn
        self.dn1 = dn1
        self.sn = sn
        pass


def compute_variables(particle_params, i):
    cn = term_c_n(particle_params.ur, particle_params.m, particle_params.x, i)
    conj_cn = np.conj(cn)
    cn1 = term_c_n(particle_params.ur, particle_params.m, particle_params.x, (i + 1))
    conj_cn1 = np.conj(cn1)
    rn = term_r_n(particle_params.m, particle_params.x, i)
    rn1 = term_r_n(particle_params.m, particle_params.x, (i + 1))
    dn = term_d_n(particle_params.ur, particle_params.m, particle_params.x, i)
    conj_dn = np.conj(dn)
    dn1 = term_d_n(particle_params.ur, particle_params.m, particle_params.x, (i + 1))
    sn = term_s_n(particle_params.m, particle_params.x, i)

    return SummationVariables(cn, conj_cn, cn1, conj_cn1, rn, rn1, dn, conj_dn, dn1, sn)
