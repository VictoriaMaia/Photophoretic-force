import numpy as np
from .cn import term_c_n
from .rn import term_r_n
from .dn import term_d_n
from .sn import term_s_n


class SummationVariables:
    def __init__(self, particle_params, i):
        self.cn = term_c_n(
            particle_params.ur, particle_params.m, particle_params.x, i)
        self.conj_cn = np.conj(self.cn)

        self.cn1 = term_c_n(
            particle_params.ur, particle_params.m, particle_params.x, (i + 1))
        self.conj_cn1 = np.conj(self.cn1)

        self.rn = term_r_n(particle_params.m, particle_params.x, i)
        self.rn1 = term_r_n(particle_params.m, particle_params.x, (i + 1))

        self.dn = term_d_n(
            particle_params.ur, particle_params.m, particle_params.x, i)
        self.conj_dn = np.conj(self.dn)

        self.dn1 = term_d_n(
            particle_params.ur, particle_params.m, particle_params.x, (i + 1))

        self.sn = term_s_n(particle_params.m, particle_params.x, i)
        pass
